# operator dalam bentuk methods

## merubah case pada string

# merubah semua ke upper case
salam = "bro!"
print("normal " + salam)
salam = salam.upper()
print("upper " + salam)
salam1 = "Haloo Bro"
ucaapan = salam1.upper()
print (ucaapan)

# merubah semua ke lower case
alay = "aKu KeCe AbieeZZZ"
print("normal " + alay)
alay = alay.lower()
print("lower " + alay)

## method is, untuk pengecekan

# contoh isupper()
salam = "SIST"
apakah_upper = salam.isupper()
print(salam + " is upper? " + str(apakah_upper))
salam = salam.lower()
apakah_upper = salam.isupper()
print(salam + " is upper? " + str(apakah_upper))

# islower() <- untuk pengecekan apakah lower case semua
# isalpha() <- untuk mengecek apakah huruf semua
# isalnum() <- apakah huruf dan angka
# isdecimal() <- apakah numeric
# isspace() <- apakah isinya spasi, tab dan enter (newline \n)
# istitle() <- huruf pertama setiap kata upper case

# Apakah semua huruf awal dari kalimat adalah kapital
# Jika semua kapital maka TRUE
judul = "It Is Okay To Not Be orkay"
cek_judul = judul.istitle()
print(judul + " is title? " + str(cek_judul))


judul1 = "Buku Panduan Berkemah Di Gunung"
cek1 = judul1.istitle()
print (judul1 + str(cek1))



# startwith() dan endwith() <-- keren
# Mengecek kalimat dalam variable ada di posisi mana
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start " + str(cek_start))
cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end " + str(cek_end))

cekstart = "Halo Fauzan".startswith("Halo")
print("Halo" + str(cekstart))

# join() dan split() <-- buat orang males
# Mengisi di bagian koma
pisah = ['aku','sayang','kamu']
gabungan = ' ehm '.join(pisah)
print(pisah)
print(gabungan)

pisah1 = ['aku','ingin','kamu']
gabungan = 'kontol' .join(pisah1)

gabungan = "naik vespa keliling kota"
pisah = gabungan.split()
print(gabungan)
print(pisah)

gabungan = "naikehmvespaehmkelilingehmkota"
pisah = gabungan.split("ehm")
print(gabungan)
print(pisah)

# alokasi karakter
print("'kiri      '")

kanan = "kanan".rjust(20) # rata kanan dengan 20 karakter
print("'" + kanan + "'")

kiri = "kiri".ljust(20) # rata kiri dengan 20 karakter
print("'" + kiri + "'")

tengah ="tengah".center(20) # rata tengah dengan 20 karakter
print("'" + tengah + "'")

tengah ="tengah".center(20,'-') # rata tengah dengan 20 karakter
print("'" + tengah + "'")

# kebalikan dari alokasi karakter
kanan = kanan.strip()
print("'" + kanan + "'")
tengah = tengah.strip('-')
print("'" + tengah + "'")