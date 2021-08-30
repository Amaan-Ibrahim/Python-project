from tkinter import *                       
from random import choice
from PIL import Image, ImageTk


ask   = ["hi", "salam"]                         
hi    = ["hi too", "w salam"]                    
error = ["sorry, i don't know", "what u said?" ]            
                                                                    
root = Tk()                             
root.geometry("1000x500") 
user = StringVar()                          
bot  = StringVar()                          

image = Image.open("images.jpg")
photo = ImageTk.PhotoImage(image)
haris_label = Label(image=photo)
haris_label.place(x=10, y=20 )

root.title(" Simple ChatBot ")                  
Label(root, text=" user : ").place(x=250, y=20)                
Entry(root, textvariable=user).place(x=300, y=20)                
Label(root, text=" Bot  : ").place(x=750, y=60)                
Entry(root, textvariable=bot).place(x=800, y=60)               
                                                           
def main():                             
       question = user.get()                        
       if question in ask:                      
             bot.set(choice(hi))                    
       else:                                
             bot.set(choice(error))                 
                                
Button(root, text="Enter", command=main).pack(side=LEFT)                                
mainloop()
