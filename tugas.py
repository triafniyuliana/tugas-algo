Nama = input("Nama : ")
Nim = input("NIM : ")
cek_biaya = input("apakah biaya sudah dilunasi : ")
jas_almamater = input("apakah anda memakai jas almamater : ")
kartu_ujian = input("apakah anda membawa kartu ujian : ")
nilai_kehadiran = float(input("nilai kehadiran : "))

allowed_respon = ['ya']

if cek_biaya in allowed_respon and jas_almamater in allowed_respon and kartu_ujian in allowed_respon and nilai_kehadiran >=90 :
    print(Nama,"anda boleh mengikuti ujian")
else:
    print(Nama, "Tidak bisa mengikuti ujian")


