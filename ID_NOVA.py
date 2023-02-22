with open('nova_all.txt','r',encoding='utf8') as input_file:
    with open('nova_all_prepis.txt', 'w', encoding='utf8') as output_file:
        i = 0
        vsebina = input_file.readlines()
        uporabnik = 0
        id_komentarja = 0
        for number, vrstica in enumerate(vsebina):
            if vrstica.startswith('uporabnik'):
                prejsnji_uporabnik = uporabnik
                prejsnji_ID = id_komentarja
                uporabnik = vrstica.rstrip(' </span>').rstrip().split('uporabnik: ')[-1]
                #print(uporabnik)
                output_file.write(vrstica)
                id_komentarja = "nova24_" + str(i)
                output_file.write('ID_komentarja: ' + id_komentarja+'\n')
                i += 1
                if vsebina[number+2].startswith('komentar: '):
                    glavni_uporabnik = uporabnik
                    id_glavnega_komentarja = id_komentarja
            elif vrstica.startswith("odgovor_uporabniku:"):
                if vrstica.rstrip().split('uporabniku: ')[-1] == glavni_uporabnik:
                    output_file.write('odgovor na: ' + id_glavnega_komentarja + '\n')
                elif vrstica.rstrip().split('uporabniku: ')[-1] == prejsnji_uporabnik:
                    output_file.write('odgovor_na: ' + prejsnji_ID+ '\n')
            else:
                output_file.write(vrstica)