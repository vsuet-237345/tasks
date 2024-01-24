def print_odd_numbers():
    number = int(input())
    if number != 0:
        if number % 2 != 0:
            print(number)
        print_odd_numbers()

print_odd_numbers()
