#!/bin/python3
#KhanhNguyen9872
#This is main windows!

if (__name__ != '__main__'):
    print('This is a main script!')
    exit()

# Import thư viện
try:
    import math
    import os
    import threading
    import time
    import subprocess
    import base64
    import time
    import sys
    import tkinter
    import urllib
    import urllib.request
    import codecs
    import platform
    import struct
    import webbrowser
    import hashlib
    from random import *
    from tkinter import *
    from tkinter import filedialog
    from urllib.request import urlretrieve
    from threading import Thread
    from pathlib import Path
    from os.path import exists
    from tkinter import messagebox
except:
    print('Error when try import library')
    if (os.name != 'nt'):
        print('try to install [sudo apt-get install python3-tk]')
    exit()

# Nhóm (class)
####UNDERLINE

# Gán giá trị
BUF_SIZE = 65536        # Buffer size for Download
flag=0                  # Download
python00=[]             # Array for check python version
total=int(30)           # Maximum Menu
temp=[]                 # Temp array
language=str("")        # Language
amd64_or_32 = 0         # Default is 0 (64bit)

### Required file
checkicon = Path('khanh.ico')
if (os.name == 'nt'):
    english = Path('language\en-US.khanh')
    vietnamese = Path('language\vi-VN.khanh')
    settings_showcode = Path('settings\showcode.ini')
    mainpyexe_name = 'python_exercises_khanhnguyen9872.exe'
    mainpyexe = Path(f"{mainpyexe_name}")
    khanhlocal = os.getenv('LOCALAPPDATA')
    khanhlocal1 = os.getenv('PROGRAMFILES')
    WINDOWS_DIRECTORY = os.getenv('WINDIR')
    khanhlocal2 = os.getenv('PROGRAMFILES(X86)')
    cmd_exe = Path(f'{WINDOWS_DIRECTORY}\system32\cmd.exe')
else:
    #################
    mainpyexe_name = 'khanh.ico'
    mainpyexe = Path(f"{mainpyexe_name}")
    WINDOWS_DIRECTORY = '/bin'
    cmd_exe0 = str(subprocess.check_output("which bash 2> /dev/null", shell=True).rstrip().decode("utf-8"))
    cmd_exe = Path(f"{cmd_exe0}")
    english = Path('language/en-US.khanh')
    vietnamese = Path('language/vi-VN.khanh')
    settings_showcode = Path('./settings/showcode.ini')
    all_term=["qterminal","gnome-terminal","lxterminal","xfce4-terminal","terminator","xterm","konsole","rxvt"]
    for term in all_term:
        if (term == "xterm"):
            try:
                checkterm = str(subprocess.check_output(f"{term} -help 2> /dev/null", shell=True).rstrip().decode("utf-8"))
            except:
                checkterm = ""
        else:
            try:
                checkterm = str(subprocess.check_output(f"{term} --version 2> /dev/null", shell=True).rstrip().decode("utf-8"))
            except:
                checkterm = ""
        if (checkterm == ""):
            terminal = ""
            continue
        else:
            terminal=str(f"{term}")
            break
    if (terminal == ""):
        print("cannot detect terminal")
        exit()

# Hàm dành cho hệ thống
def clear():
    if (os.name == 'nt'):
        cmd('cls')
    else:
        cmd('clear')

def mkdir(folder):
    if (os.name == 'nt'):
        cmd(f"mkdir {folder} 2> NUL")
    else:
        folder.replace("\\", "/")
        cmd(f"mkdir {folder} 2> /dev/null")

def rmdir(folder):
    if (os.name == 'nt'):
        cmd(f"rmdir /q /s {folder} 2> NUL")
    else:
        folder.replace("\\", "/")
        cmd(f"rm -rf {folder} 2> /dev/null")

def rm(file):
    if (os.name == 'nt'):
        cmd(f"del /f {file} 2> NUL")
    else:
        file.replace("\\", "/")
        cmd(f"rm -f {file} 2> /dev/null")

def killall(process):
    if (os.name == 'nt'):
        cmd(f"taskkill /f /im {process} 2> NUL")
    else:
        cmd(f"killall {process} 2> /dev/null")

def pause():
    if (os.name == 'nt'):
        cmd(f"pause > NUL")
    else:
        cmd(f"read -p '' pause")

def touch(file):
    if (os.name == 'nt'):
        cmd(f"echo khanhnguyen9872 > {file} 2> NUL")
    else:
        file.replace("\\", "/")
        cmd(f"touch {file} 2> /dev/null")

def cmd(args):
    subprocess.call(f"{args}", shell=True)

def close_process():
    killall('python_exercises_khanhnguyen9872.exe')
    killall('python.exe')
    rmdir('khanh')
    exit()

def popup(main,geometry,error):
    mainerror = tkinter.Tk()
    mainerror.title(f"{main} | {pyver} (KhanhNguyen9872)")
    if (os.name == 'nt'):
        mainerror.iconbitmap('khanh.ico')
    mainerror.geometry(f"{geometry}")
    mainerror.resizable(False, False)
    texterror = Text(mainerror)
    texterror.insert(INSERT, f"{error}")
    texterror.pack()
    mainerror.mainloop()

def showcodeisnull():
    maincodenull = tkinter.Tk()
    maincodenull.title(f'No ShowCode Application | Python (KhanhNguyen9872)')
    if (os.name == 'nt'):
        maincodenull.iconbitmap('khanh.ico')
    maincodenull.geometry("400x60")
    maincodenull.resizable(False, False)
    Label(maincodenull, text="Show code as Application is not found!", font=('BOLD')).grid(row=0, sticky=W)
    Label(maincodenull, text="You can go to Settings to change it!", font=('BOLD')).grid(row=1, sticky=W)
    maincodenull.mainloop()

def menu_option(menunum,main_name,text_name,name,example,copyright,copyr_number,geometry,total,name2,example2):
    exec(f"""{main_name} = tkinter.Tk()""")
    exec(f"""{main_name}.title(f'Bài {menunum} | {pyver} (KhanhNguyen9872)')""")
    if (os.name == 'nt'):
        exec(f"""{main_name}.iconbitmap('khanh.ico')""")
    exec(f"""{main_name}.geometry('{geometry}')""")
    exec(f"""{main_name}.resizable(False, False)""")
    exec(f"""{text_name} = Text({main_name})""")
    exec(f"""Label({main_name}, text="{name}", font=('BOLD')).grid(row=0, sticky=W)""")
    if (str(copyright)!="0"):
        exec(f"""Label({main_name}, text="   --Source: {copyright}--").grid(row=1, sticky=W)""")
    else:
        exec(f"""Label({main_name}, text="{example}").grid(row=1, sticky=W)""")
    exec(f"""SHOW = Button({main_name}, text="Show Code", command=lambda: showcode(int({menunum}),0)).grid(row=2, column=0, sticky=W)""")
    exec(f"""SHOWAPP = Button({main_name}, text="Show Code as Application", command=lambda: showcode(int({menunum}),1)).grid(row=3, column=0, sticky=W)""")
    exec(f"""Label({main_name}, text="").grid(row=2, column=1, sticky=W)""")
    exec(f"""RUN_ON_TERMINAL = Button({main_name}, text="Run as Terminal", command=lambda: showcode(int({menunum}),9)).grid(row=2, column=2, sticky=W)""")
    if (str(copyright)!="0"):
        exec(f"""SOURCEBY = Button({main_name}, text="{copyright}", command=lambda: sourcecre(int({copyr_number}))).grid(row=3, column=2, sticky=W)""")
    exec(f"""Label({main_name}, text="").grid(row=4, sticky=W)""")
    if (int(total)==2):
        exec(f"""Label({main_name}, text="{name2}", font=('BOLD')).grid(row=5, sticky=W)""")
        exec(f"""Label({main_name}, text="{example2}").grid(row=6, sticky=W)""")
        exec(f"""SHOW = Button({main_name}, text="Show Code", command=lambda: showcode(str({menunum}),0)).grid(row=7, column=0, sticky=W)""")
        exec(f"""SHOWAPP = Button({main_name}, text="Show Code as Application", command=lambda: showcode(str({menunum}),1)).grid(row=8, column=0, sticky=W)""")
        exec(f"""Label({main_name}, text="").grid(row=7, column=1, sticky=W)""")
        exec(f"""RUN_ON_TERMINAL = Button({main_name}, text="Run as Terminal", command=lambda: showcode(str({menunum}),9)).grid(row=7, column=2, sticky=W)""")
        exec(f"""Label({main_name}, text="").grid(row=9, sticky=W)""")

