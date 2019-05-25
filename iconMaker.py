# -*- coding: utf-8 -*-
#encoding=utf-8
# 目标：根据提供的图生成对应像素的图还有名字

from PIL import Image

baseP = "/Users/chenzuo/Desktop/icons" #保存地址

fenshen_sizes = [20,29,40,50,57,58,60,72,76,80,87,100,114,120,144,152,167,180,1024]
chuanqi_sizes = [20,29,40,41,42,58,59,60,76,80,81,87,120,121,152,167,180,1024]
custom_sizes = [58,87,29,80,120,57,114,120,180]
mengjian_sizes = [144,72,114,57,20,29,40,50,57,58,60,76,80,87,100,120,152,167,180,1024]
canqiong_sizes = [20,40,40,60,29,29,58,58,87,40,80,120,50,100,57,114,120,180,72,144,76,152,167,1024,72,144,57,114]

def makeIcons(icon_name, type):
    im_path = '/Users/chenzuo/Desktop/%s.png' % (icon_name)
    # im_path = '/Users/chenzuo/Desktop/Icon-1024.png'  # 原图地址
    im = Image.open(im_path)

    sizes = []

    if type == 0:
        sizes = fenshen_sizes
    elif type == 1:
        sizes = chuanqi_sizes
    elif type == 2:
        sizes = mengjian_sizes
    elif type == 3:
        sizes = canqiong_sizes
    else:
        sizes = custom_sizes

    for i in range(len(sizes)):
        # 调整特别尺寸
        if sizes[i] == 41:
            resizedIm = im.resize((sizes[i] - 1, sizes[i] -1))
        elif sizes[i] == 42:
            resizedIm = im.resize((sizes[i] - 2, sizes[i] - 2))
        elif sizes[i] == 81:
            resizedIm = im.resize((sizes[i] - 1, sizes[i] - 1))
        elif sizes[i] == 121:
            resizedIm = im.resize((sizes[i] - 1, sizes[i] - 1))
        else:
            resizedIm = im.resize((sizes[i], sizes[i]))

        if type == 0:
            name = "%s/_%s.png" % (baseP, sizes[i])
            resizedIm.save(name)
            if sizes[i] == 57:
                resizedIm.save("%s/Icon.png" % (baseP))
            elif sizes[i] == 72:
                resizedIm.save("%s/Icon-72.png" % (baseP))
            elif sizes[i] == 114:
                resizedIm.save("%s/icon@2x.png" % (baseP))
            elif sizes[i] == 144:
                resizedIm.save("%s/Icon-144.png" % (baseP))
        elif type == 1:
            name = "%s/icon-%s.png" % (baseP, sizes[i])
            resizedIm.save(name)
        elif type == 2:
            name = "%s/_%s.png" % (baseP, sizes[i])
            resizedIm.save(name)
        elif type == 3:

            str = ""
            if i == 0:
                str = "-20-ipad"
            elif i == 1:
                str = "-20@2x-ipad"
            elif i == 2:
                str = "-20@2x"
            elif i == 3:
                str= "-20@3x"
            elif i == 4:
                str = "-29-ipad"
            elif i == 5:
                str = "-29"
            elif i == 6:
                str = "-29@2x-ipad"
            elif i == 7:
                str = "-29@2x"
            elif i == 8:
                str = "-29@3x"
            elif i == 9:
                str = "-40"
            elif i == 10:
                str = "-40@2x"
            elif i == 11:
                str = "-40@3x"
            elif i == 12:
                str = "-50"
            elif i == 13:
                str = "-50@2x"
            elif i == 14:
                str = "-57"
            elif i == 15:
                str = "-57@2x"
            elif i == 16:
                str = "-60@2x"
            elif i == 17:
                str = "-60@3x"
            elif i == 18:
                str = "-72"
            elif i == 19:
                str = "-72@2x"
            elif i == 20:
                str = "-76"
            elif i == 21:
                str = "-76@2x"
            elif i == 22:
                str = "-83.5@2x"
            elif i == 23:
                str = "-1024"
            elif i == 24:
                str = "-72"
            elif i == 25:
                str = "-144"
            elif i == 26:
                str = ""
            elif i == 27:
                str = "@2x"


            name = "%s/icon%s.png" %(baseP, str)
            print(name)
            resizedIm.save(name)

        else:
            name = "%s/icon-%s.png" % (baseP, sizes[i])
            resizedIm.save(name)




        # name = "%s/_%s.png" % (baseP, sizes[i])
        # name = "%s/icon-%s.png" % (baseP, sizes[i])现在需要个什么读取文件

        # print (name)
        # resizedIm.save(name)


def creat_icon(img_name, size, name_list):

    # img_name 图片名称 size 裁剪尺寸 name_list 修改后的名字规格XXX会替换成size

    # im_path = '/Users/chenzuo/Desktop/%s.png' % (img_name)
    # im = Image.open(im_path)


    # name_list = ['123','234','345']
    for name in name_list:
        #
        print(name)





if __name__ == "__main__":
    icon_name = input('输入icon名称：')
    type = input('输入icon 类型（封神：0，传奇：1，灵剑仙师：2，剑凌苍穹：3）：')
    makeIcons(icon_name, int(type))
    # makeIcons("1024", int("0"))
    # name_list = ['123', '234', '345']
    # creat_icon('123',123,name_list)

