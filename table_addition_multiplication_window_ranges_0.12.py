# Tabliczka dodawania i mnożenia - wersja okienkowa
# Komputer przepytuje z tabliczek dodawania i mmożenia

from tkinter import *
import winsound
import random

board_a = []
board_m = []
zakres_a = 0
zakres_b = 0

#POCZĄTEK OKNA

class Application(Frame):
    """ Aplikacja z GUI, która przepytuje z tabliczki dodawania i mnożenia. """
    def __init__(self, master):
        """ Inicjalizuj ramkę. """
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()
#        self.master.geometry('-50+15')
        self.master.geometry('+60+15')

    def create_widgets(self):
        """
       widżety potrzebne do pobrania odpowiedi podanych przez
        gracza i wyświetlenia wyniku.
        """
        #etykietę z tytułem
        self.title_lbl1 = Label(self, font = ('Calibri', 8),
              text =
"  ────────────────────────────────────────────────────────────────────────────────────────────────\n\
   2  +  1  =  ?       15  +  27  =  ?       83  +  9  =  ?       81  +  3  = ?\
       27  +  5  =  ?       9  +  2  =  ?       3  +  11  =  ?\n\
  ────────────────────────────────────────────────────────────────────────────────────────────────"
              ).grid(row = 0, column = 0, columnspan = 13)
        
        self.title_lbl2 = Label(self, font = ('Calibri', 11),
              text =
" TABLICZKA DODAWANIA / MNOŻENIA\n\
  Witaj w największym intelektualnym wyzwaniu wszech czasów, jakimi są zmagania z :\n\
  'Tabliczką dodawania'     i     'Tabliczką mnożenia'."
              ).grid(row = 1, column = 0, columnspan = 13)

        self.title_lbl3 = Label(self, font = ('Calibri', 8),
              text =
" ────────────────────────────────────────────────────────────────────────────────────────────────\n\
   2  *  43  =  ?       51  *  9  =  ?       7  *  41  =  ?       8  *  5  = ?\
       24  *  84  =  ?       97  *  2  =  ?       3  *  9  =  ?\n\
  ────────────────────────────────────────────────────────────────────────────────────────────────"
              ).grid(row = 2, column = 0, columnspan = 13)

        # utworzenie zmiennej, która ma reprezentować wybór tabliczki
        self.table = StringVar()
        self.table.set(None)
        #przyciski opcji do wyboru tabliczki dodawania lub mnożenia

        Radiobutton(self, font=('Calibri', 11),
                    text = "Tabliczka dodawania",
                    indicatoron = 0,
                    width = 23,
                    pady = 10,
                    variable = self.table,
                    value = "a",
                    command = self.addition_table
                    ).grid(row = 15, column = 1,columnspan = 4)

        Radiobutton(self, font=('Calibri', 11),
                    text = "Tabliczka mnożenia  ",
                    indicatoron = 0,
                    width = 23,
                    variable = self.table,
                    pady = 10,
                    value = "m",
                    command = self.multiplication_table
                    ).grid(row = 15, column = 8, columnspan = 4)

        #etykieta z pustą linią nad oknem tytułu tabliczki
        self.linia = Label(self, font = ('Courier New', 5),text = " ").grid(row = 16, column = 1)

        # utwórzenie zmiennej, która ma reprezentować wybór nowej tabliczki dodawania
        self.table_a = StringVar()
        self.table_a.set(None)
        # utwórzenie przycisku opcji do wyboru tabliczki dodawania nowa
        Radiobutton(self, font=('Calibri', 10),
                    text = "Nowa tabliczka",
                    indicatoron = 0,
                    width = 19,
                    variable = self.table_a,
                    value = "n",
                    command = self.addition_table_new
                    ).grid(row = 17, column = 1,columnspan = 4)

        # utwórzenie zmiennej, która ma reprezentować wybór nowej tabliczki mnożenia
        self.table_m = StringVar()
        self.table_m.set(None)
        # utwórzenie przycisku opcji do wyboru tabliczki mnożenia
        Radiobutton(self, font=('Calibri', 10),
                    text = "Nowa tabliczka",
                    indicatoron = 0,
                    width = 19,
                    variable = self.table_m,
                    value = "n",
                    command = self.multiplication_table_new
                    ).grid(row = 17, column = 8,columnspan = 4)#, sticky = E)


        #etykieta z pustą linią nad przycIskiem nowych tabliczek
        self.linia = Label(self, font = ('Courier New', 5),text = " ").grid(row = 18, column = 1)

        self.range_a = StringVar()
        self.range_a.set(None)#'p')
        # utwórzenie przycisku opcji do wyboru tabliczki dodawania nowa
        Radiobutton(self, font=('Calibri', 10),
                    text = "Zakres\n1 ÷ 10",
                    indicatoron = 0,
                    width = 11,
                    height = 2,
                    variable = self.range_a,
                    value = "p",
                    command = self.addition_table_new_range
                    ).grid(row = 19, column = 1,columnspan = 2, sticky = W)

        # utwórzenie przycisku opcji do wyboru tabliczki dodawania kontynuacja
        Radiobutton(self, font=('Calibri', 10),
                    text = "Zakres\n1 ÷ 100",
                    indicatoron = 0,
                    width = 11,
                    height = 2,
                    variable = self.range_a,
                    value = "r",
                    command = self.addition_table_new_range
                    ).grid(row = 19, column = 3, columnspan = 2, sticky = E)

        #utwórzenie zmiennej, która ma reprezentować wybór zakresu
        #zakres zmiennych tabliczki dodawania: 1 ÷ 10 lub 1 ÷ 100
        self.range_m = StringVar()
        self.range_m.set(None)#'p')
        # utwórzenie przycisku opcji do wyboru tabliczki dodawania nowa
        Radiobutton(self, font=('Calibri', 10),
                    text = "Zakres\n1 ÷ 10",
                    indicatoron = 0,
                    width = 11,
                    variable = self.range_m,
                    height = 2,
                    value = "p",
                    command = self.multiplication_table_new_range
                    ).grid(row = 19, column = 8,columnspan = 2, sticky = W)

        # utwórzenie przycisku opcji do wyboru tabliczki dodawania kontynuacja
        Radiobutton(self, font=('Calibri', 10),
                    text = "Zakres\n1 ÷ 100",
                    indicatoron = 0,
                    width = 11,
                    height = 2,
                    variable = self.range_m,
                    value = "r",
                    command = self.multiplication_table_new_range
                    ).grid(row = 19, column = 10, columnspan = 2, sticky = E)
        #etykieta z pustą linią nad oknem tytułu tabliczki
        self.linia = Label(self, font = ('Courier New', 11),text = " ").grid(row = 25, column = 1)

        #okno z tytułem tabliczki
        self.table_000_txt = Text(self,font=('Courier New',11),width= 25,height=1,padx=5,pady=5)
        self.table_000_txt.grid(row = 26, column = 3, columnspan = 7)

        #etykieta z pustą linią nad oknami pytania i odpowiedzi
        self.linia = Label(self, font = ('Courier New', 11),text = " ").grid(row = 27, column = 1)

        #etykieta i okno z pytaniem
        self.quess_lbl = Label(self,
                               font = ('Calibri', 11),
                               text = '    Ile jest :  ',
                               justify='left'
                               ).grid(row = 28, column = 1, columnspan = 2)
        #okno pytania
        self.quess_txt = Text(self, font=('Courier New', 11), bg = 'yellow', width = 11, height = 1) 
        self.quess_txt.grid(row = 28, column = 3, columnspan = 8, sticky = W)

        #etykieta i pole znakowe służące do wpisania odpowiedzi
        self.answer_lbl = Label(self, font = ('calibri', 11),
                                text = '        Twoja odpowiedź :'
                                ).grid(row = 28, column = 5, columnspan = 4)
        #pole znakowe służące do wpisania odpowiedzi z kontrolą wpisywanych znaków - tylko cyfry
        sv = StringVar()
        self.answer = Entry(self,
                            font = ('Courier New', 11),
                            justify = CENTER,
                            textvariable = sv,
                            width = 11
                            )
        self.answer.grid(row = 28, column = 9, columnspan = 4, sticky = W)#
        sv.trace('w', lambda nm, idx, mode, var=sv: self.validate_float(var)) #walidacja wprowadzanych danych

        #etykieta z pustą linią przed przyciskiem 'OK'
        self.linia = Label(self, font = ('Courier New', 11),text = " ").grid(row = 29, column = 1)

        #przycisk - Przycisk 'OK' - odpowiedź - tylko obrazek
        self.answer_OK = Button(self,
                                text = "OK",
                                font = ('calibri',13, 'underline'),
                                padx = 200,
                                pady = 2,
                                bd = 4
                                )
        self.answer_OK.grid(row = 30, column = 1, rowspan = 2, columnspan = 11)#, sticky = E)	
