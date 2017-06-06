# 在指定的盘符，如D盘，搜索出与用户给定后缀名(如：jpg,png)相关的文件
# 然后把搜索出来的信息(相关文件的绝对路径)，存放到用户指定的
# 文件(如果文件不存在，则建立相应的文件)中

import os
import time

# 指定盘符
DESK = 'E:\\'

# 信息保存文件的路径
##########        这里请先建立好此文件，我在做文件操作的过程中
##########        使用os.mknod('E:\\info.txt')，系统不会建立文件的
SAVE_FILE = 'E:\\info.txt'

# 文件后缀类型
FILE_EXT = ['bmp', 'jpeg', 'gif', 'psd', 'png', 'jpg', 'docx']

# 定义全局变量
my_dirs = []
my_files = []
# 文件个数
FILES_NUMBER = 0
# 符合要求的文件个数
RIGHT_FILES_NUMBER = 0
# 不符合要求的文件个数
NOT_RIGHT_FILES_NUMBER = 0
# 文件夹个数
DIR_NUMBER = 0


# 获取指定文件夹下面的所有文件及文件夹
# 如果指定的文件夹不存在，则返回相应的提示信息
def listdir(dir_path):
    if os.path.exists(dir_path):
        return os.listdir(dir_path)
    else:
        return '目录' + dir_path + '不存在'


# 搜索文件主函数
def search_files(path, name):
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False
    path = os.path.join(path, name)
    if os.path.isfile(path):  # 是文件
        global FILES_NUMBER
        FILES_NUMBER = FILES_NUMBER + 1
        lists = path.split('.')
        # print('============================================',lists)
        file_ext = lists[-1]  # 文件扩展名
        if file_ext in FILE_EXT:
            global RIGHT_FILES_NUMBER
            RIGHT_FILES_NUMBER = RIGHT_FILES_NUMBER + 1
            global my_files
            now = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            size = str(get_file_size(path))
            my_files.append(now + '    ' + path + '    ' + size + '\n')
            print('文件：', path)
        else:
            global NOT_RIGHT_FILES_NUMBER
            NOT_RIGHT_FILES_NUMBER = NOT_RIGHT_FILES_NUMBER + 1
    elif os.path.isdir(path):  # 是文件夹
        global DIR_NUMBER
        DIR_NUMBER = DIR_NUMBER + 1
        for name in listdir(path):
            # print(os.path.join(path,name))
            search_files(path, name)


# 获取文件大小
def get_file_size(path):
    if os.path.exists(path):
        return os.path.getsize(path)


# 写入信息
def write_info(content):
    if os.path.exists(path):
        with open(SAVE_FILE, 'w+') as fp:
            fp.write(content)
            fp.flush()
            fp.close()
    else:
        print('文件：{}不存在！'.format(SAVE_FILE))


# 读取所有信息
def read_info():
    if os.path.exists(path):
        with open(SAVE_FILE, 'r+') as fp:
            for line in fp:
                print(line)
    else:
        print('文件：{}不存在！'.format(SAVE_FILE))


if __name__ == '__main__':
    for d in listdir(DESK):
        my_dirs.append(os.path.join(DESK, d))
    print(my_dirs)
    # 这里是做测试用的，由于扫描整个盘符涉及到的文件和文件夹很多，可能要花一定的时间
    # 所以这里可以使用一个文件夹作为测试
    my_dir = ['E:\\6月']
    for path in my_dir:
        search_files(path, '')
    print('#' * 50)
    print(my_files)
    print('#' * 50)
    print('开始写入信息...')
    content = ''.join(my_files)
    write_info(content)
    print('#' * 50)
    print('开始读取信息...')
    read_info()
    print('#' * 50)
    print('搜索文件夹总数：{0},文件总数：{1}'.format(DIR_NUMBER, FILES_NUMBER))
    print('符合要求的文件总数：{0},不符合要求的文件总数：{1}'.format(RIGHT_FILES_NUMBER, NOT_RIGHT_FILES_NUMBER))
