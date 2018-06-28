def one ():
    message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    translated_message = ''
    for letter in message:
        letter_char = ord(letter)
        letter_char += 2
        new_letter = chr(letter_char)
        if letter is ' ':
            new_letter = letter
        translated_message += new_letter
    return translated_message