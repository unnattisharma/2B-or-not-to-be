# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 16:53:48 2024

@author: usharma
"""

import tkinter as tk
import random
from PIL import Image, ImageTk
import glob

# Function to update the counter and list for Button 1
def increment_button1():
    global count1
    text = entry.get()
    if text not in ['',placeholder]:
        list1.insert(tk.END, text)
        entry.delete(0, tk.END)
        count1 += 1
        label1.config(text=f"{count1} times today")
    return

# Function to update the counter and list for Button 2
def increment_button2():
    global count2
    text = entry.get()
    if text not in ['',placeholder]:
        list2.insert(tk.END, text)
        entry.delete(0, tk.END)
        count2 += 1
        label2.config(text=f"{count2} times today")
    return
    
def focus_out(entry):
    if len(entry.get()) == 0:
        new_text = placeholder
    else:
        new_text = ''
    return entry.insert(0, new_text)

def finish_day():
    if count1 >= count2:
        message = random.choice(successful_day_messages)
        image_path = random.choice(winner_images)
    elif count1 < count2:
        message = random.choice(unsuccessful_day_messages)
        image_path = random.choice(loser_images)
    text_display = tk.Text(root, height=30, width=30)
    text_display.pack(pady=10)
    text_display.insert(tk.END, message)
    image = Image.open(image_path)
    image = image.resize((200, 200), Image.ANTIALIAS)  # Resize image if needed
    photo = ImageTk.PhotoImage(image)

    # Insert the image into the Text widget
    text_display.image_create(tk.END, image=photo)
    text_display.image = photo
    return

def save_all():
    global list1_vals, list2_vals
    list1_vals = list(list1.get(0, tk.END))
    list2_vals = list(list2.get(0, tk.END))
    
    with open('previous.txt','w') as f:
            f.write(str(count1)+'\n')
            [f.write(lv1+',') for lv1 in list1_vals[0:-1]]
            f.write(list1_vals[-1]+'\n')
            f.write(str(count2)+'\n')
            [f.write(lv2+',') for lv2 in list2_vals[0:-1]]
            f.write(list2_vals[-1]+'\n')
            
    root.destroy()    
    return

def load_day():
    global count1, count2
    with open('previous.txt', 'r') as f:
        prev_data = f.readlines()
    count1 += int(prev_data[0].strip())
    count2 += int(prev_data[2].strip())
    [list1.insert(tk.END, text) for text in prev_data[1].strip().split(',')]
    [list2.insert(tk.END, text) for text in prev_data[3].strip().split(',')]
    label1.config(text=f"{count1} times today")
    label2.config(text=f"{count2} times today")
    return

def delete_entry(selected):
    return
    

placeholder = 'Decision'
with open('successful_day_messages.txt','r') as f:
    successful_day_messages=[m.strip() for m in f.readlines()]
    
with open('unsuccessful_day_messages.txt','r') as f:
    unsuccessful_day_messages=[m.strip() for m in f.readlines()]

winner_images = glob.glob('winner_images/*')
loser_images = glob.glob('loser_images/*')

# Initialize counters
count1 = 0
count2 = 0

# Initialize the main window
root = tk.Tk()
root.title("2B")
root.geometry("300x800")

menubar = tk.Menu()
main_menu = tk.Menu(menubar, tearoff=False)

main_menu.add_command(
    label="Finish day",
    command=finish_day,
    compound=tk.LEFT
)

main_menu.add_command(
    label="Load previous",
    command=load_day,
    compound=tk.LEFT
)

menubar.add_cascade(menu=main_menu, label="Options")
root.config(menu=menubar)   

# Create and place the text input field

entry = tk.Entry(root)
entry.pack(pady=10)
entry.insert(0, placeholder)
entry.bind("<FocusIn>", lambda args: entry.delete(0, 'end'))
entry.bind("<FocusOut>", lambda args: focus_out(entry))

# Create and place the first button and its label
button1 = tk.Button(root, text="Winner", command=increment_button1, bg="blue", fg="white")
button1.pack(pady=10)
label1 = tk.Label(root, text="0 times today")
label1.pack()

# Create and place the listbox for Button 1
list1 = tk.Listbox(root)
list1.pack()

# Create and place the second button and its label
button2 = tk.Button(root, text="Loser", command=increment_button2, bg="red", fg="white")
button2.pack(pady=10)
label2 = tk.Label(root, text="0 times today")
label2.pack()

# Create and place the listbox for Button 2
list2 = tk.Listbox(root)
list2.pack()

#list1_vals = list1.get(0, tk.END)
root.protocol("WM_DELETE_WINDOW", save_all)

# Run the application
root.mainloop()

