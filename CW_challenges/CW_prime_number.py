def is_prime(number):
    if number < 2 or number % 2 == 0:
        return False
    elif number == 2:
        return True
    else:
        for i in range(3, number, 2):
            if number % i == 0:
                return False
        return True