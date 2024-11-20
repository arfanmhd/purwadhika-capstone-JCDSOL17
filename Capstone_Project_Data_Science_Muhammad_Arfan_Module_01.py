# Nama = Muhammad Arfan
# Capstone Project Module 01 - Data Science and Machine Learning
# Aplikasi Manajemen Stock Gudang

print("Aplikasi Manajemen Stock Gudang")

list_menu= ['1. Menampilkan daftar barang', '2. Menambah barang', '3. Menghapus barang', '4. Update/perubahan data barang', '5. Check-out Barang', '6. Summary','7. exit program']
daftar_barang = [[0,'Pasir', 20, 10000],[1,'Batu', 15, 15000], [2,'Semen', 25, 20000]]
total_harga = 0
added_items= []
removed_items = []
updated_items= []
checkout_items = []

def menu_choice():
     for menu in list_menu:
          print(menu)

def daftar(barang):   
    print('{}\t |{}     \t |{}\t |{}'.format(barang[0], barang[1],barang[2],barang[3]))


def tambah():
     nama_barang = str(input("Masukkan nama barang: "))
     stock_barang = int(input("Masukkan stock barang: "))
     harga_barang = int(input("Masukkan harga barang: "))
     added_items.append([nama_barang, stock_barang, harga_barang])

     daftar_barang.append([len(daftar_barang), nama_barang, stock_barang, harga_barang])
     print('Indeks\t |Nama     \t |Stock\t |Harga ')
     for barang in daftar_barang:
          daftar(barang)


def hapus():
     for barang in daftar_barang:
          print(f"{barang[1]} memiliki indeks {barang[0]} ")

     hapus_barang = int(input("Masukkan indeks barang rusak/dibuang: "))
     removed_items.append(daftar_barang[hapus_barang][1])
     for barang in daftar_barang:
          if barang[0] == hapus_barang:
               daftar_barang.remove(barang)
     if hapus_barang == 0:
          for i in range(len(daftar_barang)):
               daftar_barang[i][0] -= 1
     else:
          for i in range(len(daftar_barang)-1):   
             if daftar_barang[i+1][0] - [i][0] != 1:
                 daftar_barang[i+1][0] -= 1      
     print('Indeks\t |Nama     \t |Stock\t |Harga ')
     for barang in daftar_barang:
          daftar(barang)


def update():
     for barang in daftar_barang:
          print(f"{barang[1]} memiliki indeks {barang[0]} ")
     try:
         update_barang = int(input("Masukkan indeks barang: "))
         update_stock = int(input("Masukkan stock barang: "))
         update_harga = int(input("Masukkan harga barang: "))
         updated_items.append([daftar_barang[update_barang][1], update_stock, update_harga])

         for barang in daftar_barang:
             if barang[0] == update_barang:
                 barang [2] = update_stock
                 barang [3] = update_harga
     except ValueError:
          print("Input harus berupa angka")
     print('Indeks\t |Nama     \t |Stock\t |Harga ')
     for barang in daftar_barang:
          daftar(barang)


def check_out():

     while True:
         for barang in daftar_barang:
           print(f"{barang[1]} memiliki indeks {barang[0]} ")
 
         try:
             indeks_barang= int(input("Masukkan indeks barang: "))
             barang_found = False
             for barang in daftar_barang: 
                 if barang[0] == indeks_barang:
                     barang_found = True
                     harga_barang= barang[3]
                     try:
                         qty_barang= int(input("Masukkan stock barang: "))
                         if qty_barang <= barang[2]:
                             checkout_items.append([daftar_barang[indeks_barang][1], qty_barang, harga_barang])
                             barang[2] -= qty_barang
                             print(f'Jumlah {barang[1]} yang tersisa: {barang[2]} ') 
                             cek_lanjut = str(input("Tambah list barang yang dicheckout? (y/n): "))
                             if cek_lanjut == 'n':
                                  return
                         else:
                             print("Jumlah barang tidak tersedia")
                             
                     except ValueError:
                         print("Input harus berupa angka")            
             if not barang_found:
                  print("Barang tidak tersedia")
                
         except ValueError:
              print("Input harus berupa angka")
              break
         except Exception as e:
              print(f"Error: {e}")
                                 
  
