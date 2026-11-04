from data_io import baca_data
from analisis import hitung_statistik
from utilitas import tentukan_status, simpan_laporan


def main():
    data = baca_data("data/nilai_siswa.txt")

    if not data:
        print("Tidak ada data yang dapat dianalisis.")
        return

    statistik = hitung_statistik(data)
    status = tentukan_status(data, 70)

    print("\n=== HASIL ANALISIS NILAI SISWA ===")
    print("Jumlah siswa:", len(data))
    print("Rata-rata:", round(statistik["rata_rata"], 2))
    print("Nilai tertinggi:", statistik["maksimum"])
    print("Nilai terendah:", statistik["minimum"])
    print("Jumlah siswa tuntas:", status["tuntas"])
    print("Jumlah siswa belum tuntas:", status["belum_tuntas"])

    simpan_laporan(statistik, status)


if __name__ == "__main__":
    main()