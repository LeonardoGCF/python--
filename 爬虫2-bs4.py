import requests
from bs4 import BeautifulSoup

url = "http://www.baidu.com"
r = requests.get(url)
r.encoding = r.apparent_encoding

demo = r.text()
soup = BeautifulSoup(demo , 'html.paser')
soup2 = BeautifulSoup(open("D://demo.html"),'html.paser')

#===========
print(soup.title)

tag = soup.a

name = soup.a.name

parent_name = soup.a.parent.name

grand_parent_name = soup.a.parent.parent.name

attributes = soup.a.attrs

String = soup.a.string

content = soup.a.contents

HowManychildren = len(soup.a.contents)

PickFirstOne = soup.a.contents[1]

soup.prettify()#使标签分行显示

for child in soup.a.children:
    print(child)

for descentant in soup.a.descendants:
    print(descentant)

for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

#信息提取
#找tag为a,属性为attributes的所有内容
for link in soup.find_all('a',id='attributes'):
    print(link.get('href'))

for link in soup.find_all(['a','b']):
    print(link.get('href'))

#找所有以b开头的tag,包含link的属性
import re
for tag in soup.find_all(re.compile('b'),id = re.compile("link")):
    print(tag.name)