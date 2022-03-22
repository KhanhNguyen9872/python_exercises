#!/bin/python3
#KhanhNguyen9872
#This is main windows!

# Import thư viện
import math
import os
import base64
import time
import tkinter
import urllib
import urllib.request
import codecs
import platform
import struct
import hashlib
from random import *
from tkinter import *
from tkinter import filedialog
from pathlib import Path
from tkinter import messagebox

# Hàm dành cho hệ thống
def clear():
    os.system('cls')

def pause():
    os.system('pause > NUL')

def close_process():
    kill_process = """
@echo off
taskkill /f /im python_exercises_khanhnguyen9872.exe > NUL
rmdir /q /s khanh > NUL
exit
    """
    os.system('mkdir khanh')
    close_process_bat = codecs.open(f".\khanh\khanh_kill.bat", "w", 'utf-8')
    close_process_bat.write(kill_process)
    close_process_bat.close()
    os.system("start cmd /c khanh\khanh_kill.bat")
    time.sleep(1)
    exit()

def showcodeisnull():
    maincodenull = tkinter.Tk()
    maincodenull.title(f'No ShowCode Application | Python (KhanhNguyen9872)')
    maincodenull.iconbitmap('khanh.ico')
    maincodenull.geometry("400x60")
    maincodenull.resizable(False, False)
    Label(maincodenull, text="Show code as Application is not found!", font=('BOLD')).grid(row=0, sticky=W)
    Label(maincodenull, text="You can go to Settings to change it!", font=('BOLD')).grid(row=1, sticky=W)
    maincodenull.mainloop()

# Nhóm (class)
####UNDERLINE

# Gán giá trị
BUF_SIZE = 65536        # Buffer size for Download
python00=[]             # Array for check python version
total=int(30)           # Maximum Menu
temp=[]                 # Temp array
language=str("")        # Language
amd64_or_32 = 0         # Default is 0 (64bit)

### Required file
checkicon = Path('khanh.ico')
mainpyexe = Path('python_exercises_khanhnguyen9872.exe')
english = Path('language\en-US.khanh')
vietnamese = Path('language\vi-VN.khanh')
settings_showcode = Path('settings\showcode.ini')
khanhlocal = os.getenv('LOCALAPPDATA')
khanhlocal1 = os.getenv('PROGRAMFILES')
WINDOWS_DIRECTORY = os.getenv('WINDIR')
khanhlocal2 = os.getenv('PROGRAMFILES(X86)')
cmd_exe = Path(f'{WINDOWS_DIRECTORY}\system32\cmd.exe')

# Check
if (cmd_exe.is_file()):
    del cmd_exe
else:
    mainicon = tkinter.Tk()
    mainicon.title(f'CMD is not found! | Python (KhanhNguyen9872)')
    mainicon.geometry("350x40")
    mainicon.resizable(False, False)
    Label(mainicon, text="Program can't start without CMD", font=('BOLD')).grid(row=0, sticky=W)
    mainicon.mainloop()
    time.sleep(0)
    exit()

if (mainpyexe.is_file()):
    del mainpyexe
else:
    mainicon = tkinter.Tk()
    mainicon.title(f'Missing File | Python (KhanhNguyen9872)')
    mainicon.geometry("350x80")
    mainicon.resizable(False, False)
    Label(mainicon, text="Missing required file!\nFile: python_exercises_khanhnguyen9872.exe", font=('BOLD')).grid(row=0, sticky=W)
    CONFIRM1 = Button(mainicon, text="  Close program  ", command=close_process).grid(row=1, column=0, sticky=W)
    mainicon.mainloop()
    time.sleep(0)
    exit()

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
            os.remove('settings\\showcode.ini')
            mainshowcodeini = tkinter.Tk()
            mainshowcodeini.title(f'Settings ERROR | Python (KhanhNguyen9872)')
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
    os.system('mkdir settings > NUL')
    showcode_app_select = str(f"{WINDOWS_DIRECTORY}\\notepad.exe")
    showcode_app = str("")
    len_showcodesettings = "-" + str(len(showcode_app_select)+1)
    for s in range(-1,int(len_showcodesettings),-1):
        if (showcode_app_select[int(s)]) == str(f"/") or (showcode_app_select[int(s)]) == str(f"\\"):
            showcodemain = codecs.open(f".\settings\showcode.ini", "w", 'utf-8')
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
            os.remove('settings\\showcode.ini')
            mainshowcodeini = tkinter.Tk()
            mainshowcodeini.title(f'Settings ERROR | Python (KhanhNguyen9872)')
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

name_showcode_app = str(showcode_app[-1] + showcode_app [-2] + showcode_app [-3] + showcode_app [-4])
name_showcode_app = str(''.join(reversed(name_showcode_app)))
if (name_showcode_app!=".exe"):
    os.system('mkdir settings > NUL')
    showcode_app_select = str(f"{WINDOWS_DIRECTORY}\\notepad.exe")
    showcode_app = str("")
    len_showcodesettings = "-" + str(len(showcode_app_select)+1)
    for s in range(-1,int(len_showcodesettings),-1):
        if (showcode_app_select[int(s)]) == str(f"/") or (showcode_app_select[int(s)]) == str(f"\\"):
            showcodemain = codecs.open(f".\settings\showcode.ini", "w", 'utf-8')
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
            os.remove('settings\\showcode.ini')
            mainshowcodeini = tkinter.Tk()
            mainshowcodeini.title(f'Settings ERROR | Python (KhanhNguyen9872)')
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
    os.system('rmdir /q /s language > NUL')
    os.system('mkdir language > NUL')
    vietnamese_lan = codecs.open(f"language\\vi-VN.khanh", "w", 'utf-8')
    vietnamese_lan.write("khanhnguyen9872")
    vietnamese_lan.close()
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
    os.system('rmdir /q /s language > NUL')
    os.system('mkdir language > NUL')
    vietnamese_lan = codecs.open(f"language\\vi-VN.khanh", "w", 'utf-8')
    vietnamese_lan.write("khanhnguyen9872")
    language=str("Vietnamese")
    vietnamese_lan.close()
    del vietnamese
    del english

## Main windows
main = tkinter.Tk()
main.title(f'Python  (KhanhNguyen9872)')
main.iconbitmap('khanh.ico')
main.geometry("460x280")
main.resizable(False, False)

# Hàm chương trình
def showcode(menunumber,app):
    if (menunumber==1):
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
        if (app!=1):
            mainshow1 = tkinter.Tk()
            mainshow1.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow1.iconbitmap('khanh.ico')
            mainshow1.geometry("600x380")
            mainshow1.resizable(False, False)
            text0 = Text(mainshow1)
            text0.insert(INSERT, code1)
            text0.pack()
            text0.config(state=DISABLED)
            #text0.tag_add("start", "1.0", "99.0")
            #text0.tag_config("start", background = "gray", foreground = "white")
            mainshow1.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow1a = codecs.open(f".\khanh\code1.py", "w", 'utf-8')
                mainshow1a.write(code1)
                mainshow1a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code1.py')
            else:
                showcodeisnull()

    elif (menunumber==2):
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
        if (app!=1):
            mainshow2 = tkinter.Tk()
            mainshow2.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow2.iconbitmap('khanh.ico')
            mainshow2.geometry("600x380")
            mainshow2.resizable(False, False)
            text0 = Text(mainshow2)
            text0.insert(INSERT, code2)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow2.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow2a = codecs.open(f".\khanh\code2.py", "w", 'utf-8')
                mainshow2a.write(code2)
                mainshow2a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code2.py')
            else:
                showcodeisnull()
        
    elif (menunumber=="2"):
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
        if (app!=1):
            mainshow2m = tkinter.Tk()
            mainshow2m.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow2m.iconbitmap('khanh.ico')
            mainshow2m.geometry("600x380")
            mainshow2m.resizable(False, False)
            text0 = Text(mainshow2m)
            text0.insert(INSERT, code2_min)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow2m.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow2aa = codecs.open(f".\khanh\code2min.py", "w", 'utf-8')
                mainshow2aa.write(code2_min)
                mainshow2aa.close()
                os.system(f'"{showcodemain_read}" .\khanh\code2min.py')
            else:
                showcodeisnull()

    elif (menunumber==3):
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
        if (app!=1):
            mainshow3 = tkinter.Tk()
            mainshow3.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow3.iconbitmap('khanh.ico')
            mainshow3.geometry("600x380")
            mainshow3.resizable(False, False)
            text0 = Text(mainshow3)
            text0.insert(INSERT, code3)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow3.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow3a = codecs.open(f".\khanh\code3.py", "w", 'utf-8')
                mainshow3a.write(code3)
                mainshow3a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code3.py')
            else:
                showcodeisnull()

    elif (menunumber=="3"):
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
        if (app!=1):
            mainshow3m = tkinter.Tk()
            mainshow3m.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow3m.iconbitmap('khanh.ico')
            mainshow3m.geometry("600x380")
            mainshow3m.resizable(False, False)
            text0 = Text(mainshow3m)
            text0.insert(INSERT, code3_min)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow3m.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow3aa = codecs.open(f".\khanh\code3min.py", "w", 'utf-8')
                mainshow3aa.write(code3_min)
                mainshow3aa.close()
                os.system(f'"{showcodemain_read}" .\khanh\code3min.py')
            else:
                showcodeisnull()

    elif (menunumber==4):
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
        if (app!=1):
            mainshow4 = tkinter.Tk()
            mainshow4.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow4.iconbitmap('khanh.ico')
            mainshow4.geometry("600x380")
            mainshow4.resizable(False, False)
            text0 = Text(mainshow4)
            text0.insert(INSERT, code4)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow4.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow4a = codecs.open(f".\khanh\code4.py", "w", 'utf-8')
                mainshow4a.write(code4)
                mainshow4a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code4.py')
            else:
                showcodeisnull()
    

    elif (menunumber==5):
        code5='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Mã hóa 1 chuỗi string bằng base64

import base64

string = str(input("Nhập chuỗi: "))

string_encode = base64.b64encode(string.encode('utf-8',errors = 'strict')).decode("utf-8") 

