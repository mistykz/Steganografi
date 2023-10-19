import os
from PIL import Image

def check_rgb():
    # Buka gambar yang ingin di cek
    gambar= input("Input Image dengan Extensinya: ")
    image = Image.open(gambar)

    # Tentukan koordinat titik yang ingin dibaca
    x = int(input("Input koordinat x: "))
    y = int(input("Input koordinat y: "))

    # Baca nilai RGB dari pixel di titik tertentu
    pixel_color = image.getpixel((x, y))

    # Pisahkan nilai RGB
    red, green, blue = pixel_color

    print(f"Nilai RGB pada titik ({x}, {y}):")
    print(f"Red: {red}")
    print(f"Green: {green}")
    print(f"Blue: {blue}")

def edit_rgb():
    # Buka gambar yang ingin dirubah
    image=input("Input Image dengan Extensinya: ")
    citra_cover = Image.open(image)

    # Koordinat titik di mana kita ingin menulis nilai RGB
    x = int(input("Input koordinat x: "))
    y = int(input("Input koordinat y: "))

    # Baca nilai RGB dari pixel di titik tertentu
    pixel_color = citra_cover.getpixel((x, y))

    # Pisahkan nilai RGB
    red, green, blue = pixel_color

    # Nilai RGB yang ingin ditulis
    print(f"Nilai RGB yang ingin di rubah pada titik ({x}, {y}):")
    print(f"Red: {red}")
    print(f"Green: {green}")
    print(f"Blue: {blue}")

   # memasukkan warna RGB baru dalam format "R G B" pada titik yang dipilih
    input_warna_baru = input(
        "Masukkan Nilai RGB baru (Contoh, 255 0 0 untuk merah): ")

    # Memecah input RGB baru menjadi tiga komponen warna (R, G, B)
    komponen_warna = input_warna_baru.split()

    # Memastikan ada tiga komponen RGB yang valid
    if len(komponen_warna) == 3:
        red_new, green_new, blue_new = map(int, komponen_warna)

        # Ganti warna di titik yang sama dengan warna baru
        warna_baru = (red_new, green_new, blue_new)
        citra_cover.putpixel((x, y), warna_baru)
    else:
        print("Format warna RGB tidak valid. Harap masukkan tiga komponen Warna (R G B).")
    

    # Simpan citra cover yang telah diperbarui
    nama= input("Berikan nama untuk citra baru dan ekstensi (misal output.bmp): ")
    citra_cover.save(nama)

    # Tutup citra
    citra_cover.close()


while True:
    print("PROGRAM Baca dan Edit RGB")
    print("-------------")
    print("1. Baca RGB")
    print("2. Edit RGB")
    print("3. Keluar")

    pilihan = input("Input pilihan: ")

    if pilihan == '1':
        check_rgb()
    elif pilihan == '2':
        edit_rgb()
    elif pilihan == '3':
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
    user_input = input("Press Enter to continue...")