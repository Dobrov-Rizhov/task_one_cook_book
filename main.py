import os
# Домавашнее задание №1.txt
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
    print(shop_list)

    # Убрал избыточные копии словаря
    # new_shop_list = {}
    # for key, value in shop_list.items():
    #     new_shop_list[key] = value
    # print(new_shop_list)

# Домашняя работа №3
def homeWorktree(text1, text2, text3):
    result = []
    filename = [text1, text2, text3]
    for name in filename:
        name_text = name.split('.')[0]
        with open(name) as file:
            count = 0
            connects = file.read()
            line = connects.split('\n')
            for i in line:
                if i:
                    count += 1
                print(f'Строка номер {count} файла номер {name_text}')

    print(result)


if __name__ == '__main__':
    get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Утка по-пекински'], 4)
    homeWorktree('1.txt', '2.txt', '3.txt')
