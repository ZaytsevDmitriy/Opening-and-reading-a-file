from pprint import pprint

def prepare_dict(file_name: str) -> dict:
    cook_book = {}

    with open(file_name, encoding="UTF-8") as file:
        for line in file:
            dish_name = line.strip()
            ingridient_quantity = int(file.readline())
            list = []
            for ingridient in range(ingridient_quantity):
                ingredient_name, quantity, measure = file.readline().split('|')
                list.append(
                    {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure.rstrip()}
                )
            cook_book[dish_name] = list
            file.readline()
        return cook_book
cook_book = prepare_dict('api.txt')
pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = prepare_dict('api.txt')
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list = dict()
            if ingridient['ingredient_name'] not in shop_list:
                new_shop_list['measure'] = ingridient['measure']
                new_shop_list['quantity'] = int(ingridient['quantity']) * person_count
                shop_list[ingridient['ingredient_name']] = new_shop_list
            else:
                shop_list[new_shop_list['ingridient_name']]['quantity'] += new_shop_list['quantity']
    return shop_list

shop_list1 = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(shop_list1)
