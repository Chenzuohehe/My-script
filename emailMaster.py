# -*- coding: utf-8 -*-
#encoding=utf-8
# 目标：根据读取excel的账号密码，登录邮箱，读取邮件标题，收件时间。询问是否打开邮箱

# 126密码在旁边 yehoo，gamil好像国外的有点行不通？


import xlrd
from datetime import date,datetime
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

import os, sys, string
import poplib

from openpyxl import Workbook
from openpyxl.styles import Alignment
from openpyxl.styles import Font, Color
from openpyxl.styles import colors


excel_patch = "/Users/chenzuo/Desktop/松鼠游戏苹果后台(1).xlsx"
sheet_name = "松鼠后台"

class email_model:
    user_name = ""
    pass_word = ""
    froms = []
    dates = []
    subjects = []


# 假设21行开始 xianzai xieyi xie shenme jiaoben ne youshenme chongfu xing hengaode huodong shengcheng P12wenjian

# 获取用户名密码 list
def set_users_passwords(start_cow, end_cow):

    # start_cow = int(input("请输入从哪一行开始："))
    # end_cow = int(input("请输入从哪一行结束："))

    ExcelFile = xlrd.open_workbook(excel_patch) # 获取目标EXCEL文件sheet名
    sheet = ExcelFile.sheet_by_name(sheet_name)

    users = sheet.col_values(1) #
    print ("账号list：" , users[start_cow:end_cow])

    passwords = sheet.col_values(3)  #
    print ("密码list：" , passwords[start_cow:end_cow])

    user_list = users[start_cow:end_cow]
    password_list = passwords[start_cow:end_cow]

    return user_list, password_list



def login_email(user_list, password_list):

    email_objects = []

    for i in range(0, len(user_list)):

        username = user_list[i]
        password = password_list[i]

        # host拼接
        # host = "pop.yeah.net"


        froms = []
        dates = []
        subjects = []

        # 容错
        try:
            path_index = username.find('@')
            point_path = username.find('.')
            # 去除.后面的多余东西
            host = "pop." + username[(path_index + 1):(point_path + 4)]
            print (host)

            if host == "pop.gmail.com":
                print ("我gamil被墙了")
                continue
            elif host == "pop.yahoo.com":
                print ("我yahoo登不上去")
                continue
            else:
                # 创建一个pop3对象，这个时候实际上已经连接上服务器了
                pp = poplib.POP3(host)
                # 设置调试模式，可以看到与服务器的交互信息
                pp.set_debuglevel(1)
                # 向服务器发送用户名
                pp.user(username)
                # 向服务器发送密码
                pp.pass_(password)
                # 获取服务器上信件信息，返回是一个列表，第一项是一共有多上封邮件，第二项是共有多少字节

                resp, mails, octets = pp.list()
                # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
                # 获取最新一封邮件, 注意索引号从1开始:
                index = len(mails)

                # 倒叙查看最新邮件
                for i in range(index, 0, -1):
                    resp, lines, octets = pp.retr(i)
                    msg_content = b'\r\n'.join(lines).decode('utf-8')
                    msg = Parser().parsestr(msg_content)
                    from_str, date, subject_str = print_info(msg)
                    froms.append(from_str)
                    dates.append(date)
                    subjects.append(subject_str)

                pp.quit()

        except:
            print (username, password, "---------------当前邮箱错误---------------------")

        email_object = email_model()
        email_object.user_name = username
        email_object.pass_word = password
        email_object.froms = froms
        email_object.dates = dates
        email_object.subjects = subjects
        email_objects.append(email_object)

    creat_excel(email_objects)


def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def print_info(msg, indent=0):
    from_str = ""
    date_str = ""
    subject_str = ""

    if indent == 0:
        for header in ['From', 'Subject', 'Date']:
            value = msg.get(header, '')

            if value:
                if header=='Subject':
                    value = decode_str(value)
                elif header=='Date':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            # print('%s%s: %s' % ('  ' * indent, header, value))
            if header == "From":
                from_str = value
            elif header == 'Date':
                date_str = value
            else:
                subject_str = value
    return (from_str,date_str, subject_str)

# 生成表格
def creat_excel(email_objects):

    titile_list = ["邮箱名称","密码","来自","时间","标题"]

    work_book = Workbook()
    book_sheet = work_book.active
    book_sheet.append(titile_list)

    # 邮件添加内容
    max_row = 1
    max_col = len(titile_list)

    for email_object in email_objects:
        length = len(email_object.froms)
        # 这边是错误的邮箱
        if length == 0:
            line_list = []
            line_list.append(email_object.user_name)
            line_list.append(email_object.pass_word)
            book_sheet.append(line_list)
            max_row += 1

        for i in range(0, length):
            line_list = []
            if i == 0:
                line_list.append(email_object.user_name)
                line_list.append(email_object.pass_word)
            else:
                line_list.append("")
                line_list.append("")
            line_list.append(email_object.froms[i])
            line_list.append(email_object.dates[i])
            line_list.append(email_object.subjects[i])
            book_sheet.append(line_list)
            max_row += 1

    # 设置自适应宽度
    for column_index in range(1, max_col + 1):
        maxWidth = 0
        for row_index in range(1, max_row + 1):
            value = book_sheet.cell(row=row_index, column=column_index).value
            if value:
                if isinstance(value, int):
                    value = str(value)  # 将中间int类型改变
                chineseNum = (len(value.encode('utf-8')) - len(value)) / 2
                width = len(value.encode('utf-8')) - chineseNum + 4  # +4 留下多余空间
                if width > maxWidth:
                    maxWidth = width

        codeAsc = ord(str(column_index)) + 16
        book_sheet.column_dimensions[chr(codeAsc)].width = maxWidth


    def find_key_world(key_word, col_char, color):

        for i in range(1, max_row + 1):
            path = col_char + str(i)
            sheet_obj = book_sheet[path]
            if sheet_obj.value:
                if key_word in sheet_obj.value:
                    sheet_obj.font = Font(color=color)

        # if sheet_obj.value:
        #     if key_word in sheet_obj.value:
        #         sheet_obj.font = Font(color=color)

    # 发件人名称或者邮件包含apple 一律红色字
    # for i in range(1, max_row + 1):
    #     path = "C" + str(i)
    #     sheet_obj = book_sheet[path]
    #
    #     if sheet_obj.value:
    #         if "apple" in sheet_obj.value:
    #             sheet_obj.font = Font(color=colors.RED)

    find_key_world("apple", "C", colors.RED)
    find_key_world("Notice of Termination", "E", "4169E1")

    # 当标题里面包含Notice of Termination 标色
    # yueguoshanqu ,woyaozuoyige meiyou mubiao de xianyu le ma ,kenengxianshi jiushi zheyangde ba 

    work_book.save("查看邮件" + ".xlsx")

# 删除 包含关键字的


if __name__ == '__main__':
    user_list = []
    password_list = []
    user_list, password_list = set_users_passwords(15,60)
    login_email(user_list, password_list)



