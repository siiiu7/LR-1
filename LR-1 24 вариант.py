'''
Лабораторная работа №1
Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом, читающимся поблочно), распознает,
преобразует и выводит на экран числа по определенному правилу.
Числа распознаются по законам грамматики русского языка. 
Преобразование делать по возможности через словарь.
Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа. 
Регулярные выражения использовать нельзя.

Вариант 24.
Шеснадцатиричные числа, не превышающие 1024 расположенные в порядке убывания.
Для каждой такой последовательности максимальное число вывести прописью.
'''
buffer = ''
chislo = ''
maxim = '0'
colich_1 = 0
colich_2 = 0
slovar = {0:'ноль',1:'один',2:'два',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',9:'девять',\
     'A':'десять','B':'одинадцать','C':'двенадцать','D':'тринадцать','E':'четырнадцать','F':'пятнадцать'}
with open("test.txt",'r') as f:
    buffer = f.readline(1)
    if not buffer:
        print("Файл является пустым")
        colich_2 +=1
    while buffer:
        while buffer in ['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F']:
            chislo += buffer
            buffer = f.readline(1)
        if len(chislo) > 0 and int(chislo,16) <= 1024 and int(chislo,16) > int(maxim,16):
            maxim = chislo
            colich_1+=1
            print('Максимальное из чисел:', end=' ')
            for j in range(len(maxim)):
                for l in slovar:
                    if str(l) == maxim[j]:
                        print(slovar[l], end=' ')
                        break
            print('')
        elif len(chislo) > 0 and int(chislo,16) <= 1024 and int(chislo,16) < int(maxim,16):
            maxim = chislo
        chislo = ''
        buffer = f.read(1)
if colich_1 == 0 and colich_2 == 0:
        print("Чисел не найдено", end=" ")
