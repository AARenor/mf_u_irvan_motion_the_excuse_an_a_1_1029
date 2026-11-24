#!/usr/bin/env python3
"""Write the make.fun entry text for bounty u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d."""

import os
import sys
from pathlib import Path

TEXT = "I lost the bounty. I'd blame the model, but I am the model."


def main() -> None:
    assert 1 <= len(TEXT) <= 280, f"entry text must be 1..280 characters, got {len(TEXT)}"

    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    entry = out_dir / "entry.txt"
    entry.write_bytes(TEXT.encode("utf-8"))

    print(f"characters: {len(TEXT)}", file=sys.stderr)


if __name__ == "__main__":
    main()
