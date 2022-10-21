import random
import sys

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
    ace_dict = {}
    score_dict = {}
    MAX_SCORES = 21

    @classmethod
    def compare(cls, p):
        return p <= cls.MAX_SCORES

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
            if sc.m == 11:
                if key in self.ace_dict:
                    self.ace_dict[key] += sc.m
                else:
                    self.ace_dict[key] = sc.m
        else:
            self.score_dict[key] = sc.m

    def overscores_with_ace(self, key):
        if key in self.ace_dict and self.ace_dict[key] > 0:
            if not self.compare(sc.score_dict[key]):
                self.ace_dict[key] -= 11
                self.score_dict[key] -= 10
                print(f"DEALER SAY: {key}'s ace is converted from 11 to 1 score, otherwise {key} would have lost")

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
        print(f"{self.name.upper()} SAYS: I want to invite {N} player(s) more!")
        print("DEALER SAYS:", self.name, ", here your cards")
        c.give_card()
        sc.adding_to_dict(self.name)
        c.give_card()
        sc.adding_to_dict(self.name)
        sc.overscores_with_ace(self.name)
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
                    sc.overscores_with_ace(i)
                sc.score_table(i)
                k += 1


class DealerName:
    def __init__(self, d_name1):
        self.d_name1 = d_name1

    def __str__(self):
        name_of_dealer = ["I", "am", "your", "Dealer", "today", "and", "my", "name", "is", self.d_name1]
        return " ".join(name_of_dealer)

d_name_ = DealerName("Frank")



class Dealer:
    def __init__(self, d_name_=None):
        self.d_name_ = d_name_

    def anouncment(self):
        print("DEALER SAYS: NOW I'M TAKING ONE CARD MORE")

    def lose(self):
        print("DEALER SAYS: Ohhhh, I have more than 21 scores. PLAYERS THAT ARE STILL IN THE GAME HAVE JUST WON")
        if len(list(set(bot_obj).difference(set(bot_to_del)))) != 0:
            for j in list(set(bot_obj).difference(set(bot_to_del))):
                print(f"{j.name} has won!", end="")
        if len(pl_to_del) != 0:
            print(f"{pl_to_del[0].name} has won!")

    def pl_lose(self, pl_name):
        self.pl_name = pl_name
        print(f"DEALER SAYS: {self.pl_name}, YOU seem to have more scores than permitted! YOU LOSE!")

    def win(self):
        print("DEALER SAYS: You have won! You have more scores than me!")

    def double_bet(self):
        print("DEALER SAYS: Done! Your bet is doubled. You received one more card! You can not hit anymore")

    def hit_card(self):
        print("DEALER SAYS: Done! You just received one more card!")

    def surrender_pl(self):
        print("DEALER SAYS: I wish you would continue. Next time you'll have luck on your side")

    def stand_cards(self):
        print("DEALER SAYS: Okay. You keep sitting with your cards")


dealername = input("DEALER SAYS: Should I say my name to you? Say 'yes' if I should or anything else if I should not  ")

if dealername == "yes":    # here I used composition due to a requirement of the project, its usage is not obligatory
    dl1 = Dealer(d_name_)
    print(dl1.d_name_)

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
sc.overscores_with_ace("DEALER")



def pl_on():
    for i in range(len(bot_obj)):
        if i == 0:
            print("DEALER SAYS: Say your words!")
            print("""                                       OPTIONS
                    1 - hit    2 - stand    3 - double    4 - surrender""")
            option = input(f"Type your option, {pl.name} > ")
            match option:
                case "1":
                    pl.hit()
                    dl.hit_card()
                    c.give_card()
                    sc.adding_to_dict(pl.name)
                    sc.overscores_with_ace(pl.name)
                    sc.score_table(pl.name)
                    if not Scores.compare(sc.score_dict[pl.name]):
                        dl.pl_lose(pl.name)
                        pl_to_del.pop(0)
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
                sc.overscores_with_ace(bot_obj[i-1].name)
                sc.score_table(bot_obj[i-1].name)
                if not Scores.compare(sc.score_dict[bot_obj[i-1].name]):
                    dl.pl_lose(bot_obj[i-1].name)
                    bot_to_del.append(bot_obj[i - 1])
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
            sc.overscores_with_ace("DEALER")
            if not Scores.compare(sc.score_dict["DEALER"]):
                dl.lose()
                print("GAME OVER!")
                sys.exit()
        case _:
            print("DEALER SAYS: I STAND!")

    for el in bot_to_del:
        if el in bot_obj:
            bot_obj.remove(el)



def pl_off():
    print("DEALER SAYS: LADIES AND GENTELMEN! Say your words!")
    for i in range(len(bot_obj)):
        chosen_one = random.randrange(1, 5)
        match chosen_one:
            case 1:
                bot_obj[i].hit()
                dl.hit_card()
                c.give_card()
                sc.adding_to_dict(bot_obj[i].name)
                sc.overscores_with_ace(bot_obj[i].name)
                sc.score_table(bot_obj[i].name)
                if not Scores.compare(sc.score_dict[bot_obj[i].name]):
                    dl.pl_lose(bot_obj[i].name)
                    bot_to_del.append(bot_obj[i])
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
    dealers_choice = random.randrange(1, 3)
    match dealers_choice:
        case 1:
            dl.anouncment()
            c.give_card()
            sc.adding_to_dict("DEALER")
            sc.overscores_with_ace("DEALER")
            if not Scores.compare(sc.score_dict["DEALER"]):
                dl.lose()
                print("GAME OVER!")
                sys.exit()
        case _:
            print("DEALER SAYS: I STAND!")

    for el in bot_to_del:
        if el in bot_obj:
            bot_obj.remove(el)


def game_cycle():
    if len(pl_to_del) != 0:
        pl_on()
    else:
        if len(bot_obj) == 0:
            print("NOBODY IN GAME! DEALER HAS WON! GAME OVER")
            sys.exit()
        pl_off()


while True:
    game_cycle()