def showcode_py(menunumber,main_name,text_name,geometry,pycode):
    exec(f"""{main_name} = tkinter.Tk()""")
    exec(f"""{main_name}.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')""")
    if (os.name == 'nt'):
        exec(f"""{main_name}.iconbitmap('khanh.ico')""")
    exec(f"""{main_name}.geometry("{geometry}")""")
    exec(f"""{main_name}.resizable(False, False)""")
    exec(f"""{text_name} = Text({main_name})""")
    exec(f"""{text_name}.insert(INSERT, {pycode})""")
    exec(f"""{text_name}.pack()""")
    exec(f"""{text_name}.config(state=DISABLED)""")
    #{text_name}.tag_add("start", "1.0", "99.0")
    #{text_name}.tag_config("start", background = "gray", foreground = "white")
    exec(f"""{main_name}.mainloop()""")

def showcode_withapp(showcodemain_read,main_name,pycode):
    if (showcodemain_read!=""):
        if (os.name == 'nt'):
            exec(f"""{main_name} = codecs.open(f".\khanh\{pycode}.py", "w", 'utf-8')""")
            exec(f"""{main_name}.write({pycode})""")
            exec(f"""{main_name}.close()""")
            cmd(f'''"{showcodemain_read}" .\khanh\{pycode}.py''')
        else:
            exec(f"""{main_name} = codecs.open(f"./khanh/{pycode}.py", "w", 'utf-8')""")
            exec(f"""{main_name}.write({pycode})""")
            exec(f"""{main_name}.close()""")
            python_fpath = str(subprocess.check_output(f"readlink -f ./khanh/{pycode}.py", shell=True).rstrip().decode("utf-8"))
            os.system(f"{terminal} -e '{showcodemain_read} {python_fpath}' 2> /dev/null &> /dev/null &")
    else:
        showcodeisnull()

def run_terminal(menunumber,pyver,main_name,pycode):
    exec(f"global {pycode}")
    if (os.name == 'nt'):
        temp=f"""@echo off
TITLE Bai {menunumber} - {pyver} (KhanhNguyen9872)
color 17
cls
python khanh\{pycode}.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        """
        exec(f"""{main_name} = codecs.open(f".\khanh\{pycode}.py", "w", 'utf-8')""")
        exec(f"""{main_name}.write({pycode})""")
        exec(f"""{main_name}_bat = codecs.open(f".\khanh\{pycode}.bat", "w", 'utf-8')""")
        exec(f"""{main_name}_bat.write(temp)""")
        cmd(f"start cmd /c khanh\{pycode}.bat")
    else:
        python_fpath = str(subprocess.check_output(f"readlink -f ./khanh/{pycode}.py", shell=True).rstrip().decode("utf-8"))
        temp=f"""#!/bin/bash
clear
python3 {python_fpath}
read
read
read
read
exit 0      
        """
        exec(f"""{main_name} = codecs.open(f"./khanh/{pycode}.py", "w", 'utf-8')""")
        exec(f"""{main_name}.write({pycode})""")
        exec(f"""{main_name}_bat = codecs.open(f"./khanh/{pycode}.sh", "w", 'utf-8')""")
        exec(f"""{main_name}_bat.write(temp)""")
        os.system(f"""{terminal} -e 'bash ./khanh/{pycode}.sh' 2> /dev/null &> /dev/null &""")

# Check
if (cmd_exe.is_file()):
    del cmd_exe
else:
    mainicon = tkinter.Tk()
    mainicon.title(f'Terminal is not found! | Python (KhanhNguyen9872)')
    mainicon.geometry("350x40")
    mainicon.resizable(False, False)
    Label(mainicon, text="Program can't start without Terminal", font=('BOLD')).grid(row=0, sticky=W)
    mainicon.mainloop()
    time.sleep(0)
    exit()

if mainpyexe.is_file():
    del mainpyexe
else:
    mainicon = tkinter.Tk()
    mainicon.title(f'Missing File | Python (KhanhNguyen9872)')
    mainicon.geometry("350x80")
    mainicon.resizable(False, False)
    Label(mainicon, text=f"Missing required file!\nFile: {mainpyexe_name}", font=('BOLD')).grid(row=0, sticky=W)
    CONFIRM1 = Button(mainicon, text="  Close program  ", command=close_process).grid(row=1, column=0, sticky=W)
    mainicon.mainloop()

if (checkicon.is_file()):
    khanhicon_orig = "b1e53fda77164aea77abbde0813834734173b05119d0559077501eb73115a9ee"
    file_hash = hashlib.sha256()
    with open(checkicon, 'rb') as f:
        fb = f.read(BUF_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BUF_SIZE)
    khanhicon = str(file_hash.hexdigest())
    if (khanhicon!=khanhicon_orig):
        mainicon = tkinter.Tk()
        mainicon.title(f'File ERROR | Python (KhanhNguyen9872)')
        mainicon.geometry("500x60")
        mainicon.resizable(False, False)
        Label(mainicon, text="FILE ERROR! There's something wrong! Try again later!", font=('BOLD')).grid(row=0, sticky=W)
        CONFIRM1 = Button(mainicon, text="  Close program  ", command=close_process).grid(row=1, column=0, sticky=W)
        mainicon.mainloop()
        time.sleep(0)
        exit()
    else:
        del checkicon
        del khanhicon_orig
        del khanhicon
        del file_hash
else:
    mainicon = tkinter.Tk()
    mainicon.title(f'Missing File | Python (KhanhNguyen9872)')
    mainicon.geometry("350x80")
    mainicon.resizable(False, False)
    Label(mainicon, text="Missing required file!\nFile: khanh.ico", font=('BOLD')).grid(row=0, sticky=W)
    CONFIRM1 = Button(mainicon, text="  Close program  ", command=close_process).grid(row=1, column=0, sticky=W)
    mainicon.mainloop()
    time.sleep(0)
    exit()

if (settings_showcode.is_file()):
    with open(f"{settings_showcode}",'r',encoding='utf-8') as file_name00:
        temp_decode = str(file_name00.read())
        try:
            temp_decode = str(temp_decode[::-1])
            temp_decode = base64.a85decode(temp_decode).decode('utf-8')
            temp_decode = str(temp_decode[::-1])
            binary_int = int(temp_decode, 2)
            byte_number = binary_int.bit_length() + 7 // 8
            binary_array = binary_int.to_bytes(byte_number, "big")
            temp_decode = binary_array.decode()
        except:
            file_name00.close()
            rm('settings\\showcode.ini')
            mainshowcodeini = tkinter.Tk()
            mainshowcodeini.title(f'Settings ERROR | Python (KhanhNguyen9872)')
            if (os.name == 'nt'):
                mainshowcodeini.iconbitmap('khanh.ico')
            mainshowcodeini.geometry("500x60")
            mainshowcodeini.resizable(False, False)
            Label(mainshowcodeini, text="SETTING ERROR! showcode.ini will be recreated!", font=('BOLD')).grid(row=0, sticky=W)
            CONFIRM1 = Button(mainshowcodeini, text="  Close program  ", command=close_process).grid(row=1, column=0, sticky=W)
            mainshowcodeini.mainloop()
            time.sleep(0)
            exit()
        string_decode = base64.b64decode(str(temp_decode)).decode("utf-8")
        showcodemain_read=str(string_decode)
    showcode_app=str("")
    len_showcodesettings = "-" + str(len(showcodemain_read)+1)
    for s in range(-1,int(len_showcodesettings),-1):
        if (showcodemain_read[int(s)]) == str(f"/") or (showcodemain_read[int(s)]) == str(f"\\"):
            file_name00.close()
            break
        else:
            showcode_app = showcode_app + showcodemain_read[s]
    showcode_app = ''.join(reversed(showcode_app))
    del temp_decode
    del binary_array
    del binary_int
    del byte_number
    del string_decode