print('\\nString đã được mã hóa:\\n' + str(string_encode))
        '''
        if (app!=1):
            mainshow5 = tkinter.Tk()
            mainshow5.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow5.iconbitmap('khanh.ico')
            mainshow5.geometry("600x380")
            mainshow5.resizable(False, False)
            text0 = Text(mainshow5)
            text0.insert(INSERT, code5)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow5.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow5a = codecs.open(f".\khanh\code5.py", "w", 'utf-8')
                mainshow5a.write(code5)
                mainshow5a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code5.py')
            else:
                showcodeisnull()

    elif (menunumber=="5"):
        code5de='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Giải mã 1 chuỗi string bị mã hóa do base64

import base64

string = str(input("Nhập chuỗi string bị mã hóa: "))

string_decode = base64.b64decode(string).decode("utf-8")

print('\\nString đã được giải mã:\\n' + str(string_decode))
        '''
        if (app!=1):
            mainshow5de = tkinter.Tk()
            mainshow5de.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow5de.iconbitmap('khanh.ico')
            mainshow5de.geometry("600x380")
            mainshow5de.resizable(False, False)
            text0 = Text(mainshow5de)
            text0.insert(INSERT, code5de)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow5de.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow5aa = codecs.open(f".\khanh\code5de.py", "w", 'utf-8')
                mainshow5aa.write(code5de)
                mainshow5aa.close()
                os.system(f'"{showcodemain_read}" .\khanh\code5de.py')
            else:
                showcodeisnull()

    elif (menunumber==6):
        code6='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Chuyển tiền USD -> VND

USD = input("Nhập số tiền USD: ")

VND = int(USD)*22645

print(f"Số tiền VND:", VND, "VND")
        '''
        if (app!=1):
            mainshow6 = tkinter.Tk()
            mainshow6.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow6.iconbitmap('khanh.ico')
            mainshow6.geometry("600x380")
            mainshow6.resizable(False, False)
            text0 = Text(mainshow6)
            text0.insert(INSERT, code6)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow6.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow6a = codecs.open(f".\khanh\code6.py", "w", 'utf-8')
                mainshow6a.write(code6)
                mainshow6a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code6.py')
            else:
                showcodeisnull()

    elif (menunumber=="6"):
        code6o='''
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
        if (app!=1):
            mainshow6o = tkinter.Tk()
            mainshow6o.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow6o.iconbitmap('khanh.ico')
            mainshow6o.geometry("600x380")
            mainshow6o.resizable(False, False)
            text0 = Text(mainshow6o)
            text0.insert(INSERT, code6o)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow6o.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow6aa = codecs.open(f".\khanh\code6o.py", "w", 'utf-8')
                mainshow6aa.write(code6o)
                mainshow6aa.close()
                os.system(f'"{showcodemain_read}" .\khanh\code6o.py')
            else:
                showcodeisnull()

    elif (menunumber==7):
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
        if (app!=1):
            mainshow7 = tkinter.Tk()
            mainshow7.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow7.iconbitmap('khanh.ico')
            mainshow7.geometry("600x380")
            mainshow7.resizable(False, False)
            text0 = Text(mainshow7)
            text0.insert(INSERT, code7)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow7.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow7a = codecs.open(f".\khanh\code7.py", "w", 'utf-8')
                mainshow7a.write(code7)
                mainshow7a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code7.py')
            else:
                showcodeisnull()

    elif (menunumber==8):
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
        if (app!=1):
            mainshow8 = tkinter.Tk()
            mainshow8.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow8.iconbitmap('khanh.ico')
            mainshow8.geometry("600x380")
            mainshow8.resizable(False, False)
            text0 = Text(mainshow8)
            text0.insert(INSERT, code8)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow8.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow8a = codecs.open(f".\khanh\code8.py", "w", 'utf-8')
                mainshow8a.write(code8)
                mainshow8a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code8.py')
            else:
                showcodeisnull()

    elif (menunumber==9):
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
        if (app!=1):
            mainshow9 = tkinter.Tk()
            mainshow9.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow9.iconbitmap('khanh.ico')
            mainshow9.geometry("600x380")
            mainshow9.resizable(False, False)
            text0 = Text(mainshow9)
            text0.insert(INSERT, code9)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow9.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow9a = codecs.open(f".\khanh\code9.py", "w", 'utf-8')
                mainshow9a.write(code9)
                mainshow9a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code9.py')
            else:
                showcodeisnull()

    elif (menunumber==10):
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
        if (app!=1):
            mainshow10 = tkinter.Tk()
            mainshow10.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow10.iconbitmap('khanh.ico')
            mainshow10.geometry("600x380")
            mainshow10.resizable(False, False)
            text0 = Text(mainshow10)
            text0.insert(INSERT, code10)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow10.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow10a = codecs.open(f".\khanh\code10.py", "w", 'utf-8')
                mainshow10a.write(code10)
                mainshow10a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code10.py')
            else:
                showcodeisnull()

    elif (menunumber==11):
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
        if (app!=1):
            mainshow11 = tkinter.Tk()
            mainshow11.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow11.iconbitmap('khanh.ico')
            mainshow11.geometry("600x380")
            mainshow11.resizable(False, False)
            text0 = Text(mainshow11)
            text0.insert(INSERT, code11)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow11.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow11a = codecs.open(f".\khanh\code11.py", "w", 'utf-8')
                mainshow11a.write(code11)
                mainshow11a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code11.py')
            else:
                showcodeisnull()

    elif (menunumber==12):
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
        if (app!=1):
            mainshow12 = tkinter.Tk()
            mainshow12.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow12.iconbitmap('khanh.ico')
            mainshow12.geometry("600x380")
            mainshow12.resizable(False, False)
            text0 = Text(mainshow12)
            text0.insert(INSERT, code12)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow12.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow12a = codecs.open(f".\khanh\code12.py", "w", 'utf-8')
                mainshow12a.write(code12)
                mainshow12a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code12.py')
            else:
                showcodeisnull()
    elif (menunumber==13):
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
        if (app!=1):
            mainshow13 = tkinter.Tk()
            mainshow13.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow13.iconbitmap('khanh.ico')
            mainshow13.geometry("600x380")
            mainshow13.resizable(False, False)
            text0 = Text(mainshow13)
            text0.insert(INSERT, code13)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow13.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow13a = codecs.open(f".\khanh\code13.py", "w", 'utf-8')
                mainshow13a.write(code13)
                mainshow13a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code13.py')
            else:
                showcodeisnull()
    elif (menunumber==14):
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
        if (app!=1):
            mainshow14 = tkinter.Tk()
            mainshow14.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow14.iconbitmap('khanh.ico')
            mainshow14.geometry("600x380")
            mainshow14.resizable(False, False)
            text0 = Text(mainshow14)
            text0.insert(INSERT, code14)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow14.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow14a = codecs.open(f".\khanh\code14.py", "w", 'utf-8')
                mainshow14a.write(code14)
                mainshow14a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code14.py')
            else:
                showcodeisnull()
    elif (menunumber==15):
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
        if (app!=1):
            mainshow15 = tkinter.Tk()
            mainshow15.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow15.iconbitmap('khanh.ico')
            mainshow15.geometry("600x380")
            mainshow15.resizable(False, False)
            text0 = Text(mainshow15)
            text0.insert(INSERT, code15)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow15.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow15a = codecs.open(f".\khanh\code15.py", "w", 'utf-8')
                mainshow15a.write(code15)
                mainshow15a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code15.py')
            else:
                showcodeisnull()
    elif (menunumber==16):
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
        if (app!=1):
            mainshow16 = tkinter.Tk()
            mainshow16.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow16.iconbitmap('khanh.ico')
            mainshow16.geometry("600x380")
            mainshow16.resizable(False, False)
            text0 = Text(mainshow16)
            text0.insert(INSERT, code16)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow16.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow16a = codecs.open(f".\khanh\code16.py", "w", 'utf-8')
                mainshow16a.write(code16)
                mainshow16a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code16.py')
            else:
                showcodeisnull()

    elif (menunumber==17):
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
        if (app!=1):
            mainshow17 = tkinter.Tk()
            mainshow17.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow17.iconbitmap('khanh.ico')
            mainshow17.geometry("600x380")
            mainshow17.resizable(False, False)
            text0 = Text(mainshow17)
            text0.insert(INSERT, code17)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow17.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow17a = codecs.open(f".\khanh\code17.py", "w", 'utf-8')
                mainshow17a.write(code17)
                mainshow17a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code17.py')
            else:
                showcodeisnull()
    
    elif (menunumber==18):
        code18='''

        '''
        if (app!=1):
            mainshow18 = tkinter.Tk()
            mainshow18.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow18.iconbitmap('khanh.ico')
            mainshow18.geometry("600x380")
            mainshow18.resizable(False, False)
            text0 = Text(mainshow18)
            text0.insert(INSERT, code18)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow18.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow18a = codecs.open(f".\khanh\code18.py", "w", 'utf-8')
                mainshow18a.write(code18)
                mainshow18a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code18.py')
            else:
                showcodeisnull()

    elif (menunumber==19):
        code19='''

        '''
        if (app!=1):
            mainshow19 = tkinter.Tk()
            mainshow19.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow19.iconbitmap('khanh.ico')
            mainshow19.geometry("600x380")
            mainshow19.resizable(False, False)
            text0 = Text(mainshow19)
            text0.insert(INSERT, code19)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow19.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow19a = codecs.open(f".\khanh\code19.py", "w", 'utf-8')
                mainshow19a.write(code19)
                mainshow19a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code19.py')
            else:
                showcodeisnull()

    elif (menunumber==20):
        code20='''

        '''
        if (app!=1):
            mainshow20 = tkinter.Tk()
            mainshow20.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow20.iconbitmap('khanh.ico')
            mainshow20.geometry("600x380")
            mainshow20.resizable(False, False)
            text0 = Text(mainshow20)
            text0.insert(INSERT, code20)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow20.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow20a = codecs.open(f".\khanh\code20.py", "w", 'utf-8')
                mainshow20a.write(code20)
                mainshow20a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code20.py')
            else:
                showcodeisnull()

    elif (menunumber==21):
        code21='''

        '''
        if (app!=1):
            mainshow21 = tkinter.Tk()
            mainshow21.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow21.iconbitmap('khanh.ico')
            mainshow21.geometry("600x380")
            mainshow21.resizable(False, False)
            text0 = Text(mainshow21)
            text0.insert(INSERT, code21)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow21.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow21a = codecs.open(f".\khanh\code21.py", "w", 'utf-8')
                mainshow21a.write(code21)
                mainshow21a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code21.py')
            else:
                showcodeisnull()

    elif (menunumber==22):
        code22='''

        '''
        if (app!=1):
            mainshow22 = tkinter.Tk()
            mainshow22.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow22.iconbitmap('khanh.ico')
            mainshow22.geometry("600x380")
            mainshow22.resizable(False, False)
            text0 = Text(mainshow22)
            text0.insert(INSERT, code22)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow22.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow22a = codecs.open(f".\khanh\code22.py", "w", 'utf-8')
                mainshow22a.write(code22)
                mainshow22a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code22.py')
            else:
                showcodeisnull()

    elif (menunumber==23):
        code23='''

        '''
        if (app!=1):
            mainshow23 = tkinter.Tk()
            mainshow23.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow23.iconbitmap('khanh.ico')
            mainshow23.geometry("600x380")
            mainshow23.resizable(False, False)
            text0 = Text(mainshow23)
            text0.insert(INSERT, code23)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow23.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow23a = codecs.open(f".\khanh\code23.py", "w", 'utf-8')
                mainshow23a.write(code23)
                mainshow23a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code23.py')
            else:
                showcodeisnull()

    elif (menunumber==24):
        code24='''

        '''
        if (app!=1):
            mainshow24 = tkinter.Tk()
            mainshow24.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow24.iconbitmap('khanh.ico')
            mainshow24.geometry("600x380")
            mainshow24.resizable(False, False)
            text0 = Text(mainshow24)
            text0.insert(INSERT, code24)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow24.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow24a = codecs.open(f".\khanh\code24.py", "w", 'utf-8')
                mainshow24a.write(code24)
                mainshow24a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code24.py')
            else:
                showcodeisnull()

    elif (menunumber==25):
        code25='''

        '''
        if (app!=1):
            mainshow25 = tkinter.Tk()
            mainshow25.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow25.iconbitmap('khanh.ico')
            mainshow25.geometry("600x380")
            mainshow25.resizable(False, False)
            text0 = Text(mainshow25)
            text0.insert(INSERT, code25)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow25.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow25a = codecs.open(f".\khanh\code25.py", "w", 'utf-8')
                mainshow25a.write(code25)
                mainshow25a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code25.py')
            else:
                showcodeisnull()

    elif (menunumber==26):
        code26='''

        '''
        if (app!=1):
            mainshow26 = tkinter.Tk()
            mainshow26.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow26.iconbitmap('khanh.ico')
            mainshow26.geometry("600x380")
            mainshow26.resizable(False, False)
            text0 = Text(mainshow26)
            text0.insert(INSERT, code26)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow26.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow26a = codecs.open(f".\khanh\code26.py", "w", 'utf-8')
                mainshow26a.write(code26)
                mainshow26a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code26.py')
            else:
                showcodeisnull()

    elif (menunumber==27):
        code27='''

        '''
        if (app!=1):
            mainshow27 = tkinter.Tk()
            mainshow27.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow27.iconbitmap('khanh.ico')
            mainshow27.geometry("600x380")
            mainshow27.resizable(False, False)
            text0 = Text(mainshow27)
            text0.insert(INSERT, code27)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow27.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow27a = codecs.open(f".\khanh\code27.py", "w", 'utf-8')
                mainshow27a.write(code27)
                mainshow27a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code27.py')
            else:
                showcodeisnull()

    elif (menunumber==28):
        code28='''

        '''
        if (app!=1):
            mainshow28 = tkinter.Tk()
            mainshow28.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow28.iconbitmap('khanh.ico')
            mainshow28.geometry("600x380")
            mainshow28.resizable(False, False)
            text0 = Text(mainshow28)
            text0.insert(INSERT, code28)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow28.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow28a = codecs.open(f".\khanh\code28.py", "w", 'utf-8')
                mainshow28a.write(code28)
                mainshow28a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code28.py')
            else:
                showcodeisnull()

    elif (menunumber==29):
        code29='''

        '''
        if (app!=1):
            mainshow29 = tkinter.Tk()
            mainshow29.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow29.iconbitmap('khanh.ico')
            mainshow29.geometry("600x380")
            mainshow29.resizable(False, False)
            text0 = Text(mainshow29)
            text0.insert(INSERT, code29)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow29.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow29a = codecs.open(f".\khanh\code29.py", "w", 'utf-8')
                mainshow29a.write(code29)
                mainshow29a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code29.py')
            else:
                showcodeisnull()

    elif (menunumber==30):
        code30='''

        '''
        if (app!=1):
            mainshow30 = tkinter.Tk()
            mainshow30.title(f'Show code [{menunumber}]    |    Use: "Ctrl + C" to copy (KhanhNguyen9872)')
            mainshow30.iconbitmap('khanh.ico')
            mainshow30.geometry("600x380")
            mainshow30.resizable(False, False)
            text0 = Text(mainshow30)
            text0.insert(INSERT, code30)
            text0.pack()
            text0.config(state=DISABLED)
            mainshow30.mainloop()
        else:
            if (showcodemain_read!=""):
                mainshow30a = codecs.open(f".\khanh\code30.py", "w", 'utf-8')
                mainshow30a.write(code30)
                mainshow30a.close()
                os.system(f'"{showcodemain_read}" .\khanh\code30.py')
            else:
                showcodeisnull()













