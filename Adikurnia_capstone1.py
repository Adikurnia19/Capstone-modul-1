stock = [
        {'Nomor SKU' : 'AI01',
        'Merk' : 'Apple',
        'Tipe' : 'Iphone',
        'Seri' : '13',
        'Stock' : 4 ,
        'Warna' : 'Hitam'
        },
         {'Nomor SKU' : 'SG01',
        'Merk' : 'Samsung',
        'Tipe' : 'Galaxy',
        'Seri' : 'Note 13',
        'Stock' : 6 ,
        'Warna' : 'Grey'    
         },
          {'Nomor SKU' : 'AI03',
        'Merk' : 'Apple',
        'Tipe' : 'Iphone ',
        'Seri' : '13 Pro',
        'Stock' : 4 ,
        'Warna' : 'Green'
        },
         {'Nomor SKU' : 'AI02',
        'Merk' : 'Apple',
        'Tipe' : 'Iphone',
        'Seri' : '14',
        'Stock' : 4 ,
        'Warna' : 'Gold'
        },
         {'Nomor SKU' : 'SG04',
        'Merk' : 'Samsung',
        'Tipe' : 'S',
        'Seri' : '21',
        'Stock' : 4 ,
        'Warna' : 'Black'
        }
]

def headerMenu():
    print('*' * 20,'\tWarehouse Management System\t','*' * 20)
    print('=' * 27,'DIGICELLINDONESIA','=' * 27)
    print('\n')

def headerTable():
    print('-'*97)
    print('|\tSKU:\t|\tMERK:\t|\tTIPE:\t|\tSERI:\t|\tQTY:\t|\tWARNA:\t|')
    print('-'*97)

def mainMenu():
        global pilihan
        headerMenu()
        print('\t**MAIN MENU**\n')
        print('\t 1. Tampilkan Stock (READ)')
        print('\t 2. Tambahkan Produk Baru (CREATE) ')
        print('\t 3. Update Stock(UPDATE)')
        print('\t 4. Menghapus Produk  (DELETE)')
        print('\t 5. Keluar')

        pilihan = int(input('Masukan Pilihan : '))

########READ MENU
def showStock():
        global pilihan1
        headerMenu()
        print('\t**READ MENU**')
        pilihan1 = int(input('''
        1. Daftar Barang
        2. pencarian Berdasarkan Merk
        3. Data Riwayat Barang
        4. Kembali ke menu utama            
Masukan pilihan anda: \n'''))
###############################################################        
####SUB MENU PILIHAN 1
#####DAFTAR BARANG
def subMenuShowstock():
     global subMenuShowPilihan
     headerMenu()
     subMenuShowPilihan =  int(input('''
        1. Daftar Barang Tersedia
        2. Daftar Barang Habis
        3. Daftar Semua Barang
        4. Kembali ke Read Menu          
Masukan pilihan anda: '''))
#DAFTAR BARANG TERSEDIA
def showNotZeroStock():
    headerMenu()
    items_with_zero_stock = []
    for item in stock:
        if item['Stock'] != 0:
            items_with_zero_stock.append(item)
    if items_with_zero_stock:
        print('\t\t|Daftar barang tersedia|\t\t')
        headerTable()
        for item in items_with_zero_stock:
            print(f'|\t{item['Nomor SKU']}\t|\t{item['Merk']}\t|\t{item['Tipe']}\t|\t{item['Seri']}\t|\t{item['Stock']}\t|\t{item['Warna']}\t|')
        print('-' * 97,'\n')
# DAFTAR BARANG HABIS
def showZeroStock():
    headerMenu()
    items_with_zero_stock = []
    for item in stock:
        if item['Stock'] == 0:
            items_with_zero_stock.append(item)
    if items_with_zero_stock:
        print('Daftar barang dengan stok 0:')
        headerTable()
        for item in items_with_zero_stock:
            print(f'|\t{item['Nomor SKU']}\t|\t{item['Merk']}\t|\t{item['Tipe']}\t|\t{item['Seri']}\t|\t{item['Stock']}\t|\t{item['Warna']}\t|')
        print('-' * 97)
    else:
        print('Saat ini idak ada barang dengan stok 0.')   
# MENAMPILKAN LIST SEMUA BARANG
def showAllStock():
        print('*'*38,'DAFTAR SEMUA INVENTORY','*'*38)
        headerTable()
        for allstock in range(len(stock)):
              print(f'|\t{stock[allstock]['Nomor SKU']}\t|\t{stock[allstock]['Merk']}\t|\t{stock[allstock]['Tipe']}\t|\t{stock[allstock]['Seri']}\t|\t{stock[allstock]['Stock']}\t|\t{stock[allstock]['Warna']}\t|')
        print('-'*97,'\n')

