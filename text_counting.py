import os

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
    homeWorktree('1.txt', '2.txt', '3.txt')