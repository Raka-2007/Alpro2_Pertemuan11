#Parsing File
def baca_file(nama_file):
    data = {}
    try:
        with open(nama_file, 'r') as file:
            for baris in file:
                nim, nilai = baris.strip().split(',')
                data[nim] = int(nilai)

        return data

    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")
        return {}

#Hitung Rata-rata
def hitung_rata(data):
    if len(data) == 0:
        return 0
    return sum(data.values()) / len(data)

#Nilai Tertinggi
def nilai_tertinggi(data):
    nim = max(data, key=data.get)
    return nim, data[nim]

#Nilai Terendah
def nilai_terendah(data):
    nim = min(data, key=data.get)
    return nim, data[nim]

#Simpan Hasil
def simpan_hasil(nama_file, rata):
    with open(nama_file, 'w') as file:
        file.write(f"Hasil Rata-rata: {rata}\n")

#Main
def main():
    nama_file = input("Masukkan nama file: ")
    data = baca_file(nama_file)

    if data:
        print("Data:", data)

        rata = hitung_rata(data)
        print("Rata-rata:", rata)

        nim_tinggi, nilai_tinggi = nilai_tertinggi(data)
        print(f"Nilai tertinggi : {nilai_tinggi} (NIM {nim_tinggi})")

        nim_rendah, nilai_rendah = nilai_terendah(data)
        print(f"Nilai terendah : {nilai_rendah} (NIM {nim_rendah})")

        simpan_hasil(nama_file, rata)
        print(f"Hasil disimpan ke {nama_file}.")

main()