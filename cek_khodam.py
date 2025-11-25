import random

def cek_khodam(nama):
    daftar_khodam = []

    khodam = random.choice(daftar_khodam)
    return f"Khodam yang 'menemani' {nama}: {khodam}"

nama = input("Masukkan nama kamu: ")
print(cek_khodam(nama))
