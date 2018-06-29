
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