#coding: utf-8

import os
import shutil
import sys
import psutil     #сторонний
import random

def duplicate_file (filename):
	if os.path.isfile(filename):
		newfile = filename + '.dupl'
		shutil.copy(filename, newfile)
		if os.path.exists(newfile):
			print('Файл', newfile, 'был успешно создан')
			return True
		else:
			print('Возникли проблемы копирования')
			return False

def duble_files(dirname):
	file_list = os.listdir(dirname)
	i = 0
	while i < len(file_list):
		duplicate_file(file_list[i])
		i += 1

def random_delete (dirname):
	file_list = os.listdir(dirname)
	if file_list:
		i = random.randrange (0, len(file_list))
		fullname = os.path.join(dirname, file_list[i])
		if os.path.isfile(fullname):
			os.remove(fullname)
			print("Файл",fullname, "был случайно удалён")



def sys_info ():
	print('Вот что я знаю о системе:')
	print('Количество процессоров:', psutil.cpu_count())
	print('Платформа:', sys.platform)
	print('Кодировка файловой системы:', sys.getfilesystemencoding())
	print('Текущая директория:', os.getcwd())
	print('Текущий пользователь:', os.getlogin())

def del_duplicats(dirname):
	file_list = os.listdir(dirname)
	doubl_count = 0

	for f in file_list:
		fullname = os.path.join(dirname, f)
		if fullname.endswith('.dupl'):
			os.remove(fullname)
			if not os.path.exists (fullname):
				doubl_count +=1
				print('Файл', fullname, 'был успешно удалён')
	return doubl_count
# comment

def main():
	print('Great Python Program!')
	print('Привет, программист!')
	name = input('Ваше имя:')

	print(name, ', добро пожаловать в мир Python!')

	answer = ''
	# PEP-8
	while answer != 'Q':
		answer = input('Давайте поработаем? (Y/N/Q)')
		if answer == 'Y':
			print('Отлично, хозяин!')
			print('Я умею:')
			print('[1] - выведу список файлов')
			print('[2] - выведу информацию о системе')
			print('[3] - выведу список процессов')
			print('[4] - продублирую файлы в текущей директории')
			print('[5] - продублирую указанный вами файл')
			print('[6] - удалю дубликаты файлов')
			print('[7] - удалю случайный файл')
			do = int(input('Укажите номер действия: '))

			if do == 1:
				print(os.listdir())

			elif do == 2:
				sys_info()

			elif do == 3:
				print(psutil.pids())

			elif do == 4:
				print('=Дублирование файлов в текущей директории=')
				duble_files('.')

			elif do == 5:
				print('=Дублирование указанного файла=')
				filename = input('Укажите имя файла:')
				duplicate_file(filename)

			elif do == 6:
				print('=Удаление дубликатов в директории=')
				dirname = input('Укажите имя директории:')
				count = del_duplicats(dirname)
				print('--Удалено файлов: ', count)

			elif do == 7:
				print('=Удаление случайного файла=')
				dirname = input('Укажите имя директории:')
				random_delete(dirname)



			else:
				pass
		# type, dir, help
		elif answer == 'N':
			print('До свидания!')
		else:
			print('Неизвестный ответ')


if __name__ == "__main__":
	main( )