def runterminal(runter):
    if (runter==1):
        code1='''
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Giải phương trình bậc 2

import math

print("")

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
a = float(input("Nhập a = "))
b = float(input("Nhập b = "))
c = float(input("Nhập c = "))
print("\\n============\\n")
# Gọi hàm giải phương trình bậc 2
giaiPTBac2(a, b, c)

        '''
        code1_bat='''@echo off
TITLE Bai 1 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code1.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode1 = codecs.open(f".\khanh\code1.py", "w", 'utf-8')
        filecode1.write(code1)
        filecode1_bat = codecs.open(f".\khanh\code1.bat", "w", 'utf-8')
        filecode1_bat.write(code1_bat)
        os.system("start cmd /c khanh\code1.bat")
    elif (runter==2):
        code2='''print("")
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Tìm ra số lớn nhất

n = int(input("Nhập n: "))
list = []
max = 0

for i in range(1, n + 1):
    a = int(input(f"Nhập số lần {i}: "))
    list.append(a)
for j in list:
    if (j > max):
        max = j
    else:
        continue

print("\\n============\\n")

print(f"Số lớn nhất: {max}")
        '''
        code2_bat='''@echo off
TITLE Bai 2 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code2.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode2 = codecs.open(f".\khanh\code2.py", "w", 'utf-8')
        filecode2.write(code2)
        filecode2_bat = codecs.open(f".\khanh\code2.bat", "w", 'utf-8')
        filecode2_bat.write(code2_bat)
        os.system("start cmd /c khanh\code2.bat")
    elif (runter=="2"):
        code2_min='''print("")
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Tìm ra số bé nhất

n = int(input("Nhập n: "))
list = []

for i in range(1, n + 1):
    a = int(input(f"Nhập số lần {i}: "))
    list.append(a)

min = list[0]

for j in list:
    if (j == min):
        continue
    elif (j < min):
        min = j
    else:
        continue

print("\\n============\\n")

print(f"Số bé nhất: {min}")
        '''
        code2_min_bat='''@echo off
TITLE Bai 2 (Min) - Python (KhanhNguyen9872)
color 17
cls
python khanh\code2min.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode2min = codecs.open(f".\khanh\code2min.py", "w", 'utf-8')
        filecode2min.write(code2_min)
        filecode2min_bat = codecs.open(f".\khanh\code2min.bat", "w", 'utf-8')
        filecode2min_bat.write(code2_min_bat)
        os.system("start cmd /c khanh\code2min.bat")
    elif (runter==3):
        code3='''print("")
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Sắp xếp từ bé đến lớn

n=int(input("Nhập n: "))

answer=[]

for i in range(1,n+1):
    a=str(input(f"Nhập lần {i}: "))
    answer.append(a)

answer.sort()

print("\\n============\\n")

print("Từ bé đến lớn: " + str(', '.join(answer)))
        '''
        code3_bat='''@echo off
TITLE Bai 3 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code3.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode3 = codecs.open(f".\khanh\code3.py", "w", 'utf-8')
        filecode3.write(code3)
        filecode3_bat = codecs.open(f".\khanh\code3.bat", "w", 'utf-8')
        filecode3_bat.write(code3_bat)
        os.system("start cmd /c khanh\code3.bat")
    elif (runter=="3"):
        code3_min='''print("")
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Sắp xếp từ lớn đến bé

n=int(input("Nhập n: "))

answer=[]

for i in range(1,n+1):
    a=str(input(f"Nhập lần {i}: "))
    answer.append(a)

answer.sort(reverse=True)

print("\\n============\\n")

print("Từ lớn đến bé: " + str(', '.join(answer)))
        '''
        code3_min_bat='''@echo off
TITLE Bai 3 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code3min.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode3min = codecs.open(f".\khanh\code3min.py", "w", 'utf-8')
        filecode3min.write(code3_min)
        filecode3min_bat = codecs.open(f".\khanh\code3min.bat", "w", 'utf-8')
        filecode3min_bat.write(code3_min_bat)
        os.system("start cmd /c khanh\code3min.bat")
    elif (runter==4):
        code4='''print("")
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Đếm số lần xuất hiện của 1 chuỗi

a = []
answer = []
board = int(0)
number = str(input("Nhập chuỗi: "))

for i in range(0,len(number),1):
    if number[i] in a:
        continue
    temp=1
    dem=int(0)
    for j in range(0,len(number),1):
        if (number[i] == number[j]):
                dem += 1
    answer.append(str(number[i]) + ":" + str(dem))
    a.append(number[i])

answer.sort()
print("\\n============\\n")
print("Kết quả: ")

while (board != 3):
    for a in range(board,len(answer),3):
        print(answer[a],end="\\t")
    board += 1
    print(end="\\n")
        '''
        code4_bat='''@echo off
TITLE Bai 4 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code4.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode4 = codecs.open(f".\khanh\code4.py", "w", 'utf-8')
        filecode4.write(code4)
        filecode4_bat = codecs.open(f".\khanh\code4.bat", "w", 'utf-8')
        filecode4_bat.write(code4_bat)
        os.system("start cmd /c khanh\code4.bat")
    elif (runter==5):
        code5='''print("")
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Mã hóa 1 chuỗi string bằng base64

import base64

string = str(input("Nhập chuỗi: "))

string_encode = base64.b64encode(string.encode('utf-8',errors = 'strict')).decode("utf-8") 

print("\\n============")

print('\\nString đã được mã hóa:\\n' + str(string_encode))
        '''
        code5_bat='''@echo off
TITLE Bai 5 (Encode) - Python (KhanhNguyen9872)
color 17
cls
python khanh\code5.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode5 = codecs.open(f".\khanh\code5.py", "w", 'utf-8')
        filecode5.write(code5)
        filecode5_bat = codecs.open(f".\khanh\code5.bat", "w", 'utf-8')
        filecode5_bat.write(code5_bat)
        os.system("start cmd /c khanh\code5.bat")
    elif (runter=="5"):
        code5de='''print("")
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Giải mã 1 chuỗi string bị mã hóa do base64

