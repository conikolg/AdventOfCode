import re
from datetime import datetime
from pathlib import Path


def main():
    # Get current day
    today = datetime.today()
    # Create folder for day
    day_folder = Path(str(today.day + 1).rjust(2, "0"))
    day_folder.mkdir(exist_ok=False)

    # Create empty files for example and problem input
    with open(day_folder / "ex", "w") as f:
        pass
    with open(day_folder / "in", "w") as f:
        pass

    # Create template Python files
    content = """
def load_file(filename):
    with open(filename, "r") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


def main(lines):
    pass


if __name__ == '__main__':
    main(load_file(filename="in"))

"""
    with open(day_folder / "q1.py", "w") as f:
        f.write(content)
    with open(day_folder / "q2.py", "w") as f:
        f.write(content)

    # Get README.md contents
    with open("README.md", "r") as f:
        lines = f.readlines()

    last_line = lines[-1]
    tbd_pattern = re.compile(r"Day \d+: TBD")
    tbd_line = re.findall(tbd_pattern, last_line)
    # Hyperlink current day to folder
    current_day_line = last_line.replace(tbd_line[0], f"[{tbd_line[0]}]({str(today.day + 1).rjust(2, '0')})")
    # Create placeholder for next day
    next_day_line = last_line.replace(tbd_line[0], f"Day {str(today.day + 2).rjust(2, '0')}: TBD")

    # Adjust file contents
    lines.pop(-1)
    lines.append(current_day_line + "\n")
    lines.append(next_day_line + "\n")

    # Write contents to and update README.md
    with open("README.md", "w") as f:
        f.writelines(lines)


if __name__ == '__main__':
    main()
