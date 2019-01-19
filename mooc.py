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
        hurl = re.findall(r'http\:\/\/jdvodrvfb210d\.vod\.126\.net\/mooc-video\/nos\/mp4\S+', html)
        for i in range(len(hurl)):
            url = hurl[i].split('>')[0]
            ilt.append(url)
        for y in range(len(hurl)):
            url = hurl[y].split('>')[1]
            Title = url.split('<')[0]
            title.append(Title)
    except:
        print("")

def getMP4(title,ilt):
    y = 'yes'
    y = input('是否显示相关信息 yes/no(默认yes)')

    if y == 'yes' or y == '':
        try:
            tplt = "{:4}\t{:8}\t{:16}"
            print(tplt.format("序号", "课程名", "url链接"))
            for g in range(len(title)):
                if (g + 1) % 2 == 0:
                    print(tplt.format((g + 1) / 2, title[g], ilt[g]))
        except:
            print("")
    elif y!='yes' or y!='no' or y!='Yes' or y!='No' or y!='':
        print('请输入正确的参数！')
        quit()
    else:
        print('')

    root = 'C://Users//huxiaolin//Desktop//j//'

    try:
        if not os.path.exists(root):
            os.mkdir(root)
        for g in range(len(title)):
            if g % 2 != 0:
                if not os.path.exists(root + '{:.0f}'.format((g+1) / 2) + "  " + title[g] + '.mp4'):
                    a = requests.get(ilt[g])
                    with open(root + '{:.0f}'.format((g+1) / 2) + "  " + title[g] + '.mp4', 'wb') as f:
                        f.write(a.content)
                        f.close()
                        print('\r当前进度:{:.2f}%,{}文件保存成功'.format(g * 100 / len(title), title[g]), end='')
                else:
                    print('\r当前进度:{:.2f}%,{}文件已存在'.format(g * 100 / len(title), title[g]), end='')

    except:
        print('')


def main():
    start_url = 'http://www.feemic.cn/mooc/icourse163/1003248008'

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
