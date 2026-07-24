from __future__ import annotations

import struct

import pytest

from templex_zero.tzif_reader import TZifError, parse_tzif


def _header(
    version: bytes = b"\x00",
    *,
    isutcnt: int = 0,
    isstdcnt: int = 0,
    leapcnt: int = 0,
    timecnt: int = 0,
    typecnt: int = 1,
    charcnt: int = 4,
) -> bytes:
    return b"TZif" + version + b"\x00" * 15 + struct.pack(
        ">6I", isutcnt, isstdcnt, leapcnt, timecnt, typecnt, charcnt
    )


def _block(
    *,
    time_size: int,
    times: tuple[int, ...] = (),
    indexes: bytes = b"",
    types: tuple[tuple[int, int, int], ...] = ((0, 0, 0),),
    abbreviations: bytes = b"UTC\x00",
    leaps: tuple[tuple[int, int], ...] = (),
    isstd: bytes = b"",
    isut: bytes = b"",
) -> bytes:
    time_code = ">i" if time_size == 4 else ">q"
    out = bytearray()
    for value in times:
        out += struct.pack(time_code, value)
    out += indexes
    for utoff, dst, abbr_index in types:
        out += struct.pack(">iBB", utoff, dst, abbr_index)
    out += abbreviations
    for timestamp, correction in leaps:
        out += struct.pack(time_code, timestamp)
        out += struct.pack(">i", correction)
    out += isstd
    out += isut
    return bytes(out)


def _v1(
    *,
    times: tuple[int, ...] = (),
    indexes: bytes = b"",
    types: tuple[tuple[int, int, int], ...] = ((0, 0, 0),),
    abbreviations: bytes = b"UTC\x00",
    isstd: bytes = b"",
    isut: bytes = b"",
    header_overrides: dict[str, int] | None = None,
) -> bytes:
    kwargs = dict(
        timecnt=len(times),
        typecnt=len(types),
        charcnt=len(abbreviations),
        isstdcnt=len(isstd),
        isutcnt=len(isut),
    )
    kwargs.update(header_overrides or {})
    return _header(**kwargs) + _block(
        time_size=4,
        times=times,
        indexes=indexes,
        types=types,
        abbreviations=abbreviations,
        isstd=isstd,
        isut=isut,
    )


def _v2() -> bytes:
    header = _header(b"2")
    first = _block(time_size=4)
    second_header = _header(b"2")
    second = _block(time_size=8)
    return header + first + second_header + second + b"\nUTC0\n"


def test_minimal_v1_and_pre_first_type_zero() -> None:
    raw = _v1(
        times=(100,),
        indexes=b"\x01",
        types=((0, 0, 0), (3600, 1, 4)),
        abbreviations=b"UTC\x00DST\x00",
    )
    parsed = parse_tzif(raw)
    assert parsed.version == "1"
    assert parsed.type_at(99).index == 0
    assert parsed.type_at(100).index == 1
    pre, post = parsed.transition_at(100)
    assert (pre.index, post.index) == (0, 1)


def test_minimal_v2_footer_and_canonical_serialization() -> None:
    parsed = parse_tzif(_v2())
    assert parsed.version == "2"
    assert parsed.footer == "UTC0"
    assert parsed.canonical_bytes() == parsed.canonical_bytes()
    assert parsed.canonical_bytes().endswith(b"\n")


def test_rejects_truncated_block() -> None:
    with pytest.raises(TZifError, match="truncated"):
        parse_tzif(_v1()[:-1])


def test_rejects_inconsistent_indicator_count() -> None:
    raw = _v1(header_overrides={"isstdcnt": 2})
    with pytest.raises(TZifError, match="isstdcnt"):
        parse_tzif(raw)


def test_rejects_invalid_transition_type_index() -> None:
    raw = _v1(times=(0,), indexes=b"\x01")
    with pytest.raises(TZifError, match="transition type index"):
        parse_tzif(raw)


def test_rejects_impossible_abbreviation_index() -> None:
    raw = _v1(types=((0, 0, 4),))
    with pytest.raises(TZifError, match="abbreviation index"):
        parse_tzif(raw)


def test_rejects_unterminated_abbreviation() -> None:
    raw = _v1(abbreviations=b"UTC")
    with pytest.raises(TZifError, match="NUL-terminated"):
        parse_tzif(raw)


def test_rejects_unsupported_version() -> None:
    raw = b"TZif9" + b"\x00" * 39
    with pytest.raises(TZifError, match="unsupported"):
        parse_tzif(raw)


def test_rejects_nonascending_transitions() -> None:
    raw = _v1(times=(100, 100), indexes=b"\x00\x00")
    with pytest.raises(TZifError, match="strictly increasing"):
        parse_tzif(raw)


def test_rejects_invalid_dst_flag() -> None:
    raw = _v1(types=((0, 2, 0),))
    with pytest.raises(TZifError, match="DST flag"):
        parse_tzif(raw)


def test_rejects_v2_without_newline_footer() -> None:
    with pytest.raises(TZifError, match="footer"):
        parse_tzif(_v2()[:-1])
