import requests

def basicIdea():
    # 爬取页面url
    r = requests.get( "http://www.baidu.com" )

    # 检测是否成功PING通：若为200 表示成功, 404表示失败
    print( r.status_code )
    # 响应页面的字符串形式
    print( r.text )
    # 从header中猜测的网页编码方式 NB: 若header中不存在charset，默认编码方式为ISO-8859-1
    print( r.encoding )
    # 从文本中响应内容的编码方式
    print( r.apparent_encoding )
    # 用于响应内容的二进制形式（还原图片等）
    print( r.content )

    # 检测出内容的真实编码方式后，可以用来替换网页header的编码再响应文字图片信息
    r.encoding = 'utf-8'
    print( r.text )

    # 检测r为一个response类
    print( type( r ) )

    # 用以下方式获取get函数得到页面的头部信息
    print( r.headers )

    # POST
    payload = {"key1": "value1", "key2": "value2"}
    r = requests.post( "http://www.baidu.com", data=payload )
    print( r.text )

#==========通用框架===============
def getHTMLText(url):
    try:
        r= requests.get(url,timeout = 30)
        r.raise_for_status()#自动判断异常类型
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常！！！"



#=======关键词搜索================
keyword = "Guan Chaofeng"
url2 = "http://www.baidu.com/s"
def getKeywordInHTML(url,keyword):
    try:
        kv = {'wd': keyword}
        r = requests.get(url,params=kv)
        print(r.request.url)
        r.raise_for_status()
        print(len(r.text))
    except:
        print("爬取失败")

#图片爬取
import os

url3 = "http://www.example.com/abc.jpg"  # "图片地址"
root = "/Users/gleonardo/PycharmProjects/绘制蟒蛇//"  # 设定图片存储位置
def getPicsHTML(url,root):
    path = root + url.split( '/' )[-1]
    try:
        if not os.path.exists( root ):
            os.mkdir( root )
        if not os.path.exists( path ):
            r = requests.get( url )
            with open( path, 'wb' ) as f:
                f.write( r.content )
                f.close()
                print( "successful" )
        else:
            print( "exist" )
    except:
        print( "failed" )


#ip地址查询全代码
ipaddress ='101.2.1.2'
def IPcheck(ipaddress):
    url = "http://m.138ip.com/ip.asp?ip="
    try:
        r=requests.get(url+ipaddress)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[-500:])
    except:
        print("failed")

