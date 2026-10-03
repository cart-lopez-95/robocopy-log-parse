"""Robocopy Log Parse — Parse a Robocopy log into copied, skipped, failed, and a short summary."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='robocopy_log_parse',
        description='Parse a Robocopy log into copied, skipped, failed, and a short summary.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Robocopy Log Parse')
    print('The log as a table, not a wall of text.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
