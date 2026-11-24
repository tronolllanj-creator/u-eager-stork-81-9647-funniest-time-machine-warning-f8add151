import os
"""Write the required funny quote to entry.txt with validation and mirroring."""
# Entry validated: output is 1-120 chars, one line, deterministic.

LINE = "Accidentally preventing your own birth will be billed to your estate as an early termination fee."

def main():
    content = LINE + "\n"
    if not (1 <= len(content) <= 120 and content.strip()):
        raise ValueError("Invalid content length or whitespace-only")
    if content.count("\n") != 1 or content.endswith("\n\n"):
        raise ValueError("Must contain exactly one line")

    primary_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(primary_dir, exist_ok=True)
    primary_path = os.path.join(primary_dir, "entry.txt")

    with open(primary_path, "w", encoding="utf-8") as f:
        f.write(content)

    if primary_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass

    print(primary_path)
    print(len(content))

if __name__ == "__main__":
    main()
