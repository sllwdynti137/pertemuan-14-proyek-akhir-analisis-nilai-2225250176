def validasi_nilai(nilai):
    return 0 <= nilai <= 100


def baca_data(path):
    data = []

    try:
        with open(path, "r") as file:
            for baris in file:
                try:
                    nama, nilai = baris.strip().split(",")
                    nilai = float(nilai)

                    if validasi_nilai(nilai):
                        data.append({
                            "nama": nama,
                            "nilai": nilai
                        })
                    else:
                        print(f"Nilai {nama} tidak valid.")

                except ValueError:
                    print("Format data tidak sesuai.")

    except FileNotFoundError:
        print("File nilai tidak ditemukan.")

    return data