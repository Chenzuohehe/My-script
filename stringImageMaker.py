# -*- coding: utf-8 -*-
# 目标：根据提供的图片生成字符图（全是字符组成一个图片，我也不知道应该怎么叫）

from PIL import Image


# WIDTH = 100
# HEIGHT = 75
IMG = r'/Users/chenzuo/Desktop/icon1024.png' #原图地址
OUTPUT = "/Users/chenzuo/Desktop/icons.txt" #保存地址

#定义一个ascii的列表，其实就是让图片上的灰度与字符对应
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256): #这个调用跟im.getpixel函数有关，这个函数是根据图片的横纵坐标，把图片解析成r,g,b,alpha(灰度），有关的四个参数，所以这里输入参数是四个
    if alpha == 0: #如果灰度是0，说明这里没有图片
        return ' '
    length = len(ascii_char) #计算这些字符的长度
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b) #把图片的RGB值转换成灰度值

    unit = (257.0 )/length #257/length
    return ascii_char[int(gray/unit)] #这个相当于是选出了灰度与哪个字符对应。



if __name__ == '__main__': #如果是本程序调用，则执行以下程序

    # 读取原始图片比例

    im = Image.open(IMG) #打开图片
    # im = im.convert("l")
    WIDTH, HEIGHT = im.size

    scale = (WIDTH/100)
    WIDTH = int(WIDTH/scale)
    HEIGHT = int(HEIGHT/scale)

    # 宽高
    # print(im.size, width, height)
    # im = im.resize((WIDTH,HEIGHT), Image.NEAREST) #更改图片的显示比例

    txt = "" #txt初始值为空

    for i in range(HEIGHT): #i代表纵坐标
        for j in range(WIDTH): #j代表横坐标
            txt += get_char(*im.getpixel((j,i)))
            txt += " "#把图片按照横纵坐标解析成r,g,b以及alpha这几个参数，然后调用get_char函数，把对应的图片转换成灰度值，把对应值得字符存入txt中
        txt += '\n' #每行的结尾处，自动换行

    # print (txt) #在界面打印txt文件

    #字符画输出到文件
    with open(OUTPUT, 'w') as f:  # 文件输出
        f.write(txt)

