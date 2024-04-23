import tkinter as tk
from PIL import Image as Img, ImageDraw, ImageFont, ImageTk, ImageGrab
from tkinter import filedialog


class Watermarker:
    def __init__(self):
        self.image = None
        self.tk_image = None
        self.image_height = None
        self.image_width = None

        self.watermark = None
        self.tk_watermark = None
        self.watermark_height = None
        self.watermark_width = None
        self.watermark_opacity = None

        self.watermark_x = 20
        self.watermark_y = 20

        self.watermark_text = None
        self.watermark_font = None
        self.watermark_font_size = 50
        self.watermark_color = None

        self.image_container = None
        self.img_file_path = None

    def open_image(self, label_name):
        # Select image file
        self.img_file_path = tk.filedialog.askopenfilename()
        self.image_container = label_name
        # Check if the file was selected
        if self.img_file_path:
            image = Img.open(self.img_file_path)
            self.image_width = image.width
            self.image_height = image.height
            image = image.resize((1500, 900))
            image = image.convert('RGBA')
            self.image = image

            self.tk_image = label_name.tk_image = ImageTk.PhotoImage(image)

            self.image_container.create_image((0, 0), anchor='nw', image=self.tk_image)

    def save_image(self, canvas):
        # Ask for save path
        file_path = tk.filedialog.asksaveasfilename(defaultextension='.png',
                                                    filetypes=[('PNG files', "*.png"),
                                                               ('All files', "*.*")])
        if not file_path:
            return
        image = self.image
        if self.watermark:

            image.paste(self.watermark, (self.watermark_x, self.watermark_y), self.watermark)
        image = image.resize((self.image_width, self.image_height))
        image.save(file_path)


        pass

    def draw_watermark(self):

        # Get original image and watermark
        file_path_to_watermark = tk.filedialog.askopenfilename()

        if file_path_to_watermark:
            self.watermark = Img.open(file_path_to_watermark)
            self.watermark = self.watermark.convert('RGBA')
            self.watermark_height = self.watermark.height
            self.watermark_width = self.watermark.width

            self.tk_watermark = self.image_container.tk_watermark = ImageTk.PhotoImage(self.watermark)

            self.image_container.create_image((0, 0), anchor='nw', image=self.tk_image)
            self.image_container.create_image((self.watermark_x, self.watermark_y), anchor='nw', image=self.tk_watermark)



    def watermark_up(self):
        self.watermark_y -= 20
        self.update_image()

    def watermark_down(self):
        self.watermark_y += 20
        self.update_image()

    def watermark_left(self):
        self.watermark_x -= 20
        self.update_image()

    def watermark_right(self):
        self.watermark_x += 20
        self.update_image()

    def update_image(self):
        try:
            print(self.watermark_font)
            self.image = Img.open(self.img_file_path)
            self.image = self.image.resize((1500, 900))
            self.tk_image = self.image_container.tk_image = ImageTk.PhotoImage(self.image)

            self.image_container.create_image((0, 0), anchor='nw', image=self.tk_image)
            ImageDraw.Draw(self.image).text((self.watermark_x, self.watermark_y),
                                            self.watermark_text,
                                            font=ImageFont.truetype(f'C:\Windows\Fonts\{self.watermark_font}.ttf',
                                                                    self.watermark_font_size),
                                            fill=self.watermark_color)
            self.tk_image = self.image_container.tk_image = ImageTk.PhotoImage(self.image)
        except TypeError:
            pass
        except OSError:
            pass
        self.image_container.create_image((0, 0), anchor='nw', image=self.tk_image, activeimage=self.tk_image, disabledimage=self.tk_image)
        self.image_container.create_image((self.watermark_x, self.watermark_y), anchor='nw', image=self.tk_watermark)

    def watermark_size_up(self):
        self.watermark_font_size += 5
        try:
            self.watermark_width = int(self.watermark_width * 1.1)
            self.watermark_height = int(self.watermark_height * 1.1)
            # Resize the watermark image and assign the new image object to be default watermark object
            self.watermark = self.watermark.resize((self.watermark_width, self.watermark_height))
            self.tk_watermark = self.image_container.tk_watermark = ImageTk.PhotoImage(self.watermark)
        except TypeError:
            pass
        except AttributeError:
            pass
        self.update_image()

    def watermark_size_down(self):
        if self.watermark_font_size > 5:
            self.watermark_font_size -= 5
        else:
            pass
        try:
            self.watermark_width = int(self.watermark_width / 1.1)
            self.watermark_height = int(self.watermark_height / 1.1)

            # Resize the watermark image and assign the new image object to be default watermark object
            self.watermark = self.watermark.resize((self.watermark_width, self.watermark_height))
            self.tk_watermark = self.image_container.tk_watermark = ImageTk.PhotoImage(self.watermark)
        except TypeError:
            pass
        except AttributeError:
            pass
        self.update_image()

    def draw_text(self, entry_box):
        self.watermark_text = entry_box.get()

    def get_font(self, font_combobox):
        self.watermark_font = font_combobox.get()

    def get_color(self, color_combobox):
        self.watermark_color = color_combobox.get()
        self.update_image()

    def remove_text(self):
        self.watermark_text = None
        self.update_image()


    def delete_watermark(self):
        self.watermark = None
        self.tk_watermark = None
        self.image_container.create_image((0, 0), anchor='nw', image=self.tk_image)

    def show_popup(self):
        popup = tk.Toplevel()
        popup.title('About')
        popup.geometry("500x200")

        label = tk.Label(popup, text="Hello!\n\nThis is a simple application to add watermarks to images."
                                     "\n\n1. Open image to edit.\n"
                                     "2. Either import a watermark image or choose to add text as watermark.\n"
                                     "3. Edit the watermark style and position.\n"
                                     "4. Click Save to export the new file.\n"
                                     "\n"
                                     "v1.0", justify='left')
        label.pack(padx=20, pady=20)
