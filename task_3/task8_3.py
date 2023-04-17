import yaml

dict = {'items':['computer', 'printer', 'monitor']}
dict.update({'items_value': 5})
dict.update({'items_price': {'computer': '1000€', 'printer': '700€', 'monitor': '150€'}})

print(dict)
with open('fl.yaml', 'w', encoding='utf-8') as f_n:
    yaml.dump(dict, f_n, allow_unicode=True)
# default_flow_style
# allow_unicode = True