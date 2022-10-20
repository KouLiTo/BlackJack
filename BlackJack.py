import random

players_in_game = []
your_name = input("Enter your name: ")
N = int(input(f"{your_name}, how many players would you play with? "))


class Card:
    suits = [*["2", "3", "4",
             "5", "6", "7",
             "8", "9", "10",
             "J", "D", "K"] * 4, "♤", "♡",
             "♧", "♢"
             ]


    def __init__(self):
        pass



    def build_card(self, arg):
        for i in range(5):
            if i == 0 or i == 4:
                print(" " + "-"*7)
            elif i == 1 or i == 3:
                print("|" + " "*7 + "|")
            else:
                if len(arg) > 1:
                    sc.convert(arg)
                    print("|" + " "*2, arg, " " + "|")
                elif arg == "♤" or arg == "♡" or arg == "♧" or arg == "♢":
                    sc.convert(arg)
                    print("|" + " "*2, arg, " " + "|")
                else:
                    sc.convert(arg)
                    print("|" + " "*2, arg, " "*2 + "|")

    def give_card(self):
        print("A card has been received")
        m = random.choice(self.suits)
        self.build_card(m)
        self.suits.remove(m)

    def hidden_card(self):
        dealer_card = random.choice(self.suits)
        sc.convert(dealer_card)
        sc.adding_to_dict("DEALER")
        self.suits.remove(dealer_card)

c = Card()

class Scores:
    score_dict = {}
    MAX_SCORES = 21

    @classmethod
    def compare(cls, p):
        if cls.score_dict[p] == cls.MAX_SCORES:
            print("21 score!!!!!")

    def convert(self, m):
        self.m = m
        if self.m == "2":
            self.m = 2
        elif self.m == "3":
            self.m = 3
        elif self.m == "4":
            self.m = 4
        elif self.m == "5":
            self.m = 5
        elif self.m == "6":
            self.m = 6
        elif self.m == "7":
            self.m = 7
        elif self.m == "8":
            self.m = 8
        elif self.m == "9":
            self.m = 9
        elif self.m == "10":
            self.m = 10
        elif self.m == "J":
            self.m = 10
        elif self.m == "D":
            self.m = 10
        elif self.m == "K":
            self.m = 10
        else:
            self.m = 11

    def adding_to_dict(self, key):
        if key in self.score_dict:
            self.score_dict[key] += sc.m
        else:
            self.score_dict[key] = sc.m

    def score_table(self, key):
        print(f"Your scores: {self.score_dict[key]}")


sc = Scores()

class Player:

    def __init__(self, name):
        self.name = name

    def hit(self):
        print(self.name.upper(), "SAYS" + ":" + " " + "I need one card more please")

    def stand(self):
        print(self.name.upper(), "SAYS" + ":" + " " + "That's enough, thanks")


    def double(self):
        print(self.name.upper(), "SAYS" + ":" + " " + "Double my bet")

    def surrender(self):
        print(self.name.upper(), "SAYS" + ":" + " " + "I am ending the game. Next time I'll have more luck")


class Bots(Player):
    bot_names = ["John", "Jessica", "Bred", "Joe", "Samantha", "Julia"]

    def create_bots(self):
        print(f"My name is {self.name} and I want to invite {N} players more!")
        print("DEALER SAYS:", self.name, ", here your cards")
        c.give_card()
        sc.adding_to_dict(self.name)
        c.give_card()
        sc.adding_to_dict(self.name)
        sc.score_table(self.name)
        k = 0
        while len(players_in_game) < N:
            i = random.choice(self.bot_names)
            if i not in players_in_game:
                players_in_game.append(i)
                print(f"My name is {i}. Nice to join you. Dealer, give me my cards, please")
                print("DEALER SAYS:", i, ", here your cards")
                for f in range(2):
                    c.give_card()
                    sc.adding_to_dict(i)
                sc.score_table(i)
                k += 1


