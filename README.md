# Лабораторна робота 1.
![ua](https://img.shields.io/badge/lang-ua-blue.svg)

Дорогі студенти :smile_cat:

Вітаємо Вас на першій лабораторній роботі з програмування на мові Python! Ви зробили перший крок у захоплюючий світ програмування, і ми раді бути Вашими супутниками на цьому шляху.

Бажаємо Вам успіхів у виконанні лабораторної роботи і наснаги для подальшого навчання. 
Хай щастить!

**Для виконання нульового завдання та ознайомлення з гайдами з інсталяції Python, Git та рекомендаціями щодо IDE, будь ласка, перейдіть за цим [посиланням](GUID.md).**

## Завдання 1

Користувач вводить трьохзначне додатнє число з клавіатури. Потрібно порахувати:
* суму цифр цього числа
* модуль різниці цього числа та числа записаного тими ж цифрами, але у зворотньому порядку
* частку самого числа і суми його цифр (результат заокруглити до тисячних)

Результат роботи програми потрібно вивести у вигляді тексту (замість ... мають бути відповідні числа):
```
The sum of digits of the number ... is ...;
the absolute value of the difference of the number and reversed number is ...;
the fraction of the number ... and the sum of its digits is ...  
```

Наприклад з клавіатури введено число: 127.
На екран має бути виведений результат:
```
The sum of digits of the number 127 is 10;
the absolute value of the difference of the number and reversed number is 594;
the fraction of the number 127 and the sum of its digits is 12.7.
```

Достести:
```python
import doctest


def number_operations(number: int) -> str:
  
  """
  Finds the sum of digits of the number, 
  the absolute value of the difference of the number and reversed number
  and the fraction of the number and the sum of its digits
    
  :param number: int 
    
  >>> number_operations(124)
  The sum of digits of the number 124 is 7;
  the absolute value of the difference of the number and reversed number is 594;
  the fraction of the number 124 and the sum of its digits is 17.714.
  >>> number_operations(792)
  The sum of digits of the number 792 is 18;
  the absolute value of the difference of the number and reversed number is 495;
  the fraction of the number 792 and the sum of its digits is 44.0.
  >>> number_operations(55)
  Number of digits must be 3
  >>> number_operations(-124)
  Number must be positive
  >>> number_operations(100)
  The sum of digits of the number 100 is 1;
  the absolute value of the difference of the number and reversed number is 99;
  the fraction of the number 100 and the sum of its digits is 100.
  """

  # Тут має бути код, який реалізує Ваш алгоритм роботи з введеним числом


# Тут має бути код, який реалізує введення числа з клавіатури і його запису у змінну number (пам'ятайте про тип даних)

number_operations(number)

doctest.testmod()
```

## Ззадання 2

Тіло кинуте з висоти **H** під кутом **alpha** і має початкову швидкість **v<sub>0</sub>**. Програма має повертати:
* значення координат **x** і **y**
* значення швидкості **v** в момент часу **t**
* максимальну висоту та максимальну довжину польту. 

Вважати, що в момент початку польоту тіло має координати **x** = 0 і **y** = **H**. 
Користувач вводить з клавіатури: `час`, `початкову швидкість`, `кут` і `висоту, з якої було кинуто тіло`. 
Прискорення вільного падіння **g** вважати рівним 10. 
Результат виводиться на екран в вигляді тексту (замість ... мають стояти відповідні значення):

```
Coordinates of the body at the time moment ... are ... and ...;
the speed of the body at the time moment ... is ...;
the maximum height is ...;
the maximum length is ....
```

Всі результати, які виводяться на екран, мають бути заокруглені до сотих 

Доктести:
```python
import doctest


def body_moving(H: float, v0: float, alpha: float, t: float) -> str:
    """
    Finds coordinates and the speed of the body at the time moment t, the maximum height and
    the maximum length of the trajectory of the body which is thrown from the height H with the speed v0 and
    the angle alpha
       
    :param H: float
    :param v0: float
    :param alpha: float
    :param t: float
    
    >>> body_moving(34.5, 10.0, 90.0, 0.0)
    Coordinates of the body at the time moment 0.0 are 0.0 and 34.5;
    the speed of the body at the time moment 0.0 is 10.0;
    the maximum height is 39.5;
    the maximum length is 0.0.
    >>> body_moving(-50, 10.0, 90.0, 0.0)
    Height H must be positive number
    >>> body_moving(50, -10.0, 90.0, 0.0)
    Speed v0 must be positive number
    >>> body_moving(-50, -10.0, 90.0, 0.0)
    Height H and speed v0 must be positive numbers
    >>> body_moving(50, 10.0, 90.0, -1.0)
    Time moment t must be positive number
    >>> body_moving(-50, -10.0, 90.0, -1.0)
    Height H, speed v0 and time moment must be positive numbers
    >>> body_moving(-50, 10.0, 90.0, -1.0)
    Height H and time moment must be positive numbers
    >>> body_moving(50, -10.0, 90.0, -1.0)
    Speed v0 and time moment must be positive numbers

    """

    # Тут має бути код, який реалізує Ваш алгоритм роботи з введеним числом


# Тут має бути код, який реалізує введення параметрів з клавіатури і їх запису у
# відповідні змінні number (пам'ятайте про типи даних)

body_moving(H, v0, alpha, t)

doctest.testmod()
```
