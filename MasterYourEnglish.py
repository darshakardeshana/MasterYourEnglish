import requests
from bs4 import BeautifulSoup
import ctypes
import time 

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def displayWord():
    url = 'https://randomword.com/'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    data = soup.select('#shared_section > div')
    with open('MasterYourEnglishLog.txt','a') as txt:
        temp = data[0].text.strip() + ' : ' + data[1].text.strip() + '\n'
        txt.write(temp)
    word = data[0].text
    meaning = 'Word : ' + word + '\n\n' + 'Defination : ' + data[1].text + '\n\n\n\nTo Exit from program press cancel\nTo continue press OK'
    temp = Mbox('New Word', meaning, 1)
    return temp

while True:
    exit = displayWord()
    if exit == 2:
        break
    time.sleep(2)
