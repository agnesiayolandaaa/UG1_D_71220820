print ("================KASIR================")
total_belanjaan = 0

while True:
    harga_belanjaan = input(" Harga Barang:")

    if harga_belanjaan.isdigit():
        total_belanjaan += int(harga_belanjaan)
    else:
        print("INVALID")
    
    tanya_lagi = input("Apakah anda membeli barang lagi? (yes/no):")
    if tanya_lagi == 'yes':
        harga_belanjaan = input(" Harga Barang:")
        tanya_lagi = input("Apakah anda membeli barang lagi? (yes/no):")
    elif tanya_lagi == 'no':
        print("TOTAL BELANJA: ", total_belanjaan)
        break
    else:
        print ("INVALID")
        break

