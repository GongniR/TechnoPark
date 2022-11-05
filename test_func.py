from random import randint
import math


def Name(a, b, c):
    print(a, b, c)

list_train = [True if i%2 ==0 else False for i in range(100)]

# list_train = sorted(list_train, key = lambda a: abs(a), reverse=True)
print(list_train)