# TODO Напишите функцию find_common_participants
def find_common_participants(first_participants, second_participants, separator=','):
    participants_list_1 = first_participants.split(separator)
    participants_list_2 = second_participants.split(separator)

    common_participants = list(set(participants_list_1).intersection(participants_list_2))
    common_participants.sort()
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group)

print("Общие участники:", common_participants)

# TODO Провеьте работу функции с разделителем отличным от запятой
