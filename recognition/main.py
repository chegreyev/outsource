import json
from pprint import pprint

import requests

stop_words = ['КАЗАКСТАН', 'КАЗАХСТАН', 'РЕСПУБЛИКА', 'РЕСПУБЛИКАСЫ', 'ЖЕКЕ' ,'ТЕП' , 'КУОЛЖ' ,'I' ,'ЭКЕСIНЩ' , 'АТЫ' , 'отчество' , '/','куш' , 'i'  , 'ТУРАН','None' ,'отчество', 'ДАТА', 'РОЖДЕНИЯ', '•' , 'иин' , 'жен', 'ЛИЧНОСТИ', 'удостоверение', 'ИМЯ']
apikey = '230ed45ece88957'


def ocr_space_file(filename, overlay=False, api_key='helloworld', language='eng'):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


def getFrontData(data):
    text = json.loads(data)['ParsedResults'][0]['ParsedText'].split('\r\n')
    print(text)

    # new_text = ''
    # for i in text:
    #     if i in stop_words:
    #         continue
    #     new_text += i
    # return new_text

    # employee_data = {
    #     'last_name' : text[3][:-1],
    #     'first_name' : text[5][:-1],
    #     'father_name' : text[9][:-1],
    #     'iin' : text[12][:-1],
    # }
    #
    # return employee_data


getFrontData(ocr_space_file('indira.jpg', api_key=apikey, language='rus'))
# print(getData(data))
