def hitung_statistik(data):
    if not data:
        return None

    nilai = [siswa["nilai"] for siswa in data]

    statistik = {
        "rata_rata": sum(nilai) / len(nilai),
        "minimum": min(nilai),
        "maksimum": max(nilai)
    }

    return statistik