#        self.answer_OK.bind("<Return>",self.answer_a_get) #uruchonminie działania klawisza enter
#        self.answer_OK.bind("<Button>",self.answer_a_get) #uruchonminie działania lewego przycisku myszy
#                                state = 'active'
#                                command = self.answer_a_get

        #etykieta z pustą linią przed oknem potwierdzenia odpowiedzi
        self.linia = Label(self, font = ('Courier New', 11),text = "   ").grid(row = 32, column = 1)

        #OKNO POTWIERDZENIA ODPOWIEDZI
        self.answer_txt = Text(self,
                               font=('Courier New', 11),
                               width = 48,
                               height = 2,
                               padx = 2) #, pady = 2) 
        self.answer_txt.grid(row = 33, column = 1, columnspan = 11)

        #etykieta z pustą linią poD oknem potwierdzenia odpowiedzi
        self.linia = Label(self, font = ('Courier New', 11),text = "").grid(row = 34, column = 1)

        # puste etykiety do formatowania położenia okienek

        #etykietę z pustą linią '0' -'' - lewa ramka - kolumna lewa skrajna
        self.linia = Label(self, font = ('Courier New', 11),
              text = "            "
              ).grid(row = 60, column = 0)

       #etykietę z pustą linią '2' '' - prawa ramka - kolumna prawa skrajna
        self.linia = Label(self, font = ('Courier New', 11),
              text = "            "
              ).grid(row = 60, column = 12)

        #etykieta z pustą linią przed przyciskiem 'KONIEC'
        self.linia = Label(self, font = ('Courier New', 11),text = "").grid(row = 59, column = 1)

        #przycisk zamknięcia okna i zakończenia programu
        self.koniec_ost = Button(self,
                                 text = "KONIEC",
                                 font = ('calibri',13, 'underline'),
                                 padx = 35,
                                 command = root.destroy)
        self.koniec_ost.grid(row = 60, column = 1, columnspan = 11)

       #etykietę z pustą linią pod przyciskiem 'KONIEC'
        self.linia = Label(self, font = ('Courier New', 11),text = "").grid(row = 61, column = 1)

#POCZĄTEK OKNA TABLICZKI
#POLA TEKSTOWE TABLICZKI DO WYŚWIETLENIA PRAWIDŁOWYCH ODPOWIEDZI (11 x 11)
#WIERSZ '0'
        self.table_00_txt=Text(self,font=('Courier New',11),bg='#80ff00',width=4,height=1,padx=5,pady=5);self.table_00_txt.grid(row=40,column=1,sticky=E)
        self.table_01_txt=Text(self,font=('Courier New',11),bg='#80ff00',width=4,height=1,padx=5,pady=5);self.table_01_txt.grid(row=40,column=2,sticky=E)
        self.table_02_txt=Text(self,font=('Courier New',11),bg='#80ff00',width=4,height=1,padx=5,pady=5);self.table_02_txt.grid(row=40,column=3,sticky=E)
        self.table_03_txt=Text(self,font=('Courier New',11),bg='#80ff00',width=4,height=1,padx=5,pady=5);self.table_03_txt.grid(row=40,column=4,sticky=E)
        self.table_04_txt=Text(self,font=('Courier New',11),bg='#80ff00',width=4,height=1,padx=5,pady=5);self.table_04_txt.grid(row=40,column=5,sticky=E)
        self.table_05_txt=Text(self,font=('Courier New',11),bg='#80ff00',width=4,height=1,padx=5,pady=5);self.table_05_txt.grid(row=40,column=6,sticky=E)
        self.table_06_txt=Text(self,font=('Courier New',11),bg='#80ff00',width=4,height=1,padx=5,pady=5);self.table_06_txt.grid(row=40,column=7,sticky=E)
        self.table_07_txt=Text(self,font=('Courier New',11),bg='#80ff00',width=4,height=1,padx=5,pady=5);self.table_07_txt.grid(row=40,column=8,sticky=E)
        self.table_08_txt=Text(self,font=('Courier New',11),bg='#80ff00',width=4,height=1,padx=5,pady=5);self.table_08_txt.grid(row=40,column=9,sticky=E)
        self.table_09_txt=Text(self,font=('Courier New',11),bg='#80ff00',width=4,height=1,padx=5,pady=5);self.table_09_txt.grid(row=40,column=10,sticky=E)
        self.table_010_txt=Text(self,font=('Courier New',11),bg='#80ff00',width=4,height=1,padx=5,pady=5);self.table_010_txt.grid(row=40,column=11,sticky=E)
