#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = int(input("Начальная дистанция"))
    b = int(input("На какой процент увеличивается дистанция"))
    c = int(input("Количество дней тренировок"))

    t = 1
    d = b/100
    x = a
    while t < c:
        x += a + x*d
        t += 1
        if t == c:
            break


    if x < a:
        print("Ошибка введенных данных")
    else:
        print(x)
        exit(1)