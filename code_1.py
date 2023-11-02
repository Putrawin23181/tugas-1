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
