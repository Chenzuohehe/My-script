
# 目标：读取txt 生成CP对接资料模板
import chardet
import time


def creat_txt():
    # print(path)
    # 以二进制读写模式打开
    txt_file = open("/Users/chenzuo/Desktop/1.txt",'rb+')
    lines = txt_file.readlines()
    # encoding = chardet.detect(txt_file.read())["encoding"]

    txt_lines = []
    # 找到编码格式 并使用对应格式解码
    for line in lines:
        encoding = chardet.detect(line)["encoding"]
        if encoding != None:
            print(line,encoding)
            txt_lines.append(line.decode(encoding))


        # # 找到编码格式 并使用对应格式解码
        # encoding = chardet.detect(txt)["encoding"]
        # print (txt.decode(encoding))
    print(txt_lines)
    # ttt.find("游戏名称")


def open_txt():
    txt_file = open("/Users/chenzuo/Desktop/1.txt",'rb+')
    txt = txt_file.read()
    encoding = chardet.detect(txt)["encoding"]
    decode_str = txt.decode(encoding)
    print(decode_str.splitlines())




if __name__ == "__main__":
    # txt_path = input('请拖动txt文件于冒号后：')
    # creat_txt(txt_path)

    # 开始时间
    start = time.time()

    # creat_txt()
    open_txt()

    # 结束时间
    end = time.time()
    print ("用时：",end - start)
