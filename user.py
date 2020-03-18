from requests import post , get
from pprint import pprint
from bs4 import BeautifulSoup
url = 'http://127.0.0.1:8000/api/employees/'

class User():

    def __init__(self , data = None):
        self.data = data

    def post_data(self):

        post(url , self.data)

    def check_user(self , telegram_id):
        users = get(url).json()
        for user in users :
            if user['telegram_id'] == telegram_id and user['is_admin'] == True:
                return 'admin'
            elif user['telegram_id'] == telegram_id and user['is_hr'] == True:
                return 'hr'
            else :
                return 'none'

    def get_all(self):
        users = get(url).json()
        return users

    def user_to_string(self , user):
        text = f'ФИО: {user["first_name"]} {user["last_name"]} {user["father_name"]}\nИИН: {user["iin"]}\nНомер удв.личности: {user["udv_number"]}\nМесто получения удв.личности: {user["udv_place"]}\nАдрес проживания: {user["address"]}\nНомер банковской карты: {user["bank_card"]}\nНомер счета карты: {user["iban"]}\nКонтактный номер: {user["contact_phone"]}\nАдрес эл.почты: {user["email_address"]}'
        return text
