import csv
import re
#
x_data = []
def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = ['Изготовитель системы','Название ОС', 'Код продукта', 'Тип системы']

    for my_file in ['info_1.txt', 'info_2.txt', 'info_3.txt']:
        data = open(my_file, 'r', encoding='cp1251')
        for line in data:
            if 'Изготовитель системы:' in line:
                line = re.sub('\n', '', line)
                os_prod_list.append(re.sub('Изготовитель системы:\s*', '', line))
            if 'Название ОС:' in line:
                line = re.sub('\n', '', line)
                os_name_list.append(re.sub('Название ОС:\s*', '', line))
            if 'Код продукта:' in line:
                line = re.sub('\n', '', line)
                os_code_list.append(re.sub('Код продукта:\s*', '', line))
            if 'Тип системы:' in line:
                line = re.sub('\n', '', line)
                os_type_list.append(re.sub('Тип системы:\s*', '', line))
        data.close()

    main_data = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    current_data = []
    x_data.append(main_data)
    i = 0
    for i in range(len(os_prod_list)): #, os_name_list, os_code_list, os_type_list]:
        current_data.append(i+1)
        current_data.append(os_prod_list[i]) #, os_name_list, os_code_list, os_type_list)
        current_data.append(os_name_list[i])
        current_data.append(os_code_list[i])
        current_data.append(os_type_list[i])
        x_data.append(current_data)
        current_data = []

def write_to_csv(file_name):
    get_data()
    with open(file_name, 'w', encoding='utf-8') as f_n:
        F_N_WRITER = csv.writer(f_n)
        F_N_WRITER.writerows(x_data)

write_to_csv('my_csv.csv')