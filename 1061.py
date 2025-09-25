começo_dia = int(input('insira o dia do inicio do evento: '))
hora_inicio, minuto_inicio, segundo_inicio = map(int, input('insira a hora que começou o evento: ').split(':'))

final_dia = int(input('insira o dia final do evento: '))
hora_final, minuto_final, segundo_final = map(int, input('insira a hora final do evento: ').split(':'))

tempo_inicio_segundos = (começo_dia * 24 * 60 * 60) + (hora_inicio * 60 * 60) + (minuto_inicio * 60) + segundo_inicio
tempo_final_segundos = (final_dia * 24 * 60 * 60) + (hora_final * 60 * 60) + (minuto_final * 60) + segundo_final
duracao_segundos = tempo_final_segundos - tempo_inicio_segundos

dias = duracao_segundos // (24 * 60 * 60)  
duracao_segundos %= (24 * 60 * 60)        
horas = duracao_segundos // (60 * 60)     
duracao_segundos %= (60 * 60)             
minutos = duracao_segundos // 60          
segundos = duracao_segundos % 60          

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')