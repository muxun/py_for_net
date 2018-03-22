#Переписать скрипт на пайтон 
#сделать словарь со списком мо и ипишников
#аргумент скрипта monit выборг
#
#смотрим в словарь, выаскиваем ип
#если аргумаент a(англиская)
#фигачим весь скрипт

import os

medical_ip = {	0:'пингуем все',
				1:'192.168.88.107',
				2:'192.168.88.95'
	         }

#         0      1       2
argum = ['a','боксит','выборг']

answ = input('кого пингуем? \n').lower()

if answ == 'a':
	i = 1
	while(i < len(argum)):
		resp = os.system("ping " + medical_ip[i])
		if resp == 0:
			print("Пинг до " + argum[i] + " есть")
		else:
			print("Пинга до " + argum[i] + " нет")
		i += 1
elif answ in argum:
	resp = os.system('ping ' + medical_ip[argum.index(answ)])
	if resp == 0:
		print("Пинг до " + answ + " есть")
	else:
		print("Пинга до " + answ + " нет")

# алгоритм работает,нужно замасштабирвоать 
# и добивать логи  - системные и програмные чексы
