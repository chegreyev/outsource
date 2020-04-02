from Files.filesFunctions import *

iin = '000519500014'

def getValidatedDate(date):
    date = date.split('.')
    validated_date = date[2] + '-' + date[1] + '-' + date[0]
    return validated_date

def getBirthFromIIN__database(iin):
    year = '20' + iin[0:2]
    month = iin[2:4]
    day = iin[4:6]
    return year + '-' + month + '-' + day

print(getBirthFromIIN__database(iin))