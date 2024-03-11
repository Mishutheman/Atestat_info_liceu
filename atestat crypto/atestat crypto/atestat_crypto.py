import tkinter
from tkinter import *
from tkinter import ttk
from collections import Counter
import string
import time

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        analysisMenu = Menu(menu,tearoff=0)
        analysisMenu.add_command(label="Analiza de frecventa",command=self.freq_analysis_win)
        analysisMenu.add_command(label="Calcul invers modular",command=self.invmod_win)
        analysisMenu.add_command(label="Calcul permutare inversa",command=self.invperm_win)
        analysisMenu.add_command(label="Help",command=self.help_win)
        menu.add_cascade(label="Options", menu=analysisMenu)

        cyphersMenu=Menu(menu,tearoff=0)
        cyphersMenu.add_command(label="Caesar",command=self.open_Caesar_win)
        cyphersMenu.add_command(label="Reverse",command=self.open_Reverse_win)
        cyphersMenu.add_command(label="Substitution",command=self.open_Substitution_win)
        cyphersMenu.add_command(label="Affine",command=self.open_Affine_win)
        cyphersMenu.add_command(label="Vignere",command=self.open_Vignere_win)
        menu.add_cascade(label="Ciphers",menu=cyphersMenu)

    # Functie analiza nr de caractere
    # dintr-un mesaj introdus  
    def analysis(self):
        cuv=self.intText.get("1.0",'end-1c')
        nrlit=dict(Counter(cuv)) 
        self.iesText.delete('1.0',END)
        self.iesText.insert(END,nrlit)
        

    # Functie deschidere 
    # fereastra analiza de frecventa
    def freq_analysis_win(self):
        Freq=Toplevel(ecran)
        Freq.geometry("450x340")
        Freq.title("Analiza de frecventa")
        Freq.resizable(width=False, height=False)

        Intrare=Label(Freq,text="Introduceti textul")
        Intrare.place(x=20,y=20)

        self.intText=Text(Freq,height=4,width=50,wrap='word')
        self.intText.place(x=20,y=45)

        self.analisebutton=Button(Freq,text="Analizeaza",command=self.analysis)
        self.analisebutton.place(x=20,y=130)
        
        ies=Label(Freq,text="Caracterele din text si numarul lor de aparitii")
        ies.place(x=20,y=170)

        self.iesText=Text(Freq,height=5,width=50,wrap='word')
        self.iesText.place(x=20,y=190)

        exitfrv=Button(Freq,text="Exit",command=Freq.destroy).place(x=20,y=300)
        menufrv=self.menu(Freq)

    # Functie criptare/decriptare
    # cifru Caesar   
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
        

    # Functie deschidere 
    # fereastra cifrului Caesar
    def open_Caesar_win(self):
        Caesar=Toplevel(ecran)
        Caesar.geometry("940x500")
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

        exitCaesar=Button(Caesar,text="Exit",command=Caesar.destroy).place(x=20,y=460)

        #caseta iesire text procesat
        self.iesireCaesar=Text(Caesar,height=4,width=50,wrap='word')
        self.iesireCaesar.place(x=20,y=325)

        #buton criptare/decriptare
        encButCaesar=Button(Caesar, text="Criptare/Decriptare",command=self.Caesar_encrypt)
        encButCaesar.place(x=20,y=290)


        menuCaesar=self.menu(Caesar)

    # Functie criptare/decriptare
    # cifru Reverse  
    def Reverse_encrypt(self):
        text=self.intRev.get("1.0",'end-1c')
        cyphertext=""
        for i in range(len(text)):
            cyphertext+=text[len(text)-1-i]
        self.iesireRev.delete('1.0', END)
        self.iesireRev.insert(END,cyphertext)


    # Functie deschidere 
    # fereastra cifrului Reverse  
    def open_Reverse_win(self):
        Reverse=Toplevel(ecran)
        Reverse.geometry("930x400")
        Reverse.title("Reverse")
        Reverse.resizable(width=False, height=False)
        TitluReverse=Label(Reverse,text="Cifrul Reverse", font=("Arial Black",15))
        TitluReverse.place(x=20,y=10)
        descriere=Label(Reverse,text='Criptarea cu ajutorul cifrului Reverse se realizeaza prin inversarea ordinii caracterelor mesajului introdus. Desi ofera securitate foarte slaba daca este \n folosit de unul singur, folosirea sa alaturi de alte metode de criptare poate crea un text surprinzator de sigur.',font=("Times New Roman",11))
        descriere.place (x=20,y=40)

        self.intRev=Text(Reverse,height=4,width=100,wrap='word')
        self.intRev.place(x=20,y=100)
        self.encRev=Button(Reverse,text="Criptare/Decriptare",command=self.Reverse_encrypt)
        self.encRev.place(x=20,y=180)
        self.iesireRev=Text(Reverse,height=4,width=100,wrap='word')
        self.iesireRev.place(x=20,y=220)
        
        exitRev=Button(Reverse,text="Exit",command=Reverse.destroy).place(x=20,y=360)

        menuRev=self.menu(Reverse)
    
    # Functie criptare 
    # cifru Substitution 
    def Substitution_encrypt(self):
        key=self.intkeyS.get("1.0",'end-1c')
        key=key.lower()
        k1=list(key)
        k1.sort()
        k2=list(key)
        text=self.intSub.get("1.0",'end-1c')
        text=text.lower()
        cyphertext=""
        try:
            for char in text:
                if char != " ":
                    cyphertext+=k2[k1.index(char)]
                else:
                    cyphertext+=char
            self.iesireSub.delete('1.0',END)
            self.iesireSub.insert(END,cyphertext)
        except Exception:
            self.iesireSub.delete('1.0',END)
            self.iesireSub.insert(END,"Cheia introdusa nu este corecta!")


    # Functie decriptare 
    # cifru Substitution   
    def Substitution_decrypt(self):
        key=self.intkeyS1.get("1.0",'end-1c')
        key=key.lower()
        k1=list(key)
        k1.sort()
        k2=list(key)
        cyphertext=self.intSub1.get("1.0",'end-1c')
        textinit=""
        for char in cyphertext:
            if char != " ":
                textinit+=k2[k1.index(char)]
            else:
                textinit+=char
        self.iesireSub1.delete('1.0',END)
        self.iesireSub1.insert(END,textinit)

    
    # Functie deschidere 
    # fereastra cifrului Substitution
    def open_Substitution_win(self):
        Substitution=Toplevel(ecran)
        Substitution.geometry("930x500")
        Substitution.title("Substitution")
        Substitution.resizable(width=False, height=False)
        TitluSubstitution=Label(Substitution,text="Cifrul Substitution", font=("Arial Black",15))
        TitluSubstitution.place(x=20,y=10)
        descriere=Label(Substitution,text='Cifrul substitutiei este un tip de cifru in care fiecare caracter al unui mesaj este schimbat cu un alt caracter al unei chei criptografice. Ofera o securitate \n slaba, deoarece poate fi spart cu usurinta cu ajutorul analizei de frecventa a caracterelor.',font=("Times New Roman",11))   
        descriere.place (x=20,y=40)

        exitSub=Button(Substitution,text="Exit",command=Substitution.destroy).place(x=20,y=460)


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

        menuSub=self.menu(Substitution)

    # Functie criptare 
    # cifru Affine 
    def Affine_encrypt(self):
        self.text=self.intAff.get("1.0",'end-1c')
        a=int(self.intkeyAa.get("1.0",'end-1c'))
        b=int(self.intkeyAb.get("1.0",'end-1c'))
        cyphertext=""
        for char in self.text:
            if char.isalpha():
                nr=ord(char)
                cyphertext+=chr((( a*(nr - 97) + b ) % 26)+ 97)
            else:
                cyphertext+=char
        self.iesireAff.delete('1.0',END)
        self.iesireAff.insert(END,cyphertext)
    

    # Functie decriptare
    # cifru Affine  
    def Affine_decrypt(self):
        self.cipher=self.intAff1.get("1.0",'end-1c')
        inv=int(self.intkeyA1a.get("1.0",'end-1c'))
        b=int(self.intkeyA1b.get("1.0",'end-1c'))
        textinit=""
        for char in self.cipher:
            if char.isalpha():
                textinit+=chr((( inv*(ord(char)-ord('a') - b) % 26)+ ord('a')))
            else:
                textinit+=char
        self.iesireAff1.delete('1.0',END)
        self.iesireAff1.insert(END,textinit)           
 

    # Functie deschidere 
    # fereastra cifrului Affine  
    def open_Affine_win(self):
        Affine=Toplevel(ecran)
        Affine.geometry("930x500")
        Affine.title("Affine")
        Affine.resizable(width=False, height=False)
        TitluAffine=Label(Affine,text="Cifrul Affine", font=("Arial Black",15))
        TitluAffine.place(x=20,y=10)
        descriere=Label(Affine,text='Cifrul Affine este un tip de criptare monoalfabetica in care fiecarei litere din alfabet ii corespunde un echivalent numeric, criptat cu ajutorul unei functii \n matematice simple de forma f(x)=(ax+b) mod 26, unde b este un numar intreg, iar a este un numar pentru care exista un invers modular notat cu A, \n adica (a*A) = 1 mod 26 ',font=("Times New Roman",11))        
        descriere.place (x=20,y=40)

        exitAffine=Button(Affine,text="Exit",command=Affine.destroy).place(x=20,y=460)
 

        #caseta de intrare pt mesaj necriptat
        intrare=Label(Affine,text="Introduceti mesajul necriptat")
        intrare.place(x=20,y=130)
        self.intAff=Text(Affine,height=4,width=35,wrap='word')
        self.intAff.place(x=20,y=160)


        #caseta de intrare valoare 'a' la criptare
        intkey1=Label(Affine,text="Introduceti cheia (valoarea lui a in prima caseta, valoarea lui b in cea de-a doua)")
        intkey1.place(x=20,y=230)
        self.intkeyAa=Text(Affine,height=1,width=2)
        self.intkeyAa.place(x=20,y=260)

        #caseta de intrare valoare 'b' la criptare
        self.intkeyAb=Text(Affine,height=1,width=2)
        self.intkeyAb.place(x=60,y=260)


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


        #caseta de intrare valoare 'a' la decriptare
        intkey1=Label(Affine,text="Introduceti cheia (valoarea lui a in prima caseta, valoarea lui b in cea de-a doua)")
        intkey1.place(x=500,y=230)
        self.intkeyA1a=Text(Affine,height=1,width=2)
        self.intkeyA1a.place(x=500,y=260)

        #caseta de intrare valoare 'b' la decriptare
        self.intkeyA1b=Text(Affine,height=1,width=2)
        self.intkeyA1b.place(x=540,y=260)


        #buton decriptare
        self.decSub1=Button(Affine,text="Decriptare",command=self.Affine_decrypt)
        self.decSub1.place(x=500,y=290)
        self.iesireAff1=Text(Affine,height=4,width=35,wrap='word')
        self.iesireAff1.place(x=500,y=330)

        menuAff=self.menu(Affine)


    # Functie criptare
    # cifru Vignere  
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
     
    # Functie decriptare
    # cifru Vignere   
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
     
    # Functie deschidere 
    # fereastra cifrului Vignere
    def open_Vignere_win(self):
        Vignere=Toplevel(ecran)
        Vignere.geometry("930x500")
        Vignere.title("Vignere")
        Vignere.resizable(width=False, height=False)
        TitluVignere=Label(Vignere,text="Cifrul Vignere", font=("Arial Black",15))
        TitluVignere.place(x=20,y=10)
        descriere=Label(Vignere,text='Cifrul Vignere este o metoda de criptare polialfabetica ce are la baza un tabel alcatuit din 26 de cifruri Caesar, depinzand de o cheie criptografica. \n Cifrul este usor de inteles si implementat, dar a rezistat timp de 300 de ani incercarilor de spargere, de la data aparitiei sale in 1553 pana in 1863, \n obtinand titlul de "Le Chiffrage Indechiffrable", tradus "Cifrul Indescifrabil" din franceza.' , font=("Times New Roman",11))
        descriere.place (x=20,y=40)

        exitVig=Button(Vignere,text="Exit",command=Vignere.destroy).place(x=20,y=460)

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
        
        menuVig=self.menu(Vignere)

    # Functie fereastra help
    # indicatii, contraindicatii, mod de utilizare
    def help_win(self):
        help=Toplevel(ecran)
        help.geometry("500x300")
        help.title("Help")
        help.resizable(width=False, height=False)
        titlu=Label(help,text="Mod de utilizare, indicatii si contraindicatii",font=("Times New Roman",13)).place(x=20,y=15)
        info1=Label(help,text="Mod de utilizare: Pe fereastra principala se afla butoane catre cifrurile criptografice, iar in \n ferestrele acestora se afla indicatii si informatii legate de fiecare cifru in parte. In meniul \n bara se mai afla 2 meniuri, unul cu cifrurile criptografice, si unul cu unelte care ajuta la \n folosirea eficienta a cifrurilor.").place(x=15,y=60)
        info2=Label(help,text="Indicatii: Pot fi deschise mai multe ferestre ale aceluiasi cifru sau ale aceleiasi unelte si \n pot fi folosite separat, fara a afecta celelalte ferestre").place(x=15,y=140)
        info3=Label(help,text="Contraindicatii: Acest program prezinta in termeni largi cifrurile si modurile de criptare. \n Pentru a aprofunda tehnicile de criptare si analizare a cifrurilor criptografice, se \n recomanda studiul materialelor de specialitate.").place(x=15,y=200)
        exithelp=Button(help,text="Exit",command=help.destroy)
        exithelp.place(x=15,y=265)
        menuhelp=self.menu(help)


    # Functii de aflat inversul
    # modular, ajuta la cifrul
    # Affine
    def xgcd(self,a,b) -> int:
        prevx, x = 1, 0; prevy, y = 0, 1
        while b:
            q = a/b
            x, prevx = prevx - q*x, x
            y, prevy = prevy - q*y, y
            a, b = b, a % b
        return a, prevx, prevy

    def modinv(self):
        a=int(self.intinv.get("1.0",'end-1c')) 
        g, x, y = self.xgcd(a, 26)
        if g != 1:
            self.iesinv.delete("1.0",END)
            self.iesinv.insert(END,"NE")
        else:
            self.iesinv.delete("1.0",END)
            self.iesinv.insert(END,int(pow(a, -1, 26)))


    # Functie fereastra
    # invers modular
    def invmod_win(self):
        invmod=Toplevel(ecran)
        invmod.geometry("400x270")
        invmod.title("Invers modular")
        invmod.resizable(width=False, height=False)

        indic=Label(invmod,text="Cu ajutorul acestei ferestre poti calcula inversul modular al unei \n variabile 'a' modulo 26",font=("Times New Roman",10))
        indic.place(x=20,y=15)

        indint=Label(invmod, text="Introduceti valoarea careia doriti sa ii aflati inversul modular").place(x=20,y=60)
        self.intinv=Text(invmod,height=1,width=4)
        self.intinv.place(x=20,y=90)

        invbut=Button(invmod,text="Procesare invers modular",command=self.modinv).place(x=20,y=125)

        iesint=Label(invmod, text="Inversul modular (se afiseaza 'NE' daca nu exista invers modular)").place(x=20,y=160)
        self.iesinv=Text(invmod,height=1,width=4)
        self.iesinv.place(x=20,y=190)

        menuinv=self.menu(invmod)
        exitinv=Button(invmod,text="Exit",command=invmod.destroy).place(x=20,y=230)

    # Program calculare 
    # permutare inversa a unei
    # chei ce contine litere si simboluri
    def inper(self): 
        perm1=""
        perm2=self.intinvper.get("1.0","end-1c")
        for char in perm2:
            if char!=" ":
                if char not in perm1:
                    perm1+=char
        q=list(perm1)
        t=list(perm2)
        q.sort()
        self.iesinvper.delete("1.0",END)
        self.iesinvper.insert(END,''.join(t))
        for i in range(len(q)-1):
            for j in range(i+1,len(q)):
                if t[i]>t[j]:
                    t[i],t[j]=t[j],t[i]
                    q[i],q[j]=q[j],q[i] 
        self.iesinvper.delete("1.0",END)
        self.iesinvper.insert(END,''.join(q))
        

    # Functie de calculare
    # a permutarii inverse a
    # unei chei compuse dintr-un
    # numar de caractere
    def invperm_win(self):
        invperm=Toplevel(ecran)
        invperm.geometry("400x260")
        invperm.title("Permutare inversa")
        invperm.resizable(width=False, height=False)

        indic=Label(invperm,text="Cu ajutorul acestei ferestre poti calcula permutarea inversa a unei \n chei folosita in criptarea cu cifrul Substitution.",font=("Times New Roman",10))
        indic.place(x=20,y=15)

        indint=Label(invperm, text="Introduceti cheia careia doriti sa ii aflati permutarea inversa").place(x=20,y=60)
        self.intinvper=Text(invperm,height=1,width=30)
        self.intinvper.place(x=20,y=90)

        invperbut=Button(invperm,text="Procesare permutarea inversa",command=self.inper).place(x=20,y=125)

        iesint=Label(invperm, text="Permutarea inversa").place(x=20,y=160)
        self.iesinvper=Text(invperm,height=1,width=30)
        self.iesinvper.place(x=20,y=190)

        menuinv=self.menu(invperm)
        exitinvperm=Button(invperm,text="Exit",command=invperm.destroy).place(x=20,y=225)

    # Functie ce afiseaza meniul 
    # de pe bara principala
    # pe toate celelalte ferestre 
    def menu(self,master):
        menu = Menu(master,tearoff=0)
        master.config(menu=menu)

        analysisMenu = Menu(menu,tearoff=0)
        analysisMenu.add_command(label="Analiza de frecventa",command=self.freq_analysis_win)
        analysisMenu.add_command(label="Calcul invers modular",command=self.invmod_win)
        analysisMenu.add_command(label="Calcul permutare inversa",command=self.invperm_win)
        analysisMenu.add_command(label="Help",command=self.help_win)
        menu.add_cascade(label="Options", menu=analysisMenu)

        cyphersMenu=Menu(menu,tearoff=0)
        cyphersMenu.add_command(label="Caesar",command=self.open_Caesar_win)
        cyphersMenu.add_command(label="Reverse",command=self.open_Reverse_win)
        cyphersMenu.add_command(label="Substitution",command=self.open_Substitution_win)
        cyphersMenu.add_command(label="Affine",command=self.open_Affine_win)
        cyphersMenu.add_command(label="Vignere",command=self.open_Vignere_win)
        menu.add_cascade(label="Ciphers",menu=cyphersMenu)

    # Functie creare buton 
    # iesire de pe pagina respectiva
    def exitbutton(self,master):
        Exitbutton=Button(master,text="Exit",command=master.destroy)
        Exitbutton.place(x=20,y=560)


ecran=Tk()
ecran.resizable(width=False, height=False)
app=Window(ecran)
ecran.title('Crypto')
ecran.geometry("400x360+300+300")

# Butoane pe pagina principala

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

opt7=Button(ecran,text="Help",width=15,height=3,font=('Helvetica',10,'bold'),command=app.help_win)
opt7.place(x=130,y=220)

ecran.mainloop()
