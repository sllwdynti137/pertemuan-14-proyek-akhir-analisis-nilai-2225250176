# PROGRAM ANALISIS NILAI SISWA

## 1. Deskripsi Proyek

Program Analisis Nilai Siswa merupakan program sederhana berbasis Python yang dibuat untuk membantu proses pengolahan dan analisis nilai siswa secara otomatis.

Program ini dapat membaca data nilai siswa, melakukan validasi nilai, menghitung rata-rata, menentukan nilai tertinggi dan terendah, serta mengetahui jumlah siswa yang tuntas dan belum tuntas berdasarkan KKM.

## 2. Tujuan Proyek

1. Mempermudah proses pengolahan nilai siswa.
2. Menghitung statistik nilai secara otomatis.
3. Menentukan status ketuntasan siswa.
4. Mengurangi kesalahan dalam perhitungan manual.
5. Menyimpan hasil analisis dalam bentuk laporan.

## 3. Fitur Program

- Membaca data nilai siswa dari file.
- Memvalidasi nilai dalam rentang 0–100.
- Menghitung rata-rata nilai.
- Menampilkan nilai tertinggi dan terendah.
- Menghitung jumlah siswa tuntas dan belum tuntas.
- Menyimpan hasil analisis ke file laporan.

## 4. Pengguna Program

Program ini ditujukan untuk guru atau pengguna yang membutuhkan pengolahan dan rekapitulasi nilai siswa secara sederhana.

## 5. Teknologi yang Digunakan

- Python
- Visual Studio Code
- Git
- GitHub

## 6. Struktur Folder

```text
proyek-analisis-nilai/
│
├── README.md
├── proposal.md
├── .gitignore
│
├── data/
│   └── nilai_siswa.txt
│
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
│
├── tests/
│   └── test_case.md
│
└── output/
    └── .gitkeep
```

## 7. Input, Proses, dan Output

**Input:**
- Nama siswa.
- Nilai siswa.
- Data dari file nilai_siswa.txt.
- Kriteria Ketuntasan Minimal (KKM).

**Proses:**
- Membaca data siswa.
- Memvalidasi nilai.
- Menghitung rata-rata, nilai minimum, dan maksimum.
- Menentukan status ketuntasan.

**Output:**
- Jumlah siswa.
- Rata-rata nilai.
- Nilai tertinggi dan terendah.
- Jumlah siswa tuntas dan belum tuntas.
- Laporan hasil analisis.

## 8. Cara Menjalankan Program

Pastikan Python sudah terinstal, kemudian buka terminal VS Code dan jalankan:

```bash
python src/main.py
```

## 9. Hasil yang Diharapkan

Program dapat menampilkan hasil analisis nilai siswa melalui terminal dan menyimpan hasilnya dalam file `output/laporan_nilai.txt`.

## 10. Status Proyek

Proyek ini dirancang pada Pertemuan 14 dan dilanjutkan dengan implementasi, pengujian, debugging, serta dokumentasi pada Pertemuan 15.

## 11. Anggota Kelompok

1. Sela Widiyanti

"docs: menambahkan proposal proyek analisis nilai"