def load_recipes(file_path):
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        current_dish = ''
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.isdigit():  # Количество ингредиентов пропускаем
                continue
            if '|' not in line:
                current_dish = line
                cook_book[current_dish] = []
            else:
                ingredient_name, quantity, measure = map(str.strip, line.split('|'))
                cook_book[current_dish].append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish not in cook_book:
            print(f"Блюдо '{dish}' не найдено в книге рецептов")
            continue
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }
            else:
                shop_list[ingredient_name]['quantity'] += ingredient['quantity'] * person_count
    return shop_list


if __name__ == '__main__':
    file_path = 'recipe.txt'
    cook_book = load_recipes(file_path)

    dishes = ['Запеченный картофель', 'Омлет']
    person_count = 2
    shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)

    print("Список покупок:")
    for ingredient, details in shop_list.items():
        print(f"{ingredient}: {details['quantity']} {details['measure']}")

    print("\nКнига рецептов:")
    for dish, ingredients in cook_book.items():
        print(f"{dish}:")
        for ingredient in ingredients:
            print(f"  {ingredient['ingredient_name']} - {ingredient['quantity']} {ingredient['measure']}")
