string = ""

a = int(input("Masukkan Angka :"))
bar = a
# Looping Baris
while bar >= 0:
	# Looping Kolom Spasi Kosong
	kol = bar
	while kol > 0:
		string = string + "   "
		kol = kol - 1
	# Looping Kolom Bintang Sisi Kiri		
	kiri = 1
	while kiri < (a - (bar-1)):
		string = string + " * "
		kiri = kiri + 1		
	# Looping Kolom Bintang Sisi Kanan
	kanan = 1
	while kanan < kiri -1:
		string = string + " * "
		kanan = kanan + 1	

	string = string + "\n\n"
	bar = bar - 1

bar = 1	
# Looping Baris
while bar <= a:
	kol = bar+1
	# Looping Kolom Spasi Kosong
	while kol > 1:
		string = string + "   "
		kol = kol - 1
	# Looping Kolom Bintang Sisi Kiri	
	kiri = 0
	while kiri < (a - bar):
		string = string + " * "
		kiri = kiri + 1	
	# Looping Kolom Bintang Sisi Kanan
	kanan = kiri	
	while kanan > 1:
		string = string + " * "
		kanan = kanan - 1

	string = string + "\n\n"
	bar = bar + 1
print (string)