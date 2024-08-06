import doctest


def number_operations(number: int) -> None:
    """
    Finds the sum of digits of the number,
    the absolute value of the difference of the number and reversed number
    and the fraction of the number and the sum of its digits

    :param number: int
    :return  None

    >>> number_operations(124)
    The sum of digits of the number 124 is 7;
    the absolute value of the difference of the number and reversed number is 297;
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
    the fraction of the number 100 and the sum of its digits is 100.0.
    """

    if number < 100 and number >= 0:
        print("Number of digits must be 3")
    elif number < 0:
        print("Number must be positive")
    else:
        digit3 = number % 10
        digit2 = (number // 10) % 10
        digit1 = number // 100

        sum_of_digits = digit1 + digit2 + digit3
        reversed_number = digit3 * 100 + digit2 * 10 + digit1
        difference = abs(number - reversed_number)
        ratio = round(number / sum_of_digits, 3)

        print(f"The sum of digits of the number {number} is {sum_of_digits};\n" +
              f"the absolute value of the difference of the number and reversed number is {difference};\n" +
              f"the fraction of the number {number} and the sum of its digits is {ratio}.")


number = int(input("Input your 3-digits number: "))

number_operations(number)

doctest.testmod()