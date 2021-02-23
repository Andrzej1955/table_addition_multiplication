# Tabliczka dodawania i mnożenia
# Komputer przepytuje z tabliczek dodawania i mmożenia

import random
#A = 'A'
#M = 'M'
board_1 = ''        #tabliczka mnożenia
board_a_1 = ''      #tabliczka dodawania

def display_instruct():
    """Wyświetl instrukcję gry."""  
    print(
    """
                    TABLICZKA DODAWANIA / MNOŻENIA
    
    Witaj w największym intelektualnym wyzwaniu wszech czasów, jakim są gry

                        'Tabliczka dodawania'
                        'Tabliczka mnożenia'.
                
    Będzie to ostateczna rozgrywka między Twoim ludzkim mózgiem
    a moim krzemowym procesorem.  

    Swoje posunięcie wskażesz poprzez wprowadzenie prawidłowego wyniku
    dodawania lub mnożenia podanych dwóch liczb.
    Prawidłowa odpowiedź pojawi się na poniższej planszy:
    
    	 ╔═════╦════╦════╦════╦════╦════╦════╦════╦════╦════╦═════╗
	 ║   X ║  1 ║  2 ║  3 ║  4 ║  5 ║  6 ║  7 ║  8 ║  9 ║  10 ║
	 ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣
	 ║   1 ║    ║    ║    ║    ║    ║    ║    ║    ║    ║     ║
	 ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣
	 ║   2 ║    ║    ║    ║    ║    ║    ║    ║    ║    ║     ║
	 ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣
	 ║   3 ║    ║    ║    ║    ║    ║    ║    ║    ║    ║     ║
	 ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣
	 ║   4 ║    ║    ║    ║    ║    ║    ║    ║    ║    ║     ║
	 ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣
	 ║   5 ║    ║    ║    ║    ║    ║    ║    ║    ║    ║     ║
	 ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣
	 ║   6 ║    ║    ║    ║    ║    ║    ║    ║    ║    ║     ║
	 ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣
	 ║   7 ║    ║    ║    ║    ║    ║    ║    ║    ║    ║     ║
	 ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣
	 ║   8 ║    ║    ║    ║    ║    ║    ║    ║    ║    ║     ║
	 ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣
	 ║   9 ║    ║    ║    ║    ║    ║    ║    ║    ║    ║     ║
	 ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣
	 ║  10 ║    ║    ║    ║    ║    ║    ║    ║    ║    ║     ║
	 ╚═════╩════╩════╩════╩════╩════╩════╩════╩════╩════╩═════╝

                        Przygotuj się, Myślicielko/lu.
                    Ostateczna batalia niebawem się rozpocznie.

    """
    )



