def factorial(n):
    if n < 0:
        print (ValueError("Факториал отрицательного числа не определен"))
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def element(input_list):
    return list(set(input_list))

def sort(words):
    list = {}
    for word in words:
        length = len(word)
        if length not in list:
            list[length] = []
        list[length].append(word)
    return list