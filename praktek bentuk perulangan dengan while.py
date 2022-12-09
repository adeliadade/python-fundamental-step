"""
program perulangan penjualan gelang dengan while
"""

jumlah_stok_gelang = 40
print('owner berkata "jual semua stok gelang"')

jumlah_stok_gelang_yang_sudah_terjual = 0
print(f"jumlah stok gelang yang sudah terjual {jumlah_stok_gelang_yang_sudah_terjual}")

while jumlah_stok_gelang_yang_sudah_terjual < jumlah_stok_gelang:
    jumlah_stok_gelang_yang_sudah_terjual = jumlah_stok_gelang_yang_sudah_terjual + 1

    print(f"jumlah gelang ke {jumlah_stok_gelang_yang_sudah_terjual} sudah terjual")
