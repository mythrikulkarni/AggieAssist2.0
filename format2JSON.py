import re
import json


def major_list_2_JSON(lines, output_file):
    choose_one = []
    choose_two = []
    mandatory = []

    i = 1
    while i < len(lines):
        current_group = []
        or_group = []
        line = lines[i].strip()
        if "Choose one" in line:
            i += 1
            while i < len(lines) and (
                lines[i].startswith("or") or re.match(r"^[A-Z]{3}", lines[i])
            ):
                or_group = []
                if lines[i].startswith("or"):
                    current_group.pop()
                    or_group.append(lines[i - 1])
                    while i < len(lines) and (lines[i].startswith("or")):
                        or_group.append(lines[i][3:])
                        i += 1
                    current_group.append(or_group)
                else:
                    current_group.append(lines[i])
                    i += 1
            choose_one.append(current_group)
        elif re.search(r"choose two", line, re.IGNORECASE):
            i += 1
            while i < len(lines) and (
                lines[i].startswith("or") or re.match(r"^[A-Z]{3}", lines[i])
            ):
                or_group = []
                if lines[i].startswith("or"):
                    current_group.pop()
                    or_group.append(lines[i - 1])
                    while i < len(lines) and (lines[i].startswith("or")):
                        or_group.append(lines[i][3:])
                        i += 1
                    current_group.append(or_group)
                else:
                    current_group.append(lines[i])
                    i += 1
            choose_two.append(current_group)
        elif re.match(r"^[A-Z]{3}", line) or line.startswith("or"):
            or_group = []
            if lines[i].startswith("or"):
                mandatory.pop()
                or_group.append(lines[i - 1])
                while i < len(lines) and (lines[i].startswith("or")):
                    or_group.append(lines[i][3:])
                    i += 1
                mandatory.append(or_group)
            else:
                mandatory.append(line)
                i += 1
        else:
            i += 1

    jv_data = {
        "choose one": choose_one,
        "choose two": choose_two,
        "mandatory": mandatory,
    }

    jv_courses = {
        "courses": jv_data
    }

    jv = {
        lines[0]: jv_courses 
    }

    json.dump(jv, output_file, indent=4)


with open("major.txt", "r") as file:
    content = file.read()

split_file = content.strip().split("\n")

outfile = open("African_American_Studies.json", "w")

major_list_2_JSON(split_file, outfile)
