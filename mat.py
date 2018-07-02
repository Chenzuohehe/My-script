# 制图
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
# 表格读取
import xlrd


def set_x_y_z():
	x_list = []
	y_list = []
	z_list = []

	# 读取excel
	ExcelFile = xlrd.open_workbook("/Users/chenzuo/Desktop/数据3.xlsx")
	sheet = ExcelFile.sheet_by_name("Sheet1")
	
	row_num = sheet.row_values(0)
	col_num = sheet.col_values(0)

	# 读取数据
	for i in range(2,len(row_num)):
		x = sheet.cell(0, i).value
		
		for j in range(1, len(col_num)):
			y = sheet.cell(j,1).value
			z = float(sheet.cell(j,i).value)*10000
			
			x_list.append(x)
			y_list.append(y)
			z_list.append(z)

	x_list = np.array(x_list)
	y_list = np.array(y_list)
	z_list = np.array(z_list)
	
	# 设置3D
	ax = plt.subplot(111, projection='3d')
	
	# cmap='rainbow' /  cmap=plt.cm.coolwarm 两种颜色风格
	ax.plot_trisurf(x_list, y_list, z_list, cmap=plt.cm.rainbow)

	# 设置坐标轴名称
	ax.set_zlabel('Magnetic Flux Density / 10^-4 T',fontsize=8)
	ax.set_ylabel('Y',fontsize=8)
	ax.set_xlabel('X',fontsize=8)
	plt.show()


if __name__ == '__main__':
	set_x_y_z()