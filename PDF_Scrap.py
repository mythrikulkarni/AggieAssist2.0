# Ouputs the Prep and Depth Subject Matter for the first major in the catalog

# Read the content from the input text file
with open('output_text.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Find the index of "Code Title Units Preparatory Subject Matter"
start_index = content.find("Code Title Units Preparatory Subject Matter")

# Find the index of "Depth Subject Matter" after the start index
depth_index = content.find("Depth Subject Matter", start_index)

# Find the index of "Total Units" after the depth index
total_units_index = content.find("Total Units", depth_index)

# Extract preparatory section
preparatory_section = content[start_index:depth_index].strip()

# Extract depth section
depth_section = content[depth_index:total_units_index].strip()

# Write preparatory section to a text file
with open('output_preparatory.txt', 'w', encoding='utf-8') as prep_file:
    prep_file.write(preparatory_section)

# Write depth section to a text file
with open('output_depth.txt', 'w', encoding='utf-8') as depth_file:
    depth_file.write(depth_section)
