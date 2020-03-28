from requests import get
from user import User
from pprint import pprint
url = 'http://127.0.0.1:8000/api/employees/'
#
# data={
#     "telegram_id": 2,
#     "first_name": "asd",
#     "last_name": "asd",
#     "father_name": "asd",
#     "iin": 123,
#     "udv_number": 123,
#     "udv_place": "asd",
#     "address": "asd",
#     "bank_card": 123,
#     "iban": "qwe213",
#     "contact_phone": "1231223",
#     "email_address": "asdasdad",
#     "is_admin": False,
#     "is_hr": False
# }
#
# # user = User(data)
# # print(user.user_to_string(data))
#
# telegram_id = 260925031
#
#
# def check_user(telegram_id):
#     users = get(url).json()
#     for user in users:
#         if user['telegram_id'] == telegram_id and user['is_admin'] == True:
#             return 'admin'
#         elif user['telegram_id'] == telegram_id and user['is_hr'] == True:
#             return 'hr'
#         elif user['telegram_id'] == telegram_id:
#             return 'employee'
#
#     return 'none'

user_id = 1
def returnUserData(user_id):
    users = get(url).json()
    for user in users:
        if user['telegram_id'] == user_id:
            return user
    return None

print(returnUserData(1))