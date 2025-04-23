kalimat = "Saudara-saudara, pada tanggal 17-08-1945 Indonesia merdeka"

hasil = kalimat.split()

for kal in hasil:
  if kal[0].isdigit():
   hasil2 = kal.split("-")
   print(hasil2[1]+"/"+hasil2[0]+"/"+hasil2[2])


def anagram(kata_1,kata_2):
  kata_1 = kata_1.lower()
  kata_2 = kata_2.lower()

  if len(kata_1) != len(kata_2):
    return 'tidak sama jumlah hurufnya'
  
  for i in kata_1:
    if kata_1.count(i) != kata_2.count(i):
      return f'tidak sama hurufnya'
    else:
      return f'kata tersebut anagram'

print(anagram("atma", "tama"))



def palindrom(kata):
    # Ubah ke huruf kecil semua untuk menghindari case sensitive
    kata = kata.lower()

    # Bandingkan kata dengan versi terbaliknya
    if kata == kata[::-1]:
        return f'"{kata}" adalah palindrom'
    else:
        return f'"{kata}" bukan palindrom'

# Contoh pemakaian
print(palindrom("Katak"))
print(palindrom("Mobil"))




kalimat = 'Saya mau makan. Makan itu wajib. Mau siang atau malam saya wajib makan'
kata = 'makan'

kata_kecil = kalimat.lower()
kata_full = kata_kecil.replace('.', '')

jumlah_kata = kata_full.count(kata)
print(f'{kata} ada {jumlah_kata} jumlahnya')



kalimat = 'saya   tidak   suka   memancing ikan'
tanpa_spasi = kalimat.split()
no_spasi = " ".join(tanpa_spasi)
print(no_spasi)



kalimat = 'red snakes and and black frog in the pool'
kata = kalimat.split()

pendek = kata[0]
panjang = kata[0]

for i in kata:
  if len(i) < len(pendek):
    pendek = i
  elif len(i) > len(panjang):
    panjang = i

print("paling pendek:",pendek)
print("paling panjang:", panjang)




import re
kalimat = " Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02). "
tanggal = re.findall('\d{4}-\d{2}-\d{2}', kalimat)

Tahun_sekarang = 2025
bulan_sekarang = 4
hari_sekarang = 22

def hitung_selisih(tahun, bulan, hari):
    selisih_tahun = (Tahun_sekarang - tahun) * 365
    selisih_bulan = (bulan_sekarang - bulan) * 30
    selisih_hari = hari_sekarang - hari
    return selisih_tahun + selisih_bulan + selisih_hari

for i in tanggal:
  pecahan_tanggal = i.split('-')
  tgl_tahun = int(pecahan_tanggal[0])
  tgl_bulan = int(pecahan_tanggal[1])
  tgl_hari = int(pecahan_tanggal[2])

  hasil_selisih = hitung_selisih(tgl_tahun, tgl_bulan, tgl_hari)
  print(f'{tgl_hari:02d}-{tgl_bulan:02d}-{tgl_tahun:02d} 00:00:00 selisih {hasil_selisih} hari')



import re
from datetime import date
kalimat = " Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02). "
tanggal = re.findall(r'\d{4}-\d{2}-\d{2}', kalimat)

Tahun_sekarang = 2025
bulan_sekarang = 4
hari_sekarang = 22
tanggal_sekarang = date(Tahun_sekarang, bulan_sekarang, hari_sekarang)

for i in tanggal:
  pecahan_tanggal = i.split('-')
  tgl_tahun = int(pecahan_tanggal[0])
  tgl_bulan = int(pecahan_tanggal[1])
  tgl_hari = int(pecahan_tanggal[2])

  tanggal_dulu = date(tgl_tahun, tgl_bulan, tgl_hari)
  hasil_selisih = (tanggal_sekarang - tanggal_dulu).days
  print(f'{tgl_hari:02d}-{tgl_bulan:02d}-{tgl_tahun:02d} 00:00:00 selisih {hasil_selisih} hari')



import re, random

kalimat ='Berikut adalah daftar email dan nama pengguna dari mailing list: anton@mail.com dimiliki oleh antonius budi@gmail.co.id dimiliki oleh budi anwari slamet@getnada.com dimiliki oleh slamet slumut matahari@tokopedia.com dimiliki oleh toko matahari'
pola = re.findall(r"\S+@\S+",kalimat)

# bisa pakai (r"\S+@\S+",kalimat) tapi jika ada koma seperti @gmail.com, maka koma didepan akan ikut
# maka kita menggunakan (r"[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+",kalimat)
for i in pola:
    nama = i.split("@")[0]
    pilihan_password = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ''.join(random.choices(pilihan_password, k=8))
    print(f'{i} username: {nama}, password: {password}')





teks = "Ini adalah teks contoh. Teks ini digunakan untuk mencari kata dalam teks."
kata_dicari = "teks"
def hitung_frekuansi(teks, kata_dicari):
  baru = teks.lower()
  kata = baru.split(' ')

  count = 0
  for i in kata:
    if kata_dicari in i:
      if i.count(kata_dicari) == 1:
        count += 1
  return count
hasil = hitung_frekuansi(teks, kata_dicari)
print(f"Frekuensi kata '{kata_dicari}' adalah: {hasil}")




import re
def cek_password(password):
  besar = re.search(r'A-Z', password)
  kecil = re.search(r'a-z', password)
  angka = re.search(r'0-9', password)
  karakter = re.search(r'^\w\s', password)
  
  if len(password) < 6 or len(password) > 20:
    print('Tidak valid')
  elif re.search('\s',password):
    print('Tidak valid')
  elif besar and kecil and angka and karakter:
    print('Password kuat')
  else:
    print('Password lemah')




import re

def sensor(kalimat):
  kata = kalimat.split()
  hasil = []
  kalimat = "Hubungi saya di 081234567890 dan dia di 0821123456"
  for i in kata:
    if i.startswith('08') and i.isdigit() and 10 <= len(i) <= 13:
      awal = i[:4]
      akhir = i[-3:]
      tengah = 'x' * (len(i) - 7)
      i = awal + tengah + akhir
      hasil.append(i)
  return hasil

kalimat = "Hubungi saya di 081234567890 dan dia di 0821123456"