class Dealer:

    def anouncment(self):
        print("DEALER SAYS: NOW I'M TAKING ONE CARD MORE")

    def lose(self):
        print("DEALER SAYS: Ohhhh, I have more than 21 scores. PLAYERS HAVE JUST WON")

    def win(self):
        print("DEALER SAYS: You have won! You have more scores than me!")

    def double_bet(self):
        print("DEALER SAYS: Done! Your bet is doubled")

    def hit_card(self):
        print("DEALER SAYS: Done! You just received one more card! You cannot hit anymore")

    def surrender_pl(self):
        print("DEALER SAYS: I wish you would continue. Next time you'll have luck on your side")

    def stand_cards(self):
        print("DEALER SAYS: Okay. You let yourself with your cards")



dl = Dealer()
pl = Player(your_name)
pl_to_del = [pl]
bt = Bots(your_name)
bt.create_bots()
bot_obj = [Player(x) for x in players_in_game]
bot_to_del = []
print("DEALERS SAYS: I TAKE TWO CARDS - ONE HIDDEN AND ANOTHER ONE IS OPEN ON THE TABLE")
c.hidden_card()
c.give_card()
sc.adding_to_dict("DEALER")


def pl_on():
    for i in range(len(bot_obj)):
        if i == 0:
            print("DEALER SAYS: Say your words!")
            print(""""                                   OPTIONS
                    1 - hit    2 - stand    3 - double    4 - surrender""")
            option = input(f"Type your option, {pl.name}> ")
            match option:
                case "1":
                    pl.hit()
                    dl.hit_card()
                    c.give_card()
                    sc.adding_to_dict(pl.name)
                    sc.score_table(pl.name)
                case "2":
                    pl.stand()
                    dl.stand_cards()
                    sc.score_table(pl.name)
                case "3":
                    pl.double()
                    dl.double_bet()
                case _:
                    pl.surrender()
                    dl.surrender_pl()
                    pl_to_del.pop(0)
        chosen_one = random.randrange(1, 5)
        match chosen_one:
            case 1:
                bot_obj[i-1].hit()
                dl.hit_card()
                c.give_card()
                sc.adding_to_dict(bot_obj[i-1].name)
                sc.score_table(bot_obj[i-1].name)
            case 2:
                bot_obj[i-1].stand()
                dl.stand_cards()
                sc.score_table(bot_obj[i-1].name)
            case 3:
                bot_obj[i-1].double()
                dl.double_bet()
            case _:
                bot_obj[i-1].surrender()
                bot_to_del.append(bot_obj[i-1])
                dl.surrender_pl()
    dealers_choice = random.randrange(1, 3)
    match dealers_choice:
        case 1:
            dl.anouncment()
            c.give_card()
            sc.adding_to_dict("DEALER")
        case _:
            print("DEALER SAYS: I STAND!")

    for el in bot_to_del:
        if el in bot_obj:
            bot_obj.remove(el)



def pl_off():
    print("DEALER SAYS: Say your words!")
    for i in range(len(bot_obj)):
        chosen_one = random.randrange(1, 5)
        match chosen_one:
            case 1:
                bot_obj[i].hit()
                dl.hit_card()
                c.give_card()
                sc.adding_to_dict(bot_obj[i].name)
                sc.score_table(bot_obj[i].name)
            case 2:
                bot_obj[i].stand()
                dl.stand_cards()
                sc.score_table(bot_obj[i].name)
            case 3:
                bot_obj[i].double()
                dl.double_bet()
            case _:
                bot_obj[i].surrender()
                bot_to_del.append(bot_obj[i])
                dl.surrender_pl()
        if i == len(bot_obj):
            dealers_choice = random.randrange(1, 3)
            match dealers_choice:
                case 1:
                    dl.anouncment()
                    c.give_card()
                    sc.adding_to_dict("DEALER")
                case _:
                    print("DEALER SAYS: I STAND!")

    for el in bot_to_del:
        if el in bot_obj:
            bot_obj.remove(el)


def game_cycle():
    if len(pl_to_del) != 0:
        pl_on()
    else:
        pl_off()

game_cycle()
game_cycle()
print(sc.score_dict)

