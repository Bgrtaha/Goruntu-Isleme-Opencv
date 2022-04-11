import pywhatkit
text= input('Yazınızı buraya yazın el yazısına dönüşsün: ')
pywhatkit.text_to_handwriting(text, save_to='mytext', rgb=(0,0,225))