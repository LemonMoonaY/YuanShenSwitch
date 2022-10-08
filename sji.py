ver='2.0'

import tkinter.filedialog as fd
import tkinter as tk
import os
import subprocess
from PIL import ImageTk,Image

gamePath=''
tip=''
cfgPath1=''
cfgPath2=''
cfgPath3=''
cfgPath4=''
cfgPath5=''
lbPath=''

def getDirName():
    global gamePath,tip,lbPath
    with open('phfe.conf','w+',encoding='utf-8') as f:
        gamePath=fd.askdirectory()
        f.write(gamePath)
    tip.config(text='当前游戏文件夹位置:'+gamePath)
    lbPath.config(text='当前游戏文件夹位置:'+gamePath)

def checkPath():
    global tip,gamePath,cfgPath1,cfgPath2,cfgPath3,cfgPath4,cfgPath5,lbPath
    if gamePath=='' or gamePath==None: 
        tip.config(text='请先指定游戏文件夹目录！')
        return False
    else:
        cfgPath1=gamePath+"/config.ini"
        cfgPath2=gamePath+"/Genshin Impact Game/config.ini"
        cfgPath3=gamePath+"/Genshin Impact Game/YuanShen_Data/Plugins"
        cfgPath4=gamePath+"/Genshin Impact Game"
        cfgPath5=gamePath+"/Genshin Impact Game/GenshinImpact_Data/Plugins"
        return True

def transToB():
    global cfgPath1,cfgPath2,cfgPath3,cfgPath4,tip
    import os
    dtpath=cfgPath4
    os.chdir(dtpath)
    filelist=os.listdir(dtpath)
    print(filelist)
    old="GenshinImpact_Data"
    new="YuanShen_Data"
    if (os.path.exists('GenshinImpact_Data')):
        os.rename(old,new)
    if (os.path.exists('GenshinImpact.exe')):
        os.remove('GenshinImpact.exe')
    import shutil,os
    src=r'\原神Switching\国内服'
    des=cfgPath4
    for file in os.listdir(src):
        full_file_name=os.path.join(src,file)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name,des)
    if not checkPath():
        return
    tmp=''
    with open(cfgPath1,'r',encoding='utf-8') as f:
        tmp=f.readlines()
    with open(cfgPath1,'w+',encoding='utf-8') as f:
        for i in tmp:
            if 'cps=' in i:
                f.write('cps=bilibili\n')
            elif 'channel=' in i and 'sub' not in i:
                f.write('channel=14\n')
            elif 'sub_channel=' in i:
                f.write('sub_channel=0\n')
            else:
                f.write(i)
    with open(cfgPath2,'r',encoding='utf-8') as f:
        tmp=f.readlines()
    with open(cfgPath2,'w+',encoding='utf-8') as f:
        for i in tmp:
            if 'cps=' in i:
                f.write('cps=bilibili\n')
            elif 'channel=' in i and 'sub' not in i:
                f.write('channel=14\n')
            elif 'sub_channel=' in i:
                f.write('sub_channel=0\n')
            else:
                f.write(i)
    import shutil,os
    shutil.copy('\原神Switching\PCGameSDK.dll',cfgPath3)
    tip.config(text='已切换为b服！')
    flush()
    
def transToG():
    global cfgPath1,cfgPath2,cfgPath3,cfgPath4,tip
    import os
    dtpath=cfgPath4
    os.chdir(dtpath)
    filelist=os.listdir(dtpath)
    print(filelist)
    old="GenshinImpact_Data"
    new="YuanShen_Data"
    if (os.path.exists('GenshinImpact_Data')):
        os.rename(old,new)
    if (os.path.exists('GenshinImpact.exe')):
        os.remove('GenshinImpact.exe')
    import os,shutil
    src=r'\原神Switching\国内服'
    des=cfgPath4
    for file in os.listdir(src):
        full_file_name=os.path.join(src,file)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name,des)
    if not checkPath():
        return
    tmp=''
    with open(cfgPath1,'r',encoding='utf-8') as f:
        tmp=f.readlines()
    with open(cfgPath1,'w+',encoding='utf-8') as f:
        for i in tmp:
            if 'cps=' in i:
                f.write('cps=mihoyo\n')
            elif 'channel=' in i and 'sub' not in i:
                f.write('channel=1\n')
            elif 'sub_channel=' in i:
                f.write('sub_channel=1\n')
            else:
                f.write(i)
    with open(cfgPath2,'r',encoding='utf-8') as f:
        tmp=f.readlines()
    with open(cfgPath2,'w+',encoding='utf-8') as f:
        for i in tmp:
            if 'cps=' in i:
                f.write('cps=mihoyo\n')
            elif 'channel=' in i and 'sub' not in i:
                f.write('channel=1\n')
            elif 'sub_channel=' in i:
                f.write('sub_channel=1\n')
            else:
                f.write(i)
    tip.config(text='已切换为官服！')
    flush()
    
