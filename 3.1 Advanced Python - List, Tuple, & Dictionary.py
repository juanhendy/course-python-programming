# list
list1 = ["apple", "banana", "watermelon"]
list2 = [True, False, False]
del list2[0]
list3 = list1.copy()
print(list3[2] == "gedang")
list1[2] = "gedhang"
print(list1)

list2.extend(list1)
print(list2)

tuple1 = (1, 2, "satu", "dua")
for number in tuple1:
    print("Nomor", number)

fruit_dict = {'nama' : 'pisang',
              'jenis' : 'raja',
              'kode' : '980',
              'harga' : '99000'}
print(fruit_dict['kode'])
fruit_dict['harga'] = '76000'
print(fruit_dict)
for kategori, keterangan in fruit_dict.items():
    print("Kategori", kategori, ",", "Ket:", keterangan)
del fruit_dict