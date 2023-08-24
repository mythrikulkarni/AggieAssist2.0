import re
import json

# The input text you provided
input_text = """
Code Title Units Preparatory Subject Matter
African American & African Studies
AAS 010
or AAS 012
Choose one:
AAS 015
AAS 017
AAS 018
AAS 050
AAS 051
AAS 052
AAS 080
Choose one:
ANT 002
ECN 001A
or ECN 001AV
or ECN 001AY
African American & African Studies
ECN 001B
or ECN 001BV
SOC 001
POL 001
or PSC 001Y
POL 002
PSC 001
Choose one:
CHI 010
NAS 001
NAS 010
GSW 050
AMS 010
ASA 001
ASA 002
History
Choose two:
HIS 015A
HIS 015B
HIS 017A
HIS 017B
Choose one:
AAS 016
AAS 051
AAS/DRA 155A
DRA 041A
DRA 041B
DRA 044A
DRA 044B
MUS 028
MUS 105
Depth Subject Matter
Choose one:
AAS 100
AAS 101
AAS 107A
AAS 107B
AAS 107C
AAS 110
AAS 145B
AAS 172
AAS 180
Choose one:
AAS 150A
AAS 150B
AAS 151
AAS 152
AAS 153/COM 154
AAS/DRA 155A
AAS 156
AAS 157
AAS 160
AAS 169
AAS 170
AAS 171
AAS 175A
AAS 175B
AAS 181
AAS 182
AAS 185
Choose one:
AAS 111
AAS 123
AAS 130
AAS 133
AAS 141
AAS 145A
AAS 145B
AAS 156
AAS 162
AAS 163
AAS 165
AAS 172
AAS 176
AAS 177
Depth Subject Matter Subtotal 36
Total Units 64
"""

course_code_pattern = re.compile(r'[A-Z]{2,4}\s\d{3}')

major_data = {
    "African American & African Studies": {
        "Total Units": "",
        "Courses": {}
    }
}
current_major = "African American & African Studies"
current_course_category = None
current_courses = []

lines = input_text.strip().split('\n')

for line in lines:
    if line.startswith("Total Units"):
        major_data[current_major]["Total Units"] = line.split()[-1]
    elif course_code_pattern.match(line):
        current_courses.append(line.strip())
    elif any(keyword in line for keyword in ["Choose one", "Choose two", "Choose three", "Choose a series", "Mandatory Courses"]):
        if current_course_category and current_courses:
            major_data[current_major]["Courses"][current_course_category] = current_courses
        current_courses = []
        current_course_category = line
    elif line.strip() == "":
        if current_course_category and current_courses:
            major_data[current_major]["Courses"][current_course_category] = current_courses
        current_courses = []

json_data = {"majors": major_data}

with open('outputjson.json', 'w') as output_file:
    json.dump(json_data, output_file, indent=4)

print("JSON file 'outputjson.json' has been generated.")