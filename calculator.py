"""Данный калькулятор будет способен высчитать не только простые логические операции, но и некоторые формулы
"""

import math


def main():
  """Функция main позволяет ввести значения с клавиатуры и запустить вычисление действия калькулятора."""
  operand1 = float(input("Введите 1 число: "))
  operand2 = float(input("Введите 2 число: "))

# Смотрим какой тип данных 
  print(type(operand1), operand1)
  print(type(operand2), operand2)

  action = input("Введите действие: ")

  result = calculate(operand1, operand2, action)
  print(f"type result = {type(result)}")
  print("Результат вычисления: ", result)


def calculate(operand1, operand2, action):
  """Вычисления результата операции над двум операндами.

  Parameters:
      operand1 - значение первого операнда
      operand2 - значение второго операнда
      action   - тип арифметической операции

  Returns:
      Результат выполнения арифметической операции
  """

  if action == '+':
    result = operand1 + operand2
  elif action == '-':
    result = operand1 - operand2
  elif action == '*':
    result = operand1 * operand2
  elif action == '/':
    if operand2 != 0:
      result = operand1 / operand2
    else:
      result = 'деление на ноль невозможно'
#Целочисленное деление      
  elif action == '//':
    if operand2 != 0:
      result = operand1 // operand2
    else:
      result = 'деление на ноль невозможно'
  elif action == '^':
    if operand2 % 1 == 0:
      result = operand1**operand2
#Возведение в вещественную степень       
    else:
      if operand2 % 1 != 0:
        result=float(pow(operand1, operand2))
#Вычисление квадратного корня        
  elif action == 'K':
    if type(operand1) is float and type(operand2) is float:
       result = math.sqrt(operand1 + operand2)
#Нахождение произведения синуса и косинуса
  elif action == 'T':
    if type(operand1) is float and type(operand2) is float:
       result = math.sin(operand1) * math.cos(operand2)
  elif action == 'gcd':
    operand1=int(operand1)
    operand2=int(operand2)
    if type(operand1) is int and type(operand2) is int:
      result = math.gcd(operand1, operand2)
      #Возврат
      return result
  else:
    result = 'операция не распознана'

  return result


if __name__ == '__main__':
  main()
