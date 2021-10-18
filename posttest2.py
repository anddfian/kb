import os
import pandas as pd
from tabulate import tabulate

csv_filename_covid = "covid19.csv"

df_covid = pd.DataFrame()

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")

def back_to_show_zona():
	input("\nTekan 'Enter' untuk kembali...")
	show_zona()

def back_to_show_menu():
	input("\nTekan 'Enter' untuk kembali...")
	show_menu()

def close_app():
	clear_screen()
	print("========================================================================================================")
	print("|               Terima kasih telah menggunakan Aplikasi Klasifikasi Zona Risiko COVID-19               |")
	print("========================================================================================================")
	exit()

def show_menu():
	clear_screen()
	print("========================================================================================================")
	print("|                               PROGRAM KLASIFIKASI ZONA RISIKO COVID-19                               |")
	print("========================================================================================================")
	print("|                                                 OLEH                                                 |")
	print("========================================================================================================")
	print("|                                   ANDI ALFIAN BAHTIAR (2009106002)                                   |")
	print("|                                          INFORMATIKA A 2020                                          |")
	print("|                                            FAKULTAS TEKNIK                                           |")
	print("|                                        UNIVERSITAS MULAWARMAN                                        |")
	print("========================================================================================================")
	print("| [1] Lihat Data Zona Risiko COVID-19                                                                  |")
	print("| [2] Tambah Data Zona Risiko COVID-19                                                                 |")
	print("| [0] Keluar                                                                                           |")
	print("========================================================================================================")
	try:
		selected_menu = int(input("| Pilih menu> "))
		if selected_menu == 1:
			show_zona()
		elif selected_menu == 2:
			create_zona()
		elif selected_menu == 0:
			close_app()
		else:
			print("========================================================================================================")
			print("| Error: Kamu memilih menu yang salah!                                                                 |")
			print("========================================================================================================")
			back_to_show_menu()
	except ValueError:
		print("========================================================================================================")
		print("| Error: Kamu memilih menu yang salah!                                                                 |")
		print("========================================================================================================")
		back_to_show_menu()

def create_zona():
	dict_covid = {
		"ID": [],
		"Nama": [],
		"Terkonfirmasi": [],
		"Sembuh": [],
		"Meninggal": [],
		"Kasus Aktif": [],
		"Status": []
	}
	clear_screen()
	print("========================================================================================================")
	print("|                               PROGRAM KLASIFIKASI ZONA RISIKO COVID-19                               |")
	print("========================================================================================================")
	objek = int(input("| Masukkan Jumlah Kab/Kota             : "))
	print("========================================================================================================")
	if os.path.exists(csv_filename_covid):
		df_covid = pd.read_csv(csv_filename_covid)
		if(len(df_covid) > 0):
			for i in range(len(df_covid)):
				dict_covid["ID"].append(df_covid["ID"][i])
				dict_covid["Nama"].append(df_covid["Nama"][i])
				dict_covid["Terkonfirmasi"].append(df_covid["Terkonfirmasi"][i])
				dict_covid["Sembuh"].append(df_covid["Sembuh"][i])
				dict_covid["Meninggal"].append(df_covid["Meninggal"][i])
				dict_covid["Kasus Aktif"].append(df_covid["Kasus Aktif"][i])
				dict_covid["Status"].append(df_covid["Status"][i])
	while objek > 0:
		id = int(input("| Masukkan ID                          : "))
		nama = input("| Masukkan Nama Kota/Kab               : ")
		positif = int(input("| Masukkan Jumlah Pasien Terkonfirmasi : "))
		sembuh = int(input("| Masukkan Jumlah Pasien Sembuh        : "))
		meninggal = int(input("| Masukkan Jumlah Pasien Meninggal     : "))
		kasus_aktif = positif-sembuh-meninggal
		risiko = ""
		if kasus_aktif > 51:
			risiko = "Zona Risiko Tinggi"
		elif kasus_aktif > 25:
			risiko = "Zona Risiko Sedang"
		elif kasus_aktif > 0:
			risiko = "Zona Risiko Rendah"
		elif kasus_aktif < 1:
			risiko = "Zona Tidak Terdampak"
		print("========================================================================================================")
		print("| Status                               :", risiko)
		dict_covid["ID"].append(id)
		dict_covid["Nama"].append(nama)
		dict_covid["Terkonfirmasi"].append(positif)
		dict_covid["Sembuh"].append(sembuh)
		dict_covid["Meninggal"].append(meninggal)
		dict_covid["Kasus Aktif"].append(kasus_aktif)
		dict_covid["Status"].append(risiko)
		print("========================================================================================================")
		objek -= 1
	df_covid = pd.DataFrame(dict_covid)
	df_covid.to_csv("covid19.csv", index=False)
	back_to_show_menu()