#WIERSZ '1'
        self.table_10_txt=Text(self,font=('Courier New',11),bg='#80ff00',width=4,height=1,padx=5,pady=5);self.table_10_txt.grid(row=41,column=1,sticky=E)
        self.table_11_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_11_txt.grid(row=41,column=2,sticky=E)
        self.table_12_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_12_txt.grid(row=41,column=3,sticky=E)
        self.table_13_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_13_txt.grid(row=41,column=4,sticky=E)
        self.table_14_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_14_txt.grid(row=41,column=5,sticky=E)
        self.table_15_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_15_txt.grid(row=41,column=6,sticky=E)
        self.table_16_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_16_txt.grid(row=41,column=7,sticky=E)
        self.table_17_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_17_txt.grid(row=41,column=8,sticky=E)
        self.table_18_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_18_txt.grid(row=41,column=9,sticky=E)
        self.table_19_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_19_txt.grid(row=41,column=10,sticky=E)
        self.table_110_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_110_txt.grid(row=41,column=11,sticky=E)
#WIERSZ '2'
        self.table_20_txt=Text(self,font=('Courier New',11),bg='#80ff00',width=4,height=1,padx=5,pady=5);self.table_20_txt.grid(row=42,column=1,sticky=E)
        self.table_21_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_21_txt.grid(row=42,column=2,sticky=E)
        self.table_22_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_22_txt.grid(row=42,column=3,sticky=E)
        self.table_23_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_23_txt.grid(row=42,column=4,sticky=E)
        self.table_24_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_24_txt.grid(row=42,column=5,sticky=E)
        self.table_25_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_25_txt.grid(row=42,column=6,sticky=E)
        self.table_26_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_26_txt.grid(row=42,column=7,sticky=E)
        self.table_27_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_27_txt.grid(row=42,column=8,sticky=E)
        self.table_28_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_28_txt.grid(row=42,column=9,sticky=E)
        self.table_29_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_29_txt.grid(row=42,column=10,sticky=E)
        self.table_210_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_210_txt.grid(row=42,column=11,sticky=E)
#WIERSZ'3'
        self.table_30_txt=Text(self,font=('Courier New',11),bg='#80ff00',width=4,height=1,padx=5,pady=5);self.table_30_txt.grid(row=43,column=1,sticky=E)
        self.table_31_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_31_txt.grid(row=43,column=2,sticky=E)
        self.table_32_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_32_txt.grid(row=43,column=3,sticky=E)
        self.table_33_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_33_txt.grid(row=43,column=4,sticky=E)
        self.table_34_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_34_txt.grid(row=43,column=5,sticky=E)
        self.table_35_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_35_txt.grid(row=43,column=6,sticky=E)
        self.table_36_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_36_txt.grid(row=43,column=7,sticky=E)
        self.table_37_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_37_txt.grid(row=43,column=8,sticky=E)
        self.table_38_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_38_txt.grid(row=43,column=9,sticky=E)
        self.table_39_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_39_txt.grid(row=43,column=10,sticky=E)
        self.table_310_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_310_txt.grid(row=43,column=11,sticky=E)
#WIERSZ'4'
        self.table_40_txt=Text(self,font=('Courier New',11),bg='#80ff00',width=4,height=1,padx=5,pady=5);self.table_40_txt.grid(row=44,column=1,sticky=E)
        self.table_41_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_41_txt.grid(row=44,column=2,sticky=E)
        self.table_42_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_42_txt.grid(row=44,column=3,sticky=E)
        self.table_43_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_43_txt.grid(row=44,column=4,sticky=E)
        self.table_44_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_44_txt.grid(row=44,column=5,sticky=E)
        self.table_45_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_45_txt.grid(row=44,column=6,sticky=E)
        self.table_46_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_46_txt.grid(row=44,column=7,sticky=E)
        self.table_47_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_47_txt.grid(row=44,column=8,sticky=E)
        self.table_48_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_48_txt.grid(row=44,column=9,sticky=E)
        self.table_49_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_49_txt.grid(row=44,column=10,sticky=E)
        self.table_410_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_410_txt.grid(row=44,column=11,sticky=E)
#WIERSZ'5'
        self.table_50_txt=Text(self,font=('Courier New',11),bg='#80ff00',width=4,height=1,padx=5,pady=5);self.table_50_txt.grid(row=45,column=1,sticky=E)
        self.table_51_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_51_txt.grid(row=45,column=2,sticky=E)
        self.table_52_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_52_txt.grid(row=45,column=3,sticky=E)
        self.table_53_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_53_txt.grid(row=45,column=4,sticky=E)
        self.table_54_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_54_txt.grid(row=45,column=5,sticky=E)
        self.table_55_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_55_txt.grid(row=45,column=6,sticky=E)
        self.table_56_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_56_txt.grid(row=45,column=7,sticky=E)
        self.table_57_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_57_txt.grid(row=45,column=8,sticky=E)
        self.table_58_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_58_txt.grid(row=45,column=9,sticky=E)
        self.table_59_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_59_txt.grid(row=45,column=10,sticky=E)
        self.table_510_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_510_txt.grid(row=45,column=11,sticky=E)
#WIERSZ'6'
        self.table_60_txt=Text(self,font=('Courier New',11),bg='#80ff00',width=4,height=1,padx=5,pady=5);self.table_60_txt.grid(row=46,column=1,sticky=E)
        self.table_61_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_61_txt.grid(row=46,column=2,sticky=E)
        self.table_62_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_62_txt.grid(row=46,column=3,sticky=E)
        self.table_63_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_63_txt.grid(row=46,column=4,sticky=E)
        self.table_64_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_64_txt.grid(row=46,column=5,sticky=E)
        self.table_65_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_65_txt.grid(row=46,column=6,sticky=E)
        self.table_66_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_66_txt.grid(row=46,column=7,sticky=E)
        self.table_67_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_67_txt.grid(row=46,column=8,sticky=E)
        self.table_68_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_68_txt.grid(row=46,column=9,sticky=E)
        self.table_69_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_69_txt.grid(row=46,column=10,sticky=E)
        self.table_610_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_610_txt.grid(row=46,column=11,sticky=E)
#WIERSZ'7'
        self.table_70_txt=Text(self,font=('Courier New',11),bg='#80ff00',width=4,height=1,padx=5,pady=5);self.table_70_txt.grid(row=47,column=1,sticky=E)
        self.table_71_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_71_txt.grid(row=47,column=2,sticky=E)
        self.table_72_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_72_txt.grid(row=47,column=3,sticky=E)
        self.table_73_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_73_txt.grid(row=47,column=4,sticky=E)
        self.table_74_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_74_txt.grid(row=47,column=5,sticky=E)
        self.table_75_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_75_txt.grid(row=47,column=6,sticky=E)
        self.table_76_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_76_txt.grid(row=47,column=7,sticky=E)
        self.table_77_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_77_txt.grid(row=47,column=8,sticky=E)
        self.table_78_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_78_txt.grid(row=47,column=9,sticky=E)
        self.table_79_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_79_txt.grid(row=47,column=10,sticky=E)
        self.table_710_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_710_txt.grid(row=47,column=11,sticky=E)
