import json
from os import path
def write_order_to_json(item, quantity, price, buyer, date):
    json_file = 'test.json'
    current_dict = {}
    enc = 'utf-8'
    if path.isfile(json_file) is True:
        with open(json_file, encoding=enc) as fp:
            current_dict = json.load(fp)
    else:
        current_dict = {'orders': []}
   # print(current_dict.get('orders'))

    current_list = []
    current_list = current_dict.get('orders')
    #print(current_list)
    current_list.append({'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date})
    #print(current_list)
    current_dict.update({'orders': current_list})
    print(current_dict)

    with open(json_file, 'w', encoding=enc) as f_n:
        f_n.write(json.dumps(current_dict, indent = 4))

item_name = input('Введите название товара: ')
quantity_count = input('Введите количество товара: ')
price_size = input('Введите стоимость товара: ')
buyer_name = input('Введите имя покупателя: ')
date_order = input('Дата заказа: ')
write_order_to_json(item_name, quantity_count, price_size, buyer_name, date_order)
