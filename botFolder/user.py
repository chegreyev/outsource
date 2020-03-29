from requests import post, get, delete
from settings import db_url as url


class User():
    # Default data
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
        self.data = {
            'telegram_id': 1,
            'first_name': 'ИМЯ',
            'last_name': "ФАМИЛИЯ",
            'father_name': "ОТЧЕСТВО",
            'iin': "0005195",
            'udv_number': 123123123,
            'udv_date': "2000-05-19",
            'udv_place': "МВД РК",
            'address': 'г.Атырау , ул. Владимирского д.2 кв.4',
            'bank_card': 51694971,
            'iban': 'KZ123123',
            'contact_phone': '87022465104',
            'email_address': 'default@mail.ru',
            'is_admin': False,
            'is_hr': False,
        }

    def registerEmployee(self):
        '''
            Sends to database new employee data , registered from botFolder
            If the employee created , server sends HTTP_201
        '''
        self.registerEmployeeData()
        post(url, self.data)

    def deleteEmployee(self, user_id):
        '''
            Sends to database delete responce HTTP_204
        '''
        delete(f'http://127.0.0.1:8000/api/employees/{user_id}/')

    def check_user(self, telegram_id):
        '''
            Takes from database all users and checks by telegram_id
        :param telegram_id:
        :return: the role of employee ["admin" , "hr" , "employee" , "none"]
        '''

        users = get(url).json()
        for user in users:
            if user['telegram_id'] == telegram_id and user['is_admin'] == True:
                return 'admin'
            elif user['telegram_id'] == telegram_id and user['is_hr'] == True:
                return 'hr'
            elif user['telegram_id'] == telegram_id:
                return 'employee'
        return 'none'

    def get_user_full_name(self , telegram_id):
        '''
        :param telegram_id:
        :return: the employee's last_name and first_name
        '''
        employees = self.get_all()
        for employee in employees:
            if int(employee["telegram_id"]) == telegram_id:
                return f'{employee["last_name"]} {employee["first_name"]}'
        return None

    def get_all(self):
        '''
            Takes all employees from database and returns them.
        :return: all employees
        '''
        users = get(url).json()
        return users

    def get_hr(self):
        '''
            Takes all employees from database and checks for hr.
        :return: the None if hr not found , returns the hr employee from database
        '''

        employees = self.get_all()
        for employee in employees:
            if employee['is_hr'] == True:
                return employee['telegram_id']
        return None

    def get_admin(self):
        '''
            Takes all employees from database and checks for admin.
        :return: the None if hr not found , returns the admin from database
        '''
        employees = self.get_all()
        for employee in employees:
            if employee['is_admin'] == True:
                return employee['telegram_id']
        return None

    def user_to_string(self, user):
        text = f'Номер сотрудника: {user["telegram_id"]}\nФИО: {user["last_name"]} {user["first_name"]} {user["father_name"]}\nИИН: {user["iin"]}\nНомер удв.личности: {user["udv_number"]}\nМесто получения удв.личности: {user["udv_place"]}\nАдрес проживания: {user["address"]}\nНомер банковской карты: {user["bank_card"]}\nНомер счета карты: {user["iban"]}\nКонтактный номер: {user["contact_phone"]}\nАдрес эл.почты: {user["email_address"]}'
        return text

    def user_to_string_tg(self, user):
        '''
            Takes all entered by user info as the input
            transforms to string format and returns it.
        :param user:
        :return: the text with all info of the user
        '''
        text = f'Номер сотрудника: {user.telegram_id}\nФИО: {user.last_name} {user.first_name} {user.father_name}\nИИН: {user.iin}\nНомер удв.личности: {user.udv_number}\nМесто получения удв.личности: {user.udv_place}\nАдрес проживания: {user.address}\nНомер банковской карты: {user.bank_card}\nНомер счета карты: {user.iban}\nКонтактный номер: {user.contact_phone}\nАдрес эл.почты: {user.email_address}'
        return text

    def returnUserData( self , user_id):
        users = get(url).json()
        for user in users:
            if user['telegram_id'] == user_id:
                return user
        return None

    def registerEmployeeData(self):
        self.data = {
            'telegram_id': self.telegram_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'father_name': self.father_name,
            'iin': self.iin,
            'udv_number': self.udv_number,
            'udv_date': self.udv_date,
            'udv_place': self.udv_place,
            'address': self.address,
            'bank_card': self.bank_card,
            'iban': self.iban,
            'contact_phone': self.contact_phone,
            'email_address': self.email_address,
            'is_admin': False,
            'is_hr': False,
        }


class Vopros:
    # Question
    single_vopros = ''
    adminVopros = ''

    double_vopros = ''
    double_vopros_first = ''
    double_vopros_double = ''

    # Take Money
    aim = 'Цель займа денег'
    money = 'количество денег'

    def _request(self , user_id):
        user = User().returnUserData(user_id)
        text = f'Запрос на выдачу денег\nОтправитель : {user["last_name"]} {user["first_name"]}\nID юзера : {user["telegram_id"]}\nПричина вопроса: {self.aim}\nСумма : {self.money} тг'
        return text

    def singleVoprosRequest(self , user_id):
        user = User().returnUserData(user_id)
        text = f'Поступил новый вопрос\nОтправитель : {user["last_name"]} {user["first_name"]}\nID юзера : {user["telegram_id"]}\nВопрос : {self.single_vopros}'
        return text

    def doubleVoprosRequest(self , user_id):
        user = User().returnUserData(user_id)
        text = f'Поступил новый вопрос\nОтправитель : {user["last_name"]} {user["first_name"]}\nID юзера : {user["telegram_id"]}\nВопрос : {self.double_vopros}\n1){self.double_vopros_first}\n2){self.double_vopros_double}'
        return text
