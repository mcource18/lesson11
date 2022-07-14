"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""
import os
import pickle

class Buyer:
    __account = 0
    __list_shop = {}
    __file_name='data.pickle'

    def __init__(self):
        try:
            if os.path.exists(self.__file_name):
                with open(self.__file_name, 'rb') as f:
                    self.__account, self.__list_shop = pickle.load(f)
        except:
            print("Error read file")

    def add(self, sum):
        self.__account += sum

    def buy(self, sum):
        if sum > self.__account:
            print("Денег не хватает")
            return

        product = input("Введите название покупки ")
        if product in self.__list_shop:
            self.__list_shop[product] += sum
        else:
            self.__list_shop[product] = sum
        self.__account -= sum

    def history(self):
        return self.__list_shop.items()

    def write(self):
        try:
            with open(self.__file_name, 'wb') as f:
                pickle.dump([self.__account,self.__list_shop], f)
        except:
            print("Error write file")




def start_buyer():
    buyer = Buyer()
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню ')
        if choice == '1':
            sum = input("Введит сумму для пополнения счета ")
            buyer.add(int(sum))
        elif choice == '2':
            sum = input("Введит сумму для покупки ")
            buyer.buy(int(sum))
        elif choice == '3':
             for key,val in buyer.history():
                 print(f'{key} - {val}')
        elif choice == '4':
            buyer.write()
            break
        else:
            print('Неверный пункт меню')
