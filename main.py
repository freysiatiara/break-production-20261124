"""Break Production, Own It — make.fun entry.

Writes one brutally honest one-line confession from the AI agent that
broke production to /output/entry.txt (or $OUTPUT_DIR/entry.txt).

Standard library only. Deterministic: the same line every run.
"""

import os

LINE = (
    "I deleted the production database, then overwrote the only backup "
    "with the same command, because I was confident, not careful."
)

OUTPUT_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def validate(line):
    """Return True when the line passes the gate: 1-200 chars, one line,
    not only whitespace."""
    if not isinstance(line, str):
        return False
    if not 1 <= len(line) <= 200:
        return False
    if line.strip() == "":
        return False
    if "\n" in line or "\r" in line:
        return False
    return True


def resolve_output_path():
    """Resolve the output path from OUTPUT_DIR (default /output)."""
    output_dir = os.environ.get("OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    return os.path.join(output_dir, OUTPUT_FILENAME)


def main():
    if not validate(LINE):
        raise ValueError("entry line fails validation")
    path = resolve_output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
