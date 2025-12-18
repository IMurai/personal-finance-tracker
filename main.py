# Function Untuk Menampilkan Menu
def menu():
    print("\n" + "="*40)
    print("       CATATAN KEUANGAN SEDERHANA")
    print("="*40)
    print("1. Tambah Transaksi")
    print("2. Lihat Saldo")
    print("3. Lihat Laporan")
    print("4. Lihat Satatistik")
    print("5. Keluar")
    print("="*40)

# Function Untuk Menambahkan Catatan Keuangan
def tambah_catatan_keuangan(data_keuangan):
    data_baru = {}

    while True: # Looping untuk mengatasi input yang salah
        try:
            # Input jenis dan nominal
            data_baru['Jenis'] = input("\nIncome/Expense: ")
            data_baru['Nominal'] = float(input("Nominal: Rp "))
            data_baru['Keterangan'] = input("keterangan: ")
            break
        except ValueError:
            print("MASUKAN NILAI YANG BENAR!!")

    # Menambahkan object kedalam array
    data_keuangan.append(data_baru)
    print("✔ Catatan Keuangan Berhasil Ditambahkan!!")

# Function Untuk Mengecek Saldo
def cek_saldo(data_keuangan):
    print("\n--------- Saldo ---------")

    # Kondisi Jika Belum Terdapat Laporan Income/Expense
    if len(data_keuangan) == 0:
        print("Belum Ada Catatan Keuangan")
        return

    total_income = 0
    total_expense = 0 
    # Looping menghitung Total Income/Exepense
    for transaksi in data_keuangan:
        if transaksi['Jenis'].lower() == "income":
            total_income += transaksi['Nominal']
        elif transaksi['Jenis'].lower() == "expense":
            total_expense += transaksi['Nominal']

    #Menghitung Saldo
    saldo = total_income - total_expense

    # Output Saldo
    print(f"Total Income: Rp {total_income}")
    print(f"Total Expense: Rp {total_expense}")
    print("-" * 25)
    print(f"Saldo: Rp {saldo}")
    print("-" * 25)

    # Percabangan peringatan Saldo
    if saldo < 0:
        print("⚠️ PERINGATAN: Saldo Anda Negatif!!")
    elif saldo < 50000:
        print("💡 Hati - Hati Saldo Menipis!!")

# Function Untuk Melihat Laporan Keuangan
def lihat_laporan(data_keuangan):
    print("\n-------- Laporan Keuangan --------")

    # Kondisi Jika Belum Terdapat Laporan Income/Expense
    if len(data_keuangan) == 0:
        print("Belum Ada Catatan Keuangan")
        return
    
    # Menampilkan Tabel
    for i, data_baru in enumerate(data_keuangan, start=1):
        print(f"{i}. {data_baru['Jenis']}    Rp {data_baru['Nominal']}    {data_baru['Keterangan']}")
    print("-"*34)

# Function Untuk Melihat Statistik Keuangan
def lihat_statistik(data_keuangan):
    print("\n---- Statistik Keuangan ----")

    if len(data_keuangan) == 0:
        print("Belum Ada Catatan Keuangan")
        return
    
    jumlah_transaksi = len(data_keuangan)
    
    # Menghitung Jumlah Income/Expense
    jumlah_income = 0
    jumlah_expense = 0 
    
    for transaksi in data_keuangan:
        if transaksi['Jenis'].lower() == "income":
            jumlah_income += 1
        elif transaksi['Jenis'].lower() == "expense":
            jumlah_expense += 1

    # Output Saldo
    print(f"Jumlah Total Transaksi: {jumlah_transaksi}")
    print(f" - Income: {jumlah_income} Transaksi")
    print(f" - Expense: {jumlah_expense} Transaksi")
    print("-" * 28)

# Array Laporan
data_keuangan = []

while True: #Looping
    # Menampilkan Menu Dengan Mengunakan Function
    menu()
    
    # Melakukan Percabangan Dari Pilihan Menu Mengunakan Function
    pilihan = input("Masukan Pilihan: ")
    if pilihan == "1":
        tambah_catatan_keuangan(data_keuangan)
    elif pilihan == "2": 
        cek_saldo(data_keuangan)
    elif pilihan == "3": 
        lihat_laporan(data_keuangan) 
    elif pilihan == "4":
        lihat_statistik(data_keuangan)
    elif pilihan == "5": 
        print("Terima Kasih Telah Memakai Program Ini")
        break
    else:
        print("MASUKAN PILIHAN YANG BENAR!!")
        continue
