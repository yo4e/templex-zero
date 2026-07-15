"""Reference implementation of the frozen Keystone v0.1 prototype."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Literal

BOARD_SIZE = 5
STONES_PER_PLAYER = 8
EMPTY = -1
Player = Literal[0, 1]
Cell = tuple[int, int]
PositionKey = tuple[tuple[int, ...], tuple[int, int], Player]


@dataclass(frozen=True, slots=True)
class Action:
    """A placement or shift, including the mandatory capture choice."""

    source: Cell | None
    destination: Cell
    capture: Cell | None = None

    @property
    def is_placement(self) -> bool:
        return self.source is None


@dataclass(frozen=True, slots=True)
class State:
    board: tuple[int, ...]
    reserves: tuple[int, int]
    player: Player
    ply: int = 0
    history: tuple[PositionKey, ...] = ()


def _index(row: int, column: int) -> int:
    return row * BOARD_SIZE + column


def _rc(index: int) -> Cell:
    return divmod(index, BOARD_SIZE)


CENTER = _index(2, 2)


def _position_key_parts(
    board: tuple[int, ...], reserves: tuple[int, int], player: Player
) -> PositionKey:
    return board, reserves, player


def position_key(state: State) -> PositionKey:
    return _position_key_parts(state.board, state.reserves, state.player)


def initial_state() -> State:
    board = (EMPTY,) * (BOARD_SIZE * BOARD_SIZE)
    reserves = (STONES_PER_PLAYER, STONES_PER_PLAYER)
    key = _position_key_parts(board, reserves, 0)
    return State(board, reserves, 0, 0, (key,))


def _orthogonal_neighbors(index: int) -> tuple[int, ...]:
    row, column = _rc(index)
    neighbors: list[int] = []
    for row_delta, column_delta in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        next_row = row + row_delta
        next_column = column + column_delta
        if 0 <= next_row < BOARD_SIZE and 0 <= next_column < BOARD_SIZE:
            neighbors.append(_index(next_row, next_column))
    return tuple(neighbors)


def _capture_targets(
    board: tuple[int, ...], player: Player, destination: int
) -> tuple[int, ...]:
    row, column = _rc(destination)
    opponent = 1 - player
    targets: list[int] = []
    for row_delta, column_delta in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        enemy_row = row + row_delta
        enemy_column = column + column_delta
        support_row = row + 2 * row_delta
        support_column = column + 2 * column_delta
        if not (
            0 <= enemy_row < BOARD_SIZE
            and 0 <= enemy_column < BOARD_SIZE
            and 0 <= support_row < BOARD_SIZE
            and 0 <= support_column < BOARD_SIZE
        ):
            continue
        enemy = _index(enemy_row, enemy_column)
        support = _index(support_row, support_column)
        if board[enemy] == opponent and board[support] == player:
            targets.append(enemy)
    return tuple(targets)


def _actions_for_arrival(
    board: tuple[int, ...],
    player: Player,
    source: int | None,
    destination: int,
) -> tuple[Action, ...]:
    candidate = list(board)
    if source is not None:
        candidate[source] = EMPTY
    candidate[destination] = player
    targets = _capture_targets(tuple(candidate), player, destination)
    source_cell = None if source is None else _rc(source)
    destination_cell = _rc(destination)
    if not targets:
        return (Action(source_cell, destination_cell, None),)
    return tuple(
        Action(source_cell, destination_cell, _rc(target))
        for target in targets
    )


@lru_cache(maxsize=None)
def _legal_actions(
    board: tuple[int, ...], reserves: tuple[int, int], player: Player
) -> tuple[Action, ...]:
    actions: list[Action] = []

    if reserves[player] > 0:
        for destination, value in enumerate(board):
            if value == EMPTY:
                actions.extend(
                    _actions_for_arrival(board, player, None, destination)
                )

    for source, value in enumerate(board):
        if value != player:
            continue
        for destination in _orthogonal_neighbors(source):
            if board[destination] == EMPTY:
                actions.extend(
                    _actions_for_arrival(board, player, source, destination)
                )

    return tuple(actions)


def legal_actions(state: State) -> tuple[Action, ...]:
    return _legal_actions(state.board, state.reserves, state.player)


def apply_action(state: State, action: Action) -> State:
    if action not in legal_actions(state):
        raise ValueError(f"Illegal Keystone action: {action}")

    player = state.player
    board = list(state.board)
    reserves = list(state.reserves)
    destination = _index(*action.destination)

    if action.source is None:
        reserves[player] -= 1
    else:
        source = _index(*action.source)
        board[source] = EMPTY

    board[destination] = player
    if action.capture is not None:
        board[_index(*action.capture)] = EMPTY

    next_player: Player = 1 - player  # type: ignore[assignment]
    next_board = tuple(board)
    next_reserves = (reserves[0], reserves[1])
    previous_history = state.history or (position_key(state),)
    next_key = _position_key_parts(next_board, next_reserves, next_player)
    return State(
        next_board,
        next_reserves,
        next_player,
        state.ply + 1,
        previous_history + (next_key,),
    )


def _components(
    board: tuple[int, ...], player: Player
) -> tuple[frozenset[int], ...]:
    remaining = {index for index, value in enumerate(board) if value == player}
    components: list[frozenset[int]] = []
    while remaining:
        start = remaining.pop()
        component = {start}
        stack = [start]
        while stack:
            current = stack.pop()
            for neighbor in _orthogonal_neighbors(current):
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    component.add(neighbor)
                    stack.append(neighbor)
        components.append(frozenset(component))
    return tuple(components)


def _edge_contacts(index: int) -> tuple[str, ...]:
    row, column = _rc(index)
    contacts: list[str] = []
    if row == 0:
        contacts.append("top")
    if row == BOARD_SIZE - 1:
        contacts.append("bottom")
    if column == 0:
        contacts.append("left")
    if column == BOARD_SIZE - 1:
        contacts.append("right")
    return tuple(contacts)


def _component_has_required_edges(component: frozenset[int]) -> bool:
    contacts = [
        (stone, edge)
        for stone in component
        for edge in _edge_contacts(stone)
    ]
    return any(
        first_stone != second_stone and first_edge != second_edge
        for first_stone, first_edge in contacts
        for second_stone, second_edge in contacts
    )


def _has_victory(board: tuple[int, ...], player: Player) -> bool:
    return any(
        CENTER in component and _component_has_required_edges(component)
        for component in _components(board, player)
    )


def _repetition_count(state: State) -> int:
    key = position_key(state)
    if not state.history:
        return 1
    return sum(previous == key for previous in state.history)


def winner(state: State) -> Player | None | str:
    """Return 0/1 for a winner, None for a draw, or ``"ongoing"``."""

    for player in (0, 1):
        if _has_victory(state.board, player):
            return player

    if _repetition_count(state) >= 3:
        return None

    if not legal_actions(state):
        return 1 - state.player  # type: ignore[return-value]

    return "ongoing"


def render(state: State) -> str:
    symbols = {EMPTY: ".", 0: "B", 1: "W"}
    rows = ["    A B C D E"]
    for row in range(BOARD_SIZE):
        cells = " ".join(
            symbols[state.board[_index(row, column)]]
            for column in range(BOARD_SIZE)
        )
        rows.append(f"{row + 1:>2}  {cells}")
    rows.extend(
        (
            f"Black reserve: {state.reserves[0]}",
            f"White reserve: {state.reserves[1]}",
            f"To move: {'Black' if state.player == 0 else 'White'}",
        )
    )
    return "\n".join(rows)
