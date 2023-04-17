import time

def dataExtenso():
    day = int(input('Entre com o dia: '))
    month = int(input('Enter com o mês: '))
    year = int(input('Entre com o ano: '))

    dataList = [day, month, year]
    dataFormat1 = "/".join(map(str, dataList))
    print(f'A data digitada foi {dataFormat1}')

    def monthWrite(month):
        if month == 1:
            month = str('janeiro')
        elif month == 2:
            month = str('fevereiro')
        elif month == 3:
            month = str('março')
        elif month == 4:
            month = str('abril')
        elif month == 5:
            month = str('maio')
        elif month == 6:
            month = str('junho')
        elif month == 7:
            month = str('julho')
        elif month == 8:
            month = str('agosto')
        elif month == 9:
            month = str('setembro')  
        elif month == 10:
            month = str('outubro')
        elif month == 11:
            month = str('novembro')
        elif month == 12:
            month = str('dezembro') 
        
        return month 

    time.sleep(3)

    print(f'data digitada: {day} de {monthWrite(month)} de {year}')
dataExtenso()