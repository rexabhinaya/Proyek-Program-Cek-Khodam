import random

def cek_khodam(nama):
    daftar_khodam = [
        "Macan Pemarah", "Buaya Sunda", "Beruang Sunda", "Harimau Birahi",
        "Tutup Odol", "Tutup Panci", "Kaleng Kejepit", "Kanebo Kering",
        "Kapal Karam", "Gergaji Mesin", "Nyi Blorong", "Jin Rawa Rontek",
        "Kucing Israel", "Capung Gila", "Tumis Kangkung", "Jam Dinding Rusak",
        "Gunting Tumpul", "Kasur Empuk", "Payung Robek", "Kulkas Kosong",
        "Piring Pecah", "Meja Berdecit", "Koper Berat", "Topi Melorot",
        "Lem Super Lengket", "Keripik Garing", "Senter Mati", "Kue Kering",
        "Bantal Empuk", "Kendi Air"
    ]

    motivasi = {
        "Macan Pemarah": "Kamu marah terus tapi kerjaannya mana? Growl less, grind more.",
        "Buaya Sunda": "Jangan cuma jago PHP-in orang, mimpi kamu juga jangan di-PHP-in.",
        "Beruang Sunda": "Kalem boleh, tapi jangan sampai kalah sama nasib.",
        "Harimau Birahi": "Nafsu boleh liar, tapi ambisi jangan kalah liar.",
        "Tutup Odol": "Mulutmu banyak alasan, tapi tutupnya ga pernah rapet.",
        "Tutup Panci": "Hidupmu ribut mulu. Coba ditutup dulu dramanya.",
        "Kaleng Kejepit": "Stuck terus? Ya lepas lah, masa mau kejepit seumur hidup.",
        "Kanebo Kering": "Perasaanmu kering? Wajar, hidup juga ga selalu moist.",
        "Kapal Karam": "Karam? Ya bangun kapal baru. Bukan nangis di dasar laut.",
        "Gergaji Mesin": "Cut off people yang ngerepotin. Hidupmu bukan bengkel umum.",
        "Nyi Blorong": "Glow up dulu baru ngasih attitude.",
        "Jin Rawa Rontek": "Kejatuhan masalah? Respawn lah, bukan ngeluh.",
        "Kucing Israel": "Lu suka sendiri? Bagus, hidup ga butuh rombongan buat sukses.",
        "Capung Gila": "Chaos dikit gapapa, asal bukan masa depanmu yang chaos.",
        "Tumis Kangkung": "Cepet dong hidupnya, jangan kalah sama kangkung 2 menit jadi.",
        "Jam Dinding Rusak": "Ga tepat waktu? Ya wajar, kamu aja belum pas.",
        "Gunting Tumpul": "Skill tumpul? Asah. Jangan sok tajem sama orang.",
        "Kasur Empuk": "Rebahanmu nyaman, masa depanmu enggak.",
        "Payung Robek": "Bocor? Ya ditambal. Jangan nunggu cuacanya berubah.",
        "Kulkas Kosong": "Isi kepala jangan kosong juga ya, bahaya.",
        "Piring Pecah": "Retak dikit? At least kamu ga fake.",
        "Meja Berdecit": "Noisy banget, tapi progress nol. Fix butuh update.",
        "Koper Berat": "Bebanmu berat? Ya siapa suruh ngumpulin drama.",
        "Topi Melorot": "Lu jatuh, tapi sok gaya. Lucu sih—lanjutin.",
        "Lem Super Lengket": "Terlalu nempel sama orang? Makanya susah maju.",
        "Keripik Garing": "Garing? Minimal hasilmu jangan garing juga.",
        "Senter Mati": "Gelap? Ya jangan nunggu orang nyalain, hidup bukan bioskop.",
        "Kue Kering": "Kering tapi strong. Ga kayak beberapa orang yang moist tapi lemah.",
        "Bantal Empuk": "Nyaman itu musuh progress. Kerasin dikit hidupnya.",
        "Kendi Air": "Isi terus otakmu. Kalau nggak, isinya cuma drama sama stalking."
    }

    khodam = random.choice(daftar_khodam)
    pesan = motivasi[khodam]

    return f"Khodam yang menemani {nama}: {khodam}\nPesan Khodam: {pesan}"

nama = input("Masukkan nama kamu: ")
print(cek_khodam(nama))
