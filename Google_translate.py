import execjs
import urllib
import urllib.request

file_Path = "/Users/chenzuo/Desktop/unity3d-youtube/saoce shooter STR/01-Setting up the project.srt";


class Py4Js():
    def __init__(self):
        self.ctx = execjs.compile("""
        function TL(a) {
        var k = "";
        var b = 406644;
        var b1 = 3293161072;
        var jd = ".";
        var $b = "+-a^+6";
        var Zb = "+-3^+b+-f";
        for (var e = [], f = 0, g = 0; g < a.length; g++) {
            var m = a.charCodeAt(g);
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
            e[f++] = m >> 18 | 240,
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224,
            e[f++] = m >> 6 & 63 | 128),
            e[f++] = m & 63 | 128)
        }
        a = b;
        for (f = 0; f < e.length; f++) a += e[f],
        a = RL(a, $b);
        a = RL(a, Zb);
        a ^= b1 || 0;
        0 > a && (a = (a & 2147483647) + 2147483648);
        a %= 1E6;
        return a.toString() + jd + (a ^ b)
    };
    function RL(a, b) {
        var t = "a";
        var Yb = "+";
        for (var c = 0; c < b.length - 2; c += 3) {
            var d = b.charAt(c + 2),
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
        }
        return a
    }
    """)

    def getTk(self, text):
        return self.ctx.call("TL", text)


def open_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    data = response.read().decode('utf-8')
    return data


def translate(content):
    js = Py4Js()
    tk = js.getTk(content)

    content = urllib.parse.quote(content)
    url = "http://translate.google.cn/translate_a/single?client=t" \
          "&sl=EN&tl=zh-CN&hl=EN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
          "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
          "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, content)

    result = open_url(url)
    end = result.find("\",")
    if end > 4:
        texts = result[4:end]
    return texts

# 读取srt文件
def readSrtFile():
    with open(file_Path, encoding='utf-8') as file:
        srt = file.read()
        srtList = srt.split("\n")
        

        # 一行有五个，包括空的那一行，为了防止请求过快，每10句请求一次

        enList = []
        
        for i in range(len(srtList)):
            
            
            if i % 5 == 2:
                enStr = srtList[i]
                enList.append(enStr)
                # print (enList)

            string = "";
            # print (len(enList))
            if len(enList) == 10:
                # 这边应该翻译并且替换
                # print (enList)
                for j in range(len(enList)):
                    string = "%s\n%s" %(string, enList[j])
                print (string)

                # # print(translate(str))
                # enList = []
            

        # for i in range(len(srtList)):
        #     if i%5 == 2:
        #         print(srtList[i]);
        #         print (translate(srtList[i]))
        


if __name__ == "__main__":
    readSrtFile();