###########SUB MENU PILIHAN 3
########PENCARIAN BERDASARKAN MERK
# MENAMPILKAN LIST MERK
def showBrand():
        global input_brand
        headerMenu()
        uniqueBrand = set()
        for brand in stock:
            uniqueBrand.add(brand['Merk'])
        uniquebrandList = sorted(uniqueBrand)
        print('*'*8,'DAFTAR MERK','*'*8)
        print('-----------------')
        print('|\tMERK:\t|')
        print('-----------------')
        for brandlist in uniquebrandList:
                print(f'|\t{brandlist}\t|')
        print('-----------------')
        input_brand = input('Masukkan nama merk: ').upper()  
        print('\n')

# Pencarian Berdasarkan Merk
def searchByBrand():
    headerMenu()
    while True:
        print('*'*40,f'LIST MERK {input_brand}','*'*40)
        headerTable()
        found_items = False
        for item in stock:
            if item['Merk'].upper()  == input_brand.upper():
                found_items = True
                print(f'|\t{item['Nomor SKU']}\t|\t{item['Merk']}\t|\t{item['Tipe']}\t|\t{item['Seri']}\t|\t{item['Stock']}\t|\t{item['Warna']}\t|')
        if not found_items:
            print('*'*30,f'Merk {input_brand} belum terdaftar','*'*30)
            print('\n')
            return True
        print('-'*97)
        print('\n')
        return False


##########################################################################################################################################        
##########SUB MENU PILIHAN 3
#S####MENU DATA RIWAYAT BARANG      
def historicalMenu():
     global subMenuRiwayatPilihan
     headerMenu()
     subMenuRiwayatPilihan =  int(input('''
        1. Riwayat Barang Masuk
        2. Riwayat Barang Keluar
        3. Riwayat produk dihapus 
        4. Kembali ke menu sebelumnya        
Masukan pilihan anda: '''))
# RIWAYAT BARANG MASUK
def showHistoricalStockIn():
    headerMenu()
    if historicalStockIn:
        print('Riwayat penambahan stok/INBOUND:')
        print('-' * 128)
        print('|\tSKU:\t|\tMERK:\t|\tTIPE:\t|\tSERI:\t|\tSTOCK:\t|\tWARNA:\t|\tTANGGAL:\t|')
        print('-' * 128)
        for item in historicalStockIn:
            print(f'|\t{item['Nomor SKU']}\t|\t{item['Merk']}\t|\t{item['Tipe']}\t|\t{item['Seri']}\t|\t{item['Stock Dikurangi']}\t|\t{item['Warna']}\t|\t{item['Tanggal']}\t|')
            print('-' * 128)
            break
    else:
        print('Tidak ada riwayat penambahan stok')  
# RIWAYAT BARANG KELUAR
def showHistoricalStockOut():
    headerMenu()
    if historicalStockOut:
        print('Riwayat pengurangan stok/OUTBOUND:')
        print('-' * 128)
        print('|\tSKU:\t|\tMERK:\t|\tTIPE:\t|\tSERI:\t|\tSTOCK:\t|\tWARNA:\t|\tTANGGAL:\t|')
        print('-' * 128)
        for item in historicalStockOut:
            print(f'|\t{item['Nomor SKU']}\t|\t{item['Merk']}\t|\t{item['Tipe']}\t|\t{item['Seri']}\t|\t{item['Stock Dikurangi']}\t|\t{item['Warna']}\t|\t{item['Tanggal']}\t|')
            print('-' * 128)
    else:
        print('Tidak ada riwayat pengurangan stok.')
# RIWAYAT BARANG DIHAPUS
def showHistoricalDel():
    headerMenu()  
    if not historicalDelProd:
        print('\nTidak ada produk yang dihapus.\n')
    else:
        for item in historicalDelProd:
            print('Riwayat penghapusan produk')
            headerTable()
            print(f'|\t{item['Nomor SKU']}\t|\t{item['Merk']}\t|\t{item['Tipe']}\t|\t{item['Seri']}\t|\t{item['Stock']}\t|\t{item['Warna']}\t|')
            print('-' * 97,'\n')

#####MENU PILIHAN 2
####CREATE MENU
def addProductMenu():
     global pilihan2
     headerMenu()
     print('\t**CREATE MENU**')
     pilihan2 = int(input('''
        1. Menambahkan Produk
        2. Kembali ke menu utama           
    Masukan pilihan anda: '''))
