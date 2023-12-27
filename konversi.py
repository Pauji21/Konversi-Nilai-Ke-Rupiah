angka = 10000000
angka_lemari = list(str(angka))
angka_lemari.reverse()

for x in range(len(angka_lemari)):
    if (x+1) % 3 == 0 and x != len(angka_lemari)-1:
        angka_lemari[x] = f".{angka_lemari[x]}"
        
angka_lemari.reverse()
finals = "".join(angka_lemari)
print(f"Rp. {finals},00")