import os

import base58

INPUT_PATH = os.getenv("SOURCE_FILE", "source/LunaTV-config.json")
OUTPUT_PATH = os.getenv("BASE58_FILE", "video/config_moontv_base58.json")


def main() -> None:
    if not os.path.exists(INPUT_PATH):
        print(f"Error: File {INPUT_PATH} not found!")
        raise SystemExit(1)

    with open(INPUT_PATH, "rb") as f:
        content = f.read()

    encoded = base58.b58encode(content)

    with open(OUTPUT_PATH, "wb") as f:
        f.write(encoded)

    print(f"Successfully encoded {INPUT_PATH} to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
