size_of_disk_Mb = 1.44
count_of_pages = 100
count_of_str = 50
count_of_symbols_on_str = 25
size_of_each_symbol_Byte = 4

size_of_disk_Byte = size_of_disk_Mb * 1024 * 1024
size_of_book = count_of_pages * count_of_str *count_of_symbols_on_str * size_of_each_symbol_Byte

count_of_books = int(size_of_disk_Byte // size_of_book)

print("Количество книг, помещающихся на дискету:", count_of_books)
