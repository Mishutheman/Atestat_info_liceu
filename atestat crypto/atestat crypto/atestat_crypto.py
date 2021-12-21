import tkinter
from tkinter import *
from tkinter import ttk


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

    def Caesar_encrypt(self):
        text=self.intCaesar.get("1.0",'end-1c')
        cyphertext=""
        if len(self.intkey.get())==0:
            self.iesireCaesar.delete('1.0', END)
            self.iesireCaesar.insert(END,text)
        else:
            key=self.intkey.get()
            for char in text:
                if not char.isalpha():
                    cyphertext+=char
                else:
                    if char.isupper():
                        cyphertext += chr((ord(char) + int(key)%26 - 65) % 26 + 65)
                    else:
                        cyphertext += chr((ord(char) + int(key)%26 - 97) % 26 + 97)
            self.iesireCaesar.delete('1.0', END)
            self.iesireCaesar.insert(END,cyphertext)
        


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
        self.intCaesar=Text(Caesar,height=4,width=35)
        self.intCaesar.place(x=20,y=150)
        Intrarekey=Label(Caesar,text="Introduceti cheia (numar pozitiv)")
        Intrarekey.place(x=20,y=230)
        self.intkey=Entry(Caesar)
        self.intkey.place(x=20,y=250)

        exitCaesar=self.exitbutton(Caesar)

        self.iesireCaesar=Text(Caesar,height=4,width=35)
        self.iesireCaesar.place(x=20,y=315)

        
        encButCaesar=Button(Caesar, text="Criptare",command=self.Caesar_encrypt)
        encButCaesar.place(x=20,y=280)



    def Reverse_encrypt(self):
        text=self.intRev.get("1.0",'end-1c')
        cyphertext=""
        for i in range(len(text)):
            cyphertext+=text[len(text)-1-i]
        self.iesireRev.delete('1.0', END)
        self.iesireRev.insert(END,cyphertext)


    def open_Reverse_win(self):
        Reverse=Toplevel(ecran)
        Reverse.geometry("930x600")
        Reverse.title("Reverse")
        Reverse.resizable(width=False, height=False)
        TitluReverse=Label(Reverse,text="Cifrul Reverse", font=("Arial Black",15))
        TitluReverse.place(x=20,y=10)
        descriere=Label(Reverse,text='descriere Reverse',font=("Times New Roman",11))
        descriere.place (x=20,y=40)

        self.intRev=Text(Reverse,height=4,width=35)
        self.intRev.place(x=20,y=100)
        self.encRev=Button(Reverse,text="Criptare",command=self.Reverse_encrypt)
        self.encRev.place(x=20,y=180)
        self.iesireRev=Text(Reverse,height=4,width=35)
        self.iesireRev.place(x=20,y=220)
        exitRev=self.exitbutton(Reverse)
    




    def Substitution_encrypt(self):
        text=self.intSub.get("1.0",'end-1c')

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


        #caseta de intrare pt mesaj necriptat
        intrare=Label(Substitution,text="Introduceti mesajul necriptat")
        intrare.place(x=20,y=80)
        self.intSub=Text(Substitution,height=4,width=35)
        self.intSub.place(x=20,y=160)


        #caseta de intrare cheie la criptare
        intkey1=Label(Substitution,text="Introduceti cheia")
        intkey1.place(x=20,y=130)
        self.intkey=Text(Substitution,height=1,width=30)
        self.intkey.place(x=20,y=190)


        #buton criptare
        self.encSub=Button(Substitution,text="Criptare",command=self.Substitution_encrypt)
        self.encSub.place(x=20,y=225)


        #caseta iesire criptare
        self.iesireSub=Text(Substitution,height=4,width=35)
        self.iesireSub.place(x=20,y=260)


        #caseta de intrare pt mesaj criptat
        intrare1=Label(Substitution,text="Introduceti mesajul criptat")
        intrare1.place(x=500,y=80)
        self.intSub1=Text(Substitution,height=4,width=35)
        self.intSub1.place(x=500,y=160)


        #caseta de intrare cheie la decriptare
        intkey1=Label(Substitution,text="Introduceti cheia")
        intkey1.place(x=500,y=130)
        self.intkey1=Text(Substitution,height=1,width=30)
        self.intkey1.place(x=500,y=190)


        #buton decriptare
        self.decSub1=Button(Substitution,text="Decriptare",command=self.Substitution_encrypt)
        self.decSub1.place(x=500,y=225)
        self.iesireSub1=Text(Substitution,height=4,width=35)
        self.iesireSub1.place(x=500,y=260)




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