def new_board_a():
    """Utwórz nową planszę tabliczki dodawania."""
    board_a=[['X','1','2','3','4','5','6','7','8',' 9',' 10'],
           ['1',' ',' ',' ',' ',' ',' ',' ',' ','  ','  '],
           ['2',' ',' ',' ',' ',' ',' ',' ','  ','  ','  '],
           ['3',' ',' ',' ',' ',' ',' ','  ','  ','  ','  '],
           ['4',' ',' ',' ',' ',' ','  ','  ','  ','  ','  '],
           ['5',' ',' ',' ',' ','  ','  ','  ','  ','  ','  '],
           ['6',' ',' ',' ','  ','  ','  ','  ','  ','  ','  '],
           ['7',' ',' ','  ','  ','  ','  ','  ','  ','  ','  '],
           ['8',' ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
           ['9','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
           ['10','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ']]
    return board_a

def display_board_a(board_a):
    """Wyświetl planszę gry na ekranie."""
    print('\t ╔═════╦════╦════╦════╦════╦════╦════╦════╦════╦════╦═════╗')
    print('\t ║  ',board_a[0][0],  '║ ',board_a[0][1],'║ ',board_a[0][2],'║ ',board_a[0][3],'║ ',board_a[0][4],'║ ',board_a[0][5],'║ ',board_a[0][6],'║ ',board_a[0][7],'║ ',board_a[0][8],'║',board_a[0][9], '║',board_a[0][10],'║')
    print('\t ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣')
    print('\t ║  ',board_a[1][0],'║ ',board_a[1][1],'║ ',board_a[1][2],'║ ',board_a[1][3],'║ ',board_a[1][4],'║ ',board_a[1][5],'║ ',board_a[1][6],'║ ',board_a[1][7],'║ ',board_a[1][8],'║',board_a[1][9],'║ ',board_a[1][10],'║')
    print('\t ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣')
    print('\t ║  ',board_a[2][0],'║ ',board_a[2][1],'║ ',board_a[2][2],'║ ',board_a[2][3],'║ ',board_a[2][4],'║ ',board_a[2][5],'║ ',board_a[2][6],'║ ',board_a[2][7],'║',board_a[2][8],'║',board_a[2][9],'║ ',board_a[2][10],'║')
    print('\t ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣')
    print('\t ║  ',board_a[3][0],'║ ',board_a[3][1],'║ ',board_a[3][2],'║ ',board_a[3][3],'║ ',board_a[3][4],'║ ',board_a[3][5],'║ ',board_a[3][6],'║',board_a[3][7],'║',board_a[3][8],'║',board_a[3][9],'║ ',board_a[3][10],'║')
    print('\t ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣')
    print('\t ║  ',board_a[4][0],'║ ',board_a[4][1],'║ ',board_a[4][2],'║ ',board_a[4][3],'║ ',board_a[4][4],'║ ',board_a[4][5],'║',board_a[4][6],'║',board_a[4][7],'║',board_a[4][8],'║',board_a[4][9],'║ ',board_a[4][10],'║')
    print('\t ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣')
    print('\t ║  ',board_a[5][0],'║ ',board_a[5][1],'║ ',board_a[5][2],'║ ',board_a[5][3],'║ ',board_a[5][4],'║',board_a[5][5],'║',board_a[5][6],'║',board_a[5][7],'║',board_a[5][8],'║',board_a[5][9],'║ ',board_a[5][10],'║')
    print('\t ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣')
    print('\t ║  ',board_a[6][0],'║ ',board_a[6][1],'║ ',board_a[6][2],'║ ',board_a[6][3],'║',board_a[6][4],'║',board_a[6][5],'║',board_a[6][6],'║',board_a[6][7],'║',board_a[6][8],'║',board_a[6][9],'║ ',board_a[6][10],'║')
    print('\t ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣')
    print('\t ║  ',board_a[7][0],'║ ',board_a[7][1],'║ ',board_a[7][2],'║',board_a[7][3],'║',board_a[7][4],'║',board_a[7][5],'║',board_a[7][6],'║',board_a[7][7],'║',board_a[7][8],'║',board_a[7][9],'║ ',board_a[7][10],'║')
    print('\t ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣')
    print('\t ║  ',board_a[8][0],'║ ',board_a[8][1],'║',board_a[8][2],'║',board_a[8][3],'║',board_a[8][4],'║',board_a[8][5],'║',board_a[8][6],'║',board_a[8][7],'║',board_a[8][8],'║',board_a[8][9],'║ ',board_a[8][10],'║')
    print('\t ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣')
    print('\t ║  ',board_a[9][0],'║',board_a[9][1],'║',board_a[9][2],'║',board_a[9][3],'║',board_a[9][4],'║',board_a[9][5],'║',board_a[9][6],'║',board_a[9][7],'║',board_a[9][8],'║',board_a[9][9],'║ ',board_a[9][10],'║')
    print('\t ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣')
    print('\t ║ ',board_a[10][0],'║',board_a[10][1],'║',board_a[10][2],'║',board_a[10][3],'║',board_a[10][4],'║',board_a[10][5],'║',board_a[10][6],'║',board_a[10][7],'║',board_a[10][8],'║',board_a[10][9],'║ ',board_a[10][10],'║')
    print('\t ╚═════╩════╩════╩════╩════╩════╩════╩════╩════╩════╩═════╝')
    print('\t\tJezeli chcesz przerwać naciścnij \'Alt\' + \'F4\'\n')


def answer_a(x,y,board_a):      #odpowiedzi tabliczki dodawania
    """Udziel odpowiedzi"""
    break_ = input('\
    \t Jeżeli chesz kontynuować naciśnij "Enter"\n\
    \t jeżeli chcesz powrócić do wyboru tabliczki naciśnij "c":').lower()
    if break_ == 'c':
        choice()
    else:
        answer_a = ''
        while answer_a != x+y:
            while type (answer_a) is not int:
                print('\n\t\t\t Ile jest : ',x,' + ',y)
                try:
                    answer_a = int(input('\n\t\t\t\t --> : '))
                except:
                    print('\n\t\t     Twoja odpowiedź nie jest liczbą!!!')    
            print('\n\t\t\t Twoja odpowiedż to : ',answer_a)

            if int(answer_a) == x + y:
                print('\t\t\t Podałaś/eś prawidłowy wynik!\n')
                print('\t\t\t\t',x,'+',y,'=',answer_a,'\n')
                board_a[x][y] = x + y
            else:
                print('\n\t\t\t\t NIEPRAWDA!!!')
                print('\n\t\t\t',x,' + ',y,' nie równa się : ',answer_a)
                print('\t\t\t Musisz podać prawidłowy wynik!')
                answer_a = ''
    return board_a        

#====================================================

def new_board():
    """Utwórz nową planszę tabliczki mnożenia."""
    board=[['X','1','2','3','4','5','6','7','8',' 9',' 10'],
           ['1',' ',' ',' ',' ',' ',' ',' ',' ',' ','  '],
           ['2',' ',' ',' ',' ','  ','  ','  ','  ','  ','  '],
           ['3',' ',' ',' ','  ','  ','  ','  ','  ','  ','  '],
           ['4',' ',' ','  ','  ','  ','  ','  ','  ','  ','  '],
           ['5',' ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
           ['6',' ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
           ['7',' ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
           ['8',' ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
           ['9',' ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
           ['10','  ','  ','  ','  ','  ','  ','  ','  ','  ','   ']]
    return board

def display_board(board):
    """Wyświetl planszę gry na ekranie."""
    print('\t ╔═════╦════╦════╦════╦════╦════╦════╦════╦════╦════╦═════╗')
    print('\t ║  ',board[0][0],  '║ ',board[0][1],'║ ',board[0][2],'║ ',board[0][3],'║ ',board[0][4],'║ ',board[0][5],'║ ',board[0][6],'║ ',board[0][7],'║ ',board[0][8],'║',board[0][9], '║',board[0][10],'║')
    print('\t ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣')
    print('\t ║  ',board[1][0],'║ ',board[1][1],'║ ',board[1][2],'║ ',board[1][3],'║ ',board[1][4],'║ ',board[1][5],'║ ',board[1][6],'║ ',board[1][7],'║ ',board[1][8],'║ ',board[1][9],'║ ',board[1][10],'║')
    print('\t ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣')
    print('\t ║  ',board[2][0],'║ ',board[2][1],'║ ',board[2][2],'║ ',board[2][3],'║ ',board[2][4],'║',board[2][5],'║',board[2][6],'║',board[2][7],'║',board[2][8],'║',board[2][9],'║ ',board[2][10],'║')
    print('\t ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣')
    print('\t ║  ',board[3][0],'║ ',board[3][1],'║ ',board[3][2],'║ ',board[3][3],'║',board[3][4],'║',board[3][5],'║',board[3][6],'║',board[3][7],'║',board[3][8],'║',board[3][9],'║ ',board[3][10],'║')
    print('\t ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣')
    print('\t ║  ',board[4][0],'║ ',board[4][1],'║ ',board[4][2],'║',board[4][3],'║',board[4][4],'║',board[4][5],'║',board[4][6],'║',board[4][7],'║',board[4][8],'║',board[4][9],'║ ',board[4][10],'║')
    print('\t ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣')
    print('\t ║  ',board[5][0],'║ ',board[5][1],'║',board[5][2],'║',board[5][3],'║',board[5][4],'║',board[5][5],'║',board[5][6],'║',board[5][7],'║',board[5][8],'║',board[5][9],'║ ',board[5][10],'║')
    print('\t ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣')
    print('\t ║  ',board[6][0],'║ ',board[6][1],'║',board[6][2],'║',board[6][3],'║',board[6][4],'║',board[6][5],'║',board[6][6],'║',board[6][7],'║',board[6][8],'║',board[6][9],'║ ',board[6][10],'║')
    print('\t ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣')
    print('\t ║  ',board[7][0],'║ ',board[7][1],'║',board[7][2],'║',board[7][3],'║',board[7][4],'║',board[7][5],'║',board[7][6],'║',board[7][7],'║',board[7][8],'║',board[7][9],'║ ',board[7][10],'║')
    print('\t ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣')
    print('\t ║  ',board[8][0],'║ ',board[8][1],'║',board[8][2],'║',board[8][3],'║',board[8][4],'║',board[8][5],'║',board[8][6],'║',board[8][7],'║',board[8][8],'║',board[8][9],'║ ',board[8][10],'║')
    print('\t ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣')
    print('\t ║  ',board[9][0],'║ ',board[9][1],'║',board[9][2],'║',board[9][3],'║',board[9][4],'║',board[9][5],'║',board[9][6],'║',board[9][7],'║',board[9][8],'║',board[9][9],'║ ',board[9][10],'║')
    print('\t ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬═════╣')
    print('\t ║ ',board[10][0],'║',board[10][1],'║',board[10][2],'║',board[10][3],'║',board[10][4],'║',board[10][5],'║',board[10][6],'║',board[10][7],'║',board[10][8],'║',board[10][9],'║',board[10][10],'║')
    print('\t ╚═════╩════╩════╩════╩════╩════╩════╩════╩════╩════╩═════╝')
    print('\t\tJezeli chcesz przerwać naciścnij \'Alt\' + \'F4\'\n')



def answer(x,y,board):      #odpowiedzi tabliczki mnożenia
    """Udziel odpowiedzi"""
    break_ = input('\
    \t Jeżeli chesz kontynuować naciśnij "Enter"\n\
    \t jeżeli chcesz powrócić do wyboru tabliczki naciśnij "c":').lower()
    if break_ == 'c':
        choice()
    else:
        answer = ''
        while answer != x*y:
            while type (answer) is not int:
                print('\n\t\t\t Ile jest : ',x,' * ',y)
                try:
                    answer = int(input('\n\t\t\t\t --> : '))
                except:
                    print('\n\t\t     Twoja odpowiedź nie jest liczbą!!!')    
            print('\n\t\t\t Twoja odpowiedż to : ',answer)

            if int(answer) == x*y:
                print('\t\t\t Podałaś/eś prawidłowy wynik!\n')
                print('\t\t\t\t',x,'*',y,'=',answer,'\n')
                board[x][y] = x*y
            else:
                print('\n\t\t\t\t NIEPRAWDA!!!')
                print('\n\t\t\t',x,' * ',y,' nie równa się : ',answer)
                print('\t\t\t Musisz podać prawidłowy wynik!')
                answer = ''
    return board        

#====================================================

def ask_m_a(question):      #wybór tabliczki
    """Zadaj pytanie, na które można odpowiedzieć 'a' lub 'm'."""
    response = None
    while response not in ("a", "m"):
        response = input(question).lower()
    return response

def choice():
    """Ustal, czy tabliczka dodawania czy mnożenia."""
    go_first = ask_m_a("\
    \n\t=============================================================\
    \n\t\t\t Którą wybierasz tabliczkę:\
    \n\t=============================================================\
    \n\t\t\t 'Dodawania' - wciśnij: 'a'\
    \n\t\t\t 'Mnożenia'  - wciśnij: 'm'\n\t\t\t\t-->")
    if go_first == "a":
        print('\n\t=============================================================')
        print("\t\t\t Zaczynamy walkę z dodawaniem.")
        print('\t=============================================================')
        #table = A
        main_a()

    else:
        print('\n\t=============================================================')
        print("\t\t\t Zaczynamy walkę z mnożeniemm.")
        print('\t=============================================================')
        #table = M
        main_m()

#    return table

#====================================================
def number_r():    #losowe generowanie liczb x, y z zakresu 1 - 10
    x = random.randint(1,10)
    y = random.randint(1,10)
    return x ,y

#====================================================
def main_a():       #tabliczka dodawania
    print(
    '''
    Wybór tabliczki:
    1 - Nowa tabliczka
    2 - Kontynuacja tabliczki
        (w przypadku nowej gry - nowa tabliczka)
    '''
    )
    choice_1_2 = input("    Wybierasz: ")
    global board_a_1
    if choice_1_2 == '1':
        board_a = new_board_a()
    if choice_1_2 == '2':
        if board_a_1 == '':
            board_a = new_board_a()
        else:
            board_a = board_a_1
    for a in range(1,11):
        for b in range(1,11):
            while type (board_a[a][b]) is not int:
                x,y = number_r()
                while type (board_a[x][y]) is not int:
                    answer_a(x,y,board_a)
                    display_board_a(board_a)
                    board_a_1 = board_a
    return board_a_1

#====================================================
def main_m():       #tabliczka mnożenia
    print(
    '''
    Wybór tabliczki:
    1 - Nowa tabliczka
    2 - Kontynuacja tabliczki
        (w przypadku nowej gry - nowa tabliczka)
    '''
    )
    choice_1_2 = input("    Wybierasz: ")
    global board_1
    if choice_1_2 == '1':
        board = new_board()
    if choice_1_2 == '2':
        if board_1 == '':
            board = new_board()
        else:
            board = board_1
    for a in range(1,11):
        for b in range(1,11):
            while type (board[a][b]) is not int:
                x,y = number_r()
                while type (board[x][y]) is not int:
                    answer(x,y,board)
                    display_board(board)
                    board_1 = board
    return board_1



#====================================================
def main():
    display_instruct()
    table = choice()
#    if table == A:
#        main_a()
#    else:
#        main_m()

main()

input("\n\nAby zakończyć grę, naciśnij klawisz Enter.")
