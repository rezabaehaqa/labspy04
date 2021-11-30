# labspy04
## Tugas Pertemuan ke 9
```sh
Nama    : A. Reza Baehaqa Jamroni
Nim     : 312110494
Matkul  : Bahasa Perograman
```
Latihan

• Buatlah sebuah list sebanyak 5 elemen dengan nilai bebas yaitu

```sh
a = [4,5,6,7,8] 
```
• akses list:
    • tampilkan elemen ke 3
    • ambil nilai elemen ke 2 sampai elemen ke 4
    • ambil elemen terakhir
dari tiga akses list tersebut saya menggunakan cara sebagai berikut :
```sh 
1. a[2]
2. del a[1:4]
    print(a)
3. del a[1] 
    print(a)
```
Dengan catatan 
*Nomer indeks list selalu dimulai dari nol (0).
*Nomer indeks ini yang kita butuhkan untuk mengambil isi (item) dari list.
• ubah elemen list:
    • ubah elemen ke 4 dengan nilai lainnya
    • ubah elemen ke 4 sampai dengan elemen terakhir
ini kita menggunakan cara sebagai berikut :
```sh
a [3] = 5
print (a)
a [3:5] = 3, 4
print(a)
```
• tambah elemen list:
    • ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
    • tambah list B dengan nilai string
    • tambah list B dengan 3 nilai
    • gabungkan list B dengan list A
ini kita menggunakan cara sebagai berikut :
```sh
b = []
b.extend (a[0:2])
print(b)
b.append ('6')
print(b)
b.extend([7,8,9])
print(b)
c=a+b
print(c)
```
Berikut ini adalah tampilan visual studio codenya
![Gambar 1](screenshot/ss1.png)
Berikut output dari programnya
![Gambar 1](screenshot/ss2.png)
