# ИГРА ВИСЕЛИЦА! by vladya58


import telebot
import random
from telebot import *
def new_play(message):
	k=0
	if message == "Спорт":
		f = open('Sport.txt','r', encoding='utf_8')
		lines=f.readlines()
		for i in lines:
			k+=1
		value_word = random.randint(0,k)
		k=0
		for j in lines:
			k+=1

			if k == value_word:
				word_play = j.strip()
				f.close()
				return(word_play)

	if message == "Животные":
		f = open('Animal.txt','r', encoding='utf_8')
		lines=f.readlines()
		for i in lines:
			k+=1
		value_word = random.randint(0,k)
		k=0
		for j in lines:
			k+=1

			if k == value_word:
				word_play = j.strip()
				f.close()
				return(word_play)
	if message == "Культура":
		f = open('Culture.txt','r', encoding='utf_8')
		lines=f.readlines()
		for i in lines:
			k+=1
		value_word = random.randint(0,k)
		k=0
		for j in lines:
			k+=1

			if k == value_word:
				word_play = j.strip()
				f.close()
				return(word_play)
	if message == "Природа":
		f = open('Nature.txt','r', encoding='utf_8')
		lines=f.readlines()
		for i in lines:
			k+=1
		value_word = random.randint(0,k)
		k=0
		for j in lines:
			k+=1

			if k == value_word:
				word_play = j.strip()
				f.close()
				return(word_play)


# Начало игры - выбор темы, выбор слова.

## выбор 3х букв для старта.	
def first_step(word_play,a,b,c):
	lst_a = []
	k = -1
	lst_b = [] 
	lst_c = []
	word_lst = []
	find_word = word_play
	for i in find_word:
		k+=1
		if i  == a:
			lst_a.append(k)
		elif i  == b:
			lst_b.append(k)
		elif i  == c:
			lst_c.append(k)
		else: pass
	res = lst_a + lst_b + lst_c
	res.sort()
	k=0
	for i in range(len(find_word)):
		word_lst.append("*")
	for i in res:
		word_lst [i] = find_word [i]



	return(word_lst, res)

## Проверка хода
def check_step(word_lst, word_play, litter,res):
	booll = False
	res1 = len(res)
	k = -1
	lst_w = []
	word_lst = []
	find_word = word_play
	for i in find_word:
		k+=1
		if i  == litter:
			res.append(k)
	res.sort()
	for i in range(len(find_word)):
		word_lst.append("*")
	for i in res:
		word_lst [i] = find_word [i]
		
	if len(res) != res1:

		booll = True

	return(word_lst, res,booll)

## Правильный ход
def true_step():
	print("Правильно")
	return()




## Неравильный ход
def false_step():
	print("Неправильно")
	return()

# Проверка на ошибки.
def check_errors(check,litter,use_litters):
	alphabet = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о", "п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
	check = True
	if len(litter) !=1:
		print('Проверьте правильность ввода одной буквы')
		check = False
		return check
	for j in litter:

		if j in use_litters:
			print('Буквы была введена ранее')

			check = False
			return check

	for one_char in litter:

		if one_char in alphabet:
			check = True
		else:
			print('Проверьте правильность раскладки или сторонних символов')
			check = False
	return check




final = ""
use_litters = []
chanse = 7

check = False
tema = input() # Ввод темы раунда
word_play=new_play(tema) # Запуск функции с выбором темы и слова для игры
# Ввод первых трех букв и проверка их на ошибки
#  ******************************************
while check == False:
	a = input().lower()
	check = check_errors(check, a,use_litters)
use_litters.append(a)
check = False
while check == False:
	b = input().lower()
	check = check_errors(check, b,use_litters)
use_litters.append(b)
check = False
while check == False:
	c = input().lower()
	check = check_errors(check,c,use_litters)
use_litters.append(c)

# ***************************************

word_lst,res = first_step(word_play,a,b,c) # Проверка введеных букв на наличие в слове.

print(word_lst) #  вывод угаданных букв 


while final!=word_play: # Цикл пока не угадано слово
	check = False
	while check == False:	
		litter = input().lower() # Ввод новой буквы для игры и проверка
		check = check_errors(check,litter,use_litters)
	use_litters.append(litter)
	word_lst,res,booll = check_step(word_lst, word_play, litter,res) # Проверка была ли угадана буква
	if booll == False: 
		false_step()
		chanse-=1
		print(f'Осталось {chanse} попыток')
		if chanse == 0:

			print('Попытки кончились! Вы проиграли!')
			print(f'Загаданное слово {word_play}')


	else:
		true_step()



	print(word_lst)
	final = ''.join(map(str,word_lst))
else:
	print('Вы победили!')