def show_zona():
	clear_screen()
	print("========================================================================================================")
	print("|                               PROGRAM KLASIFIKASI ZONA RISIKO COVID-19                               |")
	print("========================================================================================================")
	print("| [1] Tabel                                                                                            |")
	print("| [2] Teks                                                                                             |")
	print("| [3] Kembali                                                                                          |")
	print("| [0] Keluar                                                                                           |")
	print("========================================================================================================")
	try:
		selected_menu = int(input("| Pilih menu> "))
		if selected_menu == 1:
			show_zona_table()
		elif selected_menu == 2:
			show_zona_text()
		elif selected_menu == 3:
			show_menu()
		elif selected_menu == 0:
			close_app()
		else:
			print("========================================================================================================")
			print("| Error: Kamu memilih menu yang salah!                                                                 |")
			print("========================================================================================================")
			back_to_show_zona()
	except ValueError:
		print("========================================================================================================")
		print("| Error: Kamu memilih menu yang salah!                                                                 |")
		print("========================================================================================================")
		back_to_show_zona()

def show_zona_table():
	clear_screen()
	print("========================================================================================================")
	print("|                               PROGRAM KLASIFIKASI ZONA RISIKO COVID-19                               |")
	print("========================================================================================================")
	if os.path.exists(csv_filename_covid):
		df_covid = pd.read_csv(csv_filename_covid)
		if len(df_covid) > 0:
			count_zona = [0, 0, 0, 0]
			for i in range(len(df_covid)):
				if df_covid["Status"][i] == "Zona Risiko Tinggi":
					count_zona[0] += 1
				elif df_covid["Status"][i] == "Zona Risiko Sedang":
					count_zona[1] += 1
				elif df_covid["Status"][i] == "Zona Risiko Rendah":
					count_zona[2] += 1
				elif df_covid["Status"][i] == "Zona Tidak Terdampak":
					count_zona[3] += 1
			df_covid = df_covid.set_index("ID")
			print(tabulate(df_covid, headers = "keys", tablefmt = "psql"))
			if count_zona[0] > 0:
				print("| Jumlah Objek Status Zona Risiko Tinggi   :", count_zona[0])
			if count_zona[1] > 0:
				print("| Jumlah Objek Status Zona Risiko Sedang   :", count_zona[1])
			if count_zona[2] > 0:
				print("| Jumlah Objek Status Zona Risiko Rendah   :", count_zona[2])
			if count_zona[3] > 0:
				print("| Jumlah Objek Status Zona Tidak Terdampak :", count_zona[3])
			print("========================================================================================================")
		else:
			print("| Error: Tidak ada data yang tersedia!                                                                 |")
			print("========================================================================================================")
	else:
		print("| Error: File CSV tidak tersedia!                                                                      |")
		print("========================================================================================================")
	back_to_show_menu()

def show_zona_text():
	clear_screen()
	print("========================================================================================================")
	print("|                               PROGRAM KLASIFIKASI ZONA RISIKO COVID-19                               |")
	print("========================================================================================================")
	if os.path.exists(csv_filename_covid):
		df_covid = pd.read_csv(csv_filename_covid)
		if len(df_covid) > 0:
			count_zona = [0, 0, 0, 0]
			for i in range(len(df_covid)):
				print("| Kota/Kab ke-%d" % (i + 1))
				print("| ID Kota/Kab                 :", df_covid["ID"][i])
				print("| Nama Kota/Kab               :", df_covid["Nama"][i])
				print("| Jumlah Pasien Terkonfirmasi :", df_covid["Terkonfirmasi"][i])
				print("| Jumlah Pasien Sembuh        :", df_covid["Sembuh"][i])
				print("| Jumlah Pasien Meninggal     :", df_covid["Meninggal"][i])
				print("| Jumlah Kasus Aktif          :", df_covid["Kasus Aktif"][i])
				print("| Status                      :", df_covid["Status"][i])
				if df_covid["Status"][i] == "Zona Risiko Tinggi":
					count_zona[0] += 1
				elif df_covid["Status"][i] == "Zona Risiko Sedang":
					count_zona[1] += 1
				elif df_covid["Status"][i] == "Zona Risiko Rendah":
					count_zona[2] += 1
				elif df_covid["Status"][i] == "Zona Tidak Terdampak":
					count_zona[3] += 1
				print("========================================================================================================")
			if count_zona[0] > 0:
				print("| Jumlah Objek Status Zona Risiko Tinggi   :", count_zona[0])
			if count_zona[1] > 0:
				print("| Jumlah Objek Status Zona Risiko Sedang   :", count_zona[1])
			if count_zona[2] > 0:
				print("| Jumlah Objek Status Zona Risiko Rendah   :", count_zona[2])
			if count_zona[3] > 0:
				print("| Jumlah Objek Status Zona Tidak Terdampak :", count_zona[3])
			print("========================================================================================================")
		else:
			print("| Error: Tidak ada data yang tersedia!                                                                 |")
			print("========================================================================================================")
	else:
		print("| Error: File CSV tidak tersedia!                                                                      |")
		print("========================================================================================================")
	back_to_show_menu()

if __name__ == "__main__":
	while True:
		try:
			show_menu()
		except KeyboardInterrupt:
			close_app()
