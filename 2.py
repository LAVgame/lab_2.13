#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from extremum_module import extremum_function

if __name__ == "__main__":
    my_collection = [3, 7, 1, 5, 9]

    # Создаем функцию-замыкание для поиска максимального значения (по умолчанию)
    max_extremum_func = extremum_function()
    max_result = max_extremum_func(my_collection)
    print("Максимальное значение в коллекции:", max_result)

    # Создаем функцию-замыкание для поиска минимального значения
    min_extremum_func = extremum_function(type='min')
    min_result = min_extremum_func(my_collection)
    print("Минимальное значение в коллекции:", min_result)