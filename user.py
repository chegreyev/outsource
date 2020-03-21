from requests import post, get , delete

url = 'http://127.0.0.1:8000/api/employees/'


class User():
    telegram_id = 1
    first_name = 'ИМЯ'
    last_name = "ФАМИЛИЯ"
    father_name = "ОТЧЕСТВО"
    iin = "0005195"
    udv_number = 123123123
    udv_date = "2000-05-19"
    udv_place = "МВД РК"
    address = 'г.Атырау , ул. Владимирского д.2 кв.4'
    bank_card = 51694971
    iban = 'KZ123123'
    contact_phone = '87022465104'
    email_address = 'default@mail.ru'
    is_admin = False
    is_hr = False

    def __init__(self, data=None):
        self.data = data

    def registerEmployee(self):
        post(url, self.data)

    def deleteEmployee(self , user_id):
        delete(f'http://127.0.0.1:8000/api/employees/{user_id}/')

    def check_user(self, telegram_id):
        users = get(url).json()
        for user in users:
            if user['telegram_id'] == telegram_id and user['is_admin'] == True:
                return 'admin'
            elif user['telegram_id'] == telegram_id and user['is_hr'] == True:
                return 'hr'
            else:
                return 'none'

    def get_all(self):
        users = get(url).json()
        return users

    def user_to_string(self, user):
        text = f'Номер сотрудника: {user["telegram_id"]}\nФИО: {user["first_name"]} {user["last_name"]} {user["father_name"]}\nИИН: {user["iin"]}\nНомер удв.личности: {user["udv_number"]}\nМесто получения удв.личности: {user["udv_place"]}\nАдрес проживания: {user["address"]}\nНомер банковской карты: {user["bank_card"]}\nНомер счета карты: {user["iban"]}\nКонтактный номер: {user["contact_phone"]}\nАдрес эл.почты: {user["email_address"]}'
        return text
