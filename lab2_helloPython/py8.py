year = int(input('Введите год от 1900 до 3000:'))
if (1900 < year < 3000) and ((year / 4) and (not year / 100 or year / 400)):
    print ('С днём рождения')
else:
    print('год НЕ високсный или год НЕ входит в выборку')
