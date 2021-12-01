#latihan pertemuan 9
print(20*'=','tugas pertemuan 9','='*20)
print(' Nama\t: A. Reza Baehaqa jamroni\t \n NIM\t: 312110494\t \n Kelas\t: TI.21.C5\t')
print(40*'=','\n')
a = [4,5,6,7,8]                                                        #membuat list sebanyak 5 elemen
print(" a = [4,5,6,7,8]\n")          

print(20*'=','akses list',20*'=') 
print('elemen ke 3 adalah', a[2])                                           # menampilkan elemen ke 3 ,
del a[1:4]                                                                  # mengambil elemen ke 2-4
print('setelah elemen 2 sampai 4 diambil maka menjadi',a)                                                              
del a[1]                                                                    # mengambil elemen terakhir
print('setelah elemen terakhir diambil maka menjadi',a,"\n")                                                              

print(20*'=','mengubah element list',20*'=')                                                      
a = [4,5,6,7,8]                                                        
a [3] =  5                                                                  #mengubah elemen ke 4 dengan nilainya , 
print('setelah merubah elemen ke-4 maka menjadi', a)
a [3:5] = 5, 6                                                            #mengubah elemen ke 4- terakhir
print('setelah merubah elemen ke-4 sampai terakhir maka menjadi', a,'\n')
print(20*'=','menambah element list',20*'=')
a = [4,5,6,7,8] 
b = []
b.extend (a[0:2])                                                           #mengambil 2 bagian dari list pertama (a) dan jadikan list ke 2 B
print ('hasil setelah mengambil 2 bagian elemen a maka b=', b)
b.append('6')                                                         #- tambah list b dengan nilai string
print('setelah menambahkan string pada elemen b hasilnya', b)
b.extend([7,8,9])                                                       #- tambah list b dengan 3 nilai
print('setelah menambahkan 3 bilai menjadi', b)
c=a+b                                                                       #- gabungkan list b dan list a
print('hasil penggabungan list a dan b hasilnya',c)