else:
    mkdir('settings')
    if (os.name == 'nt'):
        showcode_app_select = str(f"{WINDOWS_DIRECTORY}\\notepad.exe")
    else:
        showcode_app_select = str(f"{WINDOWS_DIRECTORY}/nano")
    showcode_app = str("")
    len_showcodesettings = "-" + str(len(showcode_app_select)+1)
    for s in range(-1,int(len_showcodesettings),-1):
        if (showcode_app_select[int(s)]) == str(f"/") or (showcode_app_select[int(s)]) == str(f"\\"):
            if (os.name == 'nt'):
                showcodemain = codecs.open(f".\settings\showcode.ini", "w", 'utf-8')
            else:
                showcodemain = codecs.open(f"./settings/showcode.ini", "w", 'utf-8')
            string_encode = base64.b64encode(showcode_app_select.encode('utf-8',errors = 'strict')).decode("utf-8") 
            binary_showcodeapp = ''.join(format(i, '08b') for i in bytearray(string_encode, encoding ='utf-8'))
            binary_showcodeapp = str(binary_showcodeapp[::-1])
            binary_showcodeapp = base64.a85encode(binary_showcodeapp.encode('utf-8')).decode('utf-8')
            binary_showcodeapp = str(binary_showcodeapp[::-1])
            showcodemain.write(str(binary_showcodeapp))
            showcodemain.close()
            break
        else:
            showcode_app = showcode_app + showcode_app_select[s]
    with open(f"{settings_showcode}",'r',encoding='utf-8') as file_name00:
        temp_decode = str(file_name00.read())
        try:
            temp_decode = str(temp_decode[::-1])
            temp_decode = base64.a85decode(temp_decode).decode('utf-8')
            temp_decode = str(temp_decode[::-1])
            binary_int = int(temp_decode, 2)
            byte_number = binary_int.bit_length() + 7 // 8
            binary_array = binary_int.to_bytes(byte_number, "big")
            temp_decode = binary_array.decode()
            string_decode = base64.b64decode(temp_decode).decode("utf-8")
            showcodemain_read=str(string_decode)
        except:
            file_name00.close()
            rm('settings\\showcode.ini')
            mainshowcodeini = tkinter.Tk()
            mainshowcodeini.title(f'Settings ERROR | Python (KhanhNguyen9872)')
            if (os.name == 'nt'):
                mainshowcodeini.iconbitmap('khanh.ico')
            mainshowcodeini.geometry("500x60")
            mainshowcodeini.resizable(False, False)
            Label(mainshowcodeini, text="SETTING ERROR! showcode.ini will be recreated!", font=('BOLD')).grid(row=0, sticky=W)
            CONFIRM1 = Button(mainshowcodeini, text="  Close program  ", command=close_process).grid(row=1, column=0, sticky=W)
            mainshowcodeini.mainloop()
            time.sleep(0)
            exit()
    showcode_app = str(''.join(reversed(showcode_app)))
    del temp_decode
    del binary_showcodeapp
    del len_showcodesettings
    del binary_array
    del binary_int
    del byte_number
    del string_encode
    del string_decode
    del showcode_app_select

if (os.name == 'nt'):
    name_showcode_app = str(showcode_app[-1] + showcode_app [-2] + showcode_app [-3] + showcode_app [-4])
    name_showcode_app = str(''.join(reversed(name_showcode_app)))
    if (name_showcode_app!=".exe"):
        mkdir('settings')
        if (os.name == 'nt'):
            showcode_app_select = str(f"{WINDOWS_DIRECTORY}\\notepad.exe")
        else:
            showcode_app_select = str(f"{WINDOWS_DIRECTORY}/nano")
        showcode_app = str("")
        len_showcodesettings = "-" + str(len(showcode_app_select)+1)
        for s in range(-1,int(len_showcodesettings),-1):
            if (showcode_app_select[int(s)]) == str(f"/") or (showcode_app_select[int(s)]) == str(f"\\"):
                if (os.name == 'nt'):
                    showcodemain = codecs.open(f".\settings\showcode.ini", "w", 'utf-8')
                else:
                    showcodemain = codecs.open(f"./settings/showcode.ini", "w", 'utf-8')
                string_encode = base64.b64encode(showcode_app_select.encode('utf-8',errors = 'strict')).decode("utf-8")
                binary_showcodeapp = ''.join(format(i, '08b') for i in bytearray(string_encode, encoding ='utf-8'))
                binary_showcodeapp = str(binary_showcodeapp[::-1])
                binary_showcodeapp = base64.a85encode(binary_showcodeapp.encode('utf-8')).decode('utf-8')
                binary_showcodeapp = str(binary_showcodeapp[::-1])
                showcodemain.write(str(binary_showcodeapp))
                showcodemain.close()
                break
            else:
                showcode_app = showcode_app + showcode_app_select[s]
        with open(f"{settings_showcode}",'r',encoding='utf-8') as file_name00:
            temp_decode = str(file_name00.read())
            try:
                temp_decode = str(temp_decode[::-1])
                temp_decode = base64.a85decode(temp_decode).decode('utf-8')
                temp_decode = str(temp_decode[::-1])
                binary_int = int(temp_decode, 2)
                byte_number = binary_int.bit_length() + 7 // 8
                binary_array = binary_int.to_bytes(byte_number, "big")
                temp_decode = binary_array.decode()
                string_decode = base64.b64decode(temp_decode).decode("utf-8")
                showcodemain_read=str(string_decode)
            except:
                file_name00.close()
                rm('settings\\showcode.ini')
                mainshowcodeini = tkinter.Tk()
                mainshowcodeini.title(f'Settings ERROR | Python (KhanhNguyen9872)')
                if (os.name == 'nt'):
                    mainshowcodeini.iconbitmap('khanh.ico')
                mainshowcodeini.geometry("500x60")
                mainshowcodeini.resizable(False, False)
                Label(mainshowcodeini, text="SETTING ERROR! showcode.ini will be recreated!", font=('BOLD')).grid(row=0, sticky=W)
                CONFIRM1 = Button(mainshowcodeini, text="  Close program  ", command=close_process).grid(row=1, column=0, sticky=W)
                mainshowcodeini.mainloop()
                time.sleep(0)
                exit()
        showcode_app = str(''.join(reversed(showcode_app)))
        del temp_decode
        del binary_showcodeapp
        del len_showcodesettings
        del binary_array
        del binary_int
        del byte_number
        del string_encode
        del string_decode
        del showcode_app_select
    else:
        del name_showcode_app

if (vietnamese.is_file()) and (english.is_file()):
    rmdir('language'); mkdir('language') 
    touch('language\\vi-VN.khanh')
    language=str("Vietnamese")
    del vietnamese
    del english
elif (vietnamese.is_file()) or (english.is_file()):
    if (vietnamese.is_file()):
        language=str("Vietnamese")
    elif (english.is_file()):
        language=str("English")
    del vietnamese
    del english
else:
    rmdir('language'); mkdir('language') 
    touch('language\\vi-VN.khanh')
    language=str("Vietnamese")
    del vietnamese
    del english

## Main windows
main = tkinter.Tk()
main.title(f'Python  (KhanhNguyen9872)')
if (os.name == 'nt'):
    main.iconbitmap("khanh.ico")
main.geometry("460x280")
main.resizable(False, False)

code1='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Giải phương trình bậc 2

import math
 
def giaiPTBac2(a, b, c):
    # kiểm tra các hệ số
    if (a == 0):
        if (b == 0):
            print ("Phương trình vô nghiệm!")
        else:
            print ("Phương trình có một nghiệm: x = ", + (-c / b))
        return
 
    # tính delta
    delta = b * b - 4 * a * c

    # tính nghiệm
    if (delta > 0):
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a))
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a))
        print ("Phương trình có 2 nghiệm là: x1 = ", x1, " và x2 = ", x2)
    elif (delta == 0):
        x1 = (-b / (2 * a))
        print("Phương trình có nghiệm kép: x1 = x2 = ", x1)
    else:
        print("Phương trình vô nghiệm!")
 
# Nhập các hệ số
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

# Gọi hàm giải phương trình bậc 2
giaiPTBac2(a, b, c)
'''

code2='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Tìm ra số lớn nhất

# Nhập số lần (n)
n = int(input("Nhập n:"))

# Tạo 1 list và 1 biến chứa số tối đa
list = []
max = 0

# Cho vòng lặp từ 1 tới số lần n
for i in range(1, n + 1):
    ## Nhập các số muốn so sánh lớn nhất
    a = int(input(f"Nhập số lần {i}: "))

    ## Thêm các số vừa nhập (biến a) vào list
    list.append(a)

# Cho vòng lặp các số đã được thêm vào list
for j in list:
    ## Nếu j lớn hơn max, thì sẽ thay max=j
    if (j > max):
        max = j
    else:
        continue

# In ra màn hình kết quả
print(f"Số lớn nhất: {max}")
'''

code2_min='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Tìm ra số bé nhất

# Nhập số lần (n)
n = int(input("Nhập n: "))

# Tạo 1 list
list = []

# Cho vòng lặp từ 1 tới số lần n
for i in range(1, n + 1):
    ## Nhập các số muốn so sánh bé nhất
    a = int(input(f"Nhập số lần {i}: "))
    
    ## Thêm các số vừa nhập (biến a) vào list
    list.append(a)

# Gán số đầu tiên có trong list
min = list[0]

# Cho vòng lặp các số đã được thêm vào list
for j in list:
    ## Nếu j bằng min thì bỏ qua
    if (j == min):
        continue

    ## Nếu j bé hơn min, thay min=j
    elif (j < min):
        min = j
    else:
        continue

# In ra màn hình số bé nhất
print(f"Số bé nhất: {min}")
'''

code3='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Sắp xếp từ bé đến lớn

n = int(input("Nhập n: "))

answer = []

for i in range(1, n + 1):
    a = str(input(f"Nhập lần {i}: "))
    answer.append(a)

answer.sort()
print("Từ bé đến lớn: " + str(', '.join(answer)))
'''

code3_min='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Sắp xếp từ lớn đến bé

n = int(input("Nhập n: "))

answer = []

for i in range(1, n + 1):
    a=str(input(f"Nhập lần {i}: "))
    answer.append(a)

answer.sort(reverse = True)

print("Từ lớn đến bé: " + str(', '.join(answer)))
'''

code4='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Đếm số lần xuất hiện của 1 chuỗi

a = []
answer = []
board = int(0)
number = str(input("Nhập chuỗi: "))

for i in range(0, len(number), 1):
    if number[i] in a:
        continue
    temp = 1
    dem = int(0)
    for j in range(0, len(number), 1):
        if (number[i] == number[j]):
            dem += 1
    answer.append(str(number[i]) + ":" + str(dem))
    a.append(number[i])

answer.sort()
print("\\nKết quả: ")

while (board != 3):
    for a in range(board, len(answer), 3):
        print(answer[a], end="\\t")
    board += 1
    print(end="\\n")
'''

code5='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Mã hóa 1 chuỗi string bằng base64

import base64

string = str(input("Nhập chuỗi: "))

string_encode = base64.b64encode(string.encode('utf-8',errors = 'strict')).decode("utf-8") 

print('\\nString đã được mã hóa:\\n' + str(string_encode))
'''

code5_min='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Giải mã 1 chuỗi string bị mã hóa do base64

import base64

string = str(input("Nhập chuỗi string bị mã hóa: "))

string_decode = base64.b64decode(string).decode("utf-8")

print('\\nString đã được giải mã:\\n' + str(string_decode))
'''

code6='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Chuyển tiền USD -> VND

USD = input("Nhập số tiền USD: ")

VND = int(USD)*22645

print(f"Số tiền VND:", VND, "VND")
'''

code6_min='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Chuyển tiền VND -> USD

VND = input("Nhập số tiền VND: ")

USD = float(int(VND) / 22645)

if (USD % 22645 == 0):
    USD = int(USD)
else:
    USD = float("{:.3f}".format(USD))

print(f"Số tiền USD:", USD, "USD")
'''

code7='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Tìm số giai thừa

n = int(input("Nhập số n: "))
giai_thua = 1

if (n == 0) or (n == 1):
    giai_thua = 1
else:
    for a in range(2, n + 1):
        giai_thua = giai_thua * int(a)

print("Giai thừa của " + str(n) + " là", giai_thua)
'''

code8='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Tìm ƯCLN và BCNN

def UCLN(a, b):
    if (b == 0):
        return a
    return UCLN(b, a % b)

def BCNN(a, b):
    return int((a * b) / UCLN(a, b))
 
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

print("ƯCLN của", a, "và", b, "là:", UCLN(a, b))
print("BCNN của", a, "và", b, "là:", BCNN(a, b))
'''

code9='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Kiểm tra số nguyên tố

def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print(f"Số {n} là số nguyên tố")
        return
    print(f"Số {n} không phải là số nguyên tố")
    return

n = int(input("Nhập n: "))

is_prime(n)
'''

code10='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Tạo hình tam giác trong Terminal

def tamgiac(n):
    z = n-1
    x = 1
    for i in range(0, n):
        for i in range(0, z):
            print('', end = '')
        for i in range(0,x):
            print('+', end = '')
        for i in range(0, z):
            print('', end = '')
        x = x * 2
        x = x - 1
        z = z - 1
        print()

size = int(input("Nhập kích thước: "))

tamgiac(size)
'''

code11='''
# Source: Lã Thành Trung
# Tạo pháo hoa bằng Turtle

# import module
import turtle
from random import randint, choice

# set up screen
width = 700
height = 500
S = turtle.Screen()
S.setup(width,height)
S.bgcolor('black')
S.title("Fireworks")

# colors
colors = ['red','green','yellow','gold','pink','cyan','white','orange',
         'violet','coral']

class Fireworks:
    def __init__(self,radius):
        self.T = turtle.Pen()
        self.T.speed(0)
        self.T.color(choice(colors))
        self.T.hideturtle()
        self.T.up()
        self.T.setposition(randint(-250,250),randint(0,200))
        self.T.down()
        self.radius = radius

    def update(self):
        self.T.forward(self.radius)
        self.T.backward(self.radius)
        self.T.left(10)

    def clean(self):
        self.T.clear()
        self.T.color(choice(colors))
        self.T.up()
        self.T.setposition(randint(-250,250),randint(0,200))
        self.T.down()        

# Objects
T1 = Fireworks(randint(10,100))
T2 = Fireworks(randint(10,100))
T3 = Fireworks(randint(10,100))
T4 = Fireworks(randint(10,100))
T5 = Fireworks(randint(10,100))
    
##
T = turtle.Pen()
T.sety(-150)
T.color('gold')
T.write('Happy New Year!',align='center',font=(None,20))
T.hideturtle()

while True:
        
    for i in range(36):
        T1.update()
        T2.update()
        T3.update()
        T4.update()        
        T5.update()
        
    T1.clean()
    T2.clean()
    T3.clean()
    T4.clean()   
    T5.clean()

turtle.mainloop()
'''

code12='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Tìm ra chữ có 3 kí tự trở lên trong String

temp = []
answer = []

temp = input("Nhập string: ").split()

for a in temp:
    if (len(a) > 3):
        answer.append(a)

print(f"Kết quả:",answer)
'''
code13='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Tính tổng các ước số của N (ngoại trừ N)

temp = []
answer = int(0)

n = int(input("Nhập số n: "))

for i in range(1, n):
    if (n % i == 0):
        temp.append(i)

for j in temp:
    answer += j

print(f"Kết quả:",answer)
'''

code14='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Tính lũy thừa a^b bằng hàm pow()

def luythua(a,b):
    if (b<0):
        answer = float(pow(a,b))
    else:
        answer = int(pow(a,b))
    return answer
    
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

print(f"Kết quả:",luythua(a,b))
'''

code15='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Kiểm tra là tam giác vuông, đều, cân, tù hay nhọn

def kiemtra(a,b,c):
    if (a*a == b*b + c*c) or (b*b == a*a + c*c) or (c*c == a*a + b*b):
        answer = str("Tam giác vuông")
    elif (a==b) and (b==c):
        answer = str("Tam giác đều")
    elif (a==b) or (b==c) or (c==a):
        answer = str("Tam giác cân")
    elif (a*a > b*b + c*c) or (b*b > a*a + c*c) or (c*c > a*a + b*b):
        answer = str("Tam giác tù")
    else:
        answer = str("Tam giác nhọn")    
    return answer
    
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

print(f"Kết quả:",kiemtra(a,b,c))
'''

code16='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Tìm ra các số chẵn, lẻ (Có lượt bỏ kí tự không phải số)
import re

def kiemtra(user_input):
    list = re.split(',| ', user_input)
    for a in list:
        try:
            if (a in sochan):
                continue
            elif (a in sole):
                continue
            if (int(a) % 2 == 0):
                sochan.append(a)
            else:
                sole.append(a)
        except:
            continue

    print(str(f"Số chẵn: {', '.join(sochan)}"))
    print(str(f"Số lẻ: {', '.join(sole)}"))
    return
    
user_input = str(input("Nhập dãy số (cách nhau bằng ','): "))
sochan = []
sole = []

kiemtra(user_input)
'''

code17='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Đếm kí tự In hoa, thường (Không bao gồm số)

def inhoa_inthuong():
    numup = int(0)
    numlow = int(0)
    for count in string_input:
        if count.isupper():
            numup += 1
        if count.islower():
            numlow += 1
    print("In hoa:", numup)
    print("In thường:", numlow)

string_input = str(input("Nhập chuỗi string: "))
inhoa_inthuong()

'''

# Hàm chương trình
def showcode(menunumber,app):
    if (isinstance(menunumber, int)):
       fcode=f"code{menunumber}"
    else:
        fcode=f"code{menunumber}_min"
    if (app==9):
        #run_terminal(menunumber,pyver,main_name,pycode)
        run_terminal(f"{menunumber}",f"{pyver}",f"filecode{menunumber}",f"{fcode}")
    elif (app!=1):
        #showcode_py(menunumber,main_name,text_name,geometry,pycode)
        showcode_py(f"{menunumber}",f"mainshow{menunumber}",f"text{menunumber}","600x380",f"{fcode}")
    else:
        #showcode_withapp(showcodemain_read,main_name,pycode)
        showcode_withapp(f"{showcodemain_read}",f"mainshow{menunumber}a",f"{fcode}")

def sourcecre(user):
    if (user==1):
        if (os.name == 'nt'):
            webbrowser.open('https://fb.me/trung12a4')
        else:
            webbrowser.open('https://fb.me/trung12a4')
    elif (user==2):
        pass

def dl_progress(count, blksize, filesize):
    global flag
    if flag:
        raise Exception('download canceled')

# Python Official Website
def pythonofficial(winver,winbit,win_or_linux):
    maininstall = tkinter.Tk()
    maininstall.title(f'Install Python | Python (KhanhNguyen9872)')
    if (os.name == 'nt'):
        maininstall.iconbitmap('khanh.ico')
        maininstall.geometry("520x180")
        maininstall.resizable(False, False)
        textinstall = Text(maininstall)
        textinstall.insert(INSERT, "Detecting Windows...\n")
        if (winbit=="AMD64"):
            python_ver="-amd64"
            winbit="64"
        elif (winbit=="ARM64"):
            python_ver="-arm64"
            winbit="64"
        else:
            python_ver=""
            winbit="32"
        if (winver=="7"):
            file_name = "python_version.txt"
            url = "https://raw.githubusercontent.com/KhanhNguyen9872/python_exercises/main/python_version_win7.txt"
            urllib.request.urlretrieve(url, file_name)
            with open(f"{file_name}",'r',encoding='utf-8') as file_name0:
                pyver000=str(file_name0.read().rstrip())
            pyver001=""
            textinstall.insert(INSERT, f"Found: Windows {winver} ({winbit}bit)\n\n")
            textinstall.insert(INSERT, f"Getting version....\n")
            textinstall.insert(INSERT, f"Found: {pyver000}\n")
        else:
            if (python_ver=="-arm64"):
                file_name = "python_version.txt"
                file_name2 = "python_version_beta.txt"
                url = "https://raw.githubusercontent.com/KhanhNguyen9872/python_exercises/main/python_version_arm64.txt"
                url2 = "https://raw.githubusercontent.com/KhanhNguyen9872/python_exercises/main/python_version_arm64_beta.txt"
                urllib.request.urlretrieve(url, file_name)
                urllib.request.urlretrieve(url2, file_name2)
                with open(f"{file_name}",'r',encoding='utf-8') as file_name0:
                    pyver000=str(file_name0.read().rstrip())
                with open(f"{file_name2}",'r',encoding='utf-8') as file_name00:
                    pyver001=str(file_name00.read().rstrip())
                textinstall.insert(INSERT, f"Found: Windows {winver} {winbit}bit\n\n")
                textinstall.insert(INSERT, f"Getting version....\n")
                textinstall.insert(INSERT, f"Found: {pyver000}\n")
            else:
                file_name = "python_version.txt"
                url = "https://raw.githubusercontent.com/KhanhNguyen9872/python_exercises/main/python_version.txt"
                urllib.request.urlretrieve(url, file_name)
                with open(f"{file_name}",'r',encoding='utf-8') as file_name0:
                    pyver000=str(file_name0.read().rstrip())
                pyver001=""
                textinstall.insert(INSERT, f"Found: Windows {winver} {winbit}bit\n\n")
                textinstall.insert(INSERT, f"Getting version....\n")
                textinstall.insert(INSERT, f"Found: {pyver000}{pyver001}\n")
            
        textinstall.insert(INSERT, f"\nDownloading Python v{pyver000}{pyver001}....\n")
        textinstall.insert(INSERT, f"Installing Python v{pyver000}{pyver001}....\n")
        textinstall.insert(INSERT, f"When the installation is completed! You can close this window!\n")
        textinstall.pack()
        url_python = str(f"https://www.python.org/ftp/python/{pyver000}/python-{pyver000}{pyver001}{python_ver}.exe")
        print(url_python)
        file_name_python = "khanh.exe"
        #urllib.request.urlretrieve(url_python, file_name_python)
        slient_py00 = f"""#!/bin/python3
import urllib
import urllib.request
import os
os.system('cls')
print('Downloading Python v{pyver000}{pyver001}')
urllib.request.urlretrieve("{url_python}", "{file_name_python}")
os.system('move khanh.exe khanh\\khanh.exe')
        """
        pythoninstall01 = codecs.open(f".\khanh\khanh.py", "w", 'utf-8')
        pythoninstall01.write(slient_py00)
        pythoninstall01.close()
        os.system("start python khanh\khanh.py")
        while not os.path.exists("khanh\\khanh.exe"):
            time.sleep(1)
        slient_cmd00 = f"""@echo off
TITLE Install Python v{pyver000} - KhanhNguyen9872
color 17
mode con:cols=100 lines=16
cls
echo.
echo Python v{pyver000} is installing....
echo Do not close this windows!
echo This window will close when the process is finished!
echo.
echo Your PC may reboot on its own after the installation is completed!
echo.
khanh\khanh.exe /quiet InstallAllUsers=1 PrependPath=1
taskkill /f /im python_exercises_khanhnguyen9872.exe > NUL
taskkill /f /im python_exercises_khanhnguyen9872.exe > NUL
taskkill /f /im python.exe > NUL
        """
        pythoninstall00 = codecs.open(f".\khanh\khanh.bat", "w", 'utf-8')
        pythoninstall00.write(slient_cmd00)
        pythoninstall00.close()
        os.system("start cmd /c khanh\khanh.bat")
        time.sleep(2)
        file_name0.close()
        rm(f'{file_name}')
        maininstall.mainloop()
        time.sleep(0)
        exit()
    else:
        temp=f"""#!/bin/bash
clear
sudo apt install python3 python3-pip -y
read -p "Press Enter to Exit! " pause
exit 0      
        """
        exec(f"""{main_name}_bat = codecs.open(f"./khanh/{pycode}.sh", "w", 'utf-8')""")
        exec(f"""{main_name}_bat.write(temp)""")
        os.system(f"""{terminal} -e 'bash ./khanh/{pycode}.sh' 2> /dev/null &> /dev/null &""")

# Restart popup
def close_popup():
    mainlanguagerestart = tkinter.Tk()
    mainlanguagerestart.title(f'Restart Application | Python (KhanhNguyen9872)')
    if (os.name == 'nt'):
        mainlanguagerestart.iconbitmap('khanh.ico')
    mainlanguagerestart.geometry("400x60")
    mainlanguagerestart.resizable(False, False)
    Label(mainlanguagerestart, text="This change requires a restart of the application!", font=('BOLD')).grid(row=0, sticky=W)
    CONFIRM1 = Button(mainlanguagerestart, text="  Close program  ", command=close_process).grid(row=1, column=0, sticky=W)
    mainlanguagerestart.mainloop()

# Python Shell on CMD
def pythonshell():
    if (os.name == 'nt'):
        cmd("start cmd /c python")
    else:
        os.system(f"""{terminal} -e "python3" 2> /dev/null &> /dev/null &""")
        #popup("Error","450x50",' Python Shell not work on Linux\n Try run [python3] on your Terminal to start it!')

# Control Panel
def controlpanel():
    if (os.name == 'nt'):
        cmd("start cmd /c control")
    else:
        popup("Error","450x30",' Control Panel not work on Linux!')

# Change language
def change_language(language):
    if (language=="Vietnamese"):
        rm('language\\vi-VN.khanh')
        touch('language\\en-US.khanh')
        close_popup()
        language=str("English")
        return language

    elif (language=="English"):
        rm('language\\en-US.khanh')
        touch('language\\vi-VN.khanh')
        close_popup()
        language=str("Vietnamese")
        return language

## Check python version
text = Text(main)
text.insert(INSERT, " * Program logs:\nInitializing program....\nCleanup TEMP folder.... Done\n\n")
passpy=0

# Create/Set TEMP folder
rmdir('khanh'); mkdir('khanh') 
temp_folder = Path("khanh")

####
if (os.name == 'nt'):
    windows_bit = str(struct.calcsize("P")*8)
    windows_release = str(platform.release())
    windows_machine = str(platform.machine())
    if (windows_machine=="AMD64"):
        windows_3264 = "64"
    elif (windows_machine=="ARM64"):
        windows_3264 = "64"
    else:
        windows_3264 = "32"

    text.insert(INSERT, f"Windows {windows_release} | {windows_3264}bit ({windows_machine})\nCompiled: Pyinstaller {windows_bit}bit (UPX/LZMA)\n")

    statusappshow = Path(f'{showcodemain_read}')    
    if (statusappshow.is_file()):
        statusappshowcode = "Found"
    else:
        statusappshowcode = "Not Found"
    if (statusappshowcode!="Not Found"):
        text.insert(INSERT, f"\nChecking {showcode_app}.... {statusappshowcode}\n\n")
    else:
        text.insert(INSERT, f"\nChecking {showcode_app}.... {statusappshowcode}\nWARNING: {showcode_app} Not Found!\n         ")
        showcodemain_read=str(f"{WINDOWS_DIRECTORY}\\notepad.exe")
        checknotepad = Path(f"{showcodemain_read}")
        if (checknotepad.is_file()):
            text.insert(INSERT, f"Default will select Notepad\n\n")
        else:
            text.insert(INSERT, f"ShowCode as application is NULL\n\n")
            showcodemain_read=str(f"")
            showcodeapp=str(f"")
        del checknotepad
    try:
        pyver = str(subprocess.check_output("python --version", shell=True).rstrip().decode("utf-8"))
    except:
        pyver=""

    if (amd64_or_32==0):
        python_win = "win64"
        python_win1 = "AMD64"
    else:
        python_win = "win32"
        python_win1 = "i686"

    if (pyver == ""):
        text.insert(INSERT, " ! No Python3 is installed!\n ! Please install Python first", END, "")
        Dpy = Button(main, text = "Install Python", command = lambda: pythonofficial(windows_release,windows_machine,0))
        Dpy.pack(side=BOTTOM)
        text.pack()
        time.sleep(0)
        main.mainloop()
    else:
        text.insert(INSERT, "Detected: " + str(pyver) + " (" + str(python_win) + ")\n")
        #if (int(pyver)<8):
            #text.insert(INSERT, " ! Python3 too old!\n ! Please update to latest Python3 offical!")
            #Bpy = Button(main, text = "Update Python", command = lambda: pythonofficial(windows_release,windows_machine))

    if (amd64_or_32==1) and (python_win1!=windows_machine):
        text.insert(INSERT, "\nWARNING: You are using 32bit Python on 64bit Windows!\n         Recommend using Python 64bit")

    text.insert(INSERT, "\n\nClose this window to start Program!")
    text.pack()
    main.mainloop()
else:
    windows_bit = str(struct.calcsize("P")*8)
    windows_release = str(platform.release())
    windows_machine = str(platform.machine())
    if (windows_machine=="x86_64"):
        windows_3264 = "64"
    if (windows_machine=="aarch64"):
        windows_3264 = "64"
    else:
        windows_3264 = "32"

    text.insert(INSERT, f"{windows_release} | {windows_3264}bit ({windows_machine})\nCompiled: Pyinstaller {windows_bit}bit (UPX/LZMA)\n")

    statusappshow = Path(f'{showcodemain_read}')    
    if (statusappshow.is_file()):
        statusappshowcode = "Found"
    else:
        statusappshowcode = "Not Found"
    if (statusappshowcode!="Not Found"):
        text.insert(INSERT, f"\nChecking {showcode_app}.... {statusappshowcode}\n\n")
    else:
        text.insert(INSERT, f"\nChecking {showcode_app}.... {statusappshowcode}\nWARNING: {showcode_app} Not Found!\n         ")
        showcodemain_read=str(f"{WINDOWS_DIRECTORY}/nano")
        checknotepad = Path(f"{showcodemain_read}")
        if (checknotepad.is_file()):
            text.insert(INSERT, f"Default will select Nano\n\n")
        else:
            text.insert(INSERT, f"ShowCode as application is NULL\n\n")
            showcodemain_read=str(f"")
            showcodeapp=str(f"")
        del checknotepad
    try:
        pyver = str(subprocess.check_output("python3 --version", shell=True).rstrip().decode("utf-8"))
    except:
        pyver=""

    if (amd64_or_32==0):
        python_win = "win64"
        python_win1 = "AMD64"
    else:
        python_win = "win32"
        python_win1 = "i686"

    if (pyver==""):
        text.insert(INSERT, " ! No Python3 is installed!\n ! Please install Python first", END, "")
        Dpy = Button(main, text = "Install Python", command = lambda: pythonofficial(windows_release,windows_machine,1))
        Dpy.pack(side=BOTTOM)
        text.pack()
        time.sleep(0)
        main.mainloop()
    else:
        text.insert(INSERT, "Detected: " + str(pyver) + " (" + str(python_win) + ")\n")
        #if (int(pyver)<8):
            #text.insert(INSERT, " ! Python3 too old!\n ! Please update to latest Python3 offical!")
            #Bpy = Button(main, text = "Update Python", command = lambda: pythonofficial(windows_release,windows_machine))

    if (amd64_or_32==1) and (python_win1!=windows_machine):
        text.insert(INSERT, "\nWARNING: You are using 32bit Python on 64bit Windows!\n         Recommend using Python 64bit")

    text.insert(INSERT, "\n\nClose this window to start Program!")
    text.pack()
    main.mainloop()

###############
try:
    del statusappshow
    del statusappshowcode
    del text
    del windows_bit
    del windows_3264
    del windows_machine
    del windows_release
    del khanhlocal
    del khanhlocal1
    del khanhlocal2
    del amd64_or_32
    del passpy
    del python_win1
    del python_win
    del python00
except:
    pass
###############

def get_number(a):
    print(a.widget.get())

def change_showcode():
    if (os.name == 'nt'):
        showcode_app_select = filedialog.askopenfilename(initialdir = "C:/Program Files", title = "Show Code Application", filetypes = (("Execute Application","*.exe"), ))
    else:
        showcode_app_select = filedialog.askopenfilename(initialdir = "/usr/bin", title = "Show Code Application", filetypes = (("Execute Application","*"), ))
    if (showcode_app_select==""):
        pass
    else:
        mkdir('settings')
        showcode_app = str("")
        len_showcodesettings = "-" + str(len(showcode_app_select)+1)
        for s in range(-1,int(len_showcodesettings),-1):
            if (showcode_app_select[int(s)]) == str(f"/") or (showcode_app_select[int(s)]) == str(f"\\"):
                if (os.name == 'nt'):
                    showcodemain = codecs.open(f".\settings\showcode.ini", "w", 'utf-8')
                else:
                    showcodemain = codecs.open(f"./settings/showcode.ini", "w", 'utf-8')
                string_encode = base64.b64encode(showcode_app_select.encode('utf-8',errors = 'strict')).decode("utf-8")
                binary_showcodeapp = ''.join(format(i, '08b') for i in bytearray(string_encode, encoding ='utf-8'))
                binary_showcodeapp = str(binary_showcodeapp[::-1])
                binary_showcodeapp = base64.a85encode(binary_showcodeapp.encode('utf-8')).decode('utf-8')
                binary_showcodeapp = str(binary_showcodeapp[::-1])
                showcodemain.write(str(binary_showcodeapp))
                showcodemain.close()
                break
            else:
                showcode_app = showcode_app + showcode_app_select[s]
        showcode_app = ''.join(reversed(showcode_app))
        close_popup()
        return showcode_app, showcodemain_read

def menucheck(khanhnguyen9872):
    try:
        menunum=int(E1.get())
    except:
        popup("Error","350x30",f"Vui long chon")
    if (menunum>int(total)):
        popup("Error","350x50",f"Bạn đã chọn vượt quá danh sách đang có!\n      Tối đa: 0-{total}")
    elif (menunum==-1):
        if (settings_showcode.is_file()):
            with open(f"{settings_showcode}",'r',encoding='utf-8') as file_name00:
                temp_decode = str(file_name00.read())
                try:
                    temp_decode = str(temp_decode[::-1])
                    temp_decode = base64.a85decode(temp_decode).decode('utf-8')
                    temp_decode = str(temp_decode[::-1])
                    binary_int = int(temp_decode, 2)
                    byte_number = binary_int.bit_length() + 7 // 8
                    binary_array = binary_int.to_bytes(byte_number, "big")
                    temp_decode = binary_array.decode()
                    string_decode = base64.b64decode(str(temp_decode)).decode("utf-8")
                    showcodemain_read=str(string_decode)
                except:
                    file_name00.close()
                    rm('settings\\showcode.ini')
                    mainshowcodeini = tkinter.Tk()
                    mainshowcodeini.title(f'Settings ERROR | Python (KhanhNguyen9872)')
                    if (os.name == 'nt'):
                        mainshowcodeini.iconbitmap('khanh.ico')
                    mainshowcodeini.geometry("500x60")
                    mainshowcodeini.resizable(False, False)
                    Label(mainshowcodeini, text="SETTING ERROR! showcode.ini will be recreated!", font=('BOLD')).grid(row=0, sticky=W)
                    CONFIRM1 = Button(mainshowcodeini, text="  Close program  ", command=close_process).grid(row=1, column=0, sticky=W)
                    mainshowcodeini.mainloop()
                    time.sleep(0)
                    exit()
            showcode_app=str("")
            len_showcodesettings = "-" + str(len(showcodemain_read)+1)
            for s in range(-1,int(len_showcodesettings),-1):
                if (showcodemain_read[int(s)]) == str(f"/") or (showcodemain_read[int(s)]) == str(f"\\"):
                    file_name00.close()
                    break
                else:
                    showcode_app = showcode_app + showcodemain_read[s]
            showcode_app = ''.join(reversed(showcode_app))
            del temp_decode
            del len_showcodesettings
            del binary_array
            del binary_int
            del byte_number
            del string_decode
        else:
            mkdir('settings')
            if (os.name == 'nt'):
                showcode_app_select = str(f"{WINDOWS_DIRECTORY}\\notepad.exe")
                showcodemain = codecs.open(f".\settings\showcode.ini", "w", 'utf-8')
            else:
                showcode_app_select = str(f"{WINDOWS_DIRECTORY}/nano")
                showcodemain = codecs.open(f"./settings/showcode.ini", "w", 'utf-8')
            string_encode = base64.b64encode(showcode_app_select.encode('utf-8',errors = 'strict')).decode("utf-8") 
            binary_showcodeapp = ''.join(format(i, '08b') for i in bytearray(string_encode, encoding ='utf-8'))
            binary_showcodeapp = str(binary_showcodeapp[::-1])
            binary_showcodeapp = base64.a85encode(binary_showcodeapp.encode('utf-8')).decode('utf-8')
            binary_showcodeapp = str(binary_showcodeapp[::-1])
            showcodemain.write(str(binary_showcodeapp))
            showcode_app = str("")
            len_showcodesettings = "-" + str(len(showcode_app_select)+1)
            for s in range(-1,int(len_showcodesettings),-1):
                if (showcode_app_select[int(s)]) == str(f"/") or (showcode_app_select[int(s)]) == str(f"\\"):
                    showcodemain.close()
                    break
                else:
                    showcode_app = showcode_app + showcode_app_select[s]
            with open(f"{settings_showcode}",'r',encoding='utf-8') as file_name00:
                temp_decode = str(file_name00.read())
                try:
                    temp_decode = str(temp_decode[::-1])
                    temp_decode = base64.a85decode(temp_decode).decode('utf-8')
                    temp_decode = str(temp_decode[::-1])
                    binary_int = int(temp_decode, 2)
                    byte_number = binary_int.bit_length() + 7 // 8
                    binary_array = binary_int.to_bytes(byte_number, "big")
                    temp_decode = binary_array.decode()
                    string_decode = base64.b64decode(temp_decode).decode("utf-8")
                    showcodemain_read=str(string_decode)
                except:
                    file_name00.close()
                    rm('settings\\showcode.ini')
                    mainshowcodeini = tkinter.Tk()
                    mainshowcodeini.title(f'Settings ERROR | Python (KhanhNguyen9872)')
                    if (os.name == 'nt'):
                        mainshowcodeini.iconbitmap('khanh.ico')
                    mainshowcodeini.geometry("500x60")
                    mainshowcodeini.resizable(False, False)
                    Label(mainshowcodeini, text="SETTING ERROR! showcode.ini will be recreated!", font=('BOLD')).grid(row=0, sticky=W)
                    CONFIRM1 = Button(mainshowcodeini, text="  Close program  ", command=close_process).grid(row=1, column=0, sticky=W)
                    mainshowcodeini.mainloop()
                    time.sleep(0)
                    exit()
            showcode_app = ''.join(reversed(showcode_app))
            del temp_decode
            del binary_showcodeapp
            del len_showcodesettings
            del binary_array
            del binary_int
            del byte_number
            del string_encode
            del string_decode
            del showcode_app_select

        if (os.name == 'nt'):
            name_showcode_app = str(showcode_app[-1] + showcode_app [-2] + showcode_app [-3] + showcode_app [-4])
            name_showcode_app = str(''.join(reversed(name_showcode_app)))
            if (name_showcode_app!=".exe"):
                mkdir('settings')
                if (os.name == 'nt'):
                    showcode_app_select = str(f"{WINDOWS_DIRECTORY}\\notepad.exe")
                else:
                    showcode_app_select = str(f"{WINDOWS_DIRECTORY}/nano")
                showcode_app = str("")
                len_showcodesettings = "-" + str(len(showcode_app_select)+1)
                for s in range(-1,int(len_showcodesettings),-1):
                    if (showcode_app_select[int(s)]) == str(f"/") or (showcode_app_select[int(s)]) == str(f"\\"):
                        if (os.name == 'nt'):
                            showcodemain = codecs.open(f".\settings\showcode.ini", "w", 'utf-8')
                        else:
                            showcodemain = codecs.open(f"./settings/showcode.ini", "w", 'utf-8')
                        string_encode = base64.b64encode(showcode_app_select.encode('utf-8',errors = 'strict')).decode("utf-8")
                        binary_showcodeapp = ''.join(format(i, '08b') for i in bytearray(string_encode, encoding ='utf-8'))
                        binary_showcodeapp = str(binary_showcodeapp[::-1])
                        binary_showcodeapp = base64.a85encode(binary_showcodeapp.encode('utf-8')).decode('utf-8')
                        binary_showcodeapp = str(binary_showcodeapp[::-1])
                        showcodemain.write(str(binary_showcodeapp))
                        showcodemain.close()
                        break
                    else:
                        showcode_app = showcode_app + showcode_app_select[s]
                with open(f"{settings_showcode}",'r',encoding='utf-8') as file_name00:
                    temp_decode = str(file_name00.read())
                    try:
                        temp_decode = str(temp_decode[::-1])
                        temp_decode = base64.a85decode(temp_decode).decode('utf-8')
                        temp_decode = str(temp_decode[::-1])
                        binary_int = int(temp_decode, 2)
                        byte_number = binary_int.bit_length() + 7 // 8
                        binary_array = binary_int.to_bytes(byte_number, "big")
                        temp_decode = binary_array.decode()
                        string_decode = base64.b64decode(temp_decode).decode("utf-8")
                        showcodemain_read=str(string_decode)
                    except:
                        file_name00.close()
                        rm('settings\\showcode.ini')
                        mainshowcodeini = tkinter.Tk()
                        mainshowcodeini.title(f'Settings ERROR | Python (KhanhNguyen9872)')
                        mainshowcodeini.iconbitmap('khanh.ico')
                        if (os.name == 'nt'):
                            mainshowcodeini.geometry("500x60")
                        mainshowcodeini.resizable(False, False)
                        Label(mainshowcodeini, text="SETTING ERROR! showcode.ini will be recreated!", font=('BOLD')).grid(row=0, sticky=W)
                        CONFIRM1 = Button(mainshowcodeini, text="  Close program  ", command=close_process).grid(row=1, column=0, sticky=W)
                        mainshowcodeini.mainloop()
                        time.sleep(0)
                        exit()
                showcode_app = str(''.join(reversed(showcode_app)))
            else:
                del name_showcode_app

        main001 = tkinter.Tk()
        main001.title(f'Settings | {pyver} (KhanhNguyen9872)')
        if (os.name == 'nt'):
            main001.iconbitmap('khanh.ico')
        main001.geometry("420x200")
        main001.resizable(False, False)
        Label(main001, text="Settings", font=('BOLD')).grid(row=0, sticky=W)
        Label(main001, text=f"Language (Current: {language})").grid(row=1, column=0, sticky=W)
        CONFIRM = Button(main001, text="  Change  ", command=lambda: change_language(str(language))).grid(row=1, column=1, sticky=W)
        Label(main001, text=f"Show Code as Application ({showcode_app}) ").grid(row=2, column=0, sticky=W)
        CONFIRM1 = Button(main001, text="  Change  ", command=change_showcode).grid(row=2, column=1, sticky=W)
        main001.mainloop()
    elif (menunum==0):
        main0 = tkinter.Tk()
        main0.title(f'About | {pyver} (KhanhNguyen9872)')
        if (os.name == 'nt'):
            main0.iconbitmap('khanh.ico')
        main0.geometry("500x140")
        main0.resizable(False, False)
        text0 = Text(main0)
        text0.insert(INSERT, f"Name: Nguyễn Văn Khánh\nFacebook: https://fb.me/khanh10a1\nYoutube: https://youtube.com/c/KhanhNguyen9872_Official\nGithub: https://github.com/khanhnguyen9872\nZalo: 0937927513\nPhone: +84937927513\nGenshin UID: 800983609")
        text0.pack()
        text0.config(state=DISABLED)
        main0.mainloop()
    elif (menunum==1):
    #   menu_option(menunum,main_tkinter,text_tkinter,main_name,example,copyright,user_copyright,geometry,total,name2,example2):
        menu_option(f"{menunum}",f"main{menunum}",f"text{menunum}","Giải phương trình bậc 2","CT: ax^2+bx+c=0","0","0","360x140","1","","")
    elif (menunum==2):
        menu_option(f"{menunum}",f"main{menunum}",f"text{menunum}","Tìm số lớn nhất","VD: [3,4,5,6,7,8]  ->  8","0","0","360x240","2","Tìm số bé nhất","VD: [3,4,5,6,7,8]  ->  3")
    elif (menunum==3):
        menu_option(f"{menunum}",f"main{menunum}",f"text{menunum}","Sắp xếp từ bé đến lớn","VD: [2,6,3,1,5]  ->  1, 2, 3, 5, 6","0","0","360x240","2","Sắp xếp từ lớn đến bé","VD: [2,6,3,1,5]  ->  6, 5, 3, 2, 1")
    elif (menunum==4):
        menu_option(f"{menunum}",f"main{menunum}",f"text{menunum}","Đếm số lần xuất hiện từ 1 chuỗi","VD: 'aabbbcd'  ->  a:2, b:3, c:1, d:1","0","0","400x140","1","","")
    elif (menunum==5):
        menu_option(f"{menunum}",f"main{menunum}",f"text{menunum}","Mã hóa bằng base64","VD: 'khanh'  ->  'a2hhbmg='","0","0","360x240","2","Giải mã bằng base64","VD: 'a2hhbmg='  ->  'khanh'")
    elif (menunum==6):
        menu_option(f"{menunum}",f"main{menunum}",f"text{menunum}","Chuyển tiền USD -> VND","VD: 4 USD  ->  90580 VND","0","0","360x240","2","Chuyển tiền VND -> USD","VD: 90580 VND  ->  4 USD")
    elif (menunum==7):
        menu_option(f"{menunum}",f"main{menunum}",f"text{menunum}","Tìm số giai thừa","","0","0","360x140","1","","")
    elif (menunum==8):
        menu_option(f"{menunum}",f"main{menunum}",f"text{menunum}","Tìm ƯCLN và BCNN","","0","0","360x140","1","","")
    elif (menunum==9):
        menu_option(f"{menunum}",f"main{menunum}",f"text{menunum}","Kiểm tra số nguyên tố","","0","0","360x140","1","","")
    elif (menunum==10):
        menu_option(f"{menunum}",f"main{menunum}",f"text{menunum}","Tạo hình tam giác trong Terminal","","0","0","360x140","1","","")
    elif (menunum==11):
        menu_option(f"{menunum}",f"main{menunum}",f"text{menunum}","Pháo hoa trên bằng Turtle","","Lã Thành Trung","1","400x140","1","","")
    elif (menunum==12):
        menu_option(f"{menunum}",f"main{menunum}",f"text{menunum}","Tìm ra chữ có 3 kí tự trở lên","","0","0","400x140","1","","")
    elif (menunum==13):
        menu_option(f"{menunum}",f"main{menunum}",f"text{menunum}","Tính tổng các ước số của N","","0","0","400x140","1","","")
    elif (menunum==14):
        menu_option(f"{menunum}",f"main{menunum}",f"text{menunum}","Tính lũy thừa a^b bằng pow()","","0","0","400x140","1","","")
    elif (menunum==15):
        menu_option(f"{menunum}",f"main{menunum}",f"text{menunum}","KT tam giác vuông, đều, cân, tù, nhọn","VD: a=3, b=4, c=5  ->  'Tam giác vuông'","0","0","400x140","1","","")
    elif (menunum==16):
        menu_option(f"{menunum}",f"main{menunum}",f"text{menunum}","Tìm ra các số chẵn, lẻ","VD: [3,4,6,a,9]  ->  Chẵn: 4,6 | Lẻ: 3, 9","0","0","400x140","1","","")
    elif (menunum==17):
        menu_option(f"{menunum}",f"main{menunum}",f"text{menunum}","Đếm kí tự In hoa, thường","VD: 'Khanh9872' -> In hoa: 1 | In thường: 4","0","0","440x140","1","","")

### MAIN
main1 = tkinter.Tk()
main1.title(f'Menu | {pyver} (KhanhNguyen9872)')
if (os.name == 'nt'):
    main1.iconbitmap('khanh.ico')
main1.geometry("600x420")
main1.resizable(False, False)
text = Text(main1)
text.insert(INSERT, "\nMenu các chương trình của tôi\nBy KhanhNguyen9872\n\nVui lòng chọn: \n-1. Settings\n0. KhanhNguyen9872\n1. Giải phương trình bậc 2\n2. Tìm ra số lớn nhất, bé nhất\n3. Sắp xếp từ bé đến lớn và ngược lại\n4. Đếm số lần xuất hiện của 1 chuỗi\n5. Mã hóa 1 chuỗi string\n6. Chuyển tiền USD -> VND, VND -> USD\n7. Tìm số giai thừa\n8. Tìm ƯCLN và BCNN\n9. Kiểm tra số nguyên tố\n10. Tạo hình tam giác trong Terminal\n11. Tạo pháo hoa bằng Turtle\n12. Tìm ra chữ có 3 kí tự trở lên trong String\n13. Tính tổng các ước số của N (ngoại trừ N)\n14. Tính lũy thừa a^b bằng hàm pow()\n15. Kiểm tra là tam giác vuông, đều, cân, tù hay nhọn")
text.insert(INSERT, "\n16. Tìm ra các số chẵn, lẻ (Có lượt bỏ kí tự không phải số)\n17. Đếm số các kí tự In hoa và In thường (Không bao gồm số)\n18. \n19. \n20. ")
text.insert(INSERT, "\n21. \n22. \n23. \n24. \n25. ")
text.insert(INSERT, "\n26. \n27. \n28. \n29. \n30. \n\n")
text.pack()
text.config(state=DISABLED)
#text.bind('<Control-c>', lambda _:'break')
#text.bind('<Control-v>', lambda _:'break')
#text.bind('<BackSpace>', lambda _:'break')
#text.bind('<Return>', lambda _:'break')


L1 = Label(main1, text="Choose:")
L1.pack(side = LEFT)
L2 = Label(main1, text="https://fb.me/khanh10a1")
L2.pack(side = RIGHT)
E1 = Entry(main1, bd=5)
E1.pack(side = LEFT)

E1.bind('<Return>', menucheck)
B = Button(main1, text = "OK", command = lambda: menucheck(''))
B.pack(side=LEFT)
BB = Button(main1, text = "Python Shell", command = pythonshell)
BB.pack(side=BOTTOM)

main1.mainloop()




















