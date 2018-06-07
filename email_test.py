# -*- coding: utf-8 -*-
#encoding=utf-8

from email.parser import Parser
# email.parser 解析电子邮件
    # 返回这个对象的email.message.Message实例
from email.header import decode_header
from email.utils import parseaddr
import poplib




#### 解析邮件



# 邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode
def decode_str(s):
    value, charset = decode_header(s)[0]
    # decode_header()返回一个list，因为像Cc、Bcc这样的字段可能包含多个邮件地址，所以解析出来的会有多个元素。上面的代码我们偷了个懒，只取了第一个元素。
    if charset:
        value = value.decode(charset)
    return value


# 文本邮件的内容也是str，还需要检测编码，否则，非UTF-8编码的邮件都无法正常显示
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset




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


email = "omqon8@163.com"
password = "otuf89"
pop3_server = "pop3.163.com"

# 连接到POP3服务器
server = poplib.POP3_SSL(pop3_server)
# 注意qq邮箱使用SSL连接
# 打开调试信息
server.set_debuglevel(1)
# 打印POP3服务器的欢迎文字
print(server.getwelcome())

# 身份认证
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间
print("信息数量：%s 占用空间 %s" % server.stat())
# list()返回(response, ['mesg_num octets', ...], octets)，第二项是编号
resp, mails, octets = server.list()
print("list!!!!",server.list())
# 返回的列表类似[b'1 82923', b'2 2184', ...]
print(mails)

# 获取最新一封邮件，注意索引号从1开始
# POP3.retr(which) 检索序号which的真个消息，然后设置他的出现标志 返回(response, ['line', ...], octets)这个三元组
index = len(mails)
resp, lines, ocetes = server.retr(index)

# lines 存储了邮件的原始文本的每一行
# 可以获得整个邮件的原始文本
msg_content = b"\r\n".join(lines).decode("utf-8")
# 稍后解析出邮件
msg = Parser().parsestr(msg_content)
# email.Parser.parsestr(text, headersonly=False)
    # 与parser()方法类似，不同的是他接受一个字符串对象而不是一个类似文件的对象
    # 可选的headersonly表示是否在解析玩标题后停止解析，默认为否
    # 返回根消息对象

print_info(msg)

# 关闭连接
server.quit()
