# # sedang latihan perulangan FOR
# for i in range(20):
#     if i == 5 :
#         break
#     print("Sedang Belajar Pyton")
    

#sedang belajar perulangan while

'''angka = 1
while angka <=20:
    print(angka)
    angka += 1'''

# PERCABANGAN IF ELSE
# nilai = 75
# if nilai >= 75:
#     print("Anda lulus ujian.")
# else :
#     print("Anda tidak lulus ujian.")


#Daftar nilai
nilai = {75,}

#Loop untuk memperoses semua nilai
for i in nilai:
    if i >= 80:
        Status = "Baik sekali"
    elif i >= 75:
        Status = "Baik"
    elif i >= 56:
        Status = "Cukup"
    elif i >= 45:
        Status = "Kurang"
    else:
        Status = "Tidak lulus"
    
    print(f"Nilai: {i}, Status: {Status}")








