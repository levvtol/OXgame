#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk
from playsound import playsound
import welcome
from tkinter import messagebox





clousev1,clousev2,clousev3,clousev4,clousev5,clousev6,clousev7,clousev8,clousev9 = 0,0,0,0,0,0,0,0,0



#Create an instance of tkinter frame
win = Tk()
a = 100
b = 200
#Set the geometry of tkinter frame
win.geometry("380x800")
win.title("OXgame")


#Load an image in the script
img_black= (Image.open("black.png"))
x = 0
yray = 0
y = 0
k = 0
blackb1 = 0
blackb2 = 0
blackb3 = 0
blueb1 = 0
blueb2 = 0
blueb3 = 0

yox = "0"
yoxluq1,yoxluq2,yoxluq3,yoxluq4,yoxluq5,yoxluq6,yoxluq7,yoxluq8,yoxluq9 = "0","1","2","3","4","5","6","7","8"
var = "0"
# num ----> birinci 2 olacaq sonra her istifade olunduqca 1 cixilacaq eger 0 olarsa hemin hisse bloklanacaq

def qelebe():
    if yoxluq1 == yoxluq2 and yoxluq2 == yoxluq3 and yoxluq1 == yoxluq3:
        messagebox.showinfo("won", f"{yoxluq1} won")
        win.quit()
        
        

    if yoxluq4 == yoxluq5 and yoxluq5 == yoxluq6 and yoxluq4 == yoxluq6:
        messagebox.showinfo("won", f"{yoxluq4} won")

        win.quit()
    if yoxluq7 == yoxluq8 and yoxluq8 == yoxluq9 and yoxluq7 == yoxluq9  :
        messagebox.showinfo("won", f"{yoxluq7} won")

        win.quit()
    if   yoxluq1 == yoxluq4 and yoxluq4 == yoxluq7 and yoxluq1 == yoxluq7 :
        messagebox.showinfo("won", f"{yoxluq1} won")

     
        win.quit()
    if yoxluq2 == yoxluq5 and yoxluq5 == yoxluq8 and yoxluq2 == yoxluq8:
        messagebox.showinfo("won", f"{yoxluq2} won")

    
        win.quit()
    if yoxluq3 == yoxluq6 and yoxluq6== yoxluq9 and yoxluq3 == yoxluq9 :
        messagebox.showinfo("won", f"{yoxluq3} won")

      
        win.quit()
    if yoxluq1 == yoxluq5 and yoxluq5 == yoxluq9 and yoxluq1 == yoxluq9:
        messagebox.showinfo("won", f"{yoxluq1} won")

     
        win.quit()
    if yoxluq3 == yoxluq5 and yoxluq5 == yoxluq7 and yoxluq3 == yoxluq7:
        messagebox.showinfo("won", f"{yoxluq1} won")

        win.quit()
    
    
    
    






def elebele():
    black_button_1.config(state =DISABLED)
    black_button_2.config(state = DISABLED)
    black_button_3.config(state = DISABLED)
    blue_button_4.config(state = ACTIVE)
    blue_button_5.config(state = ACTIVE)
    blue_button_6.config(state = ACTIVE)
    b_1_1.config(state = DISABLED)
    b_1_2.config(state = DISABLED)
    b_1_3.config(state = DISABLED)
    b_2_1.config(state = DISABLED)
    b_2_2.config(state = DISABLED)
    b_2_3.config(state = DISABLED)
    b_3_1.config(state = DISABLED)
    b_3_2.config(state = DISABLED)
    b_3_3.config(state = DISABLED)
    
    
