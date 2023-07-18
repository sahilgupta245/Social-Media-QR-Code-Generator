import tkinter as tk
import qrcode
from PIL import Image, ImageTk

def generate_social_media_qr(url):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="#3377FF", back_color="#FFFFFF")

    # Save the image to file as a high-resolution PNG
    image_file = "snaptag.png"
    qr_img.save(image_file, "PNG", dpi=(300, 300))
    return image_file

def generate_button_click():
    social_media_url = user_input_entry.get()
    if social_media_url:
        image_file = generate_social_media_qr(social_media_url)
        image = Image.open(image_file)
        image.thumbnail((250, 250))
        photo = ImageTk.PhotoImage(image)
        qr_code_label.config(image=photo)
        qr_code_label.image = photo
        instructions_label.config(text="Scan the QR code to visit the social media link.", fg="#3377FF")
    else:
        tk.messagebox.showerror("Error", "Please enter a social media URL.")

def close_window():
    root.destroy()        

root = tk.Tk()
root.title("Social Media QR Code Generator")
root.config(bg="#F0F0F0")
root.attributes("-fullscreen", True)

canvas = tk.Canvas(root, bg="#F0F0F0", width=350, height=350)
canvas.pack()

frame = tk.Frame(root, bg="#FFFFFF")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

title_label = tk.Label(frame, text="Social Media QR Code Generator", font=("sans-serif", 40, "bold"), bg="#FFFFFF", fg="#3377FF")
title_label.pack(pady=20)

user_input_label = tk.Label(frame, text="Social Media URL:", font=("sans-serif", 20), bg="#FFFFFF")
user_input_label.pack(pady=20)

user_input_entry = tk.Entry(frame, width=30, font=("sans-serif", 15))
user_input_entry.pack(pady=20)
user_input_entry.configure(background="#FFFFCC")

generate_button = tk.Button(frame, text="Generate QR Code", font=("sans-serif", 15, "bold"), command=generate_button_click, bg="#3377FF", fg="#FFFFFF", relief=tk.FLAT)
generate_button.pack(pady=10)

qr_code_label = tk.Label(frame, bg="#FFFFFF")
qr_code_label.pack()

instructions_label = tk.Label(frame, text="Generate the QR code first.", font=("sans-serif", 15, "bold"), bg="#FFFFFF")
instructions_label.pack(pady=10)

copyright_label = tk.Label(root, text="© Copyright reserved by sahil@InfoTech.com",font=("sans-serif", 12), fg="gray")
copyright_label.pack()

# Place the label at the bottom center of the window
copyright_label.place(relx=0.5, rely=1, anchor="s")

#close button
close_button = tk.Button(root, text="X", font=("Arial", 12, "bold"), bg="red", fg="white", relief=tk.FLAT, command=close_window)
close_button.place(x=root.winfo_screenwidth()-40, y=0, width=40, height=40)

root.mainloop()