#WIERSZ'8'
        self.table_80_txt=Text(self,font=('Courier New',11),bg='#80ff00',width=4,height=1,padx=5,pady=5);self.table_80_txt.grid(row=48,column=1,sticky=E)
        self.table_81_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_81_txt.grid(row=48,column=2,sticky=E)
        self.table_82_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_82_txt.grid(row=48,column=3,sticky=E)
        self.table_83_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_83_txt.grid(row=48,column=4,sticky=E)
        self.table_84_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_84_txt.grid(row=48,column=5,sticky=E)
        self.table_85_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_85_txt.grid(row=48,column=6,sticky=E)
        self.table_86_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_86_txt.grid(row=48,column=7,sticky=E)
        self.table_87_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_87_txt.grid(row=48,column=8,sticky=E)
        self.table_88_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_88_txt.grid(row=48,column=9,sticky=E)
        self.table_89_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_89_txt.grid(row=48,column=10,sticky=E)
        self.table_810_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_810_txt.grid(row=48,column=11,sticky=E)
#WIERSZ'9'
        self.table_90_txt=Text(self,font=('Courier New',11),bg='#80ff00',width=4,height=1,padx=5,pady=5);self.table_90_txt.grid(row=49,column=1,sticky=E)
        self.table_91_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_91_txt.grid(row=49,column=2,sticky=E)
        self.table_92_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_92_txt.grid(row=49,column=3,sticky=E)
        self.table_93_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_93_txt.grid(row=49,column=4,sticky=E)
        self.table_94_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_94_txt.grid(row=49,column=5,sticky=E)
        self.table_95_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_95_txt.grid(row=49,column=6,sticky=E)
        self.table_96_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_96_txt.grid(row=49,column=7,sticky=E)
        self.table_97_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_97_txt.grid(row=49,column=8,sticky=E)
        self.table_98_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_98_txt.grid(row=49,column=9,sticky=E)
        self.table_99_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_99_txt.grid(row=49,column=10,sticky=E)
        self.table_910_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_910_txt.grid(row=49,column=11,sticky=E)
#WIERSZ'10'
        self.table_100_txt=Text(self,font=('Courier New',11),bg='#80ff00',width=4,height=1,padx=5,pady=5);self.table_100_txt.grid(row=50,column=1,sticky=E)
        self.table_101_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_101_txt.grid(row=50,column=2,sticky=E)
        self.table_102_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_102_txt.grid(row=50,column=3,sticky=E)
        self.table_103_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_103_txt.grid(row=50,column=4,sticky=E)
        self.table_104_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_104_txt.grid(row=50,column=5,sticky=E)
        self.table_105_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_105_txt.grid(row=50,column=6,sticky=E)
        self.table_106_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_106_txt.grid(row=50,column=7,sticky=E)
        self.table_107_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_107_txt.grid(row=50,column=8,sticky=E)
        self.table_108_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_108_txt.grid(row=50,column=9,sticky=E)
        self.table_109_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_109_txt.grid(row=50,column=10,sticky=E)
        self.table_1010_txt=Text(self,font=('Courier New',11),width=4,height=1,padx=5,pady=5);self.table_1010_txt.grid(row=50,column=11,sticky=E)
#KONIEC OKNA TABLICZKI


#TABLICA - WPISANIE WYNIKÓW
    def display_board(self, x, y, board):
        """Wyświetl planszę gry na ekranie."""

#Wpisywanie odpowiedzi do tabeli dodawania i wyświetlanie tablicy z odpowiedzisami
#wiersz'0' - oznaczenia kolumn - cyfry
        self.table_00_txt.delete(0.0,END);self.table_00_txt.insert(0.0,board[0][0])
        self.table_01_txt.delete(0.0,END);self.table_01_txt.insert(0.0,board[0][1])
        self.table_02_txt.delete(0.0,END);self.table_02_txt.insert(0.0,board[0][2])
        self.table_03_txt.delete(0.0,END);self.table_03_txt.insert(0.0,board[0][3])
        self.table_04_txt.delete(0.0,END);self.table_04_txt.insert(0.0,board[0][4])
        self.table_05_txt.delete(0.0,END);self.table_05_txt.insert(0.0,board[0][5])
        self.table_06_txt.delete(0.0,END);self.table_06_txt.insert(0.0,board[0][6])
        self.table_07_txt.delete(0.0,END);self.table_07_txt.insert(0.0,board[0][7])
        self.table_08_txt.delete(0.0,END);self.table_08_txt.insert(0.0,board[0][8])
        self.table_09_txt.delete(0.0,END);self.table_09_txt.insert(0.0,board[0][9])
        self.table_010_txt.delete(0.0,END);self.table_010_txt.insert(0.0,board[0][10])
#wiersz'1' - kolumna 0 - oznaczenie wiersza - cyfra
        self.table_10_txt.delete(0.0,END);self.table_10_txt.insert(0.0,board[1][0])
        self.table_11_txt.delete(0.0,END);self.table_11_txt.insert(0.0,board[1][1])
        self.table_12_txt.delete(0.0,END);self.table_12_txt.insert(0.0,board[1][2])
        self.table_13_txt.delete(0.0,END);self.table_13_txt.insert(0.0,board[1][3])
        self.table_14_txt.delete(0.0,END);self.table_14_txt.insert(0.0,board[1][4])
        self.table_15_txt.delete(0.0,END);self.table_15_txt.insert(0.0,board[1][5])
        self.table_16_txt.delete(0.0,END);self.table_16_txt.insert(0.0,board[1][6])
        self.table_17_txt.delete(0.0,END);self.table_17_txt.insert(0.0,board[1][7])
        self.table_18_txt.delete(0.0,END);self.table_18_txt.insert(0.0,board[1][8])
        self.table_19_txt.delete(0.0,END);self.table_19_txt.insert(0.0,board[1][9])
        self.table_110_txt.delete(0.0,END);self.table_110_txt.insert(0.0,board[1][10])
#wiersz'2'
        self.table_20_txt.delete(0.0,END);self.table_20_txt.insert(0.0,board[2][0])
        self.table_21_txt.delete(0.0,END);self.table_21_txt.insert(0.0,board[2][1])
        self.table_22_txt.delete(0.0,END);self.table_22_txt.insert(0.0,board[2][2])
        self.table_23_txt.delete(0.0,END);self.table_23_txt.insert(0.0,board[2][3])
        self.table_24_txt.delete(0.0,END);self.table_24_txt.insert(0.0,board[2][4])
        self.table_25_txt.delete(0.0,END);self.table_25_txt.insert(0.0,board[2][5])
        self.table_26_txt.delete(0.0,END);self.table_26_txt.insert(0.0,board[2][6])
        self.table_27_txt.delete(0.0,END);self.table_27_txt.insert(0.0,board[2][7])
        self.table_28_txt.delete(0.0,END);self.table_28_txt.insert(0.0,board[2][8])
        self.table_29_txt.delete(0.0,END);self.table_29_txt.insert(0.0,board[2][9])
        self.table_210_txt.delete(0.0,END);self.table_210_txt.insert(0.0,board[2][10])
