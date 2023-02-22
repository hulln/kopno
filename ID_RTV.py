import re

def replace_ids(input_file, output_file):
    # regexi za ujemanje ID-jev
    id_regex = r'(ID_komentarja|odgovor_na):\s*(rtv_\d+)'

    # slovar za povezovanje starih ID-jev z novimi (skupni vzorec)
    id_map = {}

    # števec za generiranje novih ID-jev
    id_counter = 0

    # odpremo datoteko in gremo čez vsako vrstico
    with open(input_file, 'r', encoding="utf-8") as fin, open(output_file, 'w', encoding="utf-8") as fout:
        for line in fin:
            # najdemo katerekoli številke v vrstici
            matches = re.findall(id_regex, line)

            # če smo našli ID, zamenjamo z novim ID-jem
            if matches:
                for match in matches:
                    id_type = match[0]
                    old_id = match[1]

                # če nismo še videli tega ID-ja, ustvarimo nov ID in ga dodamo v slovar
                if old_id not in id_map:
                    new_id = f'rtv_{id_counter}'
                    id_map[old_id] = new_id
                    id_counter += 1
                # sicer uporabimo prej ustvarjen ID
                else:
                    new_id = id_map[old_id]

                # zamenjamo stari ID z novim v vrstici
                line = re.sub(f'{id_type}:\s*{old_id}', f'{id_type}: {new_id}', line)

            # zapišemo vrstico v output datoteko
            fout.write(line)


if __name__ == '__main__':
    replace_ids('rtv_all_old.txt', 'rtv_all.txt')
