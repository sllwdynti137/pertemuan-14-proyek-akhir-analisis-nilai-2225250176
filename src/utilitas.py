
def tentukan_status(data, kkm):
    tuntas = 0
    belum_tuntas = 0

    for siswa in data:
        if siswa["nilai"] >= kkm:
            tuntas += 1
        else:
            belum_tuntas += 1

    return {
        "tuntas": tuntas,
        "belum_tuntas": belum_tuntas
    }


def simpan_laporan(statistik, status):
    with open("output/laporan_nilai.txt", "w") as file:
        file.write("HASIL ANALISIS NILAI SISWA\n")
        file.write("==========================\n")
        file.write(f"Rata-rata: {statistik['rata_rata']:.2f}\n")
        file.write(f"Nilai tertinggi: {statistik['maksimum']}\n")
        file.write(f"Nilai terendah: {statistik['minimum']}\n")
        file.write(f"Jumlah tuntas: {status['tuntas']}\n")
        file.write(f"Jumlah belum tuntas: {status['belum_tuntas']}\n")

    print("Laporan berhasil disimpan.")
