import info_sistem as pi
def option():
    print("\nТурбаза")
    ch = int(input('Введите что хотите сделать: \n \
    1: Показать все записи \n \
    2: Поиск сотрудника по фамилии \n \
    3: Поиск сотрудника по должности \n \
    4: Удалить существующую запись \n \
    : Выход\n \
    Ваш выбор: '))

    if ch == 2:
        Surn = str(input("Введите фамилию рабочего: "))
        if Surn in pi.personal['Фамилия']:
            index = pi.personal['Фамилия'].index(Surn)
        print(f"{pi.personal['ID'][index]}, {pi.personal['Имя'][index]},{pi.personal['Фамилия'][index]}\n,{pi.personal['Дата рождения'][index]}, {pi.personal['Должность'][index]}, {pi.personal['Зарплата'][index]}")
        print('\nХотите выполнить какую-то другую операцию??? Y или N: ')
        num = input()
        if num == 'Y' or 'y' or 'У' or 'у':
            option()
        exit()

    elif ch == 3:
        Surn = str(input("Введите должность рабочего: "))
        for i in pi.personal:
            if Surn in pi.personal['Должность']:
                index = pi.personal['Должность'].index(Surn)
                print(f"{pi.personal['ID'][index]}, {pi.personal['Имя'][index]},{pi.personal['Фамилия'][index]},{pi.personal['Дата рождения'][index]}, {pi.personal['Должность'][index]}, {pi.personal['Зарплата'][index]}")
            print('\nХотите выполнить какую-то другую операцию??? Y или N: ')
            num = input()
            if num == 'Y' or 'y' or 'У' or 'у':
                option()
            exit()

    elif ch == 4:
        Surn = str(input("Введите ID сотрудника: "))
        if Surn in pi.personal['ID']:
            index = pi.personal['ID'].index(Surn)
            del pi.personal['ID'][index] 
            del pi.personal['Имя'][index]
            del pi.personal['Фамилия'][index]
            del pi.personal['Дата рождения'][index]
            del pi.personal['Должность'][index]
            del pi.personal['Зарплата'][index]
        print(pi.personal)
        print('\nХотите выполнить какую-то другую операцию??? Y или N: ')
        num = input()
        if num == 'Y' or 'y' or 'У' or 'у':
            option()
        exit()

    elif ch == 1:
        print(pi.personal)
        print('\nХотите выполнить какую-то другую операцию??? Y или N: ')
        num = input()
        if num == 'Y' or 'y' or 'У' or 'у':
            option()
        exit()

option()