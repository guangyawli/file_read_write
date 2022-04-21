# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json


def writefile(filename):
    # 方法一
    string1 = 'string1'
    try:
        f = open(filename, 'w', encoding='UTF-8')
        text = f.write('檔案名稱：'+filename+'\n')
        print(text)
    except FileNotFoundError:
        print('無此檔案')
    finally:
        f.close()

    # 方法二
    try:
        with open(filename, 'a', encoding='UTF-8') as f:
            text = f.write(string1)
            print(text)
    except FileNotFoundError:
        print('無此檔案')


def readfile(filename):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # 方法一
    try:
        f = open(filename, 'r', encoding='UTF-8')
        text = f.read()
        print("方法一： \n"+text+'\n')
    except FileNotFoundError:
        print('無此檔案')
    finally:
        f.close()

    # 方法二
    try:
        with open(filename, 'r', encoding='UTF-8') as f:
            text = f.read()
            print('方法二： \n'+text)
    except FileNotFoundError:
        print('無此檔案')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_name = 'input1.txt'
    writefile(file_name)
    readfile(file_name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