#wiersz'3'
        self.table_30_txt.delete(0.0,END);self.table_30_txt.insert(0.0,board[3][0])
        self.table_31_txt.delete(0.0,END);self.table_31_txt.insert(0.0,board[3][1])
        self.table_32_txt.delete(0.0,END);self.table_32_txt.insert(0.0,board[3][2])
        self.table_33_txt.delete(0.0,END);self.table_33_txt.insert(0.0,board[3][3])
        self.table_34_txt.delete(0.0,END);self.table_34_txt.insert(0.0,board[3][4])
        self.table_35_txt.delete(0.0,END);self.table_35_txt.insert(0.0,board[3][5])
        self.table_36_txt.delete(0.0,END);self.table_36_txt.insert(0.0,board[3][6])
        self.table_37_txt.delete(0.0,END);self.table_37_txt.insert(0.0,board[3][7])
        self.table_38_txt.delete(0.0,END);self.table_38_txt.insert(0.0,board[3][8])
        self.table_39_txt.delete(0.0,END);self.table_39_txt.insert(0.0,board[3][9])
        self.table_310_txt.delete(0.0,END);self.table_310_txt.insert(0.0,board[3][10])
#wiersz'4'
        self.table_40_txt.delete(0.0,END);self.table_40_txt.insert(0.0,board[4][0])
        self.table_41_txt.delete(0.0,END);self.table_41_txt.insert(0.0,board[4][1])
        self.table_42_txt.delete(0.0,END);self.table_42_txt.insert(0.0,board[4][2])
        self.table_43_txt.delete(0.0,END);self.table_43_txt.insert(0.0,board[4][3])
        self.table_44_txt.delete(0.0,END);self.table_44_txt.insert(0.0,board[4][4])
        self.table_45_txt.delete(0.0,END);self.table_45_txt.insert(0.0,board[4][5])
        self.table_46_txt.delete(0.0,END);self.table_46_txt.insert(0.0,board[4][6])
        self.table_47_txt.delete(0.0,END);self.table_47_txt.insert(0.0,board[4][7])
        self.table_48_txt.delete(0.0,END);self.table_48_txt.insert(0.0,board[4][8])
        self.table_49_txt.delete(0.0,END);self.table_49_txt.insert(0.0,board[4][9])
        self.table_410_txt.delete(0.0,END);self.table_410_txt.insert(0.0,board[4][10])
#wiersz'5'
        self.table_50_txt.delete(0.0,END);self.table_50_txt.insert(0.0,board[5][0])
        self.table_51_txt.delete(0.0,END);self.table_51_txt.insert(0.0,board[5][1])
        self.table_52_txt.delete(0.0,END);self.table_52_txt.insert(0.0,board[5][2])
        self.table_53_txt.delete(0.0,END);self.table_53_txt.insert(0.0,board[5][3])
        self.table_54_txt.delete(0.0,END);self.table_54_txt.insert(0.0,board[5][4])
        self.table_55_txt.delete(0.0,END);self.table_55_txt.insert(0.0,board[5][5])
        self.table_56_txt.delete(0.0,END);self.table_56_txt.insert(0.0,board[5][6])
        self.table_57_txt.delete(0.0,END);self.table_57_txt.insert(0.0,board[5][7])
        self.table_58_txt.delete(0.0,END);self.table_58_txt.insert(0.0,board[5][8])
        self.table_59_txt.delete(0.0,END);self.table_59_txt.insert(0.0,board[5][9])
        self.table_510_txt.delete(0.0,END);self.table_510_txt.insert(0.0,board[5][10])
#wiersz'6'
        self.table_60_txt.delete(0.0,END);self.table_60_txt.insert(0.0,board[6][0])
        self.table_61_txt.delete(0.0,END);self.table_61_txt.insert(0.0,board[6][1])
        self.table_62_txt.delete(0.0,END);self.table_62_txt.insert(0.0,board[6][2])
        self.table_63_txt.delete(0.0,END);self.table_63_txt.insert(0.0,board[6][3])
        self.table_64_txt.delete(0.0,END);self.table_64_txt.insert(0.0,board[6][4])
        self.table_65_txt.delete(0.0,END);self.table_65_txt.insert(0.0,board[6][5])
        self.table_66_txt.delete(0.0,END);self.table_66_txt.insert(0.0,board[6][6])
        self.table_67_txt.delete(0.0,END);self.table_67_txt.insert(0.0,board[6][7])
        self.table_68_txt.delete(0.0,END);self.table_68_txt.insert(0.0,board[6][8])
        self.table_69_txt.delete(0.0,END);self.table_69_txt.insert(0.0,board[6][9])
        self.table_610_txt.delete(0.0,END);self.table_610_txt.insert(0.0,board[6][10])
#wiersz'7'
        self.table_70_txt.delete(0.0,END);self.table_70_txt.insert(0.0,board[7][0])
        self.table_71_txt.delete(0.0,END);self.table_71_txt.insert(0.0,board[7][1])
        self.table_72_txt.delete(0.0,END);self.table_72_txt.insert(0.0,board[7][2])
        self.table_73_txt.delete(0.0,END);self.table_73_txt.insert(0.0,board[7][3])
        self.table_74_txt.delete(0.0,END);self.table_74_txt.insert(0.0,board[7][4])
        self.table_75_txt.delete(0.0,END);self.table_75_txt.insert(0.0,board[7][5])
        self.table_76_txt.delete(0.0,END);self.table_76_txt.insert(0.0,board[7][6])
        self.table_77_txt.delete(0.0,END);self.table_77_txt.insert(0.0,board[7][7])
        self.table_78_txt.delete(0.0,END);self.table_78_txt.insert(0.0,board[7][8])
        self.table_79_txt.delete(0.0,END);self.table_79_txt.insert(0.0,board[7][9])
        self.table_710_txt.delete(0.0,END);self.table_710_txt.insert(0.0,board[7][10])
#wiersz'8'
        self.table_80_txt.delete(0.0,END);self.table_80_txt.insert(0.0,board[8][0])
        self.table_81_txt.delete(0.0,END);self.table_81_txt.insert(0.0,board[8][1])
        self.table_82_txt.delete(0.0,END);self.table_82_txt.insert(0.0,board[8][2])
        self.table_83_txt.delete(0.0,END);self.table_83_txt.insert(0.0,board[8][3])
        self.table_84_txt.delete(0.0,END);self.table_84_txt.insert(0.0,board[8][4])
        self.table_85_txt.delete(0.0,END);self.table_85_txt.insert(0.0,board[8][5])
        self.table_86_txt.delete(0.0,END);self.table_86_txt.insert(0.0,board[8][6])
        self.table_87_txt.delete(0.0,END);self.table_87_txt.insert(0.0,board[8][7])
        self.table_88_txt.delete(0.0,END);self.table_88_txt.insert(0.0,board[8][8])
        self.table_89_txt.delete(0.0,END);self.table_89_txt.insert(0.0,board[8][9])
        self.table_810_txt.delete(0.0,END);self.table_810_txt.insert(0.0,board[8][10])
