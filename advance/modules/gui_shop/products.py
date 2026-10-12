import os
import json
from helpers import clean_screen
import tkinter as tk
from canvas import app
from PIL import Image, ImageTk

base_folder = os.path.dirname(__file__)

def render_products_screen():
    clean_screen()
    with open('db/products.txt') as file:
        products = [json.loads(p.strip()) for p in file]
        products_per_row = 4
        rows_for_products = len(products[0])
        for idx, product in enumerate(products):
            row = idx // products_per_row * rows_for_products
            column = idx % products_per_row

            tk.Label(app, text=product['name']).grid(row=row, column=column)

            img = Image.open(os.path.join(base_folder, 'db/images', product['img_path'])).resize((150, 150))
            photo_image = ImageTk.PhotoImage(img)
            image_label = tk.Label(image= photo_image)
            image_label.image = photo_image
            image_label.grid(row=row + 1, column=column)