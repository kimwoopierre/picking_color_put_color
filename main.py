from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import *
from tkinter import Toplevel
from threading import Thread, Event

class Test:
    def __init__(self):
        self.img = None
        self.stop_event = Event()

    def openfile(self):
        filename = filedialog.askopenfilename(initialdir="/", title='select a file', filetypes=[('all files', '*.png *.jpg *jpeg *.gif')])
        if filename:
            self.img = Image.open(filename)
            image = ImageTk.PhotoImage(self.img)
            label.config(image=image)
            label.image = image
            self.width, self.height = self.img.size
            self.new_img = self.img.copy().resize((self.width * 20, self.height * 20))
            self.new_width, self.new_height = self.new_img.size

    def pixel(self, size):
        if self.img is not None:
            filename = filedialog.askopenfilename(initialdir="/", title='select a file', filetypes=[('all files', '*.png *.jpg *jpeg *.gif')])
            newwindow = Toplevel(window)
            newwindow.title("progress bar")
            newwindow.geometry("300x100")
            progressbar = Progressbar(newwindow, length=200, mode="indeterminate")
            progressbar.start()
            progressbar.pack()
            self.stop_event.clear()

            def task():
                if filename:
                    self.pixel_img = Image.open(filename)
                    for x in range(0, self.new_width, size):
                        for y in range(0, self.new_height, size):
                            if self.stop_event.is_set():
                                newwindow.destroy()
                                return
                            window.after(1)
                            window.update()
                            color = self.new_img.getpixel((x, y))
                            if not newwindow.winfo_exists():
                                self.stop_event.set()
                                return
                            pixel_qr = self.set_color(self.pixel_img, color).resize((size, size))
                            self.new_img.paste(pixel_qr, (x, y))
                    newwindow.destroy()
                    result = self.new_img.copy().resize((300, 200))
                    image = ImageTk.PhotoImage(result)
                    label.config(image=image)
                    label.image = image

            newwindow.protocol("WM_DELETE_WINDOW", lambda: self.on_new_window_close(newwindow))
            thread = Thread(target=task)
            thread.start()

    def on_new_window_close(self, newwindow):
        self.stop_event.set()
        newwindow.destroy()

    def set_color(self, image, color):
        color += (255,)
        width, height = image.size
        new_image = image.copy()
        for x in range(0, width):
            for y in range(0, height):
                if image.getpixel((x, y)) == (0, 0, 0):
                    new_image.putpixel((x, y), color)
                elif image.getpixel((x, y)) == (255, 255, 255):
                    new_image.putpixel((x, y), (255, 255, 255, 255))
                else:
                    new_image.putpixel((x, y), (255, 255, 255, 255))
        return new_image

    def save(self):
        if self.img is not None:
            files = [('jpg', '.jpg')]
            filename = filedialog.asksaveasfile(mode='w', filetypes=files, defaultextension=files)
            if not filename:
                return
            self.new_img.save(filename)

size = 200  # small number more detail original image, less detail pixel image(large time)

def Exit():
    window.destroy()

window = tk.Tk()
window.geometry('400x300')
window.title("pixel art")
process = Test()

# menubar
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
original = filemenu.add_command(label="Open", command=process.openfile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
window.config(menu=menubar)

# image frame
frame = tk.Frame(window, width=300, height=200)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
label = tk.Label(window)
label.pack()

button_pixel = tk.Button(window, text='pixel image', command=lambda: process.pixel(size))
button_pixel.pack()

button_save = tk.Button(window, text='save image', command=process.save)
button_save.pack()

window.mainloop()






# dino = Image.open("F:\kimwo\python\picking_color_put_color\dino.jpg")
# dinos = Image.open("F:\kimwo\python\picking_color_put_color\dino_change_color.jpg")
# eye = Image.open("F:\kimwo\python\picking_color_put_color\eye.jpg")
# mask = Image.open("F:\kimwo\python\picking_color_put_color\dino_mask.jpg").resize(dino.size).convert('L')
# qrcode = Image.open("F:\kimwo\python\picking_color_put_color\\1mbJL.jpg")
# width1, height1 = eye.size  #275 183

# size = 100
# def set_color (image, color):
#     color +=(255,)
#     width, height = image.size
#     new_image = image.copy()
#     for x in range(0,width):
#         for y in range(0,height):
#             if image.getpixel((x,y)) == (0,0,0):
#                 new_image.putpixel((x,y),color)
#             elif image.getpixel((x,y)) == (255,255,255):
#                 new_image.putpixel((x,y), (255,255,255,255))
#             else:
#                 new_image.putpixel((x,y), (255,255,255,255))
#     return new_image
# # dino_width, dino_height = dino.size
# new_eye = eye.copy().resize((width1*20,height1*20))
# new_width, new_height = new_eye.size
# for x in range(0,new_width, size):
#     for y in range(0,new_height,size):
#         color = new_eye.getpixel((x,y))
#         pixel_dino = set_color(qrcode, color).resize((size,size))
#         new_eye.paste(pixel_dino,(x,y))
# new_eye.save("mosaic_eye.jpg", dpi=(300,300))



# for x in range(0,width1, 10):
#     for y in range(0,height1, 10):
#         color = eye.getpixel((x,y))
#         dino_colored = set_color(dino, color)
#         if x+dino_width <=400 and y+dino_height <=400:
#             new_image.paste(dino_colored, (x,y))
#         else:
#             box = (0,0,min(dino_width, 400-x), min(dino_height, 400-y))
#             region = dino_colored.crop(box)
#             new_image.paste(region, (x,y))
# new_image.save("result.jpg")
        
# dinos.save('dino_change_color.jpg', 'JPEG')