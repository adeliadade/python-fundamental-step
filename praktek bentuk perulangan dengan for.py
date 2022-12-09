"""
program perulangan penjualan gelang dengan for
"""

jumlah_stok_gelang = 40
print('owner berkata "jual semua stok gelang"')

jumlah_stok_gelang_yang_sudah_terjual = 0

for jumlah_stok_gelang_yang_sudah_terjual in range (1, jumlah_stok_gelang+1):
    print(f'stok gelang ke {jumlah_stok_gelang_yang_sudah_terjual} sudah terjual')