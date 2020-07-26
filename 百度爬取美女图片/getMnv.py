from urllib.request import *
#导入到开地址的函数
import re
url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1595340582907_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E6%9C%AC%E5%85%AE'
html = urlopen(url)

#获取网页源代码
obj = html.read().decode()

#获取所有链接
urls = re.findall(r'"objURL":"(.*?)"',obj)

index = 372
for url in urls:
    if index < 1000:
        try:
            print('正在下载第%d张'%(index))
            urlretrieve(url,str(index)+'.png')
            index+=1
        except Exception:
            print("下载失败%d张"%index)
            continue
    else:
        print("下载完成")
        break