def novbe():
    global blackb1,blackb2,blackb3, blueb1, blueb2, blueb3
    global xray
    global k
    k = k +1
    if k %2 != 0:
        if blackb1 < 2:
            black_button_1.config(state =ACTIVE)
        elif blackb1 == 2 or blackb1 > 2:
            black_button_1.config(state =DISABLED)
        if blackb2 < 2:
            black_button_2.config(state = ACTIVE)
        else:
            black_button_2.config(state =DISABLED)
        if blackb3 < 2:
            black_button_3.config(state = ACTIVE)
        else:
            black_button_3.config(state =DISABLED)
            

        blue_button_4.config(state = DISABLED)       
        blue_button_5.config(state = DISABLED)
        blue_button_6.config(state = DISABLED)
        blue_button_4.config(bg = "#ECECEC",activebackground ="#ECECEC")
        blue_button_5.config(bg = "#ECECEC",activebackground ="#ECECEC")
        blue_button_6.config(bg = "#ECECEC",activebackground ="#ECECEC")
        
        
    else:    
        black_button_1.config(state =DISABLED)
        black_button_2.config(state =DISABLED)
        black_button_3.config(state =DISABLED)
        if blueb1 < 2:
            blue_button_4.config(state = ACTIVE)
        else:
            blue_button_4.config(state = DISABLED)
        if blueb2 < 2:
            blue_button_5.config(state = ACTIVE)
        else:
            blue_button_5.config(state = DISABLED)
        if blueb3 < 2:
            blue_button_6.config(state = ACTIVE) 
        else: 
            blue_button_6.config(state = DISABLED)
                 
        black_button_1.config(bg = "#ECECEC",activebackground ="#ECECEC")
        black_button_2.config(bg = "#ECECEC",activebackground ="#ECECEC")
        black_button_3.config(bg = "#ECECEC",activebackground ="#ECECEC")
    



    
def color_1():
    global x,var,yray,yox,openv1
    black_button_1.config(bg = "yellow",activebackground ="yellow")
    black_button_2.config(bg = "#ECECEC",activebackground ="#ECECEC")
    black_button_3.config(bg = "#ECECEC",activebackground ="#ECECEC")
    openv1 = 1
    yray = 1
    var = "b1"
    yox = "black"
    func()
    x = 1
    yray = 1
def color_2():
    global x,var,yray,yox,openv2
    black_button_2.config(bg = "yellow",activebackground ="yellow")
    black_button_1.config(bg = "#ECECEC",activebackground ="#ECECEC")
    black_button_3.config(bg = "#ECECEC",activebackground ="#ECECEC")
    openv2 = 2
    yray = 2
    yox = "black"
    var = "b2"
    func()
    x = 2
    yray = 2
def color_3():
    global x,var,yray,yox,openv3
    black_button_3.config(bg = "yellow",activebackground ="yellow")
    black_button_2.config(bg = "#ECECEC",activebackground ="#ECECEC")
    black_button_1.config(bg = "#ECECEC",activebackground ="#ECECEC")
    openv3 = 3
    yray = 3
    yox = "black"
    var = "b3"
    func()
    x = 3
    yray = 3

def color_4():
    global x,var,yray,yox ,openv4
    blue_button_4.config(bg = "yellow",activebackground ="yellow")
    blue_button_5.config(bg = "#ECECEC",activebackground ="#ECECEC")
    blue_button_6.config(bg = "#ECECEC",activebackground ="#ECECEC")
    openv4 = 1
    yray = 4
    yox = "blue"
    var = "b4"
    func()
    x = 4
    yray = 4
def color_5():
    global x,var,yray,yox,openv5
    blue_button_5.config(bg = "yellow",activebackground ="yellow")
    blue_button_4.config(bg = "#ECECEC",activebackground ="#ECECEC")
    blue_button_6.config(bg = "#ECECEC",activebackground ="#ECECEC")
    openv5 = 2
    yray = 5
    var = "b5"
    yox = "blue"
    func()
    x = 5
    yray = 6
def color_6():
    global x,var,yray,yox,openv6
    blue_button_6.config(bg = "yellow",activebackground ="yellow")
    blue_button_5.config(bg = "#ECECEC",activebackground ="#ECECEC")
    blue_button_4.config(bg = "#ECECEC",activebackground ="#ECECEC")
    openv6 = 3
    yray = 6
    var = "b6"
    yox = "blue"
    func()
    x = 6



#---------------------------------------------------for try----------------------------


