with open('n1_all.txt','r',encoding='utf8') as input_file:
    with open('n1_all_prepis.txt', 'w', encoding='utf8') as output_file:

        i = 0
        vsebina = input_file.readlines()

        for number, vrstica in enumerate(vsebina):
            if vrstica.startswith('uporabnik'):
                uporabnik = vrstica.rstrip().split(' ')[-1]
                output_file.write(vrstica)
                id_komentarja = "n1_" + str(i)
                output_file.write('ID_komentarja: ' + id_komentarja+'\n')
                i += 1

                if vsebina[number+2].startswith('komentar: '):
                    glavni_uporabnik = uporabnik
                    id_glavnega_komentarja = id_komentarja

            elif vrstica.startswith("odgovor_uporabniku:"):
                output_file.write('odgovor_na: ' + id_glavnega_komentarja + '\n')
            else:
                output_file.write(vrstica)