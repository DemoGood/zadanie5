#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    x = list(map(int, input("Введите 10 элементов: ").split()))
    s, k = 0, 0
    # Проверить количество элементов списка
    if len(x) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    # Цикл для обхода списка
    for i in x:
        if (abs(i) < 3) and (i % 9 == 0):
            k += 1
            s += i

    if s != 0:
        print("Количество элементов меньших по модулю 3 и кратных 9: ", k)
        print("Сумма элементов меньших по модулю 3 и кратных 9: ", s)
    else:
        print("В списке нет элементов меньших по модулю 3 и кратных 9.")
