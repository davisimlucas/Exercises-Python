'''
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo
pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24
horas.
'''
hora_inicial: int; hora_final: int; duracao: int
hora_inicial = int(input('Digite a hora de início: '))
hora_final = int(input('Digite a hora final: '))
if hora_final > hora_inicial:
    duracao = hora_final - hora_inicial
    print(f'A duração do jogo foi de {duracao}h.\nHora de início: {hora_inicial}h.\nHora final: {hora_final}h do mesmo dia.')
elif hora_inicial == hora_final:
    duracao = 24
    print(f'A duração do jogo foi de {duracao}h.\nHora de início: {hora_inicial}h do dia anterior.\nHora final: {hora_final}h do dia seguinte.')
else:
    duracao = (24 - hora_inicial) + hora_final
    print(f'A duração do jogo foi de {duracao}h.\nHora de início: {hora_inicial}h do dia anterior.\nHora final: {hora_final}h do dia seguinte.')


