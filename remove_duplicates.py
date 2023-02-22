# koda s seznami
with open('comments_anon_rtv.txt', 'r', encoding="utf-8") as f:

    vsebina = f.read()

unikati = []

komentarji = vsebina.split('\n\n')
for komentar in komentarji:
    #print(f"en komentar:\n{komentar}\n")
    s_komentar = komentar.split("\n")
    new_komentar = []
    for vrstica in s_komentar:
        new_komentar.append(vrstica.strip())
    komentar = "\n".join(new_komentar)

    if komentar in unikati:
        continue
    else:
        unikati.append(komentar)


with open('comments_anon_rtv_unikati.txt', 'w', encoding="utf-8") as f:
    for komentar in unikati:
        f.write(f"{komentar}\n\n")