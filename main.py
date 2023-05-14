# Memasukkan pesan yang ingin dienkripsi
print("============")
print("| Sandi Angka  ")
print("============")
pesan = input(" Masukan Plaintext :  ")

# Array berisi kunci sandi
kunci_sandi = [1, 2, 3, 4, 5]

# Memasukkan pesan ke dalam array
pesan_array = []
for huruf in pesan:
    pesan_array.append(ord(huruf))

# Mengenkripsi pesan dengan menggeser ASCII code setiap karakter sebesar kunci sandi
pesan_terenkripsi = []
for i in range(len(pesan_array)):
    sandi = kunci_sandi[i % len(kunci_sandi)]
    pesan_terenkripsi.append(pesan_array[i] + sandi)

# Menampilkan pesan terenkripsi
print(" Pesan terenkripsi: ")
for kode in pesan_terenkripsi:
    print(kode, end=' ')

# Mendekripsi pesan dengan mengembalikan setiap karakter sesuai dengan kunci sandi
pesan_terdekripsi = ""
for i in range(len(pesan_terenkripsi)):
    sandi = kunci_sandi[i % len(kunci_sandi)]
    pesan_terdekripsi += chr(pesan_terenkripsi[i] - sandi)

# Menampilkan pesan terdekripsi
print("\n Pesan terdekripsi : ", pesan_terdekripsi)

# andhika Pratama 
