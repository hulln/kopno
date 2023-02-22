import re
import keyboard

input_file = "24ur_all_prepis.txt"
output_file = "comments_anon_24ur.txt"
final_file = "comments_anon_manual_24ur.txt"

# ta program je v prvi fazi enak tistemu za anonimizacijo uporabnikov
id_map = {}

with open(input_file, "r", encoding="utf-8") as in_file, open(output_file, "w", encoding="utf-8") as out_file:
    for line in in_file:
        match = re.search(r"uporabnik: (.+)", line)
        if match:
            username = match.group(1)
            if username not in id_map:
                id_map[username] = f"user_24ur_{len(id_map)}"
            line = line.replace(username, id_map[username])
        out_file.write(line)

# v tej fazi nastavimo ročno potrjevanje ali zavračanje zaznanih in predlaganih sprememb
with open(output_file, "r", encoding="utf-8") as in_file, open(final_file, "w", encoding="utf-8") as out_file:
    for line in in_file:
        for uid in id_map.keys():
            if uid in line:
                print("Found a match. Will replace the following:", uid)
                print(line.strip())
                indices_object = re.finditer(pattern=uid, string=line)
                indices = [index.start() for index in indices_object]
                for n, i in enumerate(indices):
                    print(" " * i + "|||||")
                print(line.replace(uid, id_map[uid]).strip())
                print("Press <enter> to accept the change or any other key to reject.")

                keyboard.read_key()
                if keyboard.is_pressed("enter"):
                    print("Change accepted!")
                    line = line.replace(uid, id_map[uid])
                else:
                    print("Change rejected!")

        out_file.write(line)