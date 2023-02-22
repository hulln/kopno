import pandas as pd

# odpremo izvorno datoteko v načinu za branje
with open('input.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# razdelimo dokument v individualne sekcije komentarjev
comments = content.split('\n\n')

# ustvarimo prazen seznam za podatke
data = []

# gremo skozi vsako sekcijo in izluščimo podatke
for comment in comments:
    # splitamo sekcijo na posamezne vrstice
    lines = comment.split('\n')

    if len(lines) not in [5, 6]: # izpustimo, če je vrstic različno od 5 ali 6
        #print(f"sekcija {lines} ima toliko vrstic: {len(lines)}, kar ni enako 5 oz. 6")
        continue


    # preverimo uporabniško ime
    #print(f"uporabnik: {lines[0]}")
    uporabnik = lines[0].split(": ")
    username = uporabnik[-1]
    #print(len(username))
    #print(f"username uporabnika: {username}")
    if len(username) < 1:
        #print("Ni uporabnika.")
        username = None

    # preverimo id komentarja
    #print(f"ID: {lines[1]}")
    id = lines[1].split(": ")
    id_komentarja = id[-1]
    #print(id_komentarja)
    if len(id_komentarja) < 1:
        id_komentarja = None

    # preverimo datum in uro
    #print(f"datum čas: {lines[2]}")
    cas = lines[2].split(": ")
    datum_ura = cas[-1]
    #print(datum_ura)
    if len(datum_ura) < 1:
        datum_ura = None


    if len(lines) == 5: # v nadaljevanju delimo komentarje z replyji in tiste brez, najprej gremo čez te brez
        # preverimo vsebino komentarja
        vsebina = lines[3].split(": ")
        komentar = vsebina[-1]
        #print(komentar)
        if len(komentar) < 1:
            komentar = None

        # preverimo vir
        link = lines[4].split(": ")
        vir = link[-1]
        #print(vir)
        if len(vir) < 1:
            vir = None

        data.append([username, id_komentarja, datum_ura, komentar, vir])


    elif len(lines) == 6: # preverjamo še za replyje
        # preverimo podatek o replyju
        odgovor = lines[3].split(": ")
        odgovor_na = odgovor[-1]
        #print(odgovor_na)
        if len(odgovor) < 1:
            odgovor = None

        # preverimo vsebino komentarja
        vsebina = lines[4].split(": ")
        komentar = vsebina[-1]
        # print(komentar)
        if len(komentar) < 1:
            komentar = None

        # preverimo vir
        link = lines[5].split(": ")
        vir = link[-1]
        # print(vir)
        if len(vir) < 1:
            vir = None

        data.append([username, id_komentarja, datum_ura, komentar, vir, odgovor_na])



# ustvarimo pandas dataframe iz seznama
df = pd.DataFrame(data, columns=['uporabnik', 'ID_komentarja', 'datum_ura', 'komentar', 'vir', 'odgovor_na'])

# shranimo dataframe kot CSV
df.to_csv('output.csv', encoding='utf-8-sig', index=False)