banknotes = { 
    "10": 1000,
    "50": 1000,
    "100": 4000,
    "500": 2000,
    "1000": 4000,
    "2000": 1000,
    "5000": 1000
}

admin = {
    "login": "admin",
    "password": 1234
}

cards= {
    "12341234": 1000,
    "43214321": 1111,
    "22222222": 2222 
}

balanc = {
    "12341234": 1_159_753,
    "43214321": 159_423,
    "22222222": 753_859
}
exchange_rate = {
    "dollar": 88.59,
    "euro": 96.58,
    "yuan": 12.27,
}

credits = {
    "mortgage": 2_432_500,
    "consumer": 650_000,
    "auto": 1_800_000
}

def comands():
    pass

def func_bank_help():
    pass

def card_password():
    user_number_card = input("Введите номер карты: ")
    count = 3
    if user_number_card in cards.keys():
        user_pin_card = cards[user_number_card]
        while count > 0:
            user_password_card = int(input("Введите пароль: "))
            count -= 1
            if user_password_card == user_pin_card:
                return "Выберите операцию"
            else: 
                print(f"Пин-код не верный, осталось {count} попытка(и)")
        else:
            return "Карта заблокирована, обратитесь в отделение банка"        
    else:
        cards[user_number_card] = input("Введите пароль: ")
        return "Выберите операцию"   


def add_card():
    user_number_card = input("Введите номер карты: ")
    print("Пароль не должен начинаться с цифры ноль")
    print("Пароль должен быть равен 4 цифры")
    user_pin_card = input("Введите пароль: ")
    first_digit = int(user_pin_card) // 1000
    if len(user_pin_card) == 4:
        if first_digit != 0:
            cards[user_number_card] = user_pin_card
            return cards
        else:
            while len(str(user_pin_card)) != 4 or first_digit == 0:
                print("Пароль не должен начинаться с цифры ноль")
                print("Пароль должен быть равен 4 цифры")
                user_pin_card = input("Введите пароль: ")
                first_digit = int(user_pin_card) // 1000
            cards[user_number_card] = int(user_pin_card)
            return cards
    else:
        print("Пароль не корректен")
        while len(str(user_pin_card)) != 4 or first_digit == 0:
            print("Пароль должен быть равен 4 цифрам и не начинаться с нуля")
            user_pin_card = input("Введите пароль: ")
            first_digit = int(user_pin_card) // 1000
        cards[user_number_card] = user_pin_card
        return cards
    


print(add_card())


