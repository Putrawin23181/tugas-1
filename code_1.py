#memanggil library PrettyTable
from prettytable import PrettyTable

#deklarasi variabel tabel
tabel = PrettyTable()
tabel_harga = PrettyTable()

#tampilan selamat datang dan input awal
print ("Selamat Datang di Pizza Hut")
jumlah_pizza = int(input("Ingin pesan berapa pizza? "))
pesanan_pizza =[] #list untuk menyimpan pesanan pizza

#perulangan program sesuai jumlah pizza yang dipesan oleh pelanggan
for _ in range(jumlah_pizza):

    #print pertama dan input
    print ("========================================================")
    print ("Daftar Topping Yang Tersedia : \n1. Frankfurter BBQ \n2. Meat Monsta \n3. Super Supreme \n4. Cheese Lovers \n5. American Favourite \n6. Pepperoni \n7. Cheese Overload \n8. Tuna Melt")
    topping = int(input("Silahkan Pilih Topping Anda (1-8): "))
    print ("--------------------------------------------------------")
    print ("Daftar Crust Yang Tersedia : \n1. Pan \n2. StuffedCrust Cheese \n3. StuffedCrust Sausage \n4. Cheesy Bites \n5. Crown Crust")
    crust = int(input("Silahkan Pilih Crust Anda (1-5): "))
    print ("--------------------------------------------------------")
    print ("Daftar Ukuran Pizza Yang Tersedia : \n1. Personal \n2. Regular \n3. Large")
    ukuran = int(input("Silahkan Pilih Ukuran Pizza Anda (1-3): "))
    print ("--------------------------------------------------------")
    xtracz = input("Apakah Anda ingin Menambahkan Extra Cheese (Y/N)? ")

    #dictionary daftar topping
    daftar_topping = {
        1: "Frankfurter BBQ",
        2: "Meat Monsta",
        3: "Super Supreme",
        4: "Cheese Lovers",
        5: "American Favourite",
        6: "Pepperoni",
        7: "Cheese Overload",
        8: "Tuna Melt"
    }

    #dictionary daftar crust
    daftar_crust = {
        1: "Pan",
        2: "StuffedCrust Cheese",
        3: "StuffedCrust Sausage",
        4: "Cheesy Bites",
        5: "Crown Crust"
    }

     #dictionary daftar ukuran
     daftar_ukuran = {
        1: "Personal",
        2: "Regular",
        3: "Large"
    }

    #mengambil nama berdasarkan nomor yang di inputkan
    nama_topping = daftar_topping[topping]
    nama_crust = daftar_crust[crust]
    nama_ukuran = daftar_ukuran[ukuran]

    #deklarasi harga awal
    harga = 0
    hargacz = 0

    #fungsi if untuk harga crust Pan beserta dengan harga per ukuran pizza
    if crust == 1:
        hargacrust = 43637 #harga crust Pan
        if ukuran == 1:
            hargacrstuk = 0 #harga jika ukuran personal
        elif ukuran == 2:
            hargacrstuk = 57273 #harga jika ukuran regular
        else:
            hargacrstuk = 89091 #harga jika ukuran large

    #fungsi if untuk harga crust StuffedCrust Cheese beserta dengan harga per ukuran pizza
    elif crust == 2:
        hargacrust = 55455 #harga crust StuffedCrust Cheese
        if ukuran == 1:
            hargacrstuk = 0 #harga jika ukuran personal
        elif ukuran == 2:
            hargacrstuk = 65455 #harga jika ukuran regular
        else:
            hargacrstuk = 104545 #harga jika ukuran large

    #fungsi if untuk harga crust StuffedCrust Sausage beserta dengan harga per ukuran pizza
    elif crust == 3:
        hargacrust = 52728 #harga crust StuffedCrust Sausage
        if ukuran == 1:
            hargacrstuk = 0 #harga jika ukuran personal
        elif ukuran == 2:
            hargacrstuk = 64545 #harga jika ukuran regular
        else:
            hargacrstuk = 102727 #harga jika ukuran large

    #fungsi if untuk harga crust Cheesy Bites beserta dengan harga per ukuran pizza
    elif crust == 4:
        hargacrust = 57273 #harga crust Cheesy Bites
        if ukuran == 1:
            hargacrstuk = 0 #harga jika ukuran personal
        elif ukuran == 2:
            hargacrstuk = 66364 #harga jika ukuran regular
        else:
            hargacrstuk = 107273 #harga jika ukuran large
    
    #fungsi if untuk harga crust Crown Crust beserta dengan harga per ukuran pizza
    else:
        hargacrust = 55455 #harga crust Crown Crust
        if ukuran == 1:
            hargacrstuk = 0 #harga jika ukuran personal
        elif ukuran == 2:
            hargacrstuk = 65455 #harga jika ukuran regular
        else:
            hargacrstuk = 104545 #harga jika ukuran large

    #fungsi if untuk jika pelanggan ingin menambahkan Extra Cheese beserta harga per ukuran pizza
    if xtracz == "Y" or "y":
        print("Add Extra Cheese")
        if ukuran == 1:
            hargacz = 13636 #harga jika ukuran personal
        elif ukuran == 2:
            hargacz = 16364 #harga jika ukuran regular
        else:
            hargacz = 19091 #harga jika ukuran large
    else:
        hargacz = 0 #harga jika pelanggan tidak menambahkan Extra Cheese

    #deklarasi perhitungan total harga
    total_harga = hargacrust + hargacrstuk + hargacz

    #memasukkan data pesanan ke dalam list
    pesanan_pizza.append({
        "Topping": nama_topping,
        "Crust": nama_crust,
        "Ukuran": nama_ukuran,
        "Extra Cheese": xtracz,
        "Total Harga": total_harga
    })

#menghitung total keseluruhan harga pizza dengan SUM
total_harga_semua_pesanan = sum(pesanan["Total Harga"] for pesanan in pesanan_pizza)

#print tampilan bill
print("========================================================")
print("-----------PIZZA HUT----------")

#membuat kolom tabel
tabel.field_names = ["Rincian Pesanan", "Harga"]
tabel_harga.field_names = ["Total Harga"]

#mengisi baris pada tabel
for pesanan in pesanan_pizza:
    rincian_pesanan = f"{pesanan['Ukuran']} {pesanan['Topping']} \n{pesanan['Crust']}"
    if pesanan['Extra Cheese'].lower() == 'y':
        rincian_pesanan += "\nAdd Extra Cheese"
    harga_pesanan = "Rp. {:,.2f}".format(pesanan['Total Harga'])
    tabel.add_row([rincian_pesanan, harga_pesanan])

#mengisi baris pada tabel_harga
tabel_harga.add_row(["Rp. {:,.2f}".format(total_harga_semua_pesanan)])

#print tabel
print(tabel)
print(tabel_harga)
print("Terima Kasih Atas Kunjungan Anda")