#MENAMBAHKAN PRODUK BARU 
def newProductInput():
    while True:
        global validasiTambah
        showAllStock()
        skuBaru = input('Masukan nomor SKU: ').upper()
        if not skuBaru.isalnum():
             print('Nomor SKU harus kombinasi Alfabet dan Angka!!') 
             newProductInput()
        if checkerSKU(skuBaru):
            break
        merkBaru = input('Masukan Merk produk: ').capitalize()
        tipeBaru = input('Masukan Tipe: ').capitalize()
        seriBaru = input('Masukan Seri barang: ').capitalize()
        stockbaru = int(input('Masukan Jumlah Stock: '))
        warnaBaru = input('Masukan Warna: ').capitalize()
        headerTable()
        print(f'|\t{skuBaru}\t|\t{merkBaru}\t|\t{tipeBaru}\t|\t{seriBaru}\t|\t{stockbaru}\t|\t{warnaBaru}\t|')
        print('-'*97,'\n')
        validasiTambah = input('Apakah anda yakin akan menambahkan produk ini? (Y/N):').upper()
        if validasiTambah == 'Y':
            print('\n')
            print('\n Produk anda sudah ditambahkan \n')
            stock.append({'Nomor SKU':skuBaru, 'Merk':merkBaru,'Tipe':tipeBaru,'Seri':seriBaru,'Stock':stockbaru,'Warna':warnaBaru})
            showAllStock()
            break
        else:
             print('\nTerima kasih\n')      
             break
# CEK DUPLIKAT NOMOR SKU Untuk SKU BAru
def checkerSKU(skuBaru):
    for sku in range(len(stock)):
        checkSku = stock[sku]['Nomor SKU']
        if checkSku == skuBaru:
            print('\nNomor yang anda masukan sudah terdaftar\n')
            return True
    return False

##########MENU PILIHAN 3
#####MENU UPDATE
def stockUpdateMenu():
     global add_del_choice
     headerMenu()
     print('\t**UPDATE MENU**')
     add_del_choice = int(input('''
        1. Menambah Produk / Inbound
        2. Mengurangi Produk / Outbound
        3. Mengubah Data Produk / Edit
        4. Kembali ke menu utama             
    Masukan pilihan anda: '''))

##MENAMBAH STOCK /INBOUND
def updateStock():
    headerMenu()
    showAllStock()
    global stockUpdate
    while True:
        skuUpdateStock = input('Masukan Nomor SKU: ').upper()
        item_match = []
        for checkSku in stock: 
            if checkSku['Nomor SKU'].upper() == skuUpdateStock.upper():
                item_match.append(checkSku)
        for showing in item_match:
            headerTable()
            print(f'\n|\t{showing['Nomor SKU']}\t|\t{showing['Merk']}\t|\t{showing['Tipe']}\t|\t{showing['Seri']}\t|\t{showing['Stock']}\t|\t{showing['Warna']}\t|')
            print('-'*97,'\n')
        if item_match:
            stockUpdate = int(input('Masukan jumlah yang akan ditambahkan kedalam stok: '))
            validasi = (input(f'\nApakah anda akan menambahkan stock {showing['Nomor SKU']} sebanyak {stockUpdate} Unit? (Y/N): ').upper())
            try:
                if validasi == 'Y':
                    for item in item_match:
                            item['Stock'] += stockUpdate
                            tanggal = input('Masukkan tanggal penambahan (DD-MM-YYY): ')
                            historicalStockIn.append({
                                'Nomor SKU': item['Nomor SKU'],
                                'Merk': item['Merk'],
                                'Tipe': item['Tipe'],
                                'Seri': item['Seri'],
                                'Stock Dikurangi': stockUpdate,
                                'Warna': item['Warna'],
                                'Tanggal': tanggal})
                            print('\nStock berhasil ditambahkan\n')
                            headerTable()
                            print(f'|\t{item['Nomor SKU']}\t|\t{item['Merk']}\t|\t{item['Tipe']}\t|\t{item['Seri']}\t|\t{item['Stock']}\t|\t{item['Warna']}\t|')
                            print('-'*97,'\n')
                    break
                elif validasi == 'N':
                    print('\nPenambahan Stock dibatalkan, terima kasih\n')  
                    break
                else:
                     print('\nFormat yang anda masukkan tidak ditemukan\n')
                     break
            except ValueError:
                    print('\nFormat yang anda masukkan tidak ditemukan\n')
        else:
             print('\nNomor SKU tidak ditemukan\n')
             break
