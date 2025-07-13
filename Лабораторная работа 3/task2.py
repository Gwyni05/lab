def find_common_participants(list_1,list_2, separator=''):
    list_1 = list_1.split(separator)
    list_2 = list_2.split(separator)
    print(list_1,list_2)
    final_list = list(set(list_1).intersection(list_2))
    final_list.sort()
    return final_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group,participants_second_group,"|"))
