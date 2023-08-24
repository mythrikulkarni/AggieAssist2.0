import re
import json

#takes txt file with course reqs for a major and formats into JSON file
def major_list_2_JSON(input_file, output_file):
    with open(input_file, "r") as file:
        content = file.read()

    #split file into list of strings
    lines = content.strip().split("\n")

    choose_one = []
    choose_two = []
    choose_three = []
    mandatory = []

    i = 2
    while i < len(lines):
        current_group = []
        or_group = []
        line = lines[i].strip()

        #if line contains 'choose one', runs thru the next following lines until a non coursecode is found
        if re.search(r"choose one", line, re.IGNORECASE): 
            i += 1
            while i < len(lines) and (
                lines[i].startswith("or") or re.match(r"^[A-Z]{3}", lines[i])):
                or_group = []
                if lines[i].startswith("or"): #creates a new embedded list for "or" classes
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

        #if line contains 'choose two', runs thru the next following lines until a non coursecode is found
        elif re.search(r"choose two", line, re.IGNORECASE):
            i += 1
            while i < len(lines) and (
                lines[i].startswith("or") or re.match(r"^[A-Z]{3}", lines[i])):
                or_group = []
                if lines[i].startswith("or"): #creates a new embedded list for "or" classes
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
        
        #if line contains 'choose three', runs thru the next following lines until a non coursecode is found
        elif re.search(r"choose three", line, re.IGNORECASE):
            i += 1
            while i < len(lines) and (
                lines[i].startswith("or") or re.match(r"^[A-Z]{3}", lines[i])):
                or_group = []
                if lines[i].startswith("or"): #creates a new embedded list for "or" classes
                    current_group.pop()
                    or_group.append(lines[i - 1])
                    while i < len(lines) and (lines[i].startswith("or")):
                        or_group.append(lines[i][3:])
                        i += 1
                    current_group.append(or_group)
                else:
                    current_group.append(lines[i])
                    i += 1
            choose_three.append(current_group)

        #if not a part of choose ___ group, coursecode is added to mandatory courses
        elif re.match(r"^[A-Z]{3}", line) or line.startswith("or"):
            or_group = []
            if lines[i].startswith("or"):
                mandatory.pop()
                or_group.append(lines[i - 1])
                while i < len(lines) and (lines[i].startswith("or")):
                    or_group.append(lines[i][3:])
                    i += 1
                choose_one.append(or_group)
            else:
                mandatory.append(line)
                i += 1
        else:
            i += 1

    jv_data = {
        "choose one": choose_one,
        "choose two": choose_two,
        "choose three": choose_three,
        "mandatory": mandatory,
    }

    jv_courses = {
        "courses": jv_data
    }

    jv = {
        lines[1]: jv_courses 
    }

    json.dump(jv, output_file, indent=4)


outfile = open("African_American_Studies.json", "w")

major_list_2_JSON("major.txt", outfile)