#wiersz'9'
        self.table_90_txt.delete(0.0,END);self.table_90_txt.insert(0.0,board[9][0])
        self.table_91_txt.delete(0.0,END);self.table_91_txt.insert(0.0,board[9][1])
        self.table_92_txt.delete(0.0,END);self.table_92_txt.insert(0.0,board[9][2])
        self.table_93_txt.delete(0.0,END);self.table_93_txt.insert(0.0,board[9][3])
        self.table_94_txt.delete(0.0,END);self.table_94_txt.insert(0.0,board[9][4])
        self.table_95_txt.delete(0.0,END);self.table_95_txt.insert(0.0,board[9][5])
        self.table_96_txt.delete(0.0,END);self.table_96_txt.insert(0.0,board[9][6])
        self.table_97_txt.delete(0.0,END);self.table_97_txt.insert(0.0,board[9][7])
        self.table_98_txt.delete(0.0,END);self.table_98_txt.insert(0.0,board[9][8])
        self.table_99_txt.delete(0.0,END);self.table_99_txt.insert(0.0,board[9][9])
        self.table_910_txt.delete(0.0,END);self.table_910_txt.insert(0.0,board[9][10])
#wiersz'10'
        self.table_100_txt.delete(0.0,END);self.table_100_txt.insert(0.0,board[10][0])
        self.table_101_txt.delete(0.0,END);self.table_101_txt.insert(0.0,board[10][1])
        self.table_102_txt.delete(0.0,END);self.table_102_txt.insert(0.0,board[10][2])
        self.table_103_txt.delete(0.0,END);self.table_103_txt.insert(0.0,board[10][3])
        self.table_104_txt.delete(0.0,END);self.table_104_txt.insert(0.0,board[10][4])
        self.table_105_txt.delete(0.0,END);self.table_105_txt.insert(0.0,board[10][5])
        self.table_106_txt.delete(0.0,END);self.table_106_txt.insert(0.0,board[10][6])
        self.table_107_txt.delete(0.0,END);self.table_107_txt.insert(0.0,board[10][7])
        self.table_108_txt.delete(0.0,END);self.table_108_txt.insert(0.0,board[10][8])
        self.table_109_txt.delete(0.0,END);self.table_109_txt.insert(0.0,board[10][9])
        self.table_1010_txt.delete(0.0,END);self.table_1010_txt.insert(0.0,board[10][10])


    #Sprawdzenie poprawności wprowadzenia liczby zmiennoprzecinkowej
    def validate_float(self,var):
        '''
        Sprawdzenie poprawności wprowadzenia liczby zmiennoprzecinkowej
        w polu "Entry":
            sv = StringVar()
            self.ac = Entry(self, .... , textvariable = sv)
          self.ac.grid(row = 3, column = 9)
          sv.trace('w', lambda nm, idx, mode, var=sv: self.validate_float(var))
        '''
        validate_old_value = ''
        new_value = var.get()
        try:
            new_value == int(new_value) 
            validate_old_value = new_value
        except:
            var.set(validate_old_value)    

#PUSTA TABLICA
    def new_board(self,zakres_a,zakres_b):
        """Utwórzenie nowej planszy tabliczki."""
        board = []
        for a in range(0,11):
            k = []
            for b in range(0,11):
                b = ''
                k.append(b)
            board.append(k)

        for p in range(1,11): board[0][p] = p
        for j in range(1,11): board[j][0] = j
        board[0][0] = ' X'

        return board

    def addition_table_new(self):
        """Utwórzenie nowej pustej tablicy dodawania."""
        global board_a

        self.table.set('a')
        self.range_a.set(None)
        self.range_m.set(None)
        self.table_m.set(None)
        
        table_a = self.table_a.get()
        if table_a == 'n':
            board_a = []        #board_m - nowa pusta tablica
        self.addition_table()

    def addition_table(self):
        """Tabliczka dodawania."""
        global board_a
        global zakres_a
        global zakres_b
        global board

        self.range_a.set(None)
        self.range_m.set(None)
        self.table_m.set(None)
        
        board = self.new_board(zakres_a,zakres_b)           #utworzenie nowej tablicy dodawania
        self.quess_txt.delete(0.0, END)                     #czyszczenie okna pytania
        self.answer.delete(0,10)                            #czyszczenie okna odpowiedzi
        self.answer_txt.delete(0.0, END)                    #czyszczenie okna potwierdzenia prawidłowości odpowiedzi
        self.display_board(0,0,board)                       #wyświetlenie pustej tablicy

        self.table_000_txt.delete(0.0, END)
        self.table_000_txt.insert(0.0, '   TABLICZKA DODAWANIA       ')#wyświetlenie tytułu tabliczko w polu tytułu
        self.table_000_txt.tag_add('000','1.0','1.100')
        self.table_000_txt.tag_config('000',background='#b1fea9')

        # utwórzenie nowej tablicy dodawania
        if board_a ==[]:
            board_a = self.new_board(zakres_a,zakres_b)#board_m - nowa pusta tablica

        #przycisk - Przycisk 'OK' - odpowiedź - dodawanie
        self.answer_OK_a = Button(self,
                                text = "OK",
                                font = ('calibri',13, 'underline'),
                                padx = 200,
                                pady = 2,
                                activebackground = '#80ff00',
                                activeforeground = 'yellow',
                                bd = 4,
                                command = self.answer_addition_get
                                )
        self.answer_OK_a.grid(row = 30, column = 1, rowspan = 2, columnspan = 11)	
