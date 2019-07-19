










from Player import Player
from Dealer import Dealer
import tkinter

class GameFrame():
    # def __init__(self):
    #     self.setup_mainwindow()

    # self.mainwindow = tkinter.Tk()
    # # self.mainwindow = tkinter.Tk()
    # self.result_text = tkinter.StringVar()
    # self.card_frame = tkinter.Frame(self.mainwindow, relief='sunken', borderwidth=1, background='green')
    # self.dealer_score_label = tkinter.IntVar()
    # self.setup_mainwindow()
    # self.setup_cardframe()
    #self.setup_dealerFrame()
    # self.setup_frameForResult()
    # self.setup_dealerScore()

    # tkinter.Label(card_frame, text="Dealer", background='blue', fg='white').grid(row=0, column=0)
    # tkinter.Label(card_frame, textvariable=dealer_score_label, background='green', fg='white').grid(row=1, column=0)
    # self.dealer_card_frame = tkinter.Frame(self.card_frame, background='green')

    def __init__(self):
        self.dealer_hand = []
        self.deck =[]

    def setup_mainwindow(self):
        self.mainwindow = tkinter.Tk()
        self.mainwindow.title(" black jack game")
        self.mainwindow.geometry("640x480")
        self.mainwindow.configure(background='green')

        self.load_images()
        self.final_deck()
        self.setup_frameForResult()

    def setup_frameForResult(self):
        self.result_text = tkinter.StringVar()
        self.result_text_label = tkinter.Label(self.mainwindow, background='red', textvariable=self.result_text)
        self.result_text_label.grid(row=0, column=0, columnspan=3)
        self.setup_cardframe()

    def setup_cardframe(self):
        self.card_frame = tkinter.Frame(self.mainwindow, relief='sunken', borderwidth=1, background='green')
        self.card_frame.grid(row=1, column=0, sticky='ew, ', rowspan=9, columnspan=3)
        self.setup_dealerScore()

    def setup_dealerScore(self):
        self.dealer_score_label = tkinter.IntVar()
        self.dealer_score = 0
        self.dealer_ace = False
        self.setup_dealerFrame()

    def setup_dealerFrame(self):
        tkinter.Label(self.card_frame, text="Dealer", background='blue', fg='white').grid(row=0, column=0)
        tkinter.Label(self.card_frame, textvariable=self.dealer_score_label, background='green', fg='white').grid(row=1, column=0)
        self.dealer_card_frame = tkinter.Frame(self.card_frame, background='green')
        self.dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)
        self.load_images()

    def load_images(self):
        suits = ['heart', 'club', 'diamond', 'spade']
        face_cards = ['king', 'queen', 'jack']
        extention = 'png'
        self.card_images = []
        for suit in suits:
            for card in range(1, 11):
                name = 'cards/cards/{}_{}.{}'.format(str(card), suit, extention)
                image = tkinter.PhotoImage(file=name)
                self.card_images.append((card, image, ))

            for card in face_cards:
                name = 'cards/cards/{}_{}.{}'.format(str(card), suit, extention)
                image = tkinter.PhotoImage(file=name)
                self.card_images.append((10, image, ))

    def final_deck(self):
        import random
        self.deck = self.deck + list(self.card_images)
        random.shuffle(self.deck)

    def _deal_cards(self,frame):
        # pop next card
        self.next_card = self.deck.pop(0)
        self.deck.append(self.next_card)
        # add image to a label and display
        # do not mix grid and pack in  the same frame
        tkinter.Label(frame, image=self.next_card[1], relief='raised').pack(side='left')
        # return card value
        return self.next_card


    def deal_dealer(self):

        self.dealer_score =1
        # player score shouldnt exceed 21
        # deal until score is more than player but less than 21
        # deal until just more than player score
        self.player_score =  15
        if self.player_score <= 21:

            while self.dealer_score < self.player_score:
                self.dealer_hand.append(self._deal_cards(self.dealer_card_frame))
                self.dealer_score = 30
                self.dealer_score_label.set(self.dealer_score)




# def setup_dealerButton(self):
    #
    # def setup_playerButton(self):
    #
    # def setup_newGameButton(self):
    #
    # def setup_shuffleButton(self):
#unhighlight this
g = GameFrame()
g.setup_mainwindow()
g.final_deck()
g.deal_dealer()
g.mainwindow.mainloop()

#g.setup_mainwindow()
# g.setup_cardframe()
# # g.setup_dealerFrame()
# g.setup_frameForResult()
# g.setup_dealerScore()

# self.setup_mainwindow()
# self.setup_cardframe()
# self.setup_dealerFrame()
# self.setup_frameForResult()
# self.setup_dealerScore()















