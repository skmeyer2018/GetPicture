from meta_ai_api import MetaAI
import tkinter as Tk

from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from datetime import datetime
import time
import urllib.request
from PIL import Image, ImageTk
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap
import requests
from io import BytesIO
import sys
app = QApplication(sys.argv)
label = QLabel()
lbl0=QLabel()
lbl1=QLabel()
lbl2=QLabel()
lbl3=QLabel()

def get_response():
	infoBox.delete("1.0","end")
	request_prompt=request_box.get()
	selected_style=combo_art_style.get()
	
	response = ai.prompt(message=inquiry_phrase + request_prompt + " in  " + selected_style  + " style")
	
	#pics=response["media"]
	#print(response["media"][1]["url"])
	#return
	url=response["media"][3]["url"]
	resp = requests.get(url)
	img_data = BytesIO(resp.content)
		# Load the image into QPixmap
	pixmap = QPixmap()
	pixmap.loadFromData(img_data.read())
		# Display the image in a label
	label.setPixmap(pixmap)
	label.show()
	fname=request_prompt+selected_style+".jpg"
	urllib.request.urlretrieve(url, fname)
	
	infoBox.insert(END, inquiry_phrase + request_prompt + " in  " + selected_style + " style\n\r" + url)
	
	#img=Image.open(fname)
	#img.show()
	#photo=ImageTk.PhotoImage(file=fname)
	#lbl_img_res.image=fname
	#lbl_img_res.config(image=photo)
	
	#lbl_img_res=QLabel()
	
	#lbl_img_res.setPixmap(pixmap)
	

	
	


ai = MetaAI(fb_email="sktech02@yahoo.com", fb_password="HickTon!2025")

#fb_email="sktech02@yahoo.com", fb_password="HickTon!2025"

master=Tk()
master.geometry("1000x700")
master.config(bg="#ccddee")
master.title("Your quick information request app")
request_label=Label(master, text="What picture would you like to see?", font=("Arial",14,"bold"), bg="#ccddee")
request_label.pack()
request_box=Entry(master, width=80)
request_box.pack()
art_style_label=Label(master, text="In what artistic style?", font=("Arial",14,"bold"), bg="#ccddee")
art_style_label.pack()
combo_art_style=ttk.Combobox(master, width=40, state="readonly")
combo_art_style["values"]=("realism","antique art","cartoonified", "abstract expressionism","art nouveau","avant-garde","bauhaus","baroque","classicism","conceptual art", 
 	"Constructivism Art",
	"blacklight fluorescent",
 	"Contemporary Art",
 	"Cubism",
 	"Dadaism",
 	"De Stijl",
	"Deconstructivist",
 	"Expressionism",
	"Fractal",
 	"Fluxus",
 	"Futurism",
 	"Gothic Art",
 	"Harlem Renaissance",
 	"Installation Art",
 	"Kinetic Art",
 	"Land Art",
 	"Magical Realism",
 	"Modern Art",
	"Mid-century Modern",
	"Medieval"
 	"Naturalism",
 	"Neoclassicism",
 	"Performance Art",
 	"Photorealism",
 	"Pop Art",
 	"Post-Impressionism",
	"Post Modern",
 	"Primitivism",
 	"Rococo",
 	"Romanticism",
 	"Renaissance",
 	"Street Art",
 	"Suprematism",
 	"Ukiyo-e",
	"Victorian",
	"3 D wax figure")

combo_art_style.pack()
inquiry_phrase="display a picture of "
get_button=Button(master, text="GET RESPONSE", command=get_response)
get_button.pack()
infoBox=scrolledtext.ScrolledText(master,height=10,width=50, fg="darkgreen")
infoBox.configure(font=("Arial",12,"bold"), fg="red")
infoBox.pack()
#dummy=Image.open("dummypic.jpg")
#photo=ImageTk.PhotoImage(dummy)
#lbl_img_res=Label(master, image=photo) #, image=photo)
#lbl_img_res.pack()
#master.update_idletasks()
mainloop()
 