#        self.answer_OK.bind("<Button>",self.answer_a_get) #uruchonmienie działania lewego przycisku myszy
#        self.answer_OK.bind("<Return>",self.answer_a_get) #uruchonmienie działania klawisza enter
#                                state = 'active'
#                                command = self.answer_a_get
 
    def addition_table_new_range(self):
        """Pobranie zakresu tabliczki."""
        global board_a
        global zakres

        self.table.set('a')
        self.range_m.set(None)#'p')

        self.quess_txt.delete(0.0, END)     #czyszczenie okna pytania
        self.answer.delete(0,10)            #czyszczenie okna odpowiedzi
        self.answer_txt.delete(0.0, END)    #czyszczenie okna potwierdzenia prawidłowości odpowiedzi

        table_a = self.table_a.get()
        if table_a == 'n' or board_a ==[]:
            board_a = self.new_board(zakres_a,zakres_b)#board_m - nowa pusta tablica

        zakres = self.range_a.get()         #pobranie zmiennej z przycisku nowej tablicy                
        self.main_addition(board_a)         #board_a - tablica do kontynuacji

    def main_addition(self,board_a):  #generowanie pytania dodawania
        global x_a
        global y_a
        global x_az
        global y_az

        self.table.set('a')
        self.table_a.set(None)

        if zakres == 'r':
            zakres_a = random.randrange(10)
            zakres_b = random.randrange(10)
        else:
            zakres_a = 0
            zakres_b = 0

        board_r = board_a

        try:
            x_a,y_a = self.number_r(board_r)            #pobieranie czynników działania
        except TypeError:                               #kończenie pobierania - przy pełnej tabeli
            self.answer_txt.delete(0.0, END)            #czyszczenie okna pytania
            self.answer_txt.insert(0.0, '       I TO JUŻ KONIEC ZMAGAŃ!  \n         ZWYCIĘŻYŁAŚ/EŚ :D              ')
            self.answer_txt.tag_add('answer','1.0','2.150')
            self.answer_txt.tag_config('answer',background='#c6ff8c', foreground='#5745f5')
            self.answer_txt.delete(0.0, END)            #czyszczenie okna informacji o odpowiedzi
            self.playsoundend()
            self.quess_txt.delete(0.0, END)     #czyszczenie okna pytania

        #wyświetlenie nagłówków kolumn i werszy
        for i in range(1,11):
            x_az0 = (zakres_b * 10) + i
            board_a[0][i] = x_az0

        for i in range(1,11):
            y_az0 = (zakres_a * 10) + i
            board_a[i][0] = y_az0

        #ustalenie wartości zmiennych w zależności od wybranego zakresu
        lista_az = []
        for k in range(0,10):
            x_az = x_a + (k * 10)
            lista_az.append(x_az)
        x_az = lista_az[zakres_a]

        lista_bz = []
        for K in range(0,10):
            y_az = y_a + (K * 10)
            lista_bz.append(y_az)
        y_az = lista_bz[zakres_b]

        self.quess_txt.delete(0.0, END)                 #czyszczenie okna pytania
        self.answer.delete(0,10)                        #czyszczenie okna odpowiedzi

        self.display_board(x_a, y_a, board_a)           #wyświetlenie tablicy dodawania
        qa_txt = ' ' + str(x_az) + ' + ' + str(y_az)    #pytanie 
        self.quess_txt.insert(0.0, qa_txt)              #wyświetlenie pytania

        return x_a,y_a,board_a

    def answer_addition_get(self):#,Button):
        """Pobranie odpowiedzi"""

        try:
            answer = int(self.answer.get())
            self.answer_addition(answer,board_a)
        except (ValueError, UnboundLocalError):
            self.playsounderror()
            self.answer_txt.delete(0.0, END)
            self.answer_txt.insert(0.0, '               WPISZ ODPOWIEDŹ! :(              \n')
            self.answer_txt.tag_add('answer','1.0','1.100')
            self.answer_txt.tag_config('answer',background='#fe7882', foreground='yellow')

    def answer_addition(self,answer,board_a):               #sprawdzenie odpowiedzi
        if answer == x_az + y_az:

            self.answer_txt.delete(0.0, END)
            self.answer_txt.insert(0.0, '            ODPOWIEDŹ PRAWIDŁOWA! :D            \n')
            self.answer_txt.tag_add('answer','1.0','1.80')
            self.answer_txt.tag_config('answer',background='#c6ff8c', foreground='#5745f5')
            answer_ok = '               ' + str(x_az) + ' + ' + str(y_az) + ' = ' + str(answer)
            self.answer_txt.insert(END, answer_ok)#wpisanie informacji o dobrej odpowiedzi

            board_a[x_a][y_a] =  x_az + y_az

            self.display_board(x_a, y_a, board_a)    #wyświetlenie tablicy dodawania
            self.quess_txt.delete(0.0, END)             #czyszczenie okna pytania
            self.main_addition(board_a)
        else:
            self.answer_txt.delete(0.0, END)
            self.answer_txt.insert(1.0, '           ODPOWIEDŹ NIEPRAWIDŁOWA! :(          \n')
            self.answer_txt.tag_add('answer','1.0','1.60')
            self.answer_txt.tag_config('answer',background='#fe7882', foreground='yellow')

            answer_error = '            ' + str(x_az) + ' + ' + str(y_az) + ' <> ' + str(answer) + '   lecz   ' + str(x_az + y_az)+'                  '
            self.answer_txt.insert(2.0, answer_error)#wpisanie informacji o błędnej odpowiedzi
            self.answer_txt.tag_add('answer1','2.0','2.60')
            self.answer_txt.tag_config('answer1',background='yellow')

            self.playsounderror()
            self.answer.delete(0,10)                    #czyszczenie okna odpowiedzi
            self.quess_txt.delete(0.0, END)             #czyszczenie okna pytania
            self.main_addition(board_a)
        return board_a


    def multiplication_table_new(self):
        """Utwórzenie nowej pustej tablicy mnożenia."""
        global board_m

        self.table.set('m')
        self.range_m.set(None)#'p')
        self.range_a.set(None)#'p')
        self.table_a.set(None)

        table_m = self.table_m.get()
        if table_m == 'n':
            board_m = []                #board_m - nowa pusta tablica
        self.multiplication_table()

    def multiplication_table(self):
        """Tabliczka mnożenia."""
        global board_m
        global zakres_a
        global zakres_b
        global board

        self.range_m.set(None)#'p')
        self.range_a.set(None)#'p')
        self.table_a.set(None)

        board = self.new_board(zakres_a,zakres_b)           #utworzenie nowej tablicy mnożenia
        self.quess_txt.delete(0.0, END)                     #czyszczenie okna pytania
        self.answer.delete(0,10)                            #czyszczenie okna odpowiedzi
        self.answer_txt.delete(0.0, END)                    #czyszczenie okna potwierdzenia prawidłowości odpowiedzi

        self.display_board(0,0,board)                   #wyświetlenie tablicy mnożenia

        self.table_000_txt.delete(0.0, END)
        self.table_000_txt.insert(0.0, '   TABLICZKA MNOŻENIA       ')
        self.table_000_txt.tag_add('000','1.0','1.100')
        self.table_000_txt.tag_config('000',background='#affefc')

        # utwórzenie nowej tablicy mnożenia
        if board_m ==[]:
            board_m = self.new_board(zakres_a,zakres_b)     #board_m - nowa pusta tablica

        #przycisk - Przycisk 'OK' - odpowiedź - mnożenie
        self.answer_OK_m = Button(self,
                                text = "OK",
                                font = ('calibri',13, 'underline'),
                                padx = 200,
                                pady = 2,
                                activebackground = '#affefc',
                                activeforeground = 'yellow',
                                bd = 4,
                                command = self.answer_multiplication_get
                                )
        self.answer_OK_m.grid(row = 30, column = 1, rowspan = 2, columnspan = 11)#, sticky = E)	
