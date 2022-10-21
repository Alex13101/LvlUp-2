# f = open('Dictionares.py', encoding="utf8")
#
# my_lst = f.readlines()
# print(my_lst)
# f.close()

#with open('Dictionares.py', encoding="utf8") as f:  #Открытие файла
                                                    # и работа сним в режиме чтения
    # s=[]
    # for line in f:
    #     s+= line
    # print(s)
    # my_lst = f.readlines()
    # print(my_lst)
""" Моды работы - чтениеб запись и т.д"""

#with open('Dictionares.py', encoding="utf8", mode="a" ) as f: #Запись в файл
                                                 # в зависимости от мода
    #f.write("Мой текс\n")


#import json  # тип файла ?????? для хранения и формирования данных
# with open (json_data.json) as json_file:
#     data = json.load(json_file)
#     print(data)
 import pickle  #Используется для хранения сложных питоновских объектов



