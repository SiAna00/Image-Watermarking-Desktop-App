from tkinter import *
from PIL import ImageTk, Image, ImageDraw, ImageFont
from tkinter import filedialog
from config import initial_dir, font_path

def select_image():

    global uploaded_image
    global filename

    # Select an image
    filename = filedialog.askopenfilename(initialdir=initial_dir, title="Select an Image", filetypes=(("JPG files", "*.jpg"), ("JPEG files", "*.jpeg"), ("PNG files", "*.png"), ("All files", "*.*")))
    selected_image = Image.open(filename)

    # Resize image
    resized_image = selected_image.resize((400, 300))

    # Show resized image
    uploaded_image = ImageTk.PhotoImage(resized_image)
    uploaded_img_label = Label(image=uploaded_image)
    uploaded_img_label.pack(pady=20)


def add_watermark(image):
    global wm_image

    # Create an image object
    new_image = Image.open(image)
    new_image = new_image.resize((400, 300))

    # Get image size
    image_width, image_height = new_image.size

    # Draw on image
    draw = ImageDraw.Draw(new_image)

    # Choose font-size
    font_size = int(image_width / 12)

    # Choose font
    font = ImageFont.truetype(font_path, font_size)

    # Choose coordinates for watermark
    x, y = int(image_width / 2), int(image_height / 2)

    # Add watermark
    wm_text = "AnaSi Was Here"
    draw.text((x, y), wm_text, font=font, fill="#FFF", anchor="ms")

    # Display image
    wm_image = ImageTk.PhotoImage(new_image)
    wm_img_label = Label(image=wm_image)
    wm_img_label.pack(pady=20)

    # Save image with watermark
    new_image.save(f"{initial_dir}/watermark_image.jpg")


# Create a window object
window = Tk()

# Personalize the window
window.title("Image Watermarking Desktop App")
window.config(bg="light salmon")
window.minsize(width=500, height=400)
window.maxsize(width=1440, height=800)
window.config(padx=20, pady=20)

# Create select button
select_button = Button(text="Select an Image", command=select_image)
select_button.config(padx=5, pady=5)
select_button.pack(pady=5)

# Create add watermark button
add_wm_button = Button(text="Add Watermark", command=lambda: add_watermark(filename))
add_wm_button.config(padx=5, pady=5)
add_wm_button.pack(pady=5)

window.mainloop()

