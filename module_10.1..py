#                        Задача "Потоковая запись в файлы":
# Необходимо создать функцию write_words(word_count, file_name), где word_count - количество записываемых слов, file_name - название файла,
# куда будут записываться слова.
# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
# Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
# В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

##  После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
 #                                10, example5.txt
#                                 30, example6.txt
#                                 200, example7.txt
#                                 100, example8.txt
#   Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
#   Также измерьте время затраченное на выполнение функций и потоков. Как это сделать рассказано в лекции к домашнему заданию.

# Импорты необходимых модулей

import time
#from time import sleep
from threading import Thread
from datetime import datetime # Класс datetime объединяет возможности работы с датой и временем.


def write_words(word_count, file_name): # где word_count - количество записываемых слов,
                # file_name - название файла
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(1, word_count + 1):
        file.write(f'Какое-то слово № {i}\n') # записываем в файл
        time.sleep(0.1)
    file.close()
    print (f'Завершилась запись в файл {file_name}') # вывести строку "Завершилась запись в файл <название файла>".

time_start = datetime.now()    #Взятие текущего времени

#  вызовите 4 раза функцию write_words, передав в неё следующие значения:
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

print('Один поток:',datetime.now() - time_start)
time_start = datetime.now()     #Взятие текущего времени

          # Создание и запуск потоков с аргументами из задачи
t_1 = Thread(target=write_words, args=(10, 'example_10_5.txt'))
t_2 = Thread(target=write_words, args=(30, 'example_10_6.txt'))
t_3 = Thread(target=write_words, args=(200, 'example_10_7.txt'))
t_4 = Thread(target=write_words, args=(100, 'example_10_8.txt'))


t_1.start()
t_2.start()
t_3.start()
t_4.start()

t_1.join() # метод остановки
t_2.join()
t_3.join()
t_4.join()

print('Четыре потока:',datetime.now() - time_start)