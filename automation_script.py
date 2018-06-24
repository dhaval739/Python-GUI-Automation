import pyautogui, time
import csv
from tkinter import *
import cv2
import numpy as np
import pytesseract
from PIL import Image
import re
from selenium import webdriver 

#path to chrome driver
chrome_path= "D:/pyautomation/chromedriver.exe"

#path to pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

def add_cont(str):
        
    if(str=='em'):
        appn='Em '
        if(w1.get()==""):
            inputfile = csv.reader(open('contact.csv','r'))
        else:
            path=w1.get()
            inputfile = csv.reader(open(path,'r'))
    else:
        appn='E '
        if(w.get()==""):
            inputfile = csv.reader(open('contact.csv','r'))
        else:
            path=w.get()
            inputfile = csv.reader(open(path,'r'))
    time.sleep(3)
        

    pyautogui.click(1299,722)
    time.sleep(2)
    ctr=0;
    for row in inputfile:
        if ctr != 0:
             name = appn+row[0]
             no=row[1]
             pyautogui.click(1268,78)
             time.sleep(2)
             pyautogui.typewrite(name, interval=0.25)
             pyautogui.click(490,372)
             pyautogui.typewrite(no, interval=0.25)
             pyautogui.click(95,82)
             time.sleep(3)
             pyautogui.press('esc')
             time.sleep(2)
             
        else:
                ctr=1
    return


def chkmiscal(msg2):
        im = pyautogui.screenshot('img1.png', region=(45,114,1278,599))

        img= cv2.imread('img1.png')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kernel = np.ones((1,1), np.uint8)
        img = cv2.dilate(img, kernel)
        img = cv2.erode(img, kernel)

        cv2.imwrite('removed_nois.png', img)

        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        cv2.imwrite('thresh.png', img)
        result = pytesseract.image_to_string(Image.open('thresh.png'))
        if 'Missed voice call' in result:
            pyautogui.typewrite(msg2, interval=0.25)
            pyautogui.press('enter')
        pyautogui.press('esc')
        time.sleep(1)
        return

def chkgrp():
    pyautogui.click(640,85)
    time.sleep(2)
    im = pyautogui.screenshot('img1.png', region=(536,272,642,352))

    img = Image.open('img1.png')
    result = pytesseract.image_to_string(img)
    start=re.findall(r'(About)',result)
    a=""
    try:
            a=start[0]
    except IndexError:
            pyautogui.press('esc')
            print('1')
            return True
    if(a!=""):
        pyautogui.press('esc')
        print('2')
        return False
    


def chkem():
        print('em')
        time.sleep(2)
        im = pyautogui.screenshot('img1.jpg', region=(75,45,189,58))

        img = Image.open('img1.jpg')
        result = pytesseract.image_to_string(img)
        a=result.find('Em ')
        if(a>-1):
            print('0')
            return True
        else:
            print('1')
            return False

def reple(emsg):
    pyautogui.click(640,85)
    time.sleep(2)
    im = pyautogui.screenshot('img1.png', region=(536,272,642,352))

    img = Image.open('img1.png')
    result = pytesseract.image_to_string(img)
    start=re.findall(r'(\d{5})',result)
    try:
        sus=start[0]
    except IndexError:
        pyautogui.press('esc')
        pyautogui.press('esc')
        return

    driver= webdriver.Chrome(chrome_path)

    driver.get("http://trace.bharatiyamobile.com")
    time.sleep(4)
    pyautogui.typewrite(sus,interval=0.25)
    pyautogui.press('enter')
    time.sleep(2)
    elements=driver.find_elements_by_css_selector('span.bluetext')
    try:
        state=elements[1].text
    except IndexError:
        driver.close()
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('c')
        pyautogui.keyUp('c')
        pyautogui.keyUp('ctrl')
        time.sleep(2)
        pyautogui.press('esc')
        pyautogui.press('esc')        
        return
    
    if(state=='MUMBAI' or state=='MAHARASHTRA'):    
        lang="mar"
    elif(state=='GUJARAT'):
        lang="guj"
    elif(state=='WEST BENGAL'):
        lang='ben'
    elif(state=='KARNATAKA'):
        lang='kan'
    elif(state=='TAMILNADU' or state=='ANDHRA PRADESH & TELANGANA'):
        lang='tam'
    else:
        lang='hin'

    driver.get("https://translate.google.com/")
    time.sleep(1)
    pyautogui.typewrite(emsg,interval=0.10)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(727,279)
    pyautogui.typewrite(lang,interval=0.25)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(586, 416)
    time.sleep(2)

    driver.close()
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('c')
    pyautogui.keyUp('c')
    pyautogui.keyUp('ctrl')

    time.sleep(2)
    pyautogui.press('esc')
    time.sleep(2)

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('v')
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.press('esc')

