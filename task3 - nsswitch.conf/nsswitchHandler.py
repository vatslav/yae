__author__ = 'django'
import re
inputFile = open('input.txt','r') #открываем файл, на чтение
outFile = open('output.txt','w')  #открываем другой файл, на запись
dns = re.compile('\sdns\s')#первая регулярка
files = re.compile('\sfiles\s')
for line in inputFile: #для каждой линии из вход.файла"""
    if line[0:6]=='hosts:' and re.search(files,line) is not None and re.search(dns,line) is not None: #проверяем, что файл нач. с хостс, что в шаблоны(см.выше) найдены)"""
        if re.search(files,line).start()<re.search(dns,line).start(): #если днс идет позже файлес"""
            line = re.sub('(?<=\s)dns(?=\s)', "", line) #заменяем днс на "" """
            N = 0
            for n in range(7,len(line[7:])): #ищем последний пробельный символ после хостс:
                if line[n].isspace():
                    N = n
                else:
                    break
            line = line[:N+1] + 'dns' + line[N:] #делаем вставку после последнего пробельного символа "днс" и дальше оставшуюся строку
    outFile.write(line) #записываем строку в выходной файл, т.е. тут такой трюк что весь вход. файл у нас в памяти не хранится: считали строку, преобразовали, записали, начинаем сначала

inputFile.close() #закрываем файлы
outFile.close()

