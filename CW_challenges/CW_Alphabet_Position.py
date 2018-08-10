def alphabet_position(text):
    text = text.lower()
    positions = [str(ord(letter) - 96) for letter in text if letter.isalpha()]
    resp = ' '.join(positions)
    return resp