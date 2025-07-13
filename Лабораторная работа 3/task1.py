# TODO Напишите функцию для поиска индекса товара
def item_search(item,list_of_item):
    k = 0
    for i in list_of_item:
        if item == i:
            return k
        k += 1
    return None





items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = item_search(find_item,items_list)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")##
    else:
        print(f"Товар '{find_item}' не найден в списке.")
