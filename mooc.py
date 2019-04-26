import getpass

import requests
import os
import re

def getHTMLText(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("")

def parsePage(ilt,title,html):
    try:
        hurl = re.findall(r'http\:\/\/jdvodrvfb210d\.vod\.126\.net\/mooc-video\/nos\/mp4.*<',html)
        for i in range(len(hurl)):
            url = hurl[i].split('>')[0]
            ilt.append(url)
            url = hurl[i].split('>')[1]
            Title = re.findall(r'\S+<',url)
            Title = "".join(Title).split('<')[0]
            title.append(Title)
    except:
        print("")

def getMP4(title,ilt):
    try:
        tplt = "{:4}\t{:8}\t{:16}"
        print(tplt.format("序号", "课程名", "url链接"))
        for g in range(len(title)):
            if (g + 1) % 2 == 0:
                print(tplt.format((g + 1) / 2, title[g], ilt[g]))
    except:
        pass
    user_name = getpass.getuser()
    root = 'C://Users//'+user_name+'//Desktop//mooc//'

    try:
        if not os.path.exists(root):
            os.mkdir(root)
        for g in range(len(title)):
            if g % 2 != 0:
                if not os.path.exists(root + '{:.0f}'.format((g+1)/2) + "  " + title[g] + '.mp4'):
                    a = requests.get(ilt[g])
                    with open(root + '{:.0f}'.format((g+1)/2) + "  " + title[g] + '.mp4', 'wb') as f:
                        f.write(a.content)
                        f.close()
                        print('\r当前进度:{:.2f}%,{}文件保存成功'.format(g * 100 / len(title), title[g]), end='')
                else:
                    print('\r当前进度:{:.2f}%,{}文件已存在'.format(g * 100 / len(title), title[g]), end='')

    except:
        print('下载失败!')


def main():
    mooc_url = input('请输入慕课网址(带有tid)')
    tid = re.findall(r'tid=\d+',mooc_url)
    tid = (" ".join(tid))
    start_url = 'http://www.feemic.cn/mooc/icourse163/'+tid[4:]

    try:
        ilt = []
        title = []
        url = start_url
        html = getHTMLText(url)
        parsePage(ilt,title,html)
        getMP4(title,ilt)
        print("\n恭喜您，所有文件已下载！")
    except:
        print('')


main()
