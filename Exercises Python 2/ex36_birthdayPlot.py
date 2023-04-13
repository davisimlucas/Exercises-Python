import time
import math
import json
from collections import Counter
from bokeh.plotting import *

output_file('plot.html')

with open('articles\ex36_fileJSON.json', 'r') as content:
    data = json.load(content)

monthsYear = {
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

months = []
for name, bithdate in data.items():
    month = int(bithdate.split('/')[0])
    months.append(monthsYear[month])
result = Counter(months)

result, counts = list(zip(*months.items()))

categories = list(monthsYear.values())
p = figure(x_range = categories, title = 'Gráfico dos meses:')
p.xaxis.major_label_orientation = math.pi/4
p.vbar(x = months, top = counts)
show(p)