def penggabungan_list(list_checkout):
     i = 0
     while i < len(list_checkout)-1:
          if list_checkout[i][0] == list_checkout[i+1][0]:
                list_checkout[i][1] += list_checkout[i+1][1]
                del list_checkout[i+1]
          else:
                 i += 1


while True:
      menu_choice()
     
      try:
            menu = int(input("Masukkan angka menu yang ingin dijalankan = " ))
          
            if menu == 7: #exit program
                print("Terima Kasih")
                break
            elif menu == 1: #menampilkan daftar barang
               print('Indeks\t |Nama     \t |Stock\t |Harga ')
               for barang in daftar_barang:
                daftar(barang)
            elif menu == 2: #menambah barang
                 tambah()
            elif menu == 3: #menghapus barang
                 hapus()
            elif menu == 4: #update barang
                 update()
            elif menu == 5: #checkout barang
                 check_out()
                 if not checkout_items:
                      print("Tidak ada yang perlu dibayar")
                 else:
           
                     for i in range(len(checkout_items)-1):
                          for j in range(i+1, len(checkout_items)):
                               if checkout_items[i][0] > checkout_items[j][0]:
                                    checkout_items[i], checkout_items[j] = checkout_items[j], checkout_items[i]  
                     penggabungan_list(checkout_items)           
      
                    
                     for order in checkout_items:
                          order.append(order[1]*order[2])
                          total_harga += (order[1] * order[2])
                     print('Nama\t |Stock\t |Harga\t |Total Harga  ')     
                     for order in checkout_items:
                           print('{}\t |{}\t |{}\t |{}\t '.format(order[0], order[1],order[2], order[3]))

                     print(f"\nJumlah uang yang perlu disetor: {total_harga} ")
                     uang_konsumen = int(input("Masukkan jumlah uang yang dibayar konsumen: "))
                     if  uang_konsumen > total_harga:
                          kembalian = uang_konsumen - total_harga
                          print(f"Uang kembalian : {kembalian}")
                     elif  uang_konsumen == total_harga:
                            print("Uang yang dibayar pas")
                     else:
                          print("Uang tidak cukup")
            elif menu == 6: #summary
                 print("Summary aktivitas user pada aplikasi manajemen gudang: ")
                 penggabungan_list(added_items)
                 penggabungan_list(updated_items)
                 penggabungan_list(removed_items)
                 if not added_items:
                      print("- Tidak ada data barang yang ditambah")
                 else:     
                     for added in added_items:
                         print(f"- Data {added[0]} ditambahkan sejumlah {added[1]} dengan harga {added[2]}")
                 
                 if not updated_items:
                      print("- Tidak ada update barang di database")
                 else:
                     for ubah in updated_items:
                          print(f"- Data {ubah[0]} diupdate menjadi sebanyak {ubah[1]} dengan harga {ubah[2]}")
                 
                 if not removed_items:
                      print("- Tidak ada data barang yang dihapus")
                 else:
                      for i in range (len(removed_items)): 
                          print(f"- Data {removed_items[i]} dihapus dari database gudang")
                         
                 if total_harga == 0:
                    print("- Tidak ada transaksi barang")
                 else:  
                     rekap_transaksi = f"- Total transaksi sebesar {total_harga} dengan rincian "
                     rincian = []
                     for barang in checkout_items:
                          rincian.append([barang[1], barang[0]])
                     if len(rincian)==1:
                          rekap_transaksi += f"{rincian[0][0]} unit {rincian[0][1]}."
                          
                          print (rekap_transaksi)
                     elif len(rincian)==2:
                           for i in range(len(rincian)):
                               if i == len(rincian)-1:
                                    rekap_transaksi += f" dan {rincian[i][0]} unit {rincian[i][1] }."
                               else:
                                    rekap_transaksi += f"{rincian[i][0]} unit {rincian[i][1] }"
                           print (rekap_transaksi)
                     elif len(rincian)>2:
                     
                          for i in range(len(rincian)):
                               if i == len(rincian)-1:
                                    rekap_transaksi += f" dan {rincian[i][0]} unit {rincian[i][1] }."
                               else:
                                    rekap_transaksi += f"{rincian[i][0]} unit {rincian[i][1]}, " 
                          print (rekap_transaksi)
      except ValueError:
            print("Input salah")
        


