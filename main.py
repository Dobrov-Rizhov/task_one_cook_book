# Домавашнее задание №1
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
print(cook_book)


# Домавашнее задание №2
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish not in cook_book:
            # Если такого блюда нет в списке то он вывидет сообщение что такого блюда нет в списке
            print(f'Блюда {dish} нет в списке')
            continue
        else:
            for ingredient in cook_book[dish]:
                ingredients = ingredient['ingredient_name']
                if ingredients not in shop_list:
                    shop_list[ingredients] = {'measure': ingredient['measure'],
                                              'quantity': ingredient['quantity'] * person_count}
                else:
                    shop_list['ingredient_name']['quantity'] += ingredient['quantity'] * person_count
    # Убрал избыточные копии словаря
    new_shop_list = {}
    for key, value in shop_list.items():
        new_shop_list[key] = value
    print(new_shop_list)

# Домашняя работа №3


if __name__ == '__main__':
    get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Утка по-пекински'], 4)
