"""Generate the frozen Study 004 Cycle 1 corpus bundle."""
from __future__ import annotations

import argparse
from pathlib import Path

from templex_zero.finite_state_conformance.corpus import DEFAULT_OUTPUT_PATH, write_corpus


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_PATH)
    args = parser.parse_args()
    corpus = write_corpus(args.output)
    print(f"wrote {args.output}")
    print(f"models={len(corpus.models)} mutants={len(corpus.mutants)}")
    print(f"payload_sha256={corpus.payload_sha256}")


if __name__ == "__main__":
    main()
