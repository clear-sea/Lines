# -*- coding: utf-8 -*-  
import os  
import tkinter as tk
from tkinter import filedialog as fd
#遍历文件夹,统计文件夹中指定格式的文件数量,返回值:->字典 {文件名:行数},->整数 总行数,->整数 总文件数
def files(file_dir,ext):
    if(ext!=''):
        filenames={}
        lines=0
        all_lines=0
        name=''
        for root, dirs, files in os.walk(file_dir):  
            for file in files:  
                if os.path.splitext(file)[1] == ext:
                    name=os.path.join(root,file)
                    try:
                        with open(name,'r') as f:
                            lines=len(f.readlines())
                            filenames[name]=lines
                            all_lines+=lines
                    except UnicodeDecodeError:
                        with open(name,'r',encoding='utf-8') as f:
                            lines=len(f.readlines())
                            filenames[name]=lines
                            all_lines+=lines
        return (filenames,all_lines,len(filenames))
#主窗口初始化
root=tk.Tk()
root.geometry("800x400+50+50")
root.resizable(False,False)
root.title("查找文件个数")
#ext
entry=tk.Entry(root,bg="white")
entry.place(x=35,y=35,width=160,height=30)
#第一个文本
label2=tk.Label(root,text="结果:",font=("宋体",9))
label2.place(x=20,y=75,width=70,height=15)
#多行文本
text=tk.Text(root)
text.place(x=35,y=105,width=730,height=240)
text.config(state="disabled")
#第三个文本
label3=tk.Label(root,text="总行数:",font=("宋体",9))
label3.place(x=35,y=345)
#第四个文本
label4=tk.Label(root,text="文件总个数:",font=("宋体",9))
label4.place(x=35,y=365)
#打开文件夹统计并输出
def opendir():
    ext=entry.get()

    path=fd.askdirectory()
    if(path!=''):
        text.delete("all")
        filelist=files(path,ext)
        text.config(state="normal")
        nums=1
        for i in filelist[0]:
            text.insert(str(nums)+'.0',i+':'+str(filelist[0][i])+'行'+'\n')
            nums+=1
        text.config(state="disabled")
        label3.config(text="总行数:"+str(filelist[1]))
        label4.config(text="文件总个数:"+str(filelist[2]))
#定义按钮
btn=tk.Button(root,text="选择文件夹",font=("楷体",12),command=opendir,cursor="hand2")
btn.place(x=200,y=35,width=90,height=30)
#主循环
root.mainloop()