#MENGURANGI STOK / OUTBOUND
def delStock():
    headerMenu()
    showAllStock()
    while True:
        skuUpdateStock = input('Masukan Nomor SKU: ').upper()
        item_match = []
        for checkSku in stock: 
            if checkSku['Nomor SKU'].upper() == skuUpdateStock.upper():
                item_match.append(checkSku)
        for showing in item_match:
                headerTable()
                print(f'|\t{showing['Nomor SKU']}\t|\t{showing['Merk']}\t|\t{showing['Tipe']}\t|\t{showing['Seri']}\t|\t{showing['Stock']}\t|\t{showing['Warna']}\t|')
                print('-'*97,'\n')
        if item_match:
            stockUpdate = int(input('Masukan jumlah yang akan dikurangi dari stock: '))
            validasi = (input(f'Apakah anda akan menambahkan stock {showing['Nomor SKU']} sebanyak {stockUpdate} Unit? (Y/N): ').upper())
            try:
                if validasi == 'Y':
                    for item in item_match:
                            item['Stock'] -= stockUpdate
                            tanggal = input('Masukkan tanggal pengurangan (DD-MM-YYYY): ')
                            historicalStockOut.append({
                                'Nomor SKU': item['Nomor SKU'],
                                'Merk': item['Merk'],
                                'Tipe': item['Tipe'],
                                'Seri': item['Seri'],
                                'Stock Dikurangi': stockUpdate,
                                'Warna': item['Warna'],
                                'Tanggal': tanggal})
                            print('\n')
                            print('Stock berhasil dikurangi')
                            headerTable()
                            print(f'|\t{item['Nomor SKU']}\t|\t{item['Merk']}\t|\t{item['Tipe']}\t|\t{item['Seri']}\t|\t{item['Stock']}\t|\t{item['Warna']}\t|')
                            print('-'*97,'\n')
                    break             
                elif validasi == 'N':
                    print('\nPengurangan Stock dibatalkan, terima kasih\n')  
                    break
                else:
                     print('\nFormat yang anda masukkan tidak ditemukan\n')
                     break
            except ValueError:
                    print('\nFormat yang anda masukkan tidak ditemukan\n')
        else:
             print('\nNomor SKU tidak ditemukan\n')
             break
#MENGUBAH DATA
def updatebyValue():
    headerMenu()
    showAllStock()
    global skubyValue
    skubyValue = input('Masukan nomor SKU yang ingin diubah: ').strip().upper()
    item_found = False
    for item in stock:
        if item['Nomor SKU'].upper() == skubyValue.upper():
            item_found = True
            headerTable()
            print(f'|\t{item['Nomor SKU']}\t|\t{item['Merk']}\t|\t{item['Tipe']}\t|\t{item['Seri']}\t|\t{item['Stock']}\t|\t{item['Warna']}\t|')
            print('-'*97,'\n')
            key_to_update = input('Masukkan nama key yang akan diubah: ').capitalize()
            if key_to_update not in item:
                print(f'\nData',{key_to_update},'tidak ditemukan\n')
                return
            newValue = input(f'Masukkan nilai baru untuk {key_to_update} dalam {skubyValue}: ')
            if key_to_update == 'Stock':
                try:
                    newValue = int(new_value)
                except ValueError:
                    print('\nJumlah stok harus berupa angka\n')
                    return
            item[key_to_update] = newValue
            print('\nData telah diperbaharui\n')

#########MENU PILIHAN 3
######MENU DELETE STOCK
def delProductMenu():
     global delMenu
     headerMenu()
     print('\n**DELETE MENU**\n')
     delMenu = int(input('''
        1. Menghapus Produk
        2. Kembali ke menu utama           
    Masukan pilihan anda: \n'''))
##MENGHAPUS PRODUK
def delProduct():
    showAllStock()
    while True:
        skuDel = input('Masukan Nomor SKU: ').upper()
        if not checkerDelStock(skuDel):
             break
        for item in stock:
            if item['Nomor SKU'] == skuDel:
                print('\n')
                headerTable()
                print(f'|\t{item['Nomor SKU']}\t|\t{item['Merk']}\t|\t{item['Tipe']}\t|\t{item['Seri']}\t|\t{item['Stock']}\t|\t{item['Warna']}\t|')
                print('-'*97,'\n')
                break
        konfirmasi = input('Apakah Anda yakin ingin menghapus produk ini? (Y/N): ').upper()
        try:
            if konfirmasi == 'Y':
                for j in range(len(stock)):
                    checker = stock[j]['Nomor SKU']
                    if checker == skuDel:
                        historicalDelProd.append(stock[j])
                        deletingIndex = j
                        del stock[deletingIndex] 
                        print(f'\nProduk dengan SKU {skuDel} telah dihapus.\n')
                        showAllStock()
                        break
                break           
            elif konfirmasi == 'N':
                print('Penghapusan dibatalkan')
            else:
                print('\nFormat yang anda masukkan tidak ditemukan\n')  
        except ValueError:
                    print('\nFormat yang anda masukkan tidak ditemukan\n') 
