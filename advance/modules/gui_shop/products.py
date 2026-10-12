import os
import json
from helpers import clean_screen
import tkinter as tk
from canvas import app
from PIL import Image, ImageTk

base_folder = os.path.dirname(__file__)

def update_current_user(username, product_id):
    with open(os.path.join(base_folder, 'db', 'users.txt'), 'r+') as file:
        users = [json.loads(u.strip()) for u in file]
        for user in users:
            if user['username'] == username:
                user['products'].append(product_id)
                file.seek(0)
                file.truncate()
                file.writelines(json.dumps(u) + '\n' for u in users)
                return

def purchase_products(product_id):
    with open(os.path.join(base_folder, 'db', 'products.txt'), 'r+') as file:
        products = [json.loads(p.strip()) for p in file]
        for product in products:
            if product['id'] == product_id:
                product['count'] -= 1
                file.seek(0)
                file.truncate()
                file.writelines(json.dumps(p) + '\n' for p in products)
                return


def buy_product(product_id):
    clean_screen()

    with open(os.path.join(base_folder, 'db', 'current_user.txt')) as file:
        username = file.read().strip()

    if username:
        update_current_user(username, product_id)
        purchase_products(product_id)

    render_products_screen()

def render_products_screen():
    clean_screen()
    with open(os.path.join(base_folder,'db', 'products.txt')) as file:
        products = [json.loads(p.strip()) for p in file]
        products = [p for p in products if p['count'] > 0]
        products_per_row = 8
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

            tk.Label(app, text=product['count']).grid(row=row + 2, column=column)
            tk.Button(app,
                      text=f'Buy { product["id"]}',
                      command= lambda p = product['id']: buy_product(p)
                      ).grid(row=row + 3, column=column)

