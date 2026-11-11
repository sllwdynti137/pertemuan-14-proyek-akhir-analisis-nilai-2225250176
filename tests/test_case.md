
# TEST CASE PROGRAM ANALISIS NILAI SISWA

## Tujuan Pengujian

Pengujian dilakukan untuk memastikan program dapat
membaca, memvalidasi, menghitung, dan menganalisis
data nilai siswa dengan benar.

## Tabel Pengujian

| ID | Kategori | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC01 | Normal | 80, 70, 90 | Rata-rata 80 | Belum diuji | - |
| TC02 | Batas | 0 | Nilai diterima | Belum diuji | - |
| TC03 | Batas | 100 | Nilai diterima | Belum diuji | - |
| TC04 | Invalid | 105 | Nilai ditolak | Belum diuji | - |
| TC05 | Invalid | File tidak ditemukan | Error ditangani | Belum diuji | - |
| TC06 | Normal | Semua nilai >= 70 | Semua siswa tuntas | Belum diuji | - |