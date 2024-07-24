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