#-------------------------------mean codes ------------------------------------------
def func():
    global var
    if var == "b1" or var == "b2" or var == "b3":
        b_1_1.config(state = ACTIVE)
        b_1_2.config(state = ACTIVE)
        b_1_3.config(state = ACTIVE)  
        b_2_1.config(state = ACTIVE)
        b_2_2.config(state = ACTIVE)
        b_2_3.config(state = ACTIVE)
        b_3_1.config(state = ACTIVE)
        b_3_2.config(state = ACTIVE)
        b_3_3.config(state = ACTIVE)
        
    elif var == "b4" or var == "b5"  or var == "b6":
        b_1_1.config(state = ACTIVE)
        b_1_2.config(state = ACTIVE)
        b_1_3.config(state = ACTIVE)
        b_2_1.config(state = ACTIVE)
        b_2_2.config(state = ACTIVE)
        b_2_3.config(state = ACTIVE)
        b_3_1.config(state = ACTIVE)
        b_3_2.config(state = ACTIVE)
        b_3_3.config(state = ACTIVE)
        
              
        
 
def novbe2_b11():
    if x == 1:
        b_1_1.configure(image = new_image)
    elif x == 2:
        b_1_1.configure(image = new_image2)
    elif x == 3:
        b_1_1.configure(image = new_image3)
    elif x == 4:
        b_1_1.configure(image = new_image4)
    elif x == 5:
        b_1_1.configure(image = new_image5)
    elif x == 6:
        b_1_1.configure(image = new_image6)
        
    elebele()
    qelebe()
    
def novbe2_b12():
    if x == 1:
        b_1_2.configure(image = new_image)
    elif x == 2:
        b_1_2.configure(image = new_image2)
    elif x == 3:
        b_1_2.configure(image = new_image3)
    elif x == 4:
        b_1_2.configure(image = new_image4)
    elif x == 5:
        b_1_2.configure(image = new_image5)
    elif x == 6:
        b_1_2.configure(image = new_image6)


    elebele()
    qelebe()
    

def novbe2_b13():
    if x == 1:
        b_1_3.configure(image = new_image)
    elif x == 2:
        b_1_3.configure(image = new_image2)
    elif x == 3:
        b_1_3.configure(image = new_image3)
    elif x == 4:
        b_1_3.configure(image = new_image4)
    elif x == 5:
        b_1_3.configure(image = new_image5)
    elif x == 6:
        b_1_3.configure(image = new_image6)
    elebele()
    qelebe()
    
def novbe2_b21():
    if x == 1:
        b_2_1.configure(image = new_image)
    elif x == 2:
        b_2_1.configure(image = new_image2)
    elif x == 3:
        b_2_1.configure(image = new_image3)
    elif x == 4:
        b_2_1.configure(image = new_image4)
    elif x == 5:
        b_2_1.configure(image = new_image5)
    elif x == 6:
        b_2_1.configure(image = new_image6)
    elebele()
    qelebe()
    
def novbe2_b22():
    if x == 1:
        b_2_2.configure(image = new_image)
    elif x == 2:
        b_2_2.configure(image = new_image2)
    elif x == 3:
        b_2_2.configure(image = new_image3)
    elif x == 4:
        b_2_2.configure(image = new_image4)
    elif x == 5:
        b_2_2.configure(image = new_image5)
    elif x == 6:
        b_2_2.configure(image = new_image6)
    elebele()
    qelebe()
    
def novbe2_b23():
    if x == 1:
        b_2_3.configure(image = new_image)
    elif x == 2:
        b_2_3.configure(image = new_image2)
    elif x == 3:
        b_2_3.configure(image = new_image3)
    elif x == 4:
        b_2_3.configure(image = new_image4)
    elif x == 5:
        b_2_3.configure(image = new_image5)
    elif x == 6:
        b_2_3.configure(image = new_image6)
    elebele()
    qelebe()
    

def novbe2_b31():
    if x == 1:
        b_3_1.configure(image = new_image)
    elif x == 2:
        b_3_1.configure(image = new_image2)
    elif x == 3:
        b_3_1.configure(image = new_image3)
    elif x == 4:
        b_3_1.configure(image = new_image4)
    elif x == 5:
        b_3_1.configure(image = new_image5)
    elif x == 6:
        b_3_1.configure(image = new_image6)
    elebele()
    qelebe()
    
