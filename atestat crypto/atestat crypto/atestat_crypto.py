import tkinter
from tkinter import *
from tkinter import ttk
#import matplotlib.pyplot as plt
import string

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        analysisMenu = Menu(menu)
        analysisMenu.add_command(label="Analiza de frecventa",command=self.freq_analysis_win)
        analysisMenu.add_command(label="Help")
        analysisMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="Options", menu=analysisMenu)

        cyphersMenu=Menu(menu)
        cyphersMenu.add_command(label="Caesar",command=self.open_Caesar_win)
        cyphersMenu.add_command(label="Reverse",command=self.open_Reverse_win)
        cyphersMenu.add_command(label="Substitution",command=self.open_Substitution_win)
        cyphersMenu.add_command(label="Affine",command=self.open_Affine_win)
        cyphersMenu.add_command(label="Vignere",command=self.open_Vignere_win)
        menu.add_cascade(label="Ciphers",menu=cyphersMenu)

        
    def exitProgram(self):
        exit()

    #de rezolvat analiza
    def analysis(self):
        Litere= {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
        Nr_aparitii=[1,2]
        text=self.intText
        for char in text:
            if char.isalpha():
                Litere[char.upper()]+=1

        plt.bar(Litere,Nr_aparitii)
        plt.title('Analiza de frecventa a textului')
        plt.xlabel('Litere')
        plt.ylabel('Numarul de aparitii')
        plt.show()

    # Fct deschidere 
    # fereastra analiza de frecventa
    # NU GATA
    def freq_analysis_win(self):
        Freq=Toplevel(ecran)
        Freq.geometry("940x600")
        Freq.title("Analiza de frecventa")
        Freq.resizable(width=False, height=False)

        Intrare=Label(Freq,text="Introduceti textul")
        Intrare.place(x=20,y=20)
        self.intText=Text(Freq,height=4,width=50)
        self.intText.place(x=20,y=40)

        self.analisebutton=Button(Freq,text="Analizeaza")#command=)
        self.analisebutton.place(x=20,y=120)
        
        exitVig=self.exitbutton(Freq)



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
        

    # Fct deschidere 
    # fereastra cifrului Caesar
    # GATA
    def open_Caesar_win(self):
        Caesar=Toplevel(ecran)
        Caesar.geometry("940x600")
        Caesar.title("Caesar")
        Caesar.resizable(width=False, height=False)
        TitluCaesar=Label(Caesar,text="Cifrul Caesar", font=("Arial Black",15))
        TitluCaesar.place(x=20,y=10)
        descriere=Label(Caesar,text='In criptografie, cifrul lui Cezar, numit si cifru cu deplasare, codul lui Cezar sau deplasarea lui Cezar, este una dintre cele mai simple tehnici de criptare. \n Este un tip de cifru al substitutiei, in care fiecare litera din textul initial este inlocuita cu o litera care se afla in alfabet la o distanta fixa fata de cea \n inlocuita. De exemplu, cu o deplasare de cinci pozitii in alfabetul limbii romane, A este inlocuit cu F, B devine G si asa mai departe. Aceasta metoda este \n numita asa dupa Iulius Cezar, care o folosea a comunica cu generalii sai. Acest cifru nu ofera securitate suficienta',font=("Times New Roman",11))
        descriere.place (x=20,y=40)

        #caseta intrare text
        IntrareC=Label(Caesar,text="Introduceti textul")
        IntrareC.place(x=20,y=120)
        self.intCaesar=Text(Caesar,height=4,width=50,wrap='word')
        self.intCaesar.place(x=20,y=150)

        #caseta intrare cheie
        Intrarekey=Label(Caesar,text="Introduceti cheia (numar intreg) (pentru decriptare folositi opusul numarului introdus drept cheie)")
        Intrarekey.place(x=20,y=230)
        self.intkey=Entry(Caesar)
        self.intkey.place(x=20,y=260)

        exitCaesar=self.exitbutton(Caesar)

        #caseta iesire text procesat
        self.iesireCaesar=Text(Caesar,height=4,width=50,wrap='word')
        self.iesireCaesar.place(x=20,y=325)

        #buton criptare/decriptare
        encButCaesar=Button(Caesar, text="Criptare/Decriptare",command=self.Caesar_encrypt)
        encButCaesar.place(x=20,y=290)



    def Reverse_encrypt(self):
        text=self.intRev.get("1.0",'end-1c')
        cyphertext=""
        for i in range(len(text)):
            cyphertext+=text[len(text)-1-i]
        self.iesireRev.delete('1.0', END)
        self.iesireRev.insert(END,cyphertext)


    # Fct deschidere 
    # fereastra cifrului Reverse
    # GATA
    def open_Reverse_win(self):
        Reverse=Toplevel(ecran)
        Reverse.geometry("930x600")
        Reverse.title("Reverse")
        Reverse.resizable(width=False, height=False)
        TitluReverse=Label(Reverse,text="Cifrul Reverse", font=("Arial Black",15))
        TitluReverse.place(x=20,y=10)
        descriere=Label(Reverse,text='descriere Reverse',font=("Times New Roman",11))
        descriere.place (x=20,y=40)

        self.intRev=Text(Reverse,height=4,width=100,wrap='word')
        self.intRev.place(x=20,y=100)
        self.encRev=Button(Reverse,text="Criptare",command=self.Reverse_encrypt)
        self.encRev.place(x=20,y=180)
        self.iesireRev=Text(Reverse,height=4,width=100,wrap='word')
        self.iesireRev.place(x=20,y=220)
        exitRev=self.exitbutton(Reverse)
    




    def Substitution_encrypt(self):
        key=self.intkeyS.get("1.0",'end-1c')
        key=key.lower()
        text=self.intSub.get("1.0",'end-1c')
        cyphertext=""
        for char in text:
            if not char.isalpha():
                cyphertext+=char
            else:
                if char.isupper():
                    cyphertext+=key[ord(char)-65]
                else:
                    cyphertext+=key[ord(char)-97]
        self.iesireSub.delete('1.0',END)
        self.iesireSub.insert(END,cyphertext)


    def Substitution_decrypt(self):
        key=self.intkeyS1.get("1.0",'end-1c')
        key=key.lower()
        text=self.intSub1.get("1.0",'end-1c')
        cyphertext=""
        for char in text:
            if not char.isalpha():
                cyphertext+=char
            else:
                if char.isupper():
                    cyphertext+=key[ord(char)-65]
                else:
                    cyphertext+=key[ord(char)-97]
        self.iesireSub1.delete('1.0',END)
        self.iesireSub1.insert(END,cyphertext)

    
    # Fct deschidere 
    # fereastra cifrului Substitution
    # GATA
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
        intrare.place(x=20,y=130)
        self.intSub=Text(Substitution,height=4,width=35,wrap='word')
        self.intSub.place(x=20,y=160)


        #caseta de intrare cheie la criptare
        intkey1=Label(Substitution,text="Introduceti cheia")
        intkey1.place(x=20,y=230)
        self.intkeyS=Text(Substitution,height=1,width=30)
        self.intkeyS.place(x=20,y=260)


        #buton criptare
        self.encSub=Button(Substitution,text="Criptare",command=self.Substitution_encrypt)
        self.encSub.place(x=20,y=290)


        #caseta iesire criptare
        self.iesireSub=Text(Substitution,height=4,width=35,wrap='word')
        self.iesireSub.place(x=20,y=330)


        #caseta de intrare pt mesaj criptat
        intrare1=Label(Substitution,text="Introduceti mesajul criptat")
        intrare1.place(x=500,y=130)
        self.intSub1=Text(Substitution,height=4,width=35,wrap='word')
        self.intSub1.place(x=500,y=160)


        #caseta de intrare cheie la decriptare
        intkey1=Label(Substitution,text="Introduceti cheia")
        intkey1.place(x=500,y=230)
        self.intkeyS1=Text(Substitution,height=1,width=30)
        self.intkeyS1.place(x=500,y=260)


        #buton decriptare
        self.decSub1=Button(Substitution,text="Decriptare",command=self.Substitution_decrypt)
        self.decSub1.place(x=500,y=290)
        self.iesireSub1=Text(Substitution,height=4,width=35,wrap='word')
        self.iesireSub1.place(x=500,y=330)





    def egcd(self):
        a=self.a
        b=self.m
        x,y, u,v = 0,1, 1,0
        while a != 0:
            q, r = b//a, b%a
            m, n = x-u*q, y-v*q
            b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
        return gcd, x, y


    def modinv(self):
        self.a=self.key[0]
        self.b=26
        gcd, x, y = self.egcd(self.a, self.m)
        if gcd != 1:
            return None
            
        else:
            return x % m

    def Affine_encrypt(self):
        text=self.intAff.get("1.0",'end-1c')
        key=self.intkeyA.get("1.0",'end-1c')
        return ''.join([ chr((( key[0]*(ord(t) - ord('a')) + key[1] ) % 26)+ ord('a')) for t in text.replace(' ','') ])
    
    def Affine_decrypt(self):
        self.cipher=self.intAff1.get("1.0",'end-1c')
        self.key=self.intkeyV1.get("1.0",'end-1c')
        return ''.join([ chr((( self.modinv()*(ord(c) - ord('a') - key[1])) % 26) + ord('a')) for c in cipher ])
                       
 

    # Fct deschidere 
    # fereastra cifrului Affine
    # GATA
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
 

        #caseta de intrare pt mesaj necriptat
        intrare=Label(Affine,text="Introduceti mesajul necriptat")
        intrare.place(x=20,y=130)
        self.intAff=Text(Affine,height=4,width=35,wrap='word')
        self.intAff.place(x=20,y=160)


        #caseta de intrare cheie la criptare
        intkey1=Label(Affine,text="Introduceti cheia (sub forma [a,b])")
        intkey1.place(x=20,y=230)
        self.intkeyA=Text(Affine,height=1,width=30)
        self.intkeyA.place(x=20,y=260)


        #buton criptare
        self.encAff=Button(Affine,text="Criptare",command=self.Affine_encrypt)
        self.encAff.place(x=20,y=290)


        #caseta iesire criptare
        self.iesireAff=Text(Affine,height=4,width=35,wrap='word')
        self.iesireAff.place(x=20,y=330)


        #caseta de intrare pt mesaj criptat
        intrare1=Label(Affine,text="Introduceti mesajul criptat")
        intrare1.place(x=500,y=130)
        self.intAff1=Text(Affine,height=4,width=35,wrap='word')
        self.intAff1.place(x=500,y=160)


        #caseta de intrare cheie la decriptare
        intkey1=Label(Affine,text="Introduceti cheia")
        intkey1.place(x=500,y=230)
        self.intkeyV1=Text(Affine,height=1,width=30)
        self.intkeyV1.place(x=500,y=260)


        #buton decriptare
        self.decSub1=Button(Affine,text="Decriptare",command=self.Affine_decrypt)
        self.decSub1.place(x=500,y=290)
        self.iesireAff1=Text(Affine,height=4,width=35,wrap='word')
        self.iesireAff1.place(x=500,y=330)


    # Fct criptare
    # cifru Vignere
    # GATA
    def Vignere_encrypt(self):
        text=self.intVig.get("1.0",'end-1c')
        self.key = self.intkeyV.get("1.0",'end-1c')
        if len(text) != len(self.key):
            for i in range(len(text) - len(self.key)):
                self.key+=(self.key[i % len(self.key)])
        cyphertext = ""
        
        for i in range(len(text)):
            if text[i] == " " or not text[i].isalpha():
                cyphertext+=text[i]
            else:
                char = ((ord(text[i])-97) + (ord(self.key[i])-97)) % 26
                char += ord('a')
                cyphertext+=chr(char)
        self.iesireVig.delete('1.0',END)
        self.iesireVig.insert(END,cyphertext)
     
    # Fct decriptare
    # cifru Vignere
    # GATA
    def Vignere_decrypt(self):
        cyphertext=self.intVig1.get("1.0",'end-1c')
        self.dec_key = self.intkeyV1.get("1.0",'end-1c')
        if len(cyphertext) != len(self.dec_key):
            for i in range(len(cyphertext) - len(self.dec_key)):
                self.dec_key+=(self.dec_key[i % len(self.dec_key)])
        text = ""
        for i in range(len(cyphertext)):
            if cyphertext[i] == " " or not cyphertext[i].isalpha():
                text+=cyphertext[i]
            else:
                char = ((ord(cyphertext[i])-97) - (ord(self.dec_key[i])-97)) % 26
                char += ord('a')
                text+=chr(char)
        self.iesireVig1.delete('1.0',END)
        self.iesireVig1.insert(END,text)
     
    # Fct deschidere 
    # fereastra cifrului Vignere
    # GATA
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

        #caseta de intrare pt mesaj necriptat
        intrare=Label(Vignere,text="Introduceti mesajul necriptat")
        intrare.place(x=20,y=130)
        self.intVig=Text(Vignere,height=4,width=35,wrap='word')
        self.intVig.place(x=20,y=160)


        #caseta de intrare cheie la criptare
        intkey1=Label(Vignere,text="Introduceti cheia (un cuvant)")
        intkey1.place(x=20,y=230)
        self.intkeyV=Text(Vignere,height=1,width=30)
        self.intkeyV.place(x=20,y=260)


        #buton criptare
        self.encVig=Button(Vignere,text="Criptare",command=self.Vignere_encrypt)
        self.encVig.place(x=20,y=290)


        #caseta iesire criptare
        self.iesireVig=Text(Vignere,height=4,width=35,wrap='word')
        self.iesireVig.place(x=20,y=330)


        #caseta de intrare pt mesaj criptat
        intrare1=Label(Vignere,text="Introduceti mesajul criptat")
        intrare1.place(x=500,y=130)
        self.intVig1=Text(Vignere,height=4,width=35,wrap='word')
        self.intVig1.place(x=500,y=160)


        #caseta de intrare cheie la decriptare
        intkey1=Label(Vignere,text="Introduceti cheia (un cuvant)")
        intkey1.place(x=500,y=230)
        self.intkeyV1=Text(Vignere,height=1,width=30)
        self.intkeyV1.place(x=500,y=260)


        #buton decriptare
        self.decVig1=Button(Vignere,text="Decriptare",command=self.Vignere_decrypt)
        self.decVig1.place(x=500,y=290)
        self.iesireVig1=Text(Vignere,height=4,width=35,wrap='word')
        self.iesireVig1.place(x=500,y=330)

    def help_page(self):
        help=Toplevel(ecran)
        help.geometry("400x300")
        help.title("Help")
        help.resizable(width=False, height=False)
        exithelp=Button(help,text="Exit",command=help.destroy)
        exithelp.place(x=15,y=265)

    def exitbutton(self,master):
        Exitbutton=Button(master,text="Exit",command=master.destroy)
        Exitbutton.place(x=20,y=560)


# Sa mai fac o pagina de help
# cu indicatii si informatii 

# Adauga si meniu la click dreapta

ecran=Tk()
ecran.resizable(width=False, height=False)
app=Window(ecran)
ecran.title('Crypto')
ecran.geometry("400x360+300+300")

# Rezolva problema cu
# butoanele de pe pagina principala
# si mai redu din dimensiunile
# unor ferestre

opt1=Button(ecran,text="Cifrul Caesar",width=17,height=3,font=('Helvetica',10,'bold'),command=app.open_Caesar_win)
opt1.place(x=30,y=20)

opt2=Button(ecran,text="Cifrul Reverse",width=17,height=3,font=('Helvetica',10,'bold'),command=app.open_Reverse_win)
opt2.place(x=30,y=80)

opt3=Button(ecran,text="Cifrul Substitution",width=17,height=3,font=('Helvetica',10,'bold'),command=app.open_Substitution_win)
opt3.place(x=30,y=140)

opt4=Button(ecran,text="Cifrul Affine",width=17,height=3,font=('Helvetica',10,'bold'),command=app.open_Affine_win)
opt4.place(x=225,y=20)

opt5=Button(ecran,text="Cifrul Vignere",width=17,height=3,font=('Helvetica',10,'bold'),command=app.open_Vignere_win)
opt5.place(x=225,y=80)

opt6=Button(ecran,text="Analiza de frecventa",width=17,height=3,font=('Helvetica',10,'bold'),command=app.freq_analysis_win)
opt6.place(x=225,y=140)

opt7=Button(ecran,text="Help",width=15,height=3,font=('Helvetica',10,'bold'),command=app.help_page)
opt7.place(x=130,y=220)

ecran.mainloop()
