import time

def dataExtenso():
    day = int(input('Entre com o dia: '))
    month = int(input('Enter com o mês: '))
    year = int(input('Entre com o ano: '))

    dataList = [day, month, year]
    dataFormat1 = "/".join(map(str, dataList))
    print(f'A data digitada foi {dataFormat1}')

    def monthWrite(month):
        monthName = {
            1: 'janeiro',
            2: 'fevereiro',
            3: 'março',
            4: 'abril',
            5: 'maio',
            6: 'junho',
            7: 'julho',
            8: 'agosto',
            9: 'setembro',
            10: 'outubro',
            11: 'novembro',
            12: 'dezembro'
        }
        
        return monthName.get(month) 

    time.sleep(3)

    print(f'data digitada: {day} de {monthWrite(month)} de {year}')
dataExtenso()