def novbe2_b32():
    if x == 1:
        b_3_2.configure(image = new_image)
    elif x == 2:
        b_3_2.configure(image = new_image2)
    elif x == 3:
        b_3_2.configure(image = new_image3)
    elif x == 4:
        b_3_2.configure(image = new_image4)
    elif x == 5:
        b_3_2.configure(image = new_image5)
    elif x == 6:
        b_3_2.configure(image = new_image6)
    elebele()
    qelebe()
    
def novbe2_b33():
    if x == 1:
        b_3_3.configure(image = new_image)
    elif x == 2:
        b_3_3.configure(image = new_image2)
    elif x == 3:
        b_3_3.configure(image = new_image3)
    elif x == 4:
        b_3_3.configure(image = new_image4)
    elif x == 5:
        b_3_3.configure(image = new_image5)
    elif x == 6:
        b_3_3.configure(image = new_image6)
    elebele()
    qelebe()
    


def changephato():
    global x,yray
    global blackb1,blackb2,blackb3,blueb1,blueb2,blueb3
    if x  == 1:
        
        playsound('sound.mp3')
        black_button_1.config(image = new_image1_2)
        blackb1 = blackb1 +1
        if blackb1 == 2 or blackb1 > 2:
            black_button_1.config(image = img, state = DISABLED)

            
            
    elif x  ==  2:
        playsound('sound.mp3')
        black_button_2.config(image = new_image2_2)
        blackb2 = blackb2 +1
        if blackb2 == 2 or blackb2 > 2:
            black_button_2.config(image = img, state = DISABLED)
            
    elif x == 3:
        playsound('sound.mp3')
        black_button_3.config(image = new_image3_2)
        blackb3 = blackb3 +1
        if blackb3 == 2 or blackb3 > 2:
            black_button_3.config(image = img, state = DISABLED)
        
        
    elif x == 4:
        playsound('sound.mp3')
        blue_button_4.config(image = new_image4_2)
        blueb1 = blueb1 +1
        if blueb1 == 2 or blueb1 > 2:
            blue_button_4.config(image = img, state = DISABLED)
    elif x == 5:
        playsound('sound.mp3')
        blue_button_5.config(image = new_image5_2)
        blueb2 = blueb2 +1
        if blueb2 == 2 or blueb2 > 2:
            blue_button_5.config(image = img, state = DISABLED)
    elif x == 6:
        playsound('sound.mp3')
        blue_button_6.config(image = new_image6_2)
        blueb3 = blueb3 +1
        if blueb3 == 2 or blueb3 > 2:
            blue_button_6.config(image = img, state = DISABLED)
    

        





# --------------------------- ---------------- BLACK PLAYER --------------------------------

