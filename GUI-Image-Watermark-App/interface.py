import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from main2 import Watermarker
app = Watermarker()


root = tk.Tk()
root.title('Watermark Application')
root.attributes('-fullscreen', True)

# Images for arrows
left_arrow = Image.open('arrow_images/arrow.png')
left_arrow = left_arrow.resize((left_arrow.width // 15, left_arrow.height // 15))
up_arrow = left_arrow.rotate(-90)
right_arrow = up_arrow.rotate(-90)
down_arrow = up_arrow.rotate(180)

tk_left_arrow = ImageTk.PhotoImage(left_arrow)
tk_up_arrow = ImageTk.PhotoImage(up_arrow)
tk_right_arrow = ImageTk.PhotoImage(right_arrow)
tk_down_arrow = ImageTk.PhotoImage(down_arrow)


# Create and locate frames
image_frame = tk.Frame(root, bg="powderblue")
control_frame = tk.Frame(root, bg="powderblue")
remote_frame = tk.Frame(root, bg="powderblue")

image_frame.grid(row=0, column=0, rowspan=2)
control_frame.grid(row=0, column=1, padx=10)
remote_frame.grid(row=1, column=1, padx=10, pady=10)

# Create and locate widgets inside image_frame
label_image = tk.Canvas(image_frame, width=1500, height=900, borderwidth=0, bg="darkseagreen", highlightthickness=0)
button_open = tk.Button(image_frame, text='Open Image From File Directory', command=lambda: app.open_image(label_image), font=('arial', 13, 'bold'))
button_save = tk.Button(image_frame, text='Save', command=lambda: app.save_image(canvas=label_image), font=('arial', 13))

label_image.grid(row=0, column=0, columnspan=2)
button_open.grid(row=1, column=0, pady=75)
button_save.grid(row=1, column=1)

# Create and locate widgets inside control_frame
button_watermark_open = tk.Button(control_frame, text='Select Watermark Image', command=app.draw_watermark, font=('arial', 11, 'bold'))
button_delete_watermark = tk.Button(control_frame, text='Remove Watermark', command=app.delete_watermark, font=('arial', 11))

label_watermark_text = tk.Label(control_frame, text='Watermark Text:', bg="powderblue", font=('arial', 13))
watermark_text = tk.Entry(control_frame)

button_add_text = tk.Button(control_frame, text='Add', command=lambda: [app.draw_text(watermark_text), app.get_font(combobox_font), app.get_color(combobox_color)], font=('arial', 13))
button_remove_text = tk.Button(control_frame, text='Remove', command=app.remove_text, font=('arial', 13))

label_font = tk.Label(control_frame, text="Select Text Font:", bg="powderblue", font=('arial', 13))
combobox_font = tk.ttk.Combobox(control_frame, values=["arial", "arialbd", "BASKVILL", "BRADHITC", "cambriab", "FREESCPT", "ITCBLKAD", "unispace bd", "verdana", "TEMPSITC"])

label_font_color = tk.Label(control_frame, text="Select Text Color:", bg="powderblue", font=('arial', 13))
combobox_color = tk.ttk.Combobox(control_frame, values=["antiquewhite", 'black', 'tomato', 'pink', 'purple', 'wheat', 'springgreen', 'powderblue', 'blanchedalmond', 'hotpink', 'magenta'])

button_watermark_open.grid(row=0, column=0, pady=100)
button_delete_watermark.grid(row=0, column=1)

label_watermark_text.grid(row=1, column=0)
watermark_text.grid(row=1, column=1, pady=10)

button_add_text.grid(row=4, column=0, pady=10)
button_remove_text.grid(row=4, column=1, pady=10)

label_font.grid(row=2, column=0, pady=5)
combobox_font.grid(row=2, column=1, padx=10)

label_font_color.grid(row=3, column=0, pady=5)
combobox_color.grid(row=3, column=1)

# Remote Frame Widgets
label_watermark_size = tk.Label(remote_frame, text='Size', bg="powderblue", font=('arial', 13, 'bold'))
button_smaller = tk.Button(remote_frame, image=tk_right_arrow, relief='flat', bd=0, command=app.watermark_size_down, bg="powderblue", activebackground="powderblue")
button_bigger = tk.Button(remote_frame, image=tk_left_arrow, relief='flat', bd=0, command=app.watermark_size_up, bg="powderblue", activebackground="powderblue")

label_location = tk.Label(remote_frame, text='Move', bg="powderblue", font=('arial', 13, 'bold'))
button_up = tk.Button(remote_frame, image=tk_up_arrow, relief='flat', bd=0, command=app.watermark_up, bg="powderblue", activebackground="powderblue")
button_down = tk.Button(remote_frame, image=tk_down_arrow, relief='flat', bd=0, command=app.watermark_down, bg="powderblue", activebackground="powderblue")
button_left = tk.Button(remote_frame, image=tk_left_arrow, relief='flat', bd=0, command=app.watermark_left, bg="powderblue", activebackground="powderblue")
button_right = tk.Button(remote_frame, image=tk_right_arrow, relief='flat', bd=0, command=app.watermark_right, bg="powderblue", activebackground="powderblue")

button_exit = tk.Button(remote_frame, text='Exit', command=root.destroy, font=('arial', 13))

label_watermark_size.grid(row=3, column=1, pady=100)
button_bigger.grid(row=3, column=0, sticky='e')
button_smaller.grid(row=3, column=2, sticky='w')

button_up.grid(row=0, column=1, sticky='s')
button_left.grid(row=1, column=0, sticky='e')
button_right.grid(row=1, column=2, sticky='w')
button_down.grid(row=2, column=1, sticky='n')

label_location.grid(row=1, column=1)

button_exit.grid(row=4, column=4, pady=20)


root.config(bg="powderblue")


# Create Menu
menu_bar = tk.Menu(root)

# Create File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=lambda: app.open_image(label_image))
file_menu.add_command(label="Save As..", command=lambda: app.save_image(canvas=label_image))

# Create About Menu
about_menu = tk.Menu(menu_bar, tearoff=0)
about_menu.add_command(label='About', command=lambda: app.show_popup())


# Add the File and Edit Menus to the Menu Bar
menu_bar.add_cascade(label='File', menu=file_menu)
menu_bar.add_separator()
menu_bar.add_cascade(label='About', menu=about_menu)

root.config(menu=menu_bar)
root.mainloop()
