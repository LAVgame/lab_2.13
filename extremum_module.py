#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def extremum_function(type='max'):
    """
    Функция-замыкание, возвращающая внутреннюю функцию для нахождения минимального или максимального значения.
    По умолчанию type равен 'max'.
    """
    def find_extremum(collection):
        """
        Внутренняя функция для нахождения минимального или максимального значения в коллекции.
        """
        if type == 'max':
            return max(collection)
        elif type == 'min':
            return min(collection)
        else:
            raise ValueError("Некорректное значение параметра type. Допустимые значения: 'min' или 'max'.")

    return find_extremum