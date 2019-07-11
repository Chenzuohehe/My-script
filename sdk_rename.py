# -*- coding: utf-8 -*-

# 后续加上文件内部的修改


import os
import sys

file_path = ""
old_keyword = ""
new_keyword = ""


def dir_rename(dir_path):
    for dir in os.listdir(dir_path):
        # 修改当前文件夹名称

        sub_dir_path = dir_path + "/" + dir
        # print (sub_dir_path)

        print (sub_dir_path)
        # print (new_dir)

        if os.path.isdir(sub_dir_path):
            # 对于子文件夹同样进行遍历
            dir_rename(sub_dir_path)
        # 修改名称
        # if old_keyword in dir:
        #     new_dir = dir.replace(old_keyword, new_keyword)
        #     print (dir)
        #     print (new_dir)

            # os.rename(dir_path + "/" + dir, dir_path + "/" + new_dir)



if __name__ == '__main__':
    file_path = input('请把文件夹过来过：')
    old_keyword = input('请输入旧关键字：')
    new_keyword = input('请输入新关键字：')


    # print(file_path, old_keyword, new_keyword)

    dir_rename(file_path)



