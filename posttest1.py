import os

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")

def back_to_menu():
	input("\nTekan 'Enter' untuk kembali...")
	show_menu()

def show_menu():
	clear_screen()
	kelompok = []
	print("============================================")
	print("| PROGRAM KLASIFIKASI ZONA RISIKO COVID-19 |")
	print("============================================")
	print("|                   OLEH                   |")
	print("============================================")
	print("|     ANDI ALFIAN BAHTIAR (2009106002)     |")
	print("|            INFORMATIKA A 2020            |")
	print("|              FAKULTAS TEKNIK             |")
	print("|          UNIVERSITAS MULAWARMAN          |")
	print("============================================")
	objek = int(input("| Masukkan Jumlah Kab/Kota : "))
	clear_screen()
	print("============================================")
	print("| PROGRAM KLASIFIKASI ZONA RISIKO COVID-19 |")
	print("============================================")
	while objek > 0:
		nama = input("| Masukkan Nama Kota/Kab               : ")
		positif = int(input("| Masukkan Jumlah Pasien Terkonfirmasi : "))
		sembuh = int(input("| Masukkan Jumlah Pasien Sembuh        : "))
		meninggal = int(input("| Masukkan Jumlah Pasien Meninggal     : "))
		kasus_aktif = positif-sembuh-meninggal
		risiko = ""
		if kasus_aktif > 51:
			risiko = "Risiko Tinggi"
		elif kasus_aktif > 25:
			risiko = "Zona Risiko Sedang"
		elif kasus_aktif > 0:
			risiko = "Zona Risiko Rendah"
		elif kasus_aktif < 1:
			risiko = "Zona Tidak Terdampak"
		kelompok.append([nama, positif, sembuh, meninggal, kasus_aktif, risiko])
		print("============================================")
		objek -= 1
	clear_screen()
	print("============================================")
	print("| PROGRAM KLASIFIKASI ZONA RISIKO COVID-19 |")
	print("============================================")
	for i in range(len(kelompok)):
		print("| Kota/Kab ke-%d" % (i + 1))
		print("| Nama Kota/Kab               :", kelompok[i][0])
		print("| Jumlah Pasien Terkonfirmasi :", kelompok[i][1])
		print("| Jumlah Pasien Sembuh        :", kelompok[i][2])
		print("| Jumlah Pasien Meninggal     :", kelompok[i][3])
		print("| Jumlah Kasus Aktif          :", kelompok[i][4])
		print("| Status                      :", kelompok[i][5])
		print("============================================")
	back_to_menu()

if __name__ == "__main__":
	try:
		show_menu()
	except KeyboardInterrupt:
		print("============================================================================")
		print("| Terima kasih telah menggunakan Aplikasi Klasifikasi Zona Risiko COVID-19 |")
		print("============================================================================")
		exit()
