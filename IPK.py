''' Inputan user '''
nim = int(input("Masukkan angka NIM anda: "))
nama = input("Masukkan nama anda: ")
alamat = input("Masukkan alamat anda: ")
asal_sekolah = input("Masukkan asal sekolah anda: ")
kode_prodi = input("Masukkan kode prodi anda: ")
ipk_awal = int(input("Masukkan nilai IPK awal anda: "))
uts = int(input("Masukkan nilai uts anda: "))
uas = int(input("Masukkan nilai uas anda: "))
tm = int(input("Masukkan nilai tm anda: "))

import math
#perhitungan nilai IPS
uts_ips = uts * 0.30
tm_ips = tm * 0.30
uas_ips = uas * 0.40
ips = math.floor(uts_ips + tm_ips + uas_ips)

#perhitungan ipk
ipk = (ips + ipk_awal) / 2

#ketentuan beasiswa

if kode_prodi == "TI" or kode_prodi == "SI":
    if ipk >75 or ipk <85:
        print("maka beasiswanya adalah 20%")
    elif ipk >85 or ipk <100:
        print("maka beasiswanya adalah 30%")
    else:
        print(" ")

if kode_prodi == "DKI" or kode_prodi == "Teknik Industri":
    if ipk >75 or ipk <85:
        print("maka beasiswanya adalah 25%")
    elif ipk >85 or ipk <100:
         print("maka beasiswanya adalah 35%")
    else:
        print(" ")

print("nama : {}".format(nama))
print("nim : {}".format(nim))
print("alamat : {}".format(alamat))
print("asal sekolah : {}".format(asal_sekolah))
print("kode prodi : {}".format(kode_prodi))
print("nilai ipk awal : {}".format(ipk_awal))
print("nilai ips : {}".format(ips))