# cHECKER   
def checkerDelStock(skuDel):
    for skuchecker in range(len(stock)):
        checkSku = stock[skuchecker]['Nomor SKU']
        if checkSku == skuDel:
            return True
    print('\nMasukan Nomor SKU yang sudah terdaftar\n')
    return False
#####vALIDASI KELUAR
def validasiKeluar():
    apakahKeluar = input('Apakah anda ingin kembali ke Menu sebelumnya? (Y/N): ').upper()
    while True:
        if apakahKeluar == 'Y':
            print('\nTERIMA KASIH\n')
            return True
        elif apakahKeluar == 'N':
            return False
        else:
            print('\nPilihan anda tidak ditemukan\n')

                               
historicalStockIn = []          
historicalStockOut = []           
historicalDelProd = []          
                
while True:
    try:
        mainMenu()
        if pilihan == 1 :
                while True:
                    try:
                        showStock()
                        if pilihan1 == 1 :
                            while True:
                                try:
                                    subMenuShowstock()
                                    if subMenuShowPilihan == 1 :
                                        showNotZeroStock()
                                    elif subMenuShowPilihan == 2 :
                                        showZeroStock()
                                    elif subMenuShowPilihan == 3 :
                                        showAllStock()
                                    elif subMenuShowPilihan == 4 :
                                        if validasiKeluar():
                                            break
                                    else:
                                        print('Masukan Sesuai Pilihan!!')
                                except ValueError:
                                     print('\n**Pilihan tidak ditemukan: Masukan angka yang ada di menu**\n')
                        elif pilihan1 == 2:
                            showBrand()
                            searchByBrand()
                        elif pilihan1 == 3:
                            try:
                                while True:
                                    historicalMenu()
                                    if subMenuRiwayatPilihan == 1:
                                        showHistoricalStockIn()
                                    elif subMenuRiwayatPilihan == 2:
                                        showHistoricalStockOut()
                                    elif subMenuRiwayatPilihan == 3:
                                        showHistoricalDel()
                                    elif subMenuRiwayatPilihan == 4 :
                                        if validasiKeluar():
                                            break
                                    else:
                                        print('Masukan Sesuai Pilihan!!')
                            except ValueError:
                                print('\n**Pilihan tidak ditemukan: Masukan angka yang ada di menu**\n')
                                    
                        elif pilihan1 == 4:
                              if validasiKeluar():
                                        break
                        else:
                              print('Masukan Sesuai Pilihan!!')
                    except ValueError:
                         print('\n**Pilihan tidak ditemukan: Masukan angka yang ada di menu**\n')
        elif pilihan == 2: 
                while True:
                    try:
                        addProductMenu()
                        if pilihan2 == 1 :
                            newProductInput()
                        elif pilihan2 == 2 :
                            if validasiKeluar():
                                break
                        else:
                            print('Masukan Sesuai Pilihan!!')
                    except ValueError:
                        print('\n**Pilihan tidak ditemukan: Masukan angka yang ada di menu**\n')        
        elif pilihan == 3:  
            while True:
                    try:
                        stockUpdateMenu()
                        if add_del_choice == 1:
                            updateStock()
                        elif add_del_choice == 2:
                            delStock()
                        elif add_del_choice == 3:
                             updatebyValue()
                        elif add_del_choice == 4:
                            if validasiKeluar():
                                break
                        else:
                            print('Masukan pilihan sesuai nomor diatas')
                    except ValueError:
                         print('\n**Pilihan tidak ditemukan: Masukan angka yang ada di menu**\n')

        elif pilihan == 4:
             while True:
                try:
                    delProductMenu()
                    if delMenu == 1:
                        delProduct()
                    elif delMenu == 2:
                        if validasiKeluar():
                            break
                    else:
                        print('\n**Pilihan tidak ditemukan: Masukan angka yang ada di menu**\n')      
                except ValueError:
                    print('\n**Pilihan tidak ditemukan: Masukan angka yang ada di menu**\n')
        elif pilihan == 5:
            if validasiKeluar():
                break
        else:
             print('\n**Pilihan tidak ditemukan: Masukan angka yang ada di menu**\n')      
    except ValueError:
        print('\n**Pilihan tidak ditemukan: Masukan angka yang ada di menu**\n')
    
     

                
         