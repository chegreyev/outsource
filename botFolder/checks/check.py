def checkRegisteredName(text):
    text = text.split(' ')
    if len(text) < 3:
        return False
    return True


def checkRegisteredIIN(text):
    if len(text) != 12 or str.isdigit(text) is not True:
        return False
    return True


def checkRegisteredUDVdate(text):
    if '.' in text:
        text = text.split('.')
        if len(text[2]) == 4:
            if len(text[1]) == 2 and int(text[1]) <= 12 and int(text[1]) >= 1:
                if len(text[0]) == 2 and int(text[0]) >= 1 and int(text[0]) <= 31:
                    return True
    return False


def checkRegisteredBankCard(text):
    new_text = ''

    if ' ' in text:
        text = text.split(' ')

        for i in text:
            new_text += i

    if len(new_text) != 16:
        return False

    return True


def checkRegisteredIBAN(text):
    if len(text) != 20:
        return False
    return True