def aut_reply():
    if(w2.get()==""):
        emsg="thank you for contacting we will contact you as soon as possible."
        
    else:
        emsg=w2.get()

    if(w3.get()==""):
        emmsg="thank you for contacting we will contact you as soon as possible."
        
    else:
        emmsg=w3.get()

    if(w4.get()==""):
        msg2="Got your Miss Call! will contact you asap"
        
    else:
        msg2=w4.get()
     
    for i in range(7):
        time.sleep(5)
        if(i==0):
            m=208
        else:
            m=205+(80*i)
        if pyautogui.pixelMatchesColor(1309,m, (9, 210, 97)):            
            pyautogui.click(1070,m)
            time.sleep(2)
            if(chkgrp()):
                time.sleep(2)
                pyautogui.press('esc')
                time.sleep(1)
            elif(chkem()):                
                print('in em')
                time.sleep(3)
                pyautogui.typewrite(emmsg, interval=0.25)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.press('esc')  
                time.sleep(1)
            else:                
                reple(emsg)
                time.sleep(2)
        
        
        else:
            pyautogui.click(950,m)
            time.sleep(1)
            print('mis cal')
            chkmiscal(msg2)


    
    pyautogui.press('down')
    while(pyautogui.pixelMatchesColor(780,740,(250,250,250))or pyautogui.pixelMatchesColor(780,740,(190,229,244))):
        pyautogui.press('down')
        
        pyautogui.press('down')
        if pyautogui.pixelMatchesColor(1309,654, (9, 210, 97)):
            pyautogui.click(1070,654)
            time.sleep(2)
            if(chkgrp()):
                pyautogui.press('esc')
                
                time.sleep(1)
            elif(chkem()):
                time.sleep(2)
                pyautogui.typewrite(emmsg, interval=0.25)
                pyautogui.press('esc')  
                time.sleep(1)
            else:
                pyautogui.press('esc')                  
                reple(emsg)
                time.sleep(2)
        
        else:
            pyautogui.press('up')
            pyautogui.press('enter')
            time.sleep(2)
            chkmiscal(msg2)
        time.sleep(2)  

     

master=Tk()
master.title("Main page")

l1= Label(master, text="Address of file to:")
l1.grid(row=0, column=0)
l2= Label(master, text="Add Employee:")
l2.grid(row=1, column=0)
w= Entry(master, bd=5, width=50)
w.grid(row=1, column=1,padx=10,pady=10)
b=Button(master, text="Add Contact", command=lambda: add_cont('e'))
b.grid(row=1,column=2,padx=10,pady=10)

l3= Label(master, text="Add Employer:")
l3.grid(row=2, column=0)
w1= Entry(master, bd=5, width=50)
w1.grid(row=2, column=1,padx=10,pady=10)
b1=Button(master, text="Add Contact", command=lambda: add_cont('em'))
b1.grid(row=2,column=2,padx=10,pady=10)


l2= Label(master, text="Custom Reply Messages:")
l2.grid(row=3, column=0)
l3= Label(master, text="For Employee:")
l3.grid(row=4, column=0)
w2= Entry(master, bd=5, width=50)
w2.grid(row=4, column=1,padx=10,pady=10)

l4= Label(master, text="For Employer:")
l4.grid(row=5, column=0)
w3= Entry(master, bd=5, width=50)
w3.grid(row=5, column=1,padx=10,pady=10)

l5= Label(master, text="For Miscall:")
l5.grid(row=6, column=0)
w4= Entry(master, bd=5, width=50)
w4.grid(row=6, column=1,padx=10,pady=10)
b2=Button(master, text="Auto Reply", command=aut_reply)
b2.grid(row=7,column=1,padx=10,pady=10)


master.mainloop()

