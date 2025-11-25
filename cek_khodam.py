import random

def cek_khodam(nama):
    daftar_khodam = []

    motivasi = {}

    khodam = random.choice(daftar_khodam)
    pesan = motivasi[khodam]
    
    return (
        f"Khodam yang menemani {nama}: {khodam}"
        f"Pesan Khodam: {pesan}
    )

nama = input("Masukkan nama kamu: ")
print(cek_khodam(nama))
