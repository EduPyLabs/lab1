def is_positive_triple_number(number: int) -> bool:
    # WRITE CODE HERE

def digits_sum(number: int) -> int:
    # WRITE CODE HERE

def number_difference(number: int) -> int:
    # WRITE CODE HERE

def number_ratio(number: int) -> float:
    # WRITE CODE HERE

def main():
    number = int(input("Input your 3-digits number: "))
    if is_positive_triple_number(number):
        print(digits_sum(number), number_difference(number), number_ratio(number))

    if not is_positive_triple_number(number):
        print("Input number must be positive and number of digits must be 3")

if __name__ == "__main__":
    main()