def transToGJ():
    global cfgPath1,cfgPath2,cfgPath3,cfgPath4,cfgPath5,tip
    import os
    dtpath=cfgPath4
    os.chdir(dtpath)
    filelist=os.listdir(dtpath)
    print(filelist)
    old="YuanShen_Data"
    new="GenshinImpact_Data"
    if (os.path.exists('YuanShen_Data')):
        os.rename(old,new)
    if (os.path.exists('YuanShen.exe')):
        os.remove('YuanShen.exe')
    if (os.path.exists('Audio_Chinese_pkg_version')):
        os.remove('Audio_Chinese_pkg_version')
    if (os.path.exists('sdk_pkg_version')):
        os.remove('sdk_pkg_version')
    if not checkPath():
        return
    tmp=''
    with open(cfgPath1,'r',encoding='utf-8') as f:
        tmp=f.readlines()
    with open(cfgPath1,'w+',encoding='utf-8') as f:
        for i in tmp:
            if 'cps=' in i:
                f.write('cps=mihoyo\n')
            elif 'channel=' in i and 'sub' not in i:
                f.write('channel=1\n')
            elif 'sub_channel=' in i:
                f.write('sub_channel=0\n')
            else:
                f.write(i)
    with open(cfgPath2,'r',encoding='utf-8') as f:
        tmp=f.readlines()
    with open(cfgPath2,'w+',encoding='utf-8') as f:
        for i in tmp:
            if 'cps=' in i:
                f.write('cps=mihoyo\n')
            elif 'channel=' in i and 'sub' not in i:
                f.write('channel=1\n')
            elif 'sub_channel=' in i:
                f.write('sub_channel=0\n')
            else:
                f.write(i)
    import os,shutil
    src=r'\原神Switching\国际服'
    des=cfgPath4
    for file in os.listdir(src):
        full_file_name=os.path.join(src,file)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name,des)
    tip.config(text='已切换为国际服！')
    flush()
    
def flush():
    global cfgPath1,cfgPath2,cfgPath3,fgPath4,fgPath5,tip
    if not checkPath():
        return
    with open(cfgPath2,'r',encoding='utf-8') as f:
        all=f.read()
        if 'cps=bilibili' in all: lbVer.config(text='b服')
        elif 'cps=mihoyo' and 'sub_channel=1' in all: lbVer.config(text='官服')
        elif 'cps=mihoyo' and 'sub_channel=0' in all: lbVer.config(text='国际服')
        else: tip.config(text='配置文件有误，未知的服务器！\n请重新下载游戏！',fg='red')

def startGame():
    global cfgPath1,cfgPath2,cfgPath3,tip,gamePath
    if not checkPath():
        return

    subprocess.Popen('"'+gamePath+'/launcher.exe'+'"',shell=True,bufsize=-1)

def get_image(filename,width,height):
    im=Image.open(filename).resize((width,height))
    return ImageTk.PhotoImage(im)

top=tk.Tk()
top.resizable(0,0)
top.title('原神切服器(三服通用)')
top.geometry('420x320')

canvas_top=tk.Canvas(top,width=420,height=320)
im_top=get_image('\原神Switching\jtp.jpg',420,320)
canvas_top.create_image(210,160,image=im_top)
canvas_top.pack()

lb1=tk.Label(top,text='Genshin Impact 路径:',wraplength=64,bg='azure')
lbPath=tk.Label(top,width=32,wraplength=220,text='请选择Genshin Impact路径\n而不是Genshin Impact Game路径',bg='azure')
bt1=tk.Button(top,text="选择文件夹",bg='azure',command=getDirName)

lb2=tk.Label(top,text='当前服务器为:',bg='azure')
lbVer=tk.Label(top,width=32,wraplength=220,bg='azure')
bt2=tk.Button(top,text="刷新",bg='azure',fg='green',width=5,command=flush)

bt3=tk.Button(top,text="切换为b服",bg='azure',fg='mediumturquoise',command=transToB)
bt4=tk.Button(top,text="切换为官服",bg='azure',fg='violet',command=transToG)
bt5=tk.Button(top,text='启动\n游戏',bg='lavender',fg='coral',width=5,height=2,command=startGame)
bt6=tk.Button(top,text="切换为国际服",bg='azure',fg='#939597',command=transToGJ)

tip=tk.Label(top,width=40,wraplength=260,bg='azure',fg='red')
tk.Label(top,text='请正确进行操作,祝你游戏愉快!',bg='azure',fg='teal').place(x=100,y=250)
tk.Label(top,text='作者b站: violet_梓玥',bg='azure',fg='orange').place(x=2,y=295)
tk.Label(top,text='Version：'+ver,bg='azure',fg='orange').place(x=335,y=295)

lb1.place(x=20,y=20)
lbPath.place(x=90,y=20)
bt1.place(x=340,y=20)

lb2.place(x=20,y=90)
lbVer.place(x=100,y=90)
bt2.place(x=340,y=90)

bt3.place(x=120,y=140)
bt4.place(x=20,y=140)
bt5.place(x=340,y=140)
bt6.place(x=220,y=140)

tip.place(x=50,y=200)

def main():
    global gamePath,tip,lbPath
    if 'ayue.conf' in os.listdir():
        with open('ayue.conf','r+',encoding='utf-8') as f:
            tmp=f.read()
            if tmp!='':
                gamePath=tmp.strip()
                tip.config(text='当前游戏文件夹位置:'+gamePath)
                lbPath.config(text='当前游戏文件夹位置:'+gamePath)
            else:
                tip.config(text='请先指定游戏文件夹目录！')
    else:
        tip.config(text='请先指定游戏文件夹目录！')

    flush()
    top.mainloop()

if __name__ == '__main__':
    main()
