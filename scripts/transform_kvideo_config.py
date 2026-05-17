import json
import os
import re
from typing import Any, Dict, List

INPUT_FILE = os.getenv("SOURCE_FILE", "source/LunaTV-config.json")
OUTPUT_FILE = os.getenv("KVIDEO_FILE", "video/config_kvideo.json")


def convert_kvideo_config(original_config: Dict[str, Any]) -> List[Dict[str, Any]]:
    result: List[Dict[str, Any]] = []
    normal_priority = 1
    premium_priority = 1

    api_site = original_config.get("api_site", {})

    numbered_keys = []
    other_keys = []

    for key in api_site.keys():
        if re.match(r"^api_\d+$", key):
            numbered_keys.append(key)
        else:
            other_keys.append(key)

    numbered_keys.sort(key=lambda x: int(x.replace("api_", "")))

    premium_keywords = [
        "AV-", "AV", "91麻豆", "奥斯卡", "奶香香", "淫水机", "玉兔",
        "白嫖", "精品", "美少女", "老色逼", "色南国", "色猫", "辣椒",
        "香奶儿", "鲨鱼", "黄AV", "JKUN", "番号", "森林", "AIVin",
        "souav", "乐播", "麻豆", "色", "黄", "淫", "91",
    ]

    for key in numbered_keys:
        item = api_site[key]
        id_num = int(key.replace("api_", ""))
        source_id = f"source_{id_num}"
        name = item.get("name", "")
        base_url = item.get("api", "")

        group = "normal"
        for keyword in premium_keywords:
            if keyword in name:
                group = "premium"
                break

        new_item = {
            "id": source_id,
            "name": name,
            "baseUrl": base_url,
            "group": group,
        }

        if group == "premium":
            new_item["enabled"] = True
            new_item["priority"] = premium_priority
            premium_priority += 1
        else:
            new_item["priority"] = normal_priority
            normal_priority += 1

        result.append(new_item)

    other_premium_keywords = [
        "快播", "杏吧", "森林", "黄色", "辣椒", "细胞采集黄色",
        "xingba", "senlin", "huangse", "lajiao", "xibao",
    ]

    for index, key in enumerate(other_keys):
        item = api_site[key]
        source_id = f"source_{len(numbered_keys) + index + 1}"
        name = item.get("name", "")
        base_url = item.get("api", "")

        group = "normal"
        for keyword in other_premium_keywords:
            if keyword in name.lower() or keyword in key.lower():
                group = "premium"
                break

        new_item = {
            "id": source_id,
            "name": name,
            "baseUrl": base_url,
            "group": group,
        }

        if group == "premium":
            new_item["enabled"] = True
            new_item["priority"] = premium_priority
            premium_priority += 1
        else:
            new_item["priority"] = normal_priority
            normal_priority += 1

        result.append(new_item)

    return result


def main() -> None:
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found in {os.getcwd()}")
        print(f"Current directory contents: {os.listdir('.')}")
        if os.path.exists("video"):
            print(f"Video directory contents: {os.listdir('video')}")
        raise SystemExit(1)

    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            original_config = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: JSON parsing failed - {e}")
        raise SystemExit(1)

    converted_array = convert_kvideo_config(original_config)

    normal_count = len([item for item in converted_array if item["group"] == "normal"])
    premium_count = len([item for item in converted_array if item["group"] == "premium"])

    print(f"Converted {len(converted_array)} sources.")
    print(f"Normal: {normal_count}, Premium: {premium_count}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(converted_array, f, ensure_ascii=False, indent=2)

    print(f"Successfully saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
