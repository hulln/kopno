# odpremo datoteko
with open("24ur_all.txt", 'r', encoding='utf8') as input_file:

    # nastavimo izhodno, novo datoteko, kamor zapisujemo
    with open("24ur_all_prepis.txt", 'w', encoding='utf8') as output_file:

        i = 0 # nastavimo neko začetno številko za pripisovanje IDjev
        vsebina = input_file.readlines()   # .readlines() prebere vsebino datoteke in jo shrani v seznam vrstic

        for vrstica in vsebina:
            if vrstica.startswith("uporabnik"): # ko se vrstica začne s tem nizom, je nov komentar
                output_file.write(vrstica)
                id_komentarja = "24ur_" + str(i) # pripišemo ID
                output_file.write('ID komentarja: ' + id_komentarja+'\n') # zapišemo metapodatek z ID-jem v izhodno datoteko
                i += 1 # povečamo spremenljivko i za 1, da je pripravljen nov ID za naslednji komentar
            elif vrstica.rstrip() == "odgovor: ne":
                id_glavnega_komentarja = id_komentarja
                output_file.write("")
            elif vrstica.rstrip() == "odgovor: da":
                output_file.write("odgovor na: " + id_glavnega_komentarja + '\n')
            else:
                output_file.write(vrstica)