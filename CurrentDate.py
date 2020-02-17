from datetime import datetime, timezone, timedelta

# BUSCA DATA E HORA ATUAL

dt_hr = datetime.now()
dt_hr_atual = dt_hr.strftime('%d/%m/%Y - %H:%M')
print(dt_hr_atual)

# CALCULA DIFERENÇA ENTRE HORÁRIOS

diferenca = timedelta(hours=-3)

#print(dif)  ->   PRINT APENAS DE TESTE

'''
PARÂMETROS QUE O TIMEDELTA ACEITA:

days (dias)
seconds (segundos)
microseconds (microsegundos)
milliseconds (milisegundos)
minutes (minutos)
hours (horas)
weeks (semanas)
'''

# BUSCA FUSO HORÁRIO

fuso = timezone(diferenca)

#print(fuso)  ->   PRINT APENAS DE TESTE

#CONVERTE O TEMPO DA MÁQUINA PARA O DE SÃO PAULO
dt_hr_SP = dt_hr.astimezone(fuso)
dt_hr_SP_txt = dt_hr_SP.strftime('Com fuso horário ativado - %d/%m/%Y - %H:%M')

print(dt_hr_SP_txt)


