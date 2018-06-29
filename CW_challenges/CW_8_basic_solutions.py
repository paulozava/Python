
#get an array of numbers, return the sum of all of the positives ones.
def positive_sum(numbers):
    positive_numbers = filter(lambda x: x>0, numbers)
    list_of_positive_numbers = list(positive_numbers)
    sum_of_it = sum(list_of_positive_numbers)
    return sum_of_it

#takes a boolean value and return a "Yes" string for true, or a "No" string for false.
def bool_to_word(boolean):
    if boolean: return 'Yes'
    return 'No'

#reverses the string value passed into it.
def reverse_string(string):
    letters = [letter for letter in string]
    letters.reverse()
    answer = ''.join(letters)
    return answer

#a function that removes the first and last characters of a string.
def remove_edge_letters(string):
    answer = string[1:-1]
    return answer

#remove the spaces from the string,
def no_space(x=''):
    x = x.strip()
    return x

# method so that it squares each number passed into it and then sums the results together
def square_sum(numbers):
    numbers = map(lambda x: x**2, numbers)
    return sum(numbers)

# a function that can transform a string into a number.
def string_to_number(string):
    number = int(string)
    return number
