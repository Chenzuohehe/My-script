# -*- coding: utf-8 -*-
# 目标：根据提供的图生成对应的图还有名字
# https://blog.csdn.net/Richie_ll/article/details/69206210


#导入模块
from PIL import Image, ImageFilter
import os
#读取文件
im_path = r'/Users/chenzuo/Desktop/test.png'
im = Image.open(im_path)
baseP = "/Users/chenzuo/Desktop"
width, height = im.size
# 宽高
print(im.size, width, height)
# 格式，以及格式的详细描述
print(im.format, im.format_description)

# im.save(r'/Users/chenzuo/Desktop/test1.png')
# im.show()



# # 新建（全新）
# # 通常使用RGB模式就可以了
# newIm= Image.new('RGB', (100, 100), 'red')
# newIm.save(r'/Users/chenzuo/Desktop/1.png')
#
# # 也可以用RGBA模式，还有其他模式查文档吧
# blcakIm = Image.new('RGB',(200, 100), 'red')
# blcakIm.save(r'/Users/chenzuo/Desktop/2.png')
# # 十六进制颜色
# blcakIm = Image.new('RGBA',(200, 100), '#FF0000')
# blcakIm.save(r'/Users/chenzuo/Desktop/3.png')
# # 传入元组形式的RGBA值或者RGB值
# # 在RGB模式下，第四个参数失效，默认255，在RGBA模式下，也可只传入前三个值，A值默认255
# blcakIm = Image.new('RGB',(200, 100), (255, 255, 0, 120))
# blcakIm.save(r'/Users/chenzuo/Desktop/4.png')

# box = (x,y,width+x,height+y)
# 这里的参数可以这么认为：从某图的(x,y)坐标开始截，截到(width+x,height+y)坐标
# cropedIm = im.crop((700, 100, 1200, 1000))
# cropedIm.save(r'%s/corpedIm.png' %(baseP))
# im.paste(cropedIm, (0, 0))
# im.show()
# im.save(r'%s/pasteIm.png' %(baseP))

# cropedIm = im.crop((700, 100, 1200, 1000))
# crop_width, crop_height = cropedIm.size
#
# copyIm = im.copy()
# # range(0, width, crop_width) 0-width， 步幅crop_width
# for left in range(0, width, crop_width):
#     for top in range(0, height, crop_height):
#         copyIm.paste(cropedIm, (left, top))
# copyIm.save(r'%s/pdupli-rabbit.png' %(baseP))

# # 不等比例缩放 自然也能等比例缩放了？
# resizedIm = im.resize((width, height+(1920-1080)))
# resizedIm.save(r'%s/resizeIm.png' %(baseP))

# 20°，expand放大图片
im.rotate(20, expand=True).save(r'%s/resizeIm.png' %(baseP))
# im.transpose(Image.FLIP_LEFT_RIGHT).save 水平翻转
# im.transpose(Image.FLIP_TOP_BOTTOM).save 垂直翻转

# 高斯模糊
im.filter(ImageFilter.GaussianBlur).save(r'%s/GaussianBlur.png' %(baseP))
# 普通模糊
im.filter(ImageFilter.BLUR).save(r'%s/BLUR.png' %(baseP))
# 边缘增强
im.filter(ImageFilter.EDGE_ENHANCE).save(r'%s/EDGE_ENHANCE.png' %(baseP))
# 找到边缘
im.filter(ImageFilter.FIND_EDGES).save(r'%s/FIND_EDGES.png' %(baseP))
# 浮雕
im.filter(ImageFilter.EMBOSS).save(r'%s/EMBOSS.png' %(baseP))
# 轮廓
im.filter(ImageFilter.CONTOUR).save(r'%s/CONTOUR.png' %(baseP))
# 锐化
im.filter(ImageFilter.SHARPEN).save(r'%s/SHARPEN.png' %(baseP))
# 平滑
im.filter(ImageFilter.SMOOTH).save(r'%s/SMOOTH.png' %(baseP))
# 细节
im.filter(ImageFilter.DETAIL).save(r'%s/DETAIL.png' %(baseP))
















