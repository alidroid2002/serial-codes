from tkinter import *
import serial, time
from PIL import ImageTk, Image

root = Tk()
root.title("LED control")
root.iconbitmap("iconArduino.ico")

try:
    ser = serial.Serial("COM1", 9600, timeout=0.1)

    myImg = ImageTk.PhotoImage(Image.open('arduino.jpg').resize((640, 360), Image.LANCZOS))
    imgLabel = Label(root, image=myImg).grid(row=0, column=0, columnspan=8)

    def sendCmd(value):
        ser.write((value+'\n').encode("utf-8"))
        print(value)

    onBtn = Button(root, text="LED ON", command=lambda: sendCmd("LED ON"), pady=20, borderwidth=5, fg="#ffffff", bg="#000000").grid(row=1, column=0, columnspan=4, sticky="we")
    offBtn = Button(root, text="LED OFF", command=lambda: sendCmd("LED OFF"), pady=20, borderwidth=5, bg="#000000", fg="#ffffff").grid(row=1, column=4, columnspan=4, sticky="we")
    quitBtn = Button(root, text="Exit Program", command=root.quit,  pady=20, borderwidth=5, bg="#000000", fg="#ffffff").grid(row=2, column=0, columnspan=8, sticky="we")

    root.mainloop()

except KeyboardInterrupt:
    print("Terminated.")