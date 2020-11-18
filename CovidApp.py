import tkinter as tk
from tkinter import font
import requests

HEIGHT = 700
WIDTH = 800

url = 'https://api.apify.com/v2/key-value-stores/tVaYRsPHLjNdNBu7S/records/LATEST?disableRedirect=true'
response = requests.get(url)
print(type(response.json()))

def get_amount(country):
    for row in response.json():
        if row['country'] == country.capitalize():
            print(row['infected'])
            print(row['tested'])
            label['text'] = "TOTAL INFECTED: %s \n\nTOTAL TESTED: %s \n\nTOTAL RECOVERED: %s" % (str(row['infected']), str(row['tested']), str(row['recovered']))

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

backgroud_image = tk.PhotoImage(file='covidPhoto.png')
backgroud_label = tk.Label(root, image=backgroud_image)
backgroud_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
 
entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get amount".upper(), font=40, command=lambda: get_amount(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Old style', 20))
label.place(relwidth=1, relheight=1)

root.mainloop()