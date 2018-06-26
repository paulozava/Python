# you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

def my_permutations_unfinished(string, k = 0, accumulator = []):
    #i have problems with return itens
    empty = ''
    sub_result = set()
    string_lenght = len(string)
    if string_lenght is 1:
        return [string]
    elif string_lenght is 2:
        return [string, string[::-1]]
    else:
        permutations_set = set(string)
        for letter in permutations_set:
            new_string = string.replace(letter, empty, 1)
            sub_permutation = permutations(new_string)
            sub_permutation_with_letter = [letter + sub for sub in sub_permutation]
            sub_result.add(sub_permutation_with_letter)
            return sub_result

def permutations2(string, k=0, result=[]):
    string_list = list(string)
    string_list_lenght = len(string_list)
    if k == string_list_lenght:
        return string_list
    else:
        for i in range(k, string_list_lenght):
            string_list[k], string_list[i] = string_list[i], string_list[k]
            result.append(permutations2(string_list, k + 1, result))
            string_list[k], string_list[i] = string_list[i], string_list[k]

def permutations3(string):
    string_list_lenght = len(string)
    if string_list_lenght == 1:
        return set(string)
    chosen_letter = string[0]
    rest_of_letters = permutations3(string[1:])
    result = set()
    for index in range(string_list_lenght):
        for letters in rest_of_letters:
            result.add(letters[0:index] + chosen_letter + letters[index:])
    return result