import getpass


def man(tries):
    if (tries == 0):
        print("  ._____\n"
            "  |     | \n"
            "  |    \n"
            "  |    \n"
            "  |    \n"
            "  |    \n"
            "__|__\n")
    elif (tries == 1):
        print("  ._____\n"
            "  |     | \n"
            "  |     O \n"
            "  |    \n"
            "  |    \n"
            "  |    \n"
            "__|__\n")
    elif (tries == 2):
        print("  ._____\n"
            "  |     | \n"
            "  |     O \n"
            "  |     | \n"
            "  |    \n"
            "  |    \n"
            "__|__\n")
    elif (tries == 3):
        print("  ._____\n"
            "  |     | \n"
            "  |     O \n"
            "  |    \| \n"
            "  |    \n"
            "  |    \n"
            "__|__\n")
    elif (tries == 4):
        print("  ._____\n"
            "  |     | \n"
            "  |     O \n"
            "  |    \|/ \n"
            "  |    \n"
            "  |    \n"
            "__|__\n")
    elif (tries == 5):
        print("  ._____\n"
            "  |     | \n"
            "  |     O \n"
            "  |    \|/ \n"
            "  |     | \n"
            "  |    \n"
            "__|__\n")
    elif (tries == 6):
        print("  ._____\n"
            "  |     | \n"
            "  |     O \n"
            "  |    \|/ \n"
            "  |     | \n"
            "  |    /  \n"
            "__|__\n")
    elif (tries == 7):
        print("  ._____\n"
            "  |     | \n"
            "  |     O \n"
            "  |    \|/ \n"
            "  |     | \n"
            "  |    / \ \n"
            "__|__\n")


def get_blanks(word):
    game = []
    won = 0
    for i in word:
        if (ord(i) == 32):
            game.append(" ")
        else:
            game.append("_")
            won += 1
    return game, won


def disp(game):
    for i in game:
        print(i, end =" ")
    print("\n")


def play(word, attempt, game, to_win, tries):
    wrong = True
    
    for i in range(0, len(word)):
        if (word[i] == attempt):
            game[i] = word[i]
            wrong = False
            to_win += 1
    if wrong:
        tries += 1
    return game, tries, to_win


def check_winner(won, to_win, tries):
    if (tries == 7):
        print("GAME OVER. TRY AGAIN LATER!")
        return False
    else:
        if (won == to_win):
            print("CONGRATULATIONS YOU WIN!!!")
            return False
    return True
            

def main():
    while True:
        try:
            print("Enter a word for hangman")
            word = str(getpass.getpass())
            word = word.upper()
        except:
            print("Enter a word no SYMBOLS or NUMBERS!\n")
        else:
            break
    table, won = get_blanks(word)
    to_win = 0
    tries = 0
    entries = []
    while check_winner(won, to_win, tries):
        disp(table)
        while True:
            try:
                attempt = input("Enter a letter: ")
                attempt = attempt.upper()
                if (len(attempt) > 1 or len(attempt) < 0):
                    raise Exception("Duplicate")
                else:
                    for i in entries:
                        if (attempt == i):
                            print("Already Entered")
                            raise Exception
            except:
                print("Enter a single letter\n")
            else:
                entries.append(attempt)
                break
        table, tries, to_win = play(word, attempt, table, to_win, tries)
        disp(table)
        man(tries)
    disp(table)

main()
