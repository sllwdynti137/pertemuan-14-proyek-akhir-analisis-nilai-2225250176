# TEST CASE PROGRAM ANALISIS NILAI SISWA

| ID | Kategori | Input | Expected Result |
|---|---|---|---|
| TC01 | Normal | 80, 70, 90 | Rata-rata 80 |
| TC02 | Batas | 0 | Nilai diterima |
| TC03 | Batas | 100 | Nilai diterima |
| TC04 | Invalid | 105 | Nilai ditolak |
| TC05 | Invalid | File tidak ditemukan | Error ditangani |
| TC06 | Normal | Semua nilai >= 70 | Semua siswa tuntas |

## Tujuan Pengujian

Pengujian dilakukan untuk memastikan program dapat
membaca, memvalidasi, menghitung, dan menganalisis
data nilai siswa dengan benar.

"test: menambahkan rancangan test case"