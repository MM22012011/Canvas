from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("canvas")
root.geometry("600x600")
root.configure(background="LightSkyBlue1")

label = Label(root, text="Enter A Colour")
label.place(relx=0.6, rely=0.9, anchor=CENTER)

input_box = Entry(root)
input_box.insert(0, "Black")
input_box.place(relx=0.8, rely=0.9, anchor=CENTER)

canvas = Canvas(root, width=590, height=510, bg = "white", highlightbackground="lightgray")
canvas.pack()

img = ImageTk.PhotoImage(Image.open ("start_point1.png"))
my_image = canvas.create_image(50, 50, image=img)

direction = ""
oldx = 50
oldy = 50
newx = 50
newy = 50

def right_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newx = newx+5
    direction = "Right"
    draw(direction, oldx, oldy, newx, newy)
    
def left_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newx = newx-5
    direction = "Left"
    draw(direction, oldx, oldy, newx, newy)    
    
def up_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newy= newy-5
    direction = "Up"
    draw(direction, oldx, oldy, newx, newy)
    
def down_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newy = newy+5
    direction = "Down"
    draw(direction, oldx, oldy, newx, newy)

def draw(direction, oldx, oldy, newx, newy):
    fill_colour = input_box.get()
    
    if (direction == "Right"):
        right_line = canvas.create_line(oldx, oldy, newx, newy, width=3, fill=fill_colour)
    if (direction == "Left"):
        right_line = canvas.create_line(oldx, oldy, newx, newy, width=3, fill=fill_colour)
    if (direction == "Up"):
        right_line = canvas.create_line(oldx, oldy, newx, newy, width=3, fill=fill_colour)
    if (direction == "Down"):
        right_line = canvas.create_line(oldx, oldy, newx, newy, width=3, fill=fill_colour)
        
root.bind("<Right>", right_dir)
root.bind("<Left>", left_dir)
root.bind("<Up>", up_dir)
root.bind("<Down>", down_dir)

root.mainloop()