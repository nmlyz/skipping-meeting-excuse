#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the excuse for skipping a
pointless meeting.

The line was picked from 36 candidates by pairwise judging against the
brief: a 90-minute meeting to pick a font, declined with a single word
that does two jobs at once — it is the font picked, and the excuse
itself. Before anything is written, the line passes a structured gate
(length, single line, no surrounding space, exact judged length); after
writing, the file is read back and checked byte for byte, digest and
all, so a silent partial write can never pass as a finished entry.
"""

import argparse
import hashlib
import os
import sys

LINE = (
    "Can't attend — the meeting is 90 minutes to pick a font, "
    "and I've already picked one: absent."
)

# The entry gate, fixed by the judged line: 93 characters, one line.
MIN_LENGTH = 1
MAX_LENGTH = 200
EXPECTED_LENGTH = 93
# sha256 of entry.txt as written (the line plus its trailing newline).
EXPECTED_SHA256 = "65ddf397a2f4e8fe539da3a91b9e434a65527822be16cb56d5f1b39c21dd067a"


def check_entry(line):
    """Return a list of gate failures for `line` (empty means it passes)."""
    problems = []
    if not MIN_LENGTH <= len(line) <= MAX_LENGTH:
        problems.append(
            f"length {len(line)} is outside the gate {MIN_LENGTH}-{MAX_LENGTH}"
        )
    if len(line) != EXPECTED_LENGTH:
        problems.append(
            f"length {len(line)} does not match the judged length "
            f"{EXPECTED_LENGTH}"
        )
    if "\n" in line or "\r" in line:
        problems.append("line must be a single line")
    if line != line.strip():
        problems.append("line must have no leading or trailing space")
    if not line.strip():
        problems.append("line must not be only whitespace")
    return problems


def write_entry(path, data):
    """Write `data` to `path`, creating the directory if needed."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)


def verify_written(path, data):
    """Read `path` back and confirm it holds exactly `data`.

    Returns a list of verification failures (empty means it matches).
    """
    problems = []
    with open(path, "rb") as f:
        actual = f.read()
    if actual != data:
        problems.append("read-back bytes differ from what was written")
        return problems
    digest = hashlib.sha256(actual).hexdigest()
    if digest != EXPECTED_SHA256:
        problems.append(f"sha256 {digest} does not match the expected digest")
    if os.stat(path).st_mode & 0o777 != 0o644:
        problems.append("file mode is not 0644")
    return problems


def parse_args(argv):
    """Parse command-line options (the output directory can be set here
    or with MAKEFUN_OUTPUT_DIR; the flag wins when both are given)."""
    parser = argparse.ArgumentParser(
        description="Write the judged excuse line to entry.txt."
    )
    parser.add_argument(
        "--out-dir",
        default=None,
        help="directory for entry.txt (default: $MAKEFUN_OUTPUT_DIR or /output)",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    problems = check_entry(LINE)
    if problems:
        for problem in problems:
            print(f"gate failed: {problem}", file=sys.stderr)
        sys.exit(1)
    out_dir = args.out_dir or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    data = (LINE + "\n").encode("utf-8")
    write_entry(path, data)
    problems = verify_written(path, data)
    if problems:
        for problem in problems:
            print(f"verify failed: {problem}", file=sys.stderr)
        sys.exit(1)
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {len(data)} bytes to {path} (sha256 {digest})")


if __name__ == "__main__":
    main()
