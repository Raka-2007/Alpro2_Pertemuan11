#Raka Emillul Fata
#Latihan 2 : Hitung Rata-rata

def hitung_rata(data):
    if len(data) == 0:
        return 0
    return sum(data.values()) / len(data)
