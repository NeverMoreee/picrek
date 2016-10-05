# py3

import tkinter
from PIL import Image

top = tkinter.Tk()
top.title('picrek')
pic = tkinter.PhotoImage(Image.open('/home/nemos/misc/pic/370987.jpg'))
label = tkinter.Label(top, image=pic)
tkinter.mainloop()
