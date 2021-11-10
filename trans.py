import pyperclip as pycl
from googletrans import Translator
from time import sleep

tr = Translator()

while True: 
    txt = pycl.paste()
    print('Clipboard Copy:',txt)
    trans_txt = tr.translate(txt,src='en',dest='ja').text
    print('Clipboard Paste: ',trans_txt)
    pycl.copy(trans_txt)

    while pycl.paste()==trans_txt:
        sleep(0.1)
        