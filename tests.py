from package.calculator import calculate

'''Проверим как работает сумма, произведение, деление'''
# Проверим сумму
def test_sum():
  assert calculate(1, 2, "+") == 3, "Сумма должна быть равна числу 3 типа int"


# проверим тип суммы
def test_type_of_result_sum():
  assert type(calculate(1, 2, "+")) is int, "Сумма должна быть равна числу 3 типа int"

#проверим умножение 
def test_mul():
  assert calculate(10, 5, "*") == 50, "Умножение должно быть равно числу 50 типа int"


# проверим тип умножения  
def test_type_of_result_mul():
  assert type(calculate(10, 5, "*")) is int, "Умножение должно быть равно числу 50 типа int"

#Проверим деление 
def test_del():
  assert calculate(28, 7, "/") == 4, "Деление должно быть равно числу 4 типа float"

#Проверим тип делеление
def test_type_of_result_del():
  assert type(calculate(25, 2, "/")) is float, "Деление должно быть равно числу 12.5 типа float"  


if __name__ == "__main__": 
    test_sum() 
    test_type_of_result_sum()
    test_mul()
    test_type_of_result_mul()
    test_del()
    test_type_of_result_del()
    print("Спасибо, что воспользовались данным калькулятором!") 

import unittest

class TestFunc(unittest.TestCase): # создаем свой класс для тестов
     def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
     def test_isupper(self):
        self.assertTrue('FOO'.isupper())

if __name__ == '__main__':
   unittest.main(verbosity=1)
