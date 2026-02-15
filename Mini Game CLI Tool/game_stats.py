import sys
from pathlib import Path


def recursion(path: Path, depth: int = 0):
    indent = " " * 4 * depth
    total_enemies = 0
    total_damage = 0
    try:
        elements = sorted(path.iterdir(), key=lambda p: p.name)
    except PermissionError:
        print(f"{indent}У вас не має доступу до {path.name}")
        return (0, 0)
    for file in elements:
        if file.is_dir():
            print(f"{indent}+ {file.name}/")
            sub_e, sub_d = recursion(file, depth + 1)
            total_enemies += sub_e
            total_damage += sub_d
        elif file.is_file():
            if file.suffix == ".txt":
                e, d = parse_log(file)
                total_enemies += e
                total_damage += d
                print(f"{indent} - {file.name} enemies: {e} damage: {d}")
    return (total_enemies, total_damage)


def parse_log(file_path: Path):
    enemy_count = 0
    damage_sum = 0
    try:
        with file_path.open("r", encoding="utf-8") as file_open:
            for line in file_open:
                clean_line = line.strip()
                if clean_line.startswith("ENEMY:"):
                    enemy_count += 1
                if clean_line.startswith("DAMAGE:"):
                    line_parts = clean_line.split(":")[1].strip()
                    try:
                        int_line_parts = int(line_parts)
                        damage_sum += int_line_parts
                    except ValueError:
                        print(f"Invalid damage value in {file_path.name}: {clean_line}")
    except PermissionError:
        print(f"No access to file: {file_path}")
        return (0, 0)
    return enemy_count, damage_sum


if len(sys.argv) != 2:
    print("Usage: python game_stats.py <folder_path>")
    sys.exit(1)
root_dir = Path(sys.argv[1])
if not root_dir.exists():
    print(f"This folder {root_dir} doesn't exist")
    sys.exit(1)
if not root_dir.is_dir():
    print(f"This {root_dir} not a directory")
    sys.exit(1)

grand_total = recursion(root_dir)
print("TOTAL:", grand_total)