#        self.answer_OK.bind("<Return>",self.answer_m_get) #uruchonmienie działania klawisza enter
#        self.answer_OK.bind("<Button>",self.answer_m_get) #uruchonmienie działania lewego przycisku myszy
#                                command = self.answer_m_get

    def multiplication_table_new_range(self):
        """Pobranie zakresu tabliczki."""
        global board_m
        global zakres

        self.table.set('m')
        self.range_a.set(None)

        self.quess_txt.delete(0.0, END)     #czyszczenie okna pytania
        self.answer.delete(0,10)            #czyszczenie okna odpowiedzi
        self.answer_txt.delete(0.0, END)    #czyszczenie okna potwierdzenia prawidłowości odpowiedzi

        table_m = self.table_m.get()
        if table_m == 'n' or board_m ==[]:
            board_m = self.new_board(zakres_a,zakres_b)#board_m - nowa pusta tablica

        zakres = self.range_m.get()
        self. main_multiplication(board_m)   #board_m - tablica do kontynuacji

    def  main_multiplication(self,board_m):  #generowanie pytania mnożenia
        global x_m
        global y_m
        global x_mz
        global y_mz

        self.table_m.set(None)

        if zakres == 'p':
            zakres_a = 0
            zakres_b = 0
        else:
            zakres_a = random.randrange(10)
            zakres_b = random.randrange(10)

        board_r = board_m
        try:
            x_m,y_m = self.number_r(board_r)    #pobieranie czynników działania
        except TypeError:                       #kończenie pobierania - przy pełnej tabeli
            self.answer_txt.delete(0.0, END)    #czyszczenie okna informacji o odpowiedzi
            self.answer_txt.insert(0.0, 'I TO JUŻ KONIEC ZMAGAŃ! ZWYCIĘŻYŁAŚ/EŚ :D')
            self.answer_txt.tag_add('answer','1.0','1.50')
            self.answer_txt.tag_config('answer',background='#c6ff8c', foreground='#5745f5')
            self.quess_txt.delete(0.0, END)     #czyszczenie okna pytania
            self.answer_txt.delete(0.0, END)    #czyszczenie okna informacji o odpowiedzi
            self.playsoundend()

        #ustalenie wyświetlenie nagłówków kolumn i wierszy w zależności od wybranego zakresu
        for i in range(1,11):
            x_mz0 = (zakres_b * 10) + i
            board_m[0][i] = x_mz0

        for i in range(1,11):
            y_mz0 = (zakres_a * 10) + i
            board_m[i][0] = y_mz0

        #ustalenie wartości zmiennych w zależności od zakresu
        lista_mz = []
        for k in range(0,10):
            x_mz = x_m + (k * 10)
            lista_mz.append(x_mz)
        x_mz = lista_mz[zakres_a]

        lista_bz = []
        for k in range(0,10):
            y_mz = y_m + (k * 10)
            lista_bz.append(y_mz)
        y_mz = lista_bz[zakres_b]

        self.quess_txt.delete(0.0, END)                 #czyszczenie okna pytania
        self.answer.delete(0,10)                        #czyszczenie okna odpowiedzi

        self.display_board(x_m, y_m, board_m)           #wyświetlenie tablicy mnożenia

        qm_txt = ' ' + str(x_mz) + ' * ' + str(y_mz)    #pytanie 
        self.quess_txt.insert(0.0, qm_txt)              #wyświetlenie pytania
        return x_m,y_m,board_m

    def answer_multiplication_get(self):#,Button):      #Pobranie odpowiedzi
        """Pobranie odpowiedzi"""

        try:
            answer = int(self.answer.get())
            self.answer_multiplication(answer,board_m)
        except (ValueError, UnboundLocalError):
            self.playsounderror()
            self.answer_txt.delete(0.0, END)
            self.answer_txt.insert(0.0, '               WPISZ ODPOWIEDŹ! :(              \n')
            self.answer_txt.tag_add('answer','1.0','1.100')
            self.answer_txt.tag_config('answer',background='#fe7882', foreground='yellow')

    def answer_multiplication(self,answer,board_m):      #sprawdzenie odpowiedzi

        if answer == x_mz * y_mz: 
            self.answer_txt.delete(0.0, END)

            self.answer_txt.insert(0.0, '            ODPOWIEDŹ PRAWIDŁOWA! :D            \n')
            self.answer_txt.tag_add('answer','1.0','1.80')
            self.answer_txt.tag_config('answer',background='#c6ff8c', foreground='#5745f5')
            answer_ok = '               ' + str(x_mz) + ' * ' + str(y_mz) + ' = ' + str(answer)
            self.answer_txt.insert(END, answer_ok)#wpisanie informacji o dobrej odpowiedzi

            board_m[x_m][y_m] =  x_mz * y_mz
            self.display_board(x_m, y_m, board_m)

            self.quess_txt.delete(0.0, END)             #czyszczenie okna pytania
            self.main_multiplication(board_m)
        else:
            self.answer_txt.delete(0.0, END)
#            self.answer_txt.insert(0.0, '      ')
            self.answer_txt.insert(1.0, '           ODPOWIEDŹ NIEPRAWIDŁOWA! :(          \n')
            self.answer_txt.tag_add('answer','1.0','1.60')
            self.answer_txt.tag_config('answer',background='#fe7882', foreground='yellow')
            answer_error = '            ' + str(x_mz) + ' * ' + str(y_mz) + ' <> ' + str(answer) + '   lecz   ' + str(x_mz * y_mz)+'                  '
            self.answer_txt.insert(2.0, answer_error)#wpisanie informacji o błędnej odpowiedzi
            self.answer_txt.tag_add('answer1','2.0','2.60')
            self.answer_txt.tag_config('answer1',background='yellow')

            self.playsounderror()
            self.answer.delete(0,10)    #czyszczenie okna odpowiedzi
            self.quess_txt.delete(0.0, END)             #czyszczenie okna pytania
            self.main_multiplication(board_m)
        return board_m    


    def playsounderror(self):   #sygnalizacja błędnej odpowiedzi
#        winsound.PlaySound('alarm-slow', winsound.SND_FILENAME)
        winsound.Beep(1500,1500)

    def playsoundend(self):     #fanfary na zakończenie
        winsound.PlaySound('dzwoneczki', winsound.SND_FILENAME)



    #generowanie liczb losowych x i y z zakresu 1 ÷ 10 w zależności od wypełninia tablic dodawania i mnożenia
    def number_r(self,board_r):    
        for a in range(1,11):
            for b in range(1,11):
                while type (board_r[a][b]) is not int:
                    x = random.randint(1,10)
                    y = random.randint(1,10)
                    while type (board_r[x][y]) is not int:
                        return x, y


# część główna
root = Tk()
root.title('Dodawanie i mnożenie')
app = Application(root)
root.mainloop()

