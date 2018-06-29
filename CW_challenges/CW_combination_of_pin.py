# a function that returns an list of all variations for an observed PIN

def possible_combinations(observed):
    actions = {
        '1': ['1', '2', '4'],
        '2': ['1','2','3','5'],
        '3': ['2', '3', '6'],
        '4': ['1','4','5','7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9'],
        '0': ['0', '8']}

    response = ['']
    for digit in observed:
        possibilities = actions[digit]
        parcial_response = []
        for possibility in possibilities:
            new_parcial_response = [element + possibility for element in response]
            parcial_response += new_parcial_response
        response = parcial_response
    return response