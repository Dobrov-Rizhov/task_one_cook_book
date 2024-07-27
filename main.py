cook_book = {}
with open('recipe.txt') as file:
    keys = ''
    for files in file:
        files = files.strip()
        if files.isdigit():  # isdigiit возвращает значение true если все символы цифры
            continue
        elif files and '|' not in files:
            cook_book[files] = []
            keys = files
        elif files and '|' in files:
            names, quantity, measure = files.split('|')
            cook_book.get(keys).append(dict(ingredient_name=names, quantity=int(quantity), measure=measure))


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
        print(shop_list)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(cook_book)