resized_image= img_black.resize((100,150), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

resized_image2= img_black.resize((60,90), Image.ANTIALIAS)
new_image2= ImageTk.PhotoImage(resized_image2)

resized_image3= img_black.resize((20,30), Image.ANTIALIAS)
new_image3= ImageTk.PhotoImage(resized_image3)



img_black2= (Image.open("black2.png"))
resized_image1_2= img_black2.resize((100,150), Image.ANTIALIAS)
new_image1_2= ImageTk.PhotoImage(resized_image1_2)

resized_image2_2= img_black2.resize((60,90), Image.ANTIALIAS)
new_image2_2= ImageTk.PhotoImage(resized_image2_2)

resized_image3_2= img_black2.resize((20,30), Image.ANTIALIAS)
new_image3_2= ImageTk.PhotoImage(resized_image3_2)

img = PhotoImage(file = "clear.png")
      
    
black_button_1 = Button(win, text = "black" ,image = new_image,command = color_1)
black_button_1.place(x = 20, y = 0 , width = 100, height = 150)

black_button_2 = Button(win, text = "black" ,image = new_image2, command = color_2)
black_button_2.place(x = 140, y = 0 , width = 100, height = 150)

black_button_3 = Button(win, text = "black" ,image = new_image3, command = color_3)
black_button_3.place(x = 260, y = 0 , width = 100, height = 150)



# ----------------------------------------------- BLUE PLAYER ----------------------------------------------


img_blue= (Image.open("blue.png"))

resized_image4= img_blue.resize((100,150), Image.ANTIALIAS)
new_image4= ImageTk.PhotoImage(resized_image4)


resized_image5= img_blue.resize((60,90), Image.ANTIALIAS)
new_image5= ImageTk.PhotoImage(resized_image5)


resized_image6= img_blue.resize((20,30), Image.ANTIALIAS)
new_image6= ImageTk.PhotoImage(resized_image6)



img_blue2= (Image.open("blue2.png"))

resized_image4_2= img_blue2.resize((100,150), Image.ANTIALIAS)
new_image4_2= ImageTk.PhotoImage(resized_image4_2)

resized_image5_2= img_blue2.resize((60,90), Image.ANTIALIAS)
new_image5_2= ImageTk.PhotoImage(resized_image5_2)

resized_image6_2= img_blue2.resize((20,30), Image.ANTIALIAS)
new_image6_2= ImageTk.PhotoImage(resized_image6_2)





#Add image to the Canvas Items

blue_button_4 = Button(win, text = "black" ,image = new_image4,command = color_4)
blue_button_4.place(x = 20, y =650 , width = 100, height = 150)




blue_button_5 = Button(win, text = "black" ,image = new_image5,command = color_5)
blue_button_5.place(x = 140, y = 650 , width = 100, height = 150)





blue_button_6 = Button(win, text = "black" ,image = new_image6,command = color_6)
blue_button_6.place(x = 260, y = 650 , width = 100, height = 150)





#----------------------------------game place ------------------------------------  
    
def x1_1():
    global yox,yoxluq1
    yoxluq1 = yox
    
    novbe()
    novbe2_b11()
    changephato()
def x1_2():
    global yox,yoxluq2
    yoxluq2 = yox
    novbe2_b12()
    novbe()
    changephato()


    
def x1_3():
    global yox,yoxluq3
    yoxluq3 = yox     
    novbe2_b13()
    novbe()
    changephato()
 
    
def x2_1():
    global yox,yoxluq4
    yoxluq4 = yox     
    novbe2_b21()
    novbe()
    changephato() 

    
def x2_2():
    global yox,yoxluq5
    yoxluq5 = yox     
    novbe2_b22()
    novbe()
    changephato()
 
 
def x2_3():
    global yox,yoxluq6
    yoxluq6 = yox     
    novbe2_b23()
    novbe()
    changephato()
 
 
def x3_1():
    global yox,yoxluq7
    yoxluq7 = yox     
    novbe2_b31()
    novbe()
    changephato()    
def x3_2():
    global yox,yoxluq8
    yoxluq8 = yox     
    novbe2_b32()
    novbe()
    changephato()

   
def x3_3():
    global yox,yoxluq9
    yoxluq9 = yox     
    novbe2_b33()
    novbe() 
    changephato()

  
    

b_1_1 = Button (win, bg= 'white', activebackground='yellow',command =x1_1)
b_1_1.place(x = 20, y = 160 , width = 100, height = 150)

b_1_2 = Button (win, bg= 'white', activebackground='yellow',command = x1_2)
b_1_2.place(x = 140, y = 160 , width = 100, height = 150)

b_1_3 = Button (win, bg= 'white', activebackground='yellow',command = x1_3)
b_1_3.place(x = 260, y = 160 , width = 100, height = 150)

b_2_1 = Button (win, bg= 'white', activebackground='yellow',command = x2_1)
b_2_1.place(x = 20, y = 325 , width = 100, height = 150)

b_2_2 = Button (win, bg= 'white', activebackground='yellow',command = x2_2)
b_2_2.place(x = 140, y = 325 , width = 100, height = 150)

b_2_3 = Button (win, bg= 'white', activebackground='yellow',command = x2_3)
b_2_3.place(x = 260, y = 325 , width = 100, height = 150)

b_3_1 = Button (win, bg= 'white', activebackground='yellow',command = x3_1)
b_3_1.place(x = 20, y = 490 , width = 100, height = 150)

b_3_2 = Button (win, bg= 'white', activebackground='yellow',command = x3_2)
b_3_2.place(x =140, y = 490 , width = 100, height = 150)

b_3_3 = Button (win, bg= 'white', activebackground='yellow',command = x3_3)
b_3_3.place(x = 260, y = 490 , width = 100, height = 150)

elebele()


win.mainloop()