import base64

string = str(input("Nhập chuỗi string bị mã hóa: "))

string_decode = base64.b64decode(string).decode("utf-8")

print("\\n============")

print('\\nString đã được giải mã:\\n' + str(string_decode))
        '''
        code5de_bat='''@echo off
TITLE Bai 5 (Decode) - Python (KhanhNguyen9872)
color 17
cls
python khanh\code5de.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode5de = codecs.open(f".\khanh\code5de.py", "w", 'utf-8')
        filecode5de.write(code5de)
        filecode5de_bat = codecs.open(f".\khanh\code5de.bat", "w", 'utf-8')
        filecode5de_bat.write(code5de_bat)
        os.system("start cmd /c khanh\code5de.bat")
    elif (runter==6):
        code6='''print("")
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Chuyển tiền USD -> VND

USD = input("Nhập số tiền USD: ")

VND = int(USD)*22645

print("\\n============\\n")

print(f"Số tiền VND:", VND, "VND")
        '''
        code6_bat='''@echo off
TITLE Bai 6 (USD -> VND) - Python (KhanhNguyen9872)
color 17
cls
python khanh\code6.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode6 = codecs.open(f".\khanh\code6.py", "w", 'utf-8')
        filecode6.write(code6)
        filecode6_bat = codecs.open(f".\khanh\code6.bat", "w", 'utf-8')
        filecode6_bat.write(code6_bat)
        os.system("start cmd /c khanh\code6.bat")
    elif (runter=="6"):
        code6o='''print("")
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Chuyển tiền VND -> USD

VND = input("Nhập số tiền VND: ")

USD = float(int(VND)/22645)

if (USD % 22645 == 0):
    USD = int(USD)
else:
    USD = float("{:.3f}".format(USD))

print("\\n============\\n")

print(f"Số tiền USD:", USD, "USD")
        '''
        code6o_bat='''@echo off
TITLE Bai 6 (VND -> USD) - Python (KhanhNguyen9872)
color 17
cls
python khanh\code6o.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode6o = codecs.open(f".\khanh\code6o.py", "w", 'utf-8')
        filecode6o.write(code6o)
        filecode6o_bat = codecs.open(f".\khanh\code6o.bat", "w", 'utf-8')
        filecode6o_bat.write(code6o_bat)
        os.system("start cmd /c khanh\code6o.bat")
    elif (runter==7):
        code7='''print("")
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Tìm số giai thừa

n = int(input("Nhập số n: "))
giai_thua = 1

if (n == 0) or (n == 1):
    giai_thua = 1
else:
    for a in range(2, n + 1):
        giai_thua = giai_thua * int(a)

print("\\n============\\n")

print("Giai thừa của " + str(n) + " là", giai_thua)
        '''
        code7_bat='''@echo off
TITLE Bai 7 (VND -> USD) - Python (KhanhNguyen9872)
color 17
cls
python khanh\code7.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode7 = codecs.open(f".\khanh\code7.py", "w", 'utf-8')
        filecode7.write(code7)
        filecode7_bat = codecs.open(f".\khanh\code7.bat", "w", 'utf-8')
        filecode7_bat.write(code7_bat)
        os.system("start cmd /c khanh\code7.bat")
    elif (runter==8):
        code8='''print("")
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

print("\\n============\\n")

print("ƯCLN của", a, "và", b, "là:", UCLN(a, b))
print("BCNN của", a, "và", b, "là:", BCNN(a, b))
        '''
        code8_bat='''@echo off
TITLE Bai 8 (VND -> USD) - Python (KhanhNguyen9872)
color 17
cls
python khanh\code8.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode8 = codecs.open(f".\khanh\code8.py", "w", 'utf-8')
        filecode8.write(code8)
        filecode8_bat = codecs.open(f".\khanh\code8.bat", "w", 'utf-8')
        filecode8_bat.write(code8_bat)
        os.system("start cmd /c khanh\code8.bat")

    elif (runter==9):
        code9='''print("")
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

print("\\n============\\n")

is_prime(n)
        '''
        code9_bat='''@echo off
TITLE Bai 9 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code9.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode9 = codecs.open(f".\khanh\code9.py", "w", 'utf-8')
        filecode9.write(code9)
        filecode9_bat = codecs.open(f".\khanh\code9.bat", "w", 'utf-8')
        filecode9_bat.write(code9_bat)
        os.system("start cmd /c khanh\code9.bat")

    elif (runter==10):
        code10='''print("")
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Tạo hình tam giác trong Terminal

def tamgiac(n):
    z = n - 1
    x = 1
    for i in range(n):
        print(' ' * z + '+' * x + ' ' * z)
        x += 2
        z -= 1

size = int(input("Nhập kích thước: "))

print("\\n============\\n")

tamgiac(size)
        '''
        code10_bat='''@echo off
TITLE Bai 10 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code10.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode10 = codecs.open(f".\khanh\code10.py", "w", 'utf-8')
        filecode10.write(code10)
        filecode10_bat = codecs.open(f".\khanh\code10.bat", "w", 'utf-8')
        filecode10_bat.write(code10_bat)
        os.system("start cmd /c khanh\code10.bat")
    elif (runter==11):
        code11='''print("")
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
colors =['red','green','yellow','gold','pink','cyan','white','orange',
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
        code11_bat='''@echo off
TITLE Bai 11 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code11.py
exit        
        '''
        filecode11 = codecs.open(f".\khanh\code11.py", "w", 'utf-8')
        filecode11.write(code11)
        filecode11_bat = codecs.open(f".\khanh\code11.bat", "w", 'utf-8')
        filecode11_bat.write(code11_bat)
        os.system("start cmd /c khanh\code11.bat")
    elif (runter==12):
        code12='''print("")
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Tìm ra chữ có 3 kí tự trở lên trong String

temp=[]
answer=[]

temp = input("Nhập string: ").split()

for a in temp:
    if (len(a)>3):
        answer.append(a)

print("\\n============\\n")

print(f"Kết quả:",answer)
        '''
        code12_bat='''@echo off
TITLE Bai 12 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code12.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode12 = codecs.open(f".\khanh\code12.py", "w", 'utf-8')
        filecode12.write(code12)
        filecode12_bat = codecs.open(f".\khanh\code12.bat", "w", 'utf-8')
        filecode12_bat.write(code12_bat)
        os.system("start cmd /c khanh\code12.bat")
    elif (runter==13):
        code13='''print("")
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

print("\\n============\\n")

print(f"Kết quả:",answer)
        '''
        code13_bat='''@echo off
TITLE Bai 13 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code13.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode13 = codecs.open(f".\khanh\code13.py", "w", 'utf-8')
        filecode13.write(code13)
        filecode13_bat = codecs.open(f".\khanh\code13.bat", "w", 'utf-8')
        filecode13_bat.write(code13_bat)
        os.system("start cmd /c khanh\code13.bat")
    elif (runter==14):
        code14='''print("")
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

print("\\n============\\n")

print(f"Kết quả:",luythua(a,b))
        '''
        code14_bat='''@echo off
TITLE Bai 14 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code14.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode14 = codecs.open(f".\khanh\code14.py", "w", 'utf-8')
        filecode14.write(code14)
        filecode14_bat = codecs.open(f".\khanh\code14.bat", "w", 'utf-8')
        filecode14_bat.write(code14_bat)
        os.system("start cmd /c khanh\code14.bat")
    elif (runter==15):
        code15='''print("")
# Code by Nguyễn Văn Khánh (KhanhNguyen9872)
# Kiểm tra tam giác vuông, đều, cân, tù, nhọn

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

print("\\n============\\n")

print(f"Kết quả:",kiemtra(a,b,c))
        '''
        code15_bat='''@echo off
TITLE Bai 15 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code15.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode15 = codecs.open(f".\khanh\code15.py", "w", 'utf-8')
        filecode15.write(code15)
        filecode15_bat = codecs.open(f".\khanh\code15.bat", "w", 'utf-8')
        filecode15_bat.write(code15_bat)
        os.system("start cmd /c khanh\code15.bat")

    elif (runter==16):
        code16='''print("")
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

print("\\n============\\n")

kiemtra(user_input)
        '''
        code16_bat='''@echo off
TITLE Bai 16 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code16.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode16 = codecs.open(f".\khanh\code16.py", "w", 'utf-8')
        filecode16.write(code16)
        filecode16_bat = codecs.open(f".\khanh\code16.bat", "w", 'utf-8')
        filecode16_bat.write(code16_bat)
        os.system("start cmd /c khanh\code16.bat")

    elif (runter==17):
        code17='''print("")
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

print("\\n============\\n")

inhoa_inthuong()
        '''
        code17_bat='''@echo off
TITLE Bai 17 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code17.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode17 = codecs.open(f".\khanh\code17.py", "w", 'utf-8')
        filecode17.write(code17)
        filecode17_bat = codecs.open(f".\khanh\code17.bat", "w", 'utf-8')
        filecode17_bat.write(code17_bat)
        os.system("start cmd /c khanh\code17.bat")
    
    elif (runter==18):
        code18='''print("")

        '''
        code18_bat='''@echo off
TITLE Bai 18 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code18.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode18 = codecs.open(f".\khanh\code18.py", "w", 'utf-8')
        filecode18.write(code18)
        filecode18_bat = codecs.open(f".\khanh\code18.bat", "w", 'utf-8')
        filecode18_bat.write(code18_bat)
        os.system("start cmd /c khanh\code18.bat")

    elif (runter==19):
        code19='''print("")

        '''
        code19_bat='''@echo off
TITLE Bai 19 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code19.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode19 = codecs.open(f".\khanh\code19.py", "w", 'utf-8')
        filecode19.write(code19)
        filecode19_bat = codecs.open(f".\khanh\code19.bat", "w", 'utf-8')
        filecode19_bat.write(code19_bat)
        os.system("start cmd /c khanh\code19.bat")

    elif (runter==20):
        code20='''print("")

        '''
        code20_bat='''@echo off
