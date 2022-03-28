import datetime as DT

date_str = input("Введите дату выпуска (dd/mm/yyyy)\n")
vypusk = DT.datetime.strptime(date_str, '%Y/%m/%d').date()
print(vypusk)