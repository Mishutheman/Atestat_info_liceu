from tkinter import *
from tkinter import ttk
import tkinter

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Item")
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)

        cyphersMenu=Menu(menu)
        cyphersMenu.add_command(label="Caesar",command=self.open_Caesar_win)
        cyphersMenu.add_command(label="Reverse",command=self.open_Reverse_win)
        cyphersMenu.add_command(label="Substitution",command=self.open_Substitution_win)
        cyphersMenu.add_command(label="Affine",command=self.open_Affine_win)
        cyphersMenu.add_command(label="Vignere",command=self.open_Vignere_win)
        menu.add_cascade(label="Ciphers",menu=cyphersMenu)

    def exitProgram(self):
        exit()

    def Caesar_encrypt(self,text,key):
        print(text+" "+key)
        cyphertext=""
        for char in text:
            if not char.isalpha():
                cyphertext+=char
            else:
                if char.isupper():
                    cyphertext += chr((ord(char) + s-65) % 26 + 65)
                
                else:
                    cyphertext += chr((ord(char) + s - 97) % 26 + 97)
        return cyphertext


    def open_Caesar_win(self):
        Caesar=Toplevel(ecran)
        Caesar.geometry("940x600")
        Caesar.title("Caesar")
        Caesar.resizable(width=False, height=False)
        TitluCaesar=Label(Caesar,text="Cifrul Caesar", font=("Arial Black",15))
        TitluCaesar.place(x=20,y=10)
        descriere=Label(Caesar,text='In criptografie, cifrul lui Cezar, numit si cifru cu deplasare, codul lui Cezar sau deplasarea lui Cezar, este una dintre cele mai simple tehnici de criptare. \n Este un tip de cifru al substitutiei, in care fiecare litera din textul initial este inlocuita cu o litera care se afla in alfabet la o distanta fixa fata de cea \n inlocuita. De exemplu, cu o deplasare de cinci pozitii in alfabetul limbii romane, A este inlocuit cu F, B devine G si asa mai departe. Aceasta metoda este \n numita asa dupa Iulius Cezar, care o folosea a comunica cu generalii sai. Acest cifru nu ofera securitate suficienta',font=("Times New Roman",11))
        descriere.place (x=20,y=40)
        IntrareC=Label(Caesar,text="Introduceti textul")
        IntrareC.place(x=20,y=120)
        intCaesar=Text(Caesar,height=4,width=35)
        intCaesar.place(x=20,y=150)
        Intrarekey=Label(Caesar,text="Introduceti cheia (numar pozitiv)")
        Intrarekey.place(x=20,y=230)
        intkey=Entry(Caesar)
        intkey.place(x=20,y=250)
        exitCaesar=self.exitbutton(Caesar)

        # trb sa vad care ii problema cu intrarea si iesirea
        iesireCaesar=Text(Caesar,height=4,width=35)
        iesireCaesar.place(x=20,y=315)


        text=intCaesar.get("1.0",'end-1c')
        key=intkey.get()
        encButCaesar=Button(Caesar, text="Criptare",command=self.Caesar_encrypt(text,key))
        encButCaesar.place(x=20,y=280)



    def open_Reverse_win(self):
        Reverse=Toplevel(ecran)
        Reverse.geometry("930x600")
        Reverse.title("Reverse")
        Reverse.resizable(width=False, height=False)
        TitluReverse=Label(Reverse,text="Cifrul Reverse", font=("Arial Black",15))
        TitluReverse.place(x=20,y=10)
        descriere=Label(Reverse,text='descriere Reverse',font=("Times New Roman",11))
        descriere.place (x=20,y=40)
        exitRev=self.exitbutton(Reverse)


    def open_Substitution_win(self):
        Substitution=Toplevel(ecran)
        Substitution.geometry("930x600")
        Substitution.title("Substitution")
        Substitution.resizable(width=False, height=False)
        TitluSubstitution=Label(Substitution,text="Cifrul Substitution", font=("Arial Black",15))
        TitluSubstitution.place(x=20,y=10)
        descriere=Label(Substitution,text='descriere Substitutie',font=("Times New Roman",11))   
        descriere.place (x=20,y=40)
        exitSub=self.exitbutton(Substitution)
 

    def open_Affine_win(self):
        Affine=Toplevel(ecran)
        Affine.geometry("930x600")
        Affine.title("Affine")
        Affine.resizable(width=False, height=False)
        TitluAffine=Label(Affine,text="Cifrul Affine", font=("Arial Black",15))
        TitluAffine.place(x=20,y=10)
        descriere=Label(Affine,text='descriere Affine',font=("Times New Roman",11))        
        descriere.place (x=20,y=40)
        exitAff=self.exitbutton(Affine)
 

    def open_Vignere_win(self):
        Vignere=Toplevel(ecran)
        Vignere.geometry("930x600")
        Vignere.title("Vignere")
        Vignere.resizable(width=False, height=False)
        TitluVignere=Label(Vignere,text="Cifrul Vignere", font=("Arial Black",15))
        TitluVignere.place(x=20,y=10)
        descriere=Label(Vignere,text='descriere Vignere',font=("Times New Roman",11))
        descriere.place (x=20,y=40)
        exitVig=self.exitbutton(Vignere)


    def exitbutton(self,master):
        Exitbutton=Button(master,text="Exit",command=master.destroy)
        Exitbutton.place(x=20,y=560)


    

    



    


ecran=Tk()
ecran.resizable(width=False, height=False)
app=Window(ecran)
ecran.title('Crypto')
ecran.geometry("930x600+10+10")
ecran.mainloop()