TITLE Bai 20 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code20.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode20 = codecs.open(f".\khanh\code20.py", "w", 'utf-8')
        filecode20.write(code20)
        filecode20_bat = codecs.open(f".\khanh\code20.bat", "w", 'utf-8')
        filecode20_bat.write(code20_bat)
        os.system("start cmd /c khanh\code20.bat")

    elif (runter==21):
        code21='''print("")

        '''
        code21_bat='''@echo off
TITLE Bai 21 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code21.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode21 = codecs.open(f".\khanh\code21.py", "w", 'utf-8')
        filecode21.write(code21)
        filecode21_bat = codecs.open(f".\khanh\code21.bat", "w", 'utf-8')
        filecode21_bat.write(code21_bat)
        os.system("start cmd /c khanh\code21.bat")

    elif (runter==22):
        code22='''print("")

        '''
        code22_bat='''@echo off
TITLE Bai 22 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code22.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode22 = codecs.open(f".\khanh\code22.py", "w", 'utf-8')
        filecode22.write(code22)
        filecode22_bat = codecs.open(f".\khanh\code22.bat", "w", 'utf-8')
        filecode22_bat.write(code22_bat)
        os.system("start cmd /c khanh\code22.bat")

    elif (runter==23):
        code23='''print("")

        '''
        code23_bat='''@echo off
TITLE Bai 23 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code23.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode23 = codecs.open(f".\khanh\code23.py", "w", 'utf-8')
        filecode23.write(code23)
        filecode23_bat = codecs.open(f".\khanh\code23.bat", "w", 'utf-8')
        filecode23_bat.write(code23_bat)
        os.system("start cmd /c khanh\code23.bat")

    elif (runter==24):
        code24='''print("")

        '''
        code24_bat='''@echo off
TITLE Bai 24 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code24.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode24 = codecs.open(f".\khanh\code24.py", "w", 'utf-8')
        filecode24.write(code24)
        filecode24_bat = codecs.open(f".\khanh\code24.bat", "w", 'utf-8')
        filecode24_bat.write(code24_bat)
        os.system("start cmd /c khanh\code24.bat")
    
    elif (runter==25):
        code25='''print("")

        '''
        code25_bat='''@echo off
TITLE Bai 25 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code25.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode25 = codecs.open(f".\khanh\code25.py", "w", 'utf-8')
        filecode25.write(code25)
        filecode25_bat = codecs.open(f".\khanh\code25.bat", "w", 'utf-8')
        filecode25_bat.write(code25_bat)
        os.system("start cmd /c khanh\code25.bat")

    elif (runter==26):
        code26='''print("")

        '''
        code26_bat='''@echo off
TITLE Bai 26 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code26.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode26 = codecs.open(f".\khanh\code26.py", "w", 'utf-8')
        filecode26.write(code26)
        filecode26_bat = codecs.open(f".\khanh\code26.bat", "w", 'utf-8')
        filecode26_bat.write(code26_bat)
        os.system("start cmd /c khanh\code26.bat")

    elif (runter==27):
        code27='''print("")

        '''
        code27_bat='''@echo off
TITLE Bai 27 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code27.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode27 = codecs.open(f".\khanh\code27.py", "w", 'utf-8')
        filecode27.write(code27)
        filecode27_bat = codecs.open(f".\khanh\code27.bat", "w", 'utf-8')
        filecode27_bat.write(code27_bat)
        os.system("start cmd /c khanh\code27.bat")

    elif (runter==28):
        code28='''print("")

        '''
        code28_bat='''@echo off
TITLE Bai 28 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code28.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode28 = codecs.open(f".\khanh\code28.py", "w", 'utf-8')
        filecode28.write(code28)
        filecode28_bat = codecs.open(f".\khanh\code28.bat", "w", 'utf-8')
        filecode28_bat.write(code28_bat)
        os.system("start cmd /c khanh\code28.bat")

    elif (runter==29):
        code29='''print("")

        '''
        code29_bat='''@echo off
TITLE Bai 29 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code29.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode29 = codecs.open(f".\khanh\code29.py", "w", 'utf-8')
        filecode29.write(code29)
        filecode29_bat = codecs.open(f".\khanh\code29.bat", "w", 'utf-8')
        filecode29_bat.write(code29_bat)
        os.system("start cmd /c khanh\code29.bat")

    elif (runter==30):
        code30='''print("")

        '''
        code30_bat='''@echo off
