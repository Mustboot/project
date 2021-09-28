#! /usr/bin/python3

# ========= Задание 4 ===========
# Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
# 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
#
# Известно, что имя сотрудника всегда в конце строки.
# Сформировать из этих имён и вывести на экран фразы вида:
# 'Привет, Игорь!' Подумать, как получить имена сотрудников
# из элементов списка, как привести их к корректному виду.
# Можно ли при этом не создавать новый список?

# ======== Решение: ================
initial_list = ['инженер-конструктор Игорь',
                'главный бухгалтер МАРИНА',
                'токарь высшего разряда нИКОЛАй',
                'директор аэлита']

print("Вариант 1:") # более читаемый вариант на мой взгляд
for element in initial_list:
    # Запустив простой цикл for..in, далее создаем f-строку для вывода результата.
    # В f-строке указываем элемент списка, с вызовом методов slice (первый вызов) и capitalize.
    # capitalize() - для последющей нормализации найденного имени.
    # В качестве параметров метода slice вновь указываем элемент списка,
    # но реверсированый и с вызовом slice (второй вызов) и метода index(" ")
    # для поиска первого пробела с конца. Результат метода index дает нам позицию первого пробела с конца
    # и это значение (со знаком минус) используем как первое значение для slice (первого вызова)...
    print(f'Привет, {element[-element[::-1].index(" "):].capitalize()}!')

print("----------------\nВариант 2:") # менее читаемый, но в одну строку
print('\n'.join([f'Привет, {element[-element[::-1].index(" "):].capitalize()}!' for element in initial_list]))
