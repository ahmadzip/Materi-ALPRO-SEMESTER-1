##variabel adalah tempat untuk menyimpan data/nilai

##penulisan variabel 1 harus dengan benar supaya tidak bingung
nama = "dzaky abdur razaq"
Nama = "zaky"

##Batasan penulisan variabel
## 1. Angka tidak bisa ditulis di depan (dimulai huruf dulu)
##Contoh : 1nama

nama1 = "dzaky abdur" ##bisa

##Penulisan variabel 2 (camel case = variabel jangan di spasi supaya tidak bingung)
namaLengkap = "dzaky abdur razaq"
NamaLengkap = "rido purnomo"
namaLengkapsaya = "Tony Stark"

##Penulisan variabel 3 (snake case) = penamaan variabel yang memiliki 2 kata dengan tanda garis bawah sebagai spasi
##contoh
Nama_lengkap = "dzaky abdur rzaq" ##bisa

##Tipe Data = Jenis nilai atau jenis datanya (cara penulisan/pemasukkan data dengan kode tertentu)
##Tipe data string
alamat = "Cilacap"
asalkota= 'Wonogiri'
umur = '1'
##tipe number
##Tipe data integer (bilangan bulat)
umurSaya = 10
nilaisaya = 100
urutan = 1
negatif = -100
##Tipe data float (Desimal)
beratBadan = 70.1
tinggiBadan = 100.1000
##Tipe data boolean
tampan = True ##Bisa bernilai 1
jelek = False ##Bisa bernilai 0

##Operator aritmatika
#1. Penjumlahan
# angka1 = 10
# angka2 = 20
# jumlah = angka1 + angka2


#2. Pengurangan
# angka1 = 10
# angka2 = 2
# jumlah = angka1 - angka2


# alas = int(input("masukkan alas : "))
# tinggi = int(input("masukkan tinggi : "))
# luas = alas * tinggi /2 


##Tipe data lanjut
#List penuliasanya menggunakan kurung siku []
# datalistNama = ["dzaky", "abdur", "razaq"]

# datalistAngka = [10,20,30,40,50]
# datalistFloat = [10.20,10.5,11.5]
# datalistBool = [True, False, False, True]
# datalistCampur = [10, 'dzaky', True, 20.30]

##Dictionary berisikan key dan value {}
# dic = {
#     "squad" : "croozle",
#     "kelas" : 10,
#     "tampan" : True,
#     "berat" : 70.5,
#     "list" :['toni', 'afnan', 'ishal']
# } 

#print(dic['tampan])
#tipe data tuple menggunakan ()
# dataTuple = ('faiz', 'toni', 'afnan')
# dataCampur = ('faiz', 10, True, 20.5)


##Tipe data set {}
# dataSet = {'faiz', 'toni', 'isal' }

##Casting data = merubah tipe data ke tipe data lainya

# dataString = '10'
# ubahInteger = int(dataString)
# ubahFloat = float(dataString)

#print("Ini diubah ke integer", ubahInteger)
#print("Ini diubah ke float", ubahFloat)

# dataInt = 10
# ubahString = str(dataInt)
# ubahFloat = float(ubahInteger)
#print("Ini diubah ke string", ubahString)
#print("Ini diubah ke float", ubahFloat)

##inputan user
#tinggi = input("masukan tinggi : ")
#userFloat = float(input("masukan tinggi: "))
#userInt = int(input("masukan tinggi : "))

# sisiAtas = input("masukan sisi atas : ")
# sisiBawah = input("masukan sisi bawah : ")
# tinggi = input("masukan tinggi : ")
# luas =  (int(tinggi))* (int(sisiAtas) + int(sisiBawah))*1/2

#Operator aritmatika lanjutan
#modulus %

# modulus = 10 % 2
# print(modulus)


#Operator aritmatika lanjutan
#modulus %

#modulus = 27 % 3

##perpangkatan
# **
#pangkat = 10 **5


##Pembagian bilangan bulat
# //
#pembagianBulat = 25 // 4

#Operator pembanding
#1. sama dengan "=="
#2. Tidak sama dengan "!="
#3. Lebih dari ">"
#4. Kurang dari "<"
#5. Lebih dari sama dengan ">="
#6. Kurang dari sama dengan "<="

##Seleksi
#if :
#elif :
#else :
#input = 2
#if input == 10 :
    #print("masuk kondisi sama dengan")
#elif input <10:
   # print    
#else :
   # print("masuk kondisi tidak sama dengang")    


#r = 21
#if r % 7==0:
   # luas = 22/7 * r**2    
#else:
 #   luas = 3.14  * r**2

input= int(input("masukan nilai : "))
if input >= 81:
  print("nilai A")
elif input >= 61:
 print("nilai B")
elif input >= 41:
 print("nilai C")
elif input >= 21:
 print("nilai D")
elif input <= 21:
 print("nilai E")