TITLE Bai 30 - Python (KhanhNguyen9872)
color 17
cls
python khanh\code30.py
pause > NUL
pause > NUL
pause > NUL
pause > NUL
exit        
        '''
        filecode30 = codecs.open(f".\khanh\code30.py", "w", 'utf-8')
        filecode30.write(code30)
        filecode30_bat = codecs.open(f".\khanh\code30.bat", "w", 'utf-8')
        filecode30_bat.write(code30_bat)
        os.system("start cmd /c khanh\code30.bat")













def giaiptbac2(*args):
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

def sourcecre(user):
    if (user==1):
        os.system('start "" "https://fb.me/trung10a4"')
    elif (user==2):
        pass

# Python Official Website
def pythonofficial(winver,winbit):
    maininstall = tkinter.Tk()
    maininstall.title(f'Install Python | Python (KhanhNguyen9872)')
    maininstall.iconbitmap('khanh.ico')
    maininstall.geometry("520x180")
    maininstall.resizable(False, False)
    textinstall = Text(maininstall)
    textinstall.insert(INSERT, "Detecting Windows...\n")
    if (winbit=="AMD64"):
        python_ver="-amd64"
        winbit="64"
    else:
        python_ver=""
        winbit="32"
    if (winver=="7"):
        file_name = "python_version.txt"
        url = "https://raw.githubusercontent.com/KhanhNguyen9872/python_exercises/main/python_version_win7.txt"
        urllib.request.urlretrieve(url, file_name)
        with open(f"{file_name}",'r',encoding='utf-8') as file_name0:
            pyver000=str(file_name0.read())
        textinstall.insert(INSERT, f"Found: Windows {winver} ({winbit}bit)\n\n")
        textinstall.insert(INSERT, f"Getting version....\n")
        textinstall.insert(INSERT, f"Found: {pyver000}\n")
    else:
        file_name = "python_version.txt"
        url = "https://raw.githubusercontent.com/KhanhNguyen9872/python_exercises/main/python_version.txt"
        urllib.request.urlretrieve(url, file_name)
        with open(f"{file_name}",'r',encoding='utf-8') as file_name0:
            pyver000=str(file_name0.read())
        textinstall.insert(INSERT, f"Found: Windows {winver} {winbit}bit\n\n")
        textinstall.insert(INSERT, f"Getting version....\n")
        textinstall.insert(INSERT, f"Found: {pyver000}\n")
        
    textinstall.insert(INSERT, f"\nDownloading Python v{pyver000}....\n")
    textinstall.insert(INSERT, f"Installing Python v{pyver000}....\n")
    textinstall.insert(INSERT, f"When the installation is completed! You can close this window!\n")
    textinstall.pack()
    url_python = str(f"https://www.python.org/ftp/python/{pyver000}/python-{pyver000}{python_ver}.exe")
    file_name_python = "khanh.exe"
    urllib.request.urlretrieve(url_python, file_name_python)
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
    """
    os.system('move khanh.exe khanh\khanh.exe')
    pythoninstall00 = codecs.open(f".\khanh\khanh.bat", "w", 'utf-8')
    pythoninstall00.write(slient_cmd00)
    pythoninstall00.close()
    os.system("start cmd /c khanh\khanh.bat")
    time.sleep(2)
    file_name0.close()
    os.remove(f'{file_name}')
    maininstall.mainloop()
    time.sleep(0)
    exit()

# Restart popup
def close_popup():
    mainlanguagerestart = tkinter.Tk()
    mainlanguagerestart.title(f'Restart Application | Python (KhanhNguyen9872)')
    mainlanguagerestart.iconbitmap('khanh.ico')
    mainlanguagerestart.geometry("400x60")
    mainlanguagerestart.resizable(False, False)
    Label(mainlanguagerestart, text="This change requires a restart of the application!", font=('BOLD')).grid(row=0, sticky=W)
    CONFIRM1 = Button(mainlanguagerestart, text="  Close program  ", command=close_process).grid(row=1, column=0, sticky=W)
    mainlanguagerestart.mainloop()

# Python Shell on CMD
def pythonshell():
    os.system("start cmd /c python")

# Control Panel
def controlpanel():
    os.system("start cmd /c control")

# Change language
def change_language(language):
    if (language=="Vietnamese"):
        os.remove('language\\vi-VN.khanh')
        english_lan = codecs.open(f"language\\en-US.khanh", "w", 'utf-8')
        english_lan.write("khanhnguyen9872")
        english_lan.close()
        close_popup()
        language=str("English")
        return language

    elif (language=="English"):
        os.remove('language\\en-US.khanh')
        vietnamese_lan = codecs.open(f"language\\vi-VN.khanh", "w", 'utf-8')
        vietnamese_lan.write("khanhnguyen9872")
        vietnamese_lan.close()
        close_popup()
        language=str("Vietnamese")
        return language

## Check python version
text = Text(main)
text.insert(INSERT, " * Program logs:\nInitializing program....\nCleanup TEMP folder.... Done\n\n")
passpy=0

# Create/Set TEMP folder
os.system('rmdir /q /s khanh > NUL')
os.system('mkdir khanh > NUL')
temp_folder = Path("khanh")

####
windows_bit = str(struct.calcsize("P")*8)
windows_release = str(platform.release())
windows_machine = str(platform.machine())
if (windows_machine=="AMD64"):
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

for pythonversion in range(0,50):
    pythonfile = Path(str(khanhlocal) + "\Programs\Python\Python3" + str(pythonversion) + "\python.exe")
    if pythonfile.is_file():
        pyver = str(pythonversion)
        text.pack()
        python00.append(pythonversion)
        passpy=1
        break
    else:
        continue

if (passpy==0):
    for pythonversion in range(0,50):
        pythonfile = Path(str(khanhlocal1) + "\Python3" + str(pythonversion) + "\python.exe")
        if pythonfile.is_file():
            pyver = str(pythonversion)
            text.pack()
            python00.append(pythonversion)
            passpy=1
            break
        else:
            continue

    if (passpy!=0):
        for pythonversion in range(0,50):
            if (pythonversion in python00):
                continue
            else:
                pythonfile = Path(str(khanhlocal1) + "\Python3" + str(pythonversion) + "\python.exe")
                if pythonfile.is_file():
                    pyver2 = str(pythonversion)
                    text.pack()
                    python00.append(pythonversion)
                    break
                else:
                    continue

if (passpy==0):
    for pythonversion in range(0,50):
        pythonfile = Path(str(khanhlocal2) + "\Python3" + str(pythonversion) + "\python.exe")
        if pythonfile.is_file():
            pyver = str(pythonversion)
            text.pack()
            python00.append(pythonversion)
            passpy=1
            break
        else:
            continue

    if (passpy!=0):
        for pythonversion in range(0,50):
            if (pythonversion in python00):
                continue
            else:
                pythonfile = Path(str(khanhlocal2) + "\Python3" + str(pythonversion) + "\python.exe")
                if pythonfile.is_file():
                    pyver2 = str(pythonversion)
                    text.pack()
                    python00.append(pythonversion)
                    break
                else:
                    continue

if (passpy==0):
    for pythonversion in range(0,50):
        pythonfile = Path("C:\Program Files\Python3" + str(pythonversion) + "\python.exe")
        if pythonfile.is_file():
            pyver = str(pythonversion)
            text.pack()
            python00.append(pythonversion)
            passpy=1
            break
        else:
            continue

    if (passpy!=0):
        for pythonversion in range(0,50):
            if (pythonversion in python00):
                continue
            else:
                pythonfile = Path("C:\Program Files\Python3" + str(pythonversion) + "\python.exe")
                if pythonfile.is_file():
                    pyver2 = str(pythonversion)
                    text.pack()
                    python00.append(pythonversion)
                    break
                else:
                    continue

if (passpy!=0):
    for pythonversion in range(0,50):
        if (pythonversion in python00):
            continue
        else:
            pythonfile = Path(str(khanhlocal) + "\Programs\Python\Python3" + str(pythonversion) + "\python.exe")
            if pythonfile.is_file():
                pyver2 = str(pythonversion)
                text.pack()
                python00.append(pythonversion)
                break
            else:
                continue

if (passpy==0):
    for pythonversion in range(0,50):
        pythonfile = Path(str(khanhlocal) + "\Programs\Python\Python3" + str(pythonversion) + "-32\python.exe")
        if pythonfile.is_file():
            pyver = str(pythonversion)
            text.pack()
            python00.append(pythonversion)
            amd64_or_32=1
            passpy=1
            break
        else:
            continue

    if (passpy!=0):
        for pythonversion in range(0,50):
            if (pythonversion in python00):
                continue
            else:
                pythonfile = Path(str(khanhlocal) + "\Programs\Python\Python3" + str(pythonversion) + "-32\python.exe")
                if pythonfile.is_file():
                    pyver2 = str(pythonversion)
                    text.pack()
                    python00.append(pythonversion)
                    amd64_or_32=1
                    break
                else:
                    continue

if (amd64_or_32==0):
    python_win = "win64"
    python_win1 = "AMD64"
else:
    python_win = "win32"
    python_win1 = "i686"

if (len(python00)==2):
    text.insert(INSERT, f"Detected: Python 3.{pyver} and Python 3.{pyver2} is installed!\n")
    if (int(pyver)>int(pyver2)):
        text.insert(INSERT, f" ! Please remove Python v3.{pyver2}!\n")
        pyver0=str(f'v3.{pyver}')
    else:
        text.insert(INSERT, f" ! Please remove Python v3.{pyver}!\n")
        pyver0=str(f'v3.{pyver2}')
elif (len(python00)==1):
    text.insert(INSERT, "Detected: Python v3." + str(pyver) + " (" + str(python_win) + ")\n")
    pyver0=str(f'v3.{pyver}')

if (passpy==0):
    text.insert(INSERT, " ! No Python3 is installed!\n ! Please install Python first", END, "")
    Dpy = Button(main, text = "Install Python", command = lambda: pythonofficial(windows_release,windows_machine))
    Dpy.pack(side=BOTTOM)
    text.pack()
    time.sleep(0)
    main.mainloop()
else:
    if (int(pyver)<8):
        text.insert(INSERT, " ! Python3 too old!\n ! Please update to latest Python3 offical!")
        Bpy = Button(main, text = "Update Python", command = lambda: pythonofficial(windows_release,windows_machine))

if (amd64_or_32==1) and (python_win1!=windows_machine):
    text.insert(INSERT, "\nWARNING: You are using 32bit Python on 64bit Windows!\n         Recommend using Python 64bit")

text.insert(INSERT, "\n\nClose this window to start Program!")
text.pack()
main.mainloop()

###############
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
###############

def get_number(a):
    print(a.widget.get())

def change_showcode():
    showcode_app_select = filedialog.askopenfilename(initialdir = "C:/Program Files", title = "Show Code Application", filetypes = (("Execute Application","*.exe"), ))
    if (showcode_app_select==""):
        pass
    else:
        os.system('mkdir settings > NUL')
        showcode_app = str("")
        len_showcodesettings = "-" + str(len(showcode_app_select)+1)
        for s in range(-1,int(len_showcodesettings),-1):
            if (showcode_app_select[int(s)]) == str(f"/") or (showcode_app_select[int(s)]) == str(f"\\"):
                showcodemain = codecs.open(f".\settings\showcode.ini", "w", 'utf-8')
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
    menunum=int(E1.get())
    if (menunum>int(total)):
        mainerror = tkinter.Tk()
        mainerror.title(f'Error | Python {pyver0} (KhanhNguyen9872)')
        mainerror.iconbitmap('khanh.ico')
        mainerror.geometry("350x50")
        mainerror.resizable(False, False)
        texterror = Text(mainerror)
        texterror.insert(INSERT, f"Bạn đã chọn vượt quá danh sách đang có!\n      Tối đa: 0-{total}")
        texterror.pack()
        mainerror.mainloop()
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
                    os.remove('settings\\showcode.ini')
                    mainshowcodeini = tkinter.Tk()
                    mainshowcodeini.title(f'Settings ERROR | Python (KhanhNguyen9872)')
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
            os.system('mkdir settings > NUL')
            showcode_app_select = str(f"{WINDOWS_DIRECTORY}\\notepad.exe")
            showcodemain = codecs.open(f".\settings\showcode.ini", "w", 'utf-8')
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
                    os.remove('settings\\showcode.ini')
                    mainshowcodeini = tkinter.Tk()
                    mainshowcodeini.title(f'Settings ERROR | Python (KhanhNguyen9872)')
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

        name_showcode_app = str(showcode_app[-1] + showcode_app [-2] + showcode_app [-3] + showcode_app [-4])
        name_showcode_app = str(''.join(reversed(name_showcode_app)))
        if (name_showcode_app!=".exe"):
            os.system('mkdir settings > NUL')
            showcode_app_select = str(f"{WINDOWS_DIRECTORY}\\notepad.exe")
            showcode_app = str("")
            len_showcodesettings = "-" + str(len(showcode_app_select)+1)
            for s in range(-1,int(len_showcodesettings),-1):
                if (showcode_app_select[int(s)]) == str(f"/") or (showcode_app_select[int(s)]) == str(f"\\"):
                    showcodemain = codecs.open(f".\settings\showcode.ini", "w", 'utf-8')
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
                    os.remove('settings\\showcode.ini')
                    mainshowcodeini = tkinter.Tk()
                    mainshowcodeini.title(f'Settings ERROR | Python (KhanhNguyen9872)')
                    mainshowcodeini.iconbitmap('khanh.ico')
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
        main001.title(f'Settings | Python {pyver0} (KhanhNguyen9872)')
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
        main0.title(f'About | Python {pyver0} (KhanhNguyen9872)')
        main0.iconbitmap('khanh.ico')
        main0.geometry("500x120")
        main0.resizable(False, False)
        text0 = Text(main0)
        text0.insert(INSERT, f"Name: Nguyễn Văn Khánh\nFacebook: https://fb.me/khanh10a1\nYoutube: https://youtube.com/c/KhanhNguyen9872_Official\nGithub: https://github.com/khanhnguyen9872\nZalo: 0937927513\nPhone: +84937927513\nGenshin UID: 800983609")
        text0.pack()
        text0.config(state=DISABLED)
        main0.mainloop()
    elif (menunum==1):
        main01 = tkinter.Tk()
        main01.title(f'Bài 1 | Python {pyver0} (KhanhNguyen9872)')
        main01.iconbitmap('khanh.ico')
        main01.geometry("320x180")
        main01.resizable(False, False)
        Label(main01, text="Giải phương trình bậc 2", font=('BOLD')).grid(row=0, sticky=W)
        Label(main01, text="CT: ax^2+bx+c=0").grid(row=1, sticky=W)
        Label(main01, text="Nhập a: ").grid(row=2, sticky=W)
        Entry(main01, textvariable='a').grid(row=2, column=1, sticky=E)
        Label(main01, text="Nhập b: ").grid(row=3, sticky=W)
        Entry(main01, textvariable='b').grid(row=3, column=1, sticky=E)
        Label(main01, text="Nhập c: ").grid(row=4, sticky=W)
        Entry(main01, textvariable='c').grid(row=4, column=1, sticky=E)
        CONFIRM = Button(main01, text="  Giải  ", command=lambda: giaiptbac2()).grid(row=5, column=1, sticky=W)
        SHOW = Button(main01, text="Show Code", command=lambda: showcode(int(menunum),0)).grid(row=5, column=0, sticky=W)
        SHOWAPP = Button(main01, text="Show Code as Application", command=lambda: showcode(int(menunum),1)).grid(row=6, column=0, sticky=W)
        RUN_ON_TERMINAL = Button(main01, text="Run as Terminal", command=lambda: runterminal(int(menunum))).grid(row=6, column=1, sticky=W)

        ############################## (NOT COMPLETED) ##############################

        main01.mainloop()
    elif (menunum==2):
        main2 = tkinter.Tk()
        main2.title(f'Bài 2 | Python {pyver0} (KhanhNguyen9872)')
        main2.iconbitmap('khanh.ico')
        main2.geometry("300x240")
        main2.resizable(False, False)
        text2 = Text(main2)
        Label(main2, text="Tìm số lớn nhất", font=('BOLD')).grid(row=0, sticky=W)
        Label(main2, text="VD: [3,4,5,6,7,8]  ->  8").grid(row=1, sticky=W)
        SHOW = Button(main2, text="Show Code", command=lambda: showcode(int(menunum),0)).grid(row=2, column=0, sticky=W)
        SHOWAPP = Button(main2, text="Show Code as Application", command=lambda: showcode(int(menunum),1)).grid(row=3, column=0, sticky=W)
        Label(main2, text="").grid(row=2, column=1, sticky=W)
        RUN_ON_TERMINAL = Button(main2, text="Run as Terminal", command=lambda: runterminal(int(menunum))).grid(row=2, column=2, sticky=W)
        Label(main2, text="").grid(row=4, sticky=W)
        Label(main2, text="Tìm số bé nhất", font=('BOLD')).grid(row=5, sticky=W)
        Label(main2, text="VD: [3,4,5,6,7,8]  ->  3").grid(row=6, sticky=W)
        SHOW = Button(main2, text="Show Code", command=lambda: showcode(str(menunum),0)).grid(row=7, column=0, sticky=W)
        SHOWAPP = Button(main2, text="Show Code as Application", command=lambda: showcode(str(menunum),1)).grid(row=8, column=0, sticky=W)
        Label(main2, text="").grid(row=7, column=1, sticky=W)
        RUN_ON_TERMINAL = Button(main2, text="Run as Terminal", command=lambda: runterminal(str(menunum))).grid(row=7, column=2, sticky=W)
        Label(main2, text="").grid(row=9, sticky=W)
        text2.pack()
    elif (menunum==3):
        main3 = tkinter.Tk()
        main3.title(f'Bài 3 | Python {pyver0} (KhanhNguyen9872)')
        main3.iconbitmap('khanh.ico')
        main3.geometry("320x240")
        main3.resizable(False, False)
        text3 = Text(main3)
        Label(main3, text="Sắp xếp từ bé đến lớn", font=('BOLD')).grid(row=0, sticky=W)
        Label(main3, text="VD: [2,6,3,1,5]  ->  1, 2, 3, 5, 6").grid(row=1, sticky=W)
        SHOW = Button(main3, text="Show Code", command=lambda: showcode(int(menunum),0)).grid(row=2, column=0, sticky=W)
        SHOWAPP = Button(main3, text="Show Code as Application", command=lambda: showcode(int(menunum),1)).grid(row=3, column=0, sticky=W)
        Label(main3, text="").grid(row=2, column=1, sticky=W)
        RUN_ON_TERMINAL = Button(main3, text="Run as Terminal", command=lambda: runterminal(int(menunum))).grid(row=2, column=2, sticky=W)
        Label(main3, text="").grid(row=4, sticky=W)
        Label(main3, text="Sắp xếp từ lớn đến bé", font=('BOLD')).grid(row=5, sticky=W)
        Label(main3, text="VD: [2,6,3,1,5]  ->  6, 5, 3, 2, 1").grid(row=6, sticky=W)
        SHOW = Button(main3, text="Show Code", command=lambda: showcode(str(menunum),0)).grid(row=7, column=0, sticky=W)
        SHOWAPP = Button(main3, text="Show Code as Application", command=lambda: showcode(str(menunum),1)).grid(row=8, column=0, sticky=W)
        Label(main3, text="").grid(row=7, column=1, sticky=W)
        RUN_ON_TERMINAL = Button(main3, text="Run as Terminal", command=lambda: runterminal(str(menunum))).grid(row=7, column=2, sticky=W)
        Label(main3, text="").grid(row=9, sticky=W)
        text3.pack()
    elif (menunum==4):
        main4 = tkinter.Tk()
        main4.title(f'Bài 4 | Python {pyver0} (KhanhNguyen9872)')
        main4.iconbitmap('khanh.ico')
        main4.geometry("360x140")
        main4.resizable(False, False)
        text4 = Text(main4)
        Label(main4, text="Đếm số lần xuất hiện từ 1 chuỗi", font=('BOLD')).grid(row=0, sticky=W)
        Label(main4, text="VD: 'aabbbcd'  ->  a:2, b:3, c:1, d:1").grid(row=1, sticky=W)
        SHOW = Button(main4, text="Show Code", command=lambda: showcode(int(menunum),0)).grid(row=2, column=0, sticky=W)
        SHOWAPP = Button(main4, text="Show Code as Application", command=lambda: showcode(int(menunum),1)).grid(row=3, column=0, sticky=W)
        Label(main4, text="").grid(row=2, column=1, sticky=W)
        RUN_ON_TERMINAL = Button(main4, text="Run as Terminal", command=lambda: runterminal(int(menunum))).grid(row=2, column=2, sticky=W)
        Label(main4, text="").grid(row=4, sticky=W)
        text4.pack()
    elif (menunum==5):
        main5 = tkinter.Tk()
        main5.title(f'Bài 5 | Python {pyver0} (KhanhNguyen9872)')
        main5.iconbitmap('khanh.ico')
        main5.geometry("360x240")
        main5.resizable(False, False)
        text5 = Text(main5)
        Label(main5, text="Mã hóa bằng base64", font=('BOLD')).grid(row=0, sticky=W)
        Label(main5, text="VD: 'khanh'  ->  'a2hhbmg='").grid(row=1, sticky=W)
        SHOW = Button(main5, text="Show Code", command=lambda: showcode(int(menunum),0)).grid(row=2, column=0, sticky=W)
        SHOWAPP = Button(main5, text="Show Code as Application", command=lambda: showcode(int(menunum),1)).grid(row=3, column=0, sticky=W)
        Label(main5, text="").grid(row=2, column=1, sticky=W)
        RUN_ON_TERMINAL = Button(main5, text="Run as Terminal", command=lambda: runterminal(int(menunum))).grid(row=2, column=2, sticky=W)
        Label(main5, text="").grid(row=4, sticky=W)
        Label(main5, text="Giải mã bằng base64", font=('BOLD')).grid(row=5, sticky=W)
        Label(main5, text="VD: 'a2hhbmg='  ->  'khanh'").grid(row=6, sticky=W)
        SHOW = Button(main5, text="Show Code", command=lambda: showcode(str(menunum),0)).grid(row=7, column=0, sticky=W)
        SHOWAPP = Button(main5, text="Show Code as Application", command=lambda: showcode(str(menunum),1)).grid(row=8, column=0, sticky=W)
        Label(main5, text="").grid(row=7, column=1, sticky=W)
        RUN_ON_TERMINAL = Button(main5, text="Run as Terminal", command=lambda: runterminal(str(menunum))).grid(row=7, column=2, sticky=W)
        Label(main5, text="").grid(row=9, sticky=W)
        text5.pack()
    elif (menunum==6):
        main6 = tkinter.Tk()
        main6.title(f'Bài 6 | Python {pyver0} (KhanhNguyen9872)')
        main6.iconbitmap('khanh.ico')
        main6.geometry("360x240")
        main6.resizable(False, False)
        text6 = Text(main6)
        Label(main6, text="Chuyển tiền USD -> VND", font=('BOLD')).grid(row=0, sticky=W)
        Label(main6, text="VD: 4 USD  ->  90580 VND").grid(row=1, sticky=W)
        SHOW = Button(main6, text="Show Code", command=lambda: showcode(int(menunum),0)).grid(row=2, column=0, sticky=W)
        SHOWAPP = Button(main6, text="Show Code as Application", command=lambda: showcode(int(menunum),1)).grid(row=3, column=0, sticky=W)
        Label(main6, text="").grid(row=2, column=1, sticky=W)
        RUN_ON_TERMINAL = Button(main6, text="Run as Terminal", command=lambda: runterminal(int(menunum))).grid(row=2, column=2, sticky=W)
        Label(main6, text="").grid(row=4, sticky=W)
        Label(main6, text="Chuyển tiền VND -> USD", font=('BOLD')).grid(row=5, sticky=W)
        Label(main6, text="VD: 90580 VND  ->  4 USD").grid(row=6, sticky=W)
        SHOW = Button(main6, text="Show Code", command=lambda: showcode(str(menunum),0)).grid(row=7, column=0, sticky=W)
        SHOWAPP = Button(main6, text="Show Code as Application", command=lambda: showcode(str(menunum),1)).grid(row=8, column=0, sticky=W)
        Label(main6, text="").grid(row=7, column=1, sticky=W)
        RUN_ON_TERMINAL = Button(main6, text="Run as Terminal", command=lambda: runterminal(str(menunum))).grid(row=7, column=2, sticky=W)
        Label(main6, text="").grid(row=9, sticky=W)
        text6.pack()
    elif (menunum==7):
        main7 = tkinter.Tk()
        main7.title(f'Bài 7 | Python {pyver0} (KhanhNguyen9872)')
        main7.iconbitmap('khanh.ico')
        main7.geometry("360x140")
        main7.resizable(False, False)
        text7 = Text(main7)
        Label(main7, text="Tìm số giai thừa", font=('BOLD')).grid(row=0, sticky=W)
        Label(main7, text="").grid(row=1, sticky=W)
        SHOW = Button(main7, text="Show Code", command=lambda: showcode(int(menunum),0)).grid(row=2, column=0, sticky=W)
        SHOWAPP = Button(main7, text="Show Code as Application", command=lambda: showcode(int(menunum),1)).grid(row=3, column=0, sticky=W)
        Label(main7, text="").grid(row=2, column=1, sticky=W)
        RUN_ON_TERMINAL = Button(main7, text="Run as Terminal", command=lambda: runterminal(int(menunum))).grid(row=2, column=2, sticky=W)
        Label(main7, text="").grid(row=4, sticky=W)
        text7.pack()
    elif (menunum==8):
        main8 = tkinter.Tk()
        main8.title(f'Bài 8 | Python {pyver0} (KhanhNguyen9872)')
        main8.iconbitmap('khanh.ico')
        main8.geometry("360x140")
        main8.resizable(False, False)
        text8 = Text(main8)
        Label(main8, text="Tìm ƯCLN và BCNN", font=('BOLD')).grid(row=0, sticky=W)
        Label(main8, text="").grid(row=1, sticky=W)
        SHOW = Button(main8, text="Show Code", command=lambda: showcode(int(menunum),0)).grid(row=2, column=0, sticky=W)
        SHOWAPP = Button(main8, text="Show Code as Application", command=lambda: showcode(int(menunum),1)).grid(row=3, column=0, sticky=W)
        Label(main8, text="").grid(row=2, column=1, sticky=W)
        RUN_ON_TERMINAL = Button(main8, text="Run as Terminal", command=lambda: runterminal(int(menunum))).grid(row=2, column=2, sticky=W)
        Label(main8, text="").grid(row=4, sticky=W)
        text8.pack()
    elif (menunum==9):
        main9 = tkinter.Tk()
        main9.title(f'Bài 9 | Python {pyver0} (KhanhNguyen9872)')
        main9.iconbitmap('khanh.ico')
        main9.geometry("360x140")
        main9.resizable(False, False)
        text9 = Text(main9)
        Label(main9, text="Kiểm tra số nguyên tố", font=('BOLD')).grid(row=0, sticky=W)
        Label(main9, text="").grid(row=1, sticky=W)
        SHOW = Button(main9, text="Show Code", command=lambda: showcode(int(menunum),0)).grid(row=2, column=0, sticky=W)
        SHOWAPP = Button(main9, text="Show Code as Application", command=lambda: showcode(int(menunum),1)).grid(row=3, column=0, sticky=W)
        Label(main9, text="").grid(row=2, column=1, sticky=W)
        RUN_ON_TERMINAL = Button(main9, text="Run as Terminal", command=lambda: runterminal(int(menunum))).grid(row=2, column=2, sticky=W)
        Label(main9, text="").grid(row=4, sticky=W)
        text9.pack()
    elif (menunum==10):
        main10 = tkinter.Tk()
        main10.title(f'Bài 10 | Python {pyver0} (KhanhNguyen9872)')
        main10.iconbitmap('khanh.ico')
        main10.geometry("360x140")
        main10.resizable(False, False)
        text10 = Text(main10)
        Label(main10, text="Tạo hình tam giác trong Terminal", font=('BOLD')).grid(row=0, sticky=W)
        Label(main10, text="").grid(row=1, sticky=W)
        SHOW = Button(main10, text="Show Code", command=lambda: showcode(int(menunum),0)).grid(row=2, column=0, sticky=W)
        SHOWAPP = Button(main10, text="Show Code as Application", command=lambda: showcode(int(menunum),1)).grid(row=3, column=0, sticky=W)
        Label(main10, text="").grid(row=2, column=1, sticky=W)
        RUN_ON_TERMINAL = Button(main10, text="Run as Terminal", command=lambda: runterminal(int(menunum))).grid(row=2, column=2, sticky=W)
        Label(main10, text="").grid(row=4, sticky=W)
        text10.pack()
    elif (menunum==11):
        main11 = tkinter.Tk()
        main11.title(f'Bài 11 | Python {pyver0} (KhanhNguyen9872)')
        main11.iconbitmap('khanh.ico')
        main11.geometry("400x140")
        main11.resizable(False, False)
        text11 = Text(main11)
        Label(main11, text="Pháo hoa trên bằng Turtle", font=('BOLD')).grid(row=0, sticky=W)
        Label(main11, text="   --Source: Lã Thành Trung--").grid(row=1, sticky=W)
        SHOW = Button(main11, text="Show Code", command=lambda: showcode(int(menunum),0)).grid(row=2, column=0, sticky=W)
        SHOWAPP = Button(main11, text="Show Code as Application", command=lambda: showcode(int(menunum),1)).grid(row=3, column=0, sticky=W)
        Label(main11, text="").grid(row=2, column=1, sticky=W)
        RUN_ON_TERMINAL = Button(main11, text="Run as Terminal", command=lambda: runterminal(int(menunum))).grid(row=2, column=2, sticky=W)
        SOURCEBY = Button(main11, text="Lã Thành Trung", command=lambda: sourcecre(int(1))).grid(row=3, column=2, sticky=W)
        Label(main11, text="").grid(row=4, sticky=W)
        text11.pack()
    elif (menunum==12):
        main12 = tkinter.Tk()
        main12.title(f'Bài 12 | Python {pyver0} (KhanhNguyen9872)')
        main12.iconbitmap('khanh.ico')
        main12.geometry("360x140")
        main12.resizable(False, False)
        text12 = Text(main12)
        Label(main12, text="Tìm ra chữ có 3 kí tự trở lên", font=('BOLD')).grid(row=0, sticky=W)
        Label(main12, text="").grid(row=1, sticky=W)
        SHOW = Button(main12, text="Show Code", command=lambda: showcode(int(menunum),0)).grid(row=2, column=0, sticky=W)
        SHOWAPP = Button(main12, text="Show Code as Application", command=lambda: showcode(int(menunum),1)).grid(row=3, column=0, sticky=W)
        Label(main12, text="").grid(row=2, column=1, sticky=W)
        RUN_ON_TERMINAL = Button(main12, text="Run as Terminal", command=lambda: runterminal(int(menunum))).grid(row=2, column=2, sticky=W)
        Label(main12, text="").grid(row=4, sticky=W)
        text12.pack()
    elif (menunum==13):
        main13 = tkinter.Tk()
        main13.title(f'Bài 13 | Python {pyver0} (KhanhNguyen9872)')
        main13.iconbitmap('khanh.ico')
        main13.geometry("360x140")
        main13.resizable(False, False)
        text13 = Text(main13)
        Label(main13, text="Tính tổng các ước số của N", font=('BOLD')).grid(row=0, sticky=W)
        Label(main13, text="(không bao gồm N)", font=('BOLD')).grid(row=0, column=2, sticky=W)
        Label(main13, text="").grid(row=1, sticky=W)
        SHOW = Button(main13, text="Show Code", command=lambda: showcode(int(menunum),0)).grid(row=2, column=0, sticky=W)
        SHOWAPP = Button(main13, text="Show Code as Application", command=lambda: showcode(int(menunum),1)).grid(row=3, column=0, sticky=W)
        Label(main13, text="").grid(row=2, column=1, sticky=W)
        RUN_ON_TERMINAL = Button(main13, text="Run as Terminal", command=lambda: runterminal(int(menunum))).grid(row=2, column=2, sticky=W)
        Label(main13, text="").grid(row=4, sticky=W)
        text13.pack()
    elif (menunum==14):
        main14 = tkinter.Tk()
        main14.title(f'Bài 14 | Python {pyver0} (KhanhNguyen9872)')
        main14.iconbitmap('khanh.ico')
        main14.geometry("360x140")
        main14.resizable(False, False)
        text14 = Text(main14)
        Label(main14, text="Tính lũy thừa a^b bằng pow()", font=('BOLD')).grid(row=0, sticky=W)
        Label(main14, text="").grid(row=1, sticky=W)
        SHOW = Button(main14, text="Show Code", command=lambda: showcode(int(menunum),0)).grid(row=2, column=0, sticky=W)
        SHOWAPP = Button(main14, text="Show Code as Application", command=lambda: showcode(int(menunum),1)).grid(row=3, column=0, sticky=W)
        Label(main14, text="").grid(row=2, column=1, sticky=W)
        RUN_ON_TERMINAL = Button(main14, text="Run as Terminal", command=lambda: runterminal(int(mennum))).grid(row=2, column=2, sticky=W)
        Label(main14, text="").grid(row=4, sticky=W)
        text14.pack()
    elif (menunum==15):
        main15 = tkinter.Tk()
        main15.title(f'Bài 15 | Python {pyver0} (KhanhNguyen9872)')
        main15.iconbitmap('khanh.ico')
        main15.geometry("360x140")
        main15.resizable(False, False)
        text15 = Text(main15)
        Label(main15, text="Kiểm tra là tam giác vuông, đều", font=('BOLD')).grid(row=0, sticky=W)
        Label(main15, text=", cân, tù hay nhọn", font=('BOLD')).grid(row=0, column=2, sticky=W)
        Label(main15, text="VD: a=3, b=4, c=5  ->  'Tam giác vuông'").grid(row=1, sticky=W)
        SHOW = Button(main15, text="Show Code", command=lambda: showcode(int(menunum),0)).grid(row=2, column=0, sticky=W)
        SHOWAPP = Button(main15, text="Show Code as Application", command=lambda: showcode(int(menunum),1)).grid(row=3, column=0, sticky=W)
        Label(main15, text="").grid(row=2, column=1, sticky=W)
        RUN_ON_TERMINAL = Button(main15, text="Run as Terminal", command=lambda: runterminal(int(menunum))).grid(row=2, column=2, sticky=W)
        Label(main15, text="").grid(row=4, sticky=W)
        text15.pack()
    elif (menunum==16):
        main16 = tkinter.Tk()
        main16.title(f'Bài 16 | Python {pyver0} (KhanhNguyen9872)')
        main16.iconbitmap('khanh.ico')
        main16.geometry("360x140")
        main16.resizable(False, False)
        text16 = Text(main16)
        Label(main16, text="Tìm ra các số chẵn, lẻ", font=('BOLD')).grid(row=0, sticky=W)
        Label(main16, text="(Có lượt bỏ kí tự)", font=('BOLD')).grid(row=0, column=2, sticky=W)
        Label(main16, text="VD: [3,4,6,a,9]  ->  Chẵn: 4,6 | Lẻ: 3, 9").grid(row=1, sticky=W)
        SHOW = Button(main16, text="Show Code", command=lambda: showcode(int(menunum),0)).grid(row=2, column=0, sticky=W)
        SHOWAPP = Button(main16, text="Show Code as Application", command=lambda: showcode(int(menunum),1)).grid(row=3, column=0, sticky=W)
        Label(main16, text="").grid(row=2, column=1, sticky=W)
        RUN_ON_TERMINAL = Button(main16, text="Run as Terminal", command=lambda: runterminal(int(menunum))).grid(row=2, column=2, sticky=W)
        Label(main16, text="").grid(row=4, sticky=W)
        text16.pack()
    elif (menunum==17):
        main17 = tkinter.Tk()
        main17.title(f'Bài 17 | Python {pyver0} (KhanhNguyen9872)')
        main17.iconbitmap('khanh.ico')
        main17.geometry("400x140")
        main17.resizable(False, False)
        text17 = Text(main17)
        Label(main17, text="Đếm kí tự In hoa, thường", font=('BOLD')).grid(row=0, sticky=W)
        Label(main17, text="(Không bao gồm số)", font=('BOLD')).grid(row=0, column=2, sticky=W)
        Label(main17, text="VD: 'Khanh9872'  ->  In hoa: 1 | In thường: 4").grid(row=1, sticky=W)
        SHOW = Button(main17, text="Show Code", command=lambda: showcode(int(menunum),0)).grid(row=2, column=0, sticky=W)
        SHOWAPP = Button(main17, text="Show Code as Application", command=lambda: showcode(int(menunum),1)).grid(row=3, column=0, sticky=W)
        Label(main17, text="").grid(row=2, column=1, sticky=W)
        RUN_ON_TERMINAL = Button(main17, text="Run as Terminal", command=lambda: runterminal(int(menunum))).grid(row=2, column=2, sticky=W)
        Label(main17, text="").grid(row=4, sticky=W)
        text17.pack()
### MAIN
main1 = tkinter.Tk()
main1.title(f'Menu | Python {pyver0} (KhanhNguyen9872)')
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




















