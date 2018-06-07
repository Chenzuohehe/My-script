# -*- coding: utf-8 -*-
#encoding=utf-8
# 目标：根据读取excel的账号密码，登录邮箱，读取邮件标题，收件时间。询问是否打开邮箱

import xlrd
from datetime import date,datetime

import os, sys, string
import poplib



excel_patch = "/Users/chenzuo/Desktop/***.xlsx"
sheet_name = "***"



# 获取用户名密码 list
def set_users_passwords():

    start_cow = int(input("请输入从哪一行开始："))
    end_cow = int(input("请输入从哪一行结束："))

    ExcelFile = xlrd.open_workbook(excel_patch) # 获取目标EXCEL文件sheet名
    sheet = ExcelFile.sheet_by_name(sheet_name)

    users = sheet.col_values(1) #
    print ( users[start_cow:end_cow])

    passwords = sheet.col_values(3)  #
    print (passwords[start_cow:end_cow])

    return (users[start_cow:end_cow], passwords[start_cow:end_cow])


def login_email():

    # pop3服务器地址
    # host = "pop3.163.com"
    # host = "pop.yeah.net"

    # 用户名
    username = "***"
    # 密码
    password = "***"
    # 创建一个pop3对象，这个时候实际上已经连接上服务器了
    pp = poplib.POP3(host)
    # 设置调试模式，可以看到与服务器的交互信息
    pp.set_debuglevel(1)
    # 向服务器发送用户名
    pp.user(username)
    # 向服务器发送密码
    pp.pass_(password)
    # 获取服务器上信件信息，返回是一个列表，第一项是一共有多上封邮件，第二项是共有多少字节
    ret = pp.stat()
    print('Messages: %s, Size: %s' % ret)

    resp, mails, octets = pp.list()
    # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
    print(mails)

    # 获取最新一封邮件, 注意索引号从1开始:
    index = len(mails)
    resp, lines, octets = pp.retr(index)

    # lines存储了邮件的原始文本的每一行,
    # 可以获得整个邮件的原始文本:
    # msg_content = b'\r\n'.join(lines)
    # print(msg_content)
    # 稍后解析出邮件:
    # msg = Parser().parsestr(msg_content)
    # print (msg)



    # for i in range(1, ret[0] + 1):
    #     # 取出信件头部。注意：top指定的行数是以信件头为基数的，也就是说当取0行，
    #     # 其实是返回头部信息，取1行其实是返回头部信息之外再多1行。
    #     mlist = pp.top(i, 0)
    #     print ('line: ', len(mlist[1]))
    # # 列出服务器上邮件信息，这个会对每一封邮件都输出id和大小。不象stat输出的是总的统计信息
    # ret = pp.list()
    # print (ret)
    #
    # down = pp.retr(1)
    # print ('lines:', len(down))
    # # 输出邮件
    # for line in down[1]:
    #     print (line)
    # 退出
    pp.quit()


# 解析邮件与构造邮件的步骤正好相反
def print_info(msg, indent=0):
    if indent ==0:
        for header in ["From", "To", "Subject"]:
            value = msg.get(header, "")
            if value:
                if header == "Subject":
                    vaule = decode_str(value)
                else:
                    hdr, addr =parseaddr(value)
                    name = decode_str(hdr)
                    value = u"%s <%s>" % (name, addr)
            print("%s%s:%s" % ("  " * indent, header, value))
        if (msg .is_multipart()):
            parts = msg.get_payload()
            for n, part in enumerate(parts):
                print('%spart %s' % ('  ' * indent, n))
                print('%s--------------------' % ('  ' * indent))
                print_info(part, indent + 1)
        else:
            content_type = msg.get_content_type()
            if content_type=='text/plain' or content_type=='text/html':
                content = msg.get_payload(decode=True)
                charset = guess_charset(msg)
                if charset:
                    content = content.decode(charset)
                print('%sText: %s' % ('  ' * indent, content + '...'))
            else:
                print('%sAttachment: %s' % ('  ' * indent, content_type))



if __name__ == '__main__':
    login_email()
