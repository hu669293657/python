import os,shutil,re

def movefile(src,dst,fname):
    try:
        if not os.path.isfile(src):
            print("{}文件不存在，操作失败！".format(src))
            input("")
        if os.path.exists(dst + "\\" + fname):

            print("{}文件已存在，操作失败!".format(dst + fname))
            input("")
        else:
            shutil.move(src, dst + "\\" + fname)
            os.system("cd " + dst + fname + " && ren *. *.jpg")
            print("移动已完成！")
            input("")
    except:
        print("操作失败！")
        input("")

def copyfile(src,dst,fname):
    try:
        if not os.path.exists(src):
            print("{}文件不存在，操作失败！".format(src))
            input("")
        if os.path.exists(dst + "\\" + fname):

            print("{}文件已存在，操作失败!".format(dst + fname))
            input("")
        else:
            shutil.copytree(src, dst + "\\" + fname)
            os.system("cd "+dst + fname + " && ren *. *.jpg")
            print("复制已完成！")
            input("")
    except:
        print("操作失败！")
        input("")

def main():

    name = input("请输入您账户的用户名：")
    hpath = "C:\\Users\\" + name + "\\appdata\\Local\\Packages\\"
    filelist = " ".join(os.listdir(hpath))
    mic = re.findall('Microsoft.Windows.ContentDeliveryManager_\w+', filelist)
    micpath = (" ".join(mic))
    src = hpath + micpath + "\\LocalState\\Assets\\"
    dst = os.getcwd() + "\\"
    # fname = src.split('\\')[-2]
    fname = "win10壁纸"
    print("1.复制")
    print("2.剪切")
    choice = int(input("请选择您的操作（输入数字即可，默认1）："))
    if choice == 1 or "":
        copyfile(src, dst,fname)
    elif choice == 2:
        movefile(src, dst,fname)
    else:
        print("请输入正确的数字！")

main()

