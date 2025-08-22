from tkinter import *
import serial

ser = serial.Serial("COM6", 9600)

root = Tk()
root.title("LED slider control")
root.geometry("300x200")

def send_value(value):
    value = int(value)
    ser.write(f"{value}\n".encode())


slider = Scale(root, from_=0, to=255, orient=HORIZONTAL, command=send_value)
slider.pack()

but = Button(root, text="Quit", command=root.quit).pack()


root.mainloop()