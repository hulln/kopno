import re

# določimo vhodno in izhodno datoteko
input_file = "input.txt"
output_file = "output.txt"

# ustvarimo slovar, ki povezuje username z anonimnimi ID-ji
id_map = {}

# odpremo input in output datoteki
with open(input_file, "r", encoding="utf-8") as in_file, open(output_file, "w", encoding="utf-8") as out_file:
    for line in in_file:
        # z regexi najdemo username v vsaki vrstici
        match = re.search(r"uporabnik: (.+)", line)
        if match:
            username = match.group(1)
            # če se username pojavi prvič, dodelimo ID
            if username not in id_map:
                id_map[username] = f"user_n1_{len(id_map)}"
            # zamenjamo username z ujemajočim ID
            line = line.replace(username, id_map[username])
        # zapišemo spremenjeno datoteko
        out_file.write(line)
