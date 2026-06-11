#Raka Emillul Fata
#Latihan 3 : Simpan Hasil

def simpan_hasil(nama_file, rata):
    with open("hasil.txt", 'w') as file:
        file.write(f"Hasil Rata-rata: {rata}\n")