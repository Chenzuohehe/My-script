#coding:utf-8
import os

base_path = r''

def list_all_files(rootdir):
    
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    
    for i in range(0,len(list)):
           path = os.path.join(rootdir,list[i])
           
           if os.path.isdir(path):
              #  如果是文件夹
              num = path.rfind(']')
              if num >= 0:
                  # 如果文件夹名字包含广告 文件夹修改命名
                  new_path = path[num + 1:]
                  os.rename(path, rootdir + "/" + new_path)
                  list_all_files(rootdir + "/" + new_path)
              else:
                  list_all_files(path)

           if os.path.isfile(path):
              #  如果是文件
              num = path.rfind(']')
              if num >= 0:
                new_name = path[num + 1:]
                os.rename(path, rootdir + "/" + new_name)

list_all_files(base_path)