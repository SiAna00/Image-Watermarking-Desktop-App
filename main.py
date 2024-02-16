import tkinter
from tkinter import filedialog

# Create a window object
window = tkinter.Tk()

# Personalize the window
window.title("Image Watermarking Desktop App")
window.config(bg="light salmon")
window.minsize(width=500, height=400)
window.config(padx=20, pady=20)

# Create label
label = tkinter.Label(text="Select image", font=("Arial", 16, "normal"), padx=10, pady=10)
label.grid(column=0, row=0)

# Open filedialog window
window.filename = filedialog.askopenfilename(initialdir="C/Users/asimi", title="Select an Image", filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpeg"), ("JPG files", "*.jpg")))



window.mainloop()

