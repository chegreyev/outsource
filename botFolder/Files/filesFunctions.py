from docxtpl import DocxTemplate, RichText
from requests import get

def changeDate(date):
    list = date.split('-')
    date = ''
    date += list[2] + '.'
    date += list[1] + '.'
    date += list[0]
    return date

def returnUserData(id):
    url = 'http://localhost:8000/api/employees/'
    users = get(url).json()
    for user in users:
        if user['telegram_id'] == int(id):
            return user
    return None

def confidemtial_dogovor(user):
    document = DocxTemplate('/Users/chegreyev/Development/outsource/botFolder/Files/Договор_о_Конфиденциальности.docx')
    last_name = RichText()
    last_name.add(user['last_name'], bold=True, font='Fira Sans Condensed ExtraLight')

    first_name = RichText()
    first_name.add(user['first_name'], bold=True, font='Fira Sans Condensed ExtraLight')

    father_name = RichText()
    father_name.add(user['father_name'], bold=True, font='Fira Sans Condensed ExtraLight')

    birth_day = RichText()
    birth_day.add(changeDate(user['birth_day']))

    udv_number = RichText()
    udv_number.add(user['udv_number'])

    udv_date = RichText()
    udv_date.add(changeDate(user['udv_date']))

    udv_place = RichText()
    udv_place.add(user['udv_place'])

    iin = RichText()
    iin.add(user['iin'])

    address = RichText()
    address.add(user['address'])

    iban = RichText()
    iban.add(user['iban'])

    contact_phone = RichText()
    contact_phone.add(user['contact_phone'])

    email_address = RichText()
    email_address.add(user['email_address'])

    context = {
        'last_name': last_name,
        'first_name': first_name,
        'father_name': father_name,
        'birth_day': birth_day,
        'udv_number': udv_number,
        'udv_date': udv_date,
        'udv_place': udv_place,
        'iin': iin,
        'address': address,
        'iban': iban,
        'contact_phone': contact_phone,
        'email_address': email_address,
        'first_name_f': user['first_name'][0],
        'father_name_f': user['father_name'][0]
    }

    document.render(context)
    document.save(f'/Users/chegreyev/Development/outsource/botFolder/Files/tempFiles/{user["last_name"]}_{user["first_name"]}_Договор_о_Конфиденциальности.docx')
    doc = open(f'/Users/chegreyev/Development/outsource/botFolder/Files/tempFiles/{user["last_name"]}_{user["first_name"]}_Договор_о_Конфиденциальности.docx' , 'rb')
    return doc

def corporate_security(user):
    document = DocxTemplate('/Users/chegreyev/Development/outsource/botFolder/Files/Соглашение_о_корпоративной_безопасности.docx')

    last_name = RichText()
    last_name.add(user['last_name'], bold=True, font='Fira Sans Condensed ExtraLight')

    first_name = RichText()
    first_name.add(user['first_name'], bold=True, font='Fira Sans Condensed ExtraLight')

    father_name = RichText()
    father_name.add(user['father_name'], bold=True, font='Fira Sans Condensed ExtraLight')

    birth_day = RichText()
    birth_day.add(changeDate(user['birth_day']))

    udv_number = RichText()
    udv_number.add(user['udv_number'])

    udv_date = RichText()
    udv_date.add(changeDate(user['udv_date']))

    udv_place = RichText()
    udv_place.add(user['udv_place'])

    iin = RichText()
    iin.add(user['iin'])

    address = RichText()
    address.add(user['address'])

    iban = RichText()
    iban.add(user['iban'])

    contact_phone = RichText()
    contact_phone.add(user['contact_phone'])

    email_address = RichText()
    email_address.add(user['email_address'])

    context = {
        'last_name': last_name,
        'first_name': first_name,
        'father_name': father_name,
        'birth_day': birth_day,
        'udv_number': udv_number,
        'udv_date': udv_date,
        'udv_place': udv_place,
        'iin': iin,
        'address': address,
        'iban': iban,
        'contact_phone': contact_phone,
        'email_address': email_address,
        'first_name_f': user['first_name'][0],
        'father_name_f': user['father_name'][0]
    }

    document.render(context)
    document.save(f'/Users/chegreyev/Development/outsource/botFolder/Files/tempFiles/{user["last_name"]}_{user["first_name"]}_Соглашение_о_корпоративной_безопасности.docx')
    doc = open(f'/Users/chegreyev/Development/outsource/botFolder/Files/tempFiles/{user["last_name"]}_{user["first_name"]}_Соглашение_о_корпоративной_безопасности.docx' , 'rb')
    return doc

def trudovoi_dogovor(user):
    document = DocxTemplate('/Users/chegreyev/Development/outsource/botFolder/Files/Трудовой_договор.docx')

    last_name = RichText()
    last_name.add(user['last_name'], bold=True, font='Fira Sans Condensed ExtraLight')

    first_name = RichText()
    first_name.add(user['first_name'], bold=True, font='Fira Sans Condensed ExtraLight')

    father_name = RichText()
    father_name.add(user['father_name'], bold=True, font='Fira Sans Condensed ExtraLight')

    birth_day = RichText()
    birth_day.add(changeDate(user['birth_day']))

    udv_number = RichText()
    udv_number.add(user['udv_number'])

    udv_date = RichText()
    udv_date.add(changeDate(user['udv_date']))

    udv_place = RichText()
    udv_place.add(user['udv_place'])

    iin = RichText()
    iin.add(user['iin'])

    address = RichText()
    address.add(user['address'])

    iban = RichText()
    iban.add(user['iban'])

    contact_phone = RichText()
    contact_phone.add(user['contact_phone'])

    email_address = RichText()
    email_address.add(user['email_address'])

    context = {
        'last_name': last_name,
        'first_name': first_name,
        'father_name': father_name,
        'birth_day': birth_day,
        'udv_number': udv_number,
        'udv_date': udv_date,
        'udv_place': udv_place,
        'iin': iin,
        'address': address,
        'iban': iban,
        'contact_phone': contact_phone,
        'email_address': email_address,
        'first_name_f': user['first_name'][0],
        'father_name_f': user['father_name'][0]
    }

    document.render(context)
    document.save(f'/Users/chegreyev/Development/outsource/botFolder/Files/tempFiles/{user["last_name"]}_{user["first_name"]}_Трудовой_договор.docx')
    doc = open(f'/Users/chegreyev/Development/outsource/botFolder/Files/tempFiles/{user["last_name"]}_{user["first_name"]}_Трудовой_договор.docx' , 'rb')
    return doc


