import random
import os

# symbol_list = ['+','-','*','/']
# symbol_number = [i for i in range(3,6)]

def compose_Formula(symbol_number,symbol_list):
    Selective_symbol = []
    numbers = []
    string = ''

    #在运算符号数中随机取一个数
    Selective_number = random.choice(symbol_number)

    #在运算符号中随机取Selective_number个符号
    for i in range(Selective_number):
        new_symbol = random.choice(symbol_number)
        Selective_symbol.append(new_symbol)
    number = Selective_number + 1

    #随机取Selective_number+1个正整数
    for i in range(number):
        n = random.randint(0,100)
        numbers.append(n)

    #组成算术运算式
    for i in range(Selective_number):
        random.shuffle(symbol_list)
        random.shuffle(numbers)
        new_Selective_symbol = random.choice(symbol_list)
        new_numbers = random.choice(numbers)
        string = string + str(new_numbers)+str(new_Selective_symbol)
    string = string + str(random.choice(numbers))

    return string

if __name__ == '__main__':
    string = compose_Formula(symbol_number,symbol_list)
    print(string)



