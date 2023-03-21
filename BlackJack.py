#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Card
# Suit,Rank, Value
from IPython.display import clear_output
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
display = {'Two':'|   |\n| 2 |\n|   |', 'Three':'|   |\n| 3 |\n|   |', 'Four':'|   |\n| 4 |\n|   |', 'Five':'|   |\n| 5 |\n|   |',
          'Six':'|   |\n| 6 |\n|   |', 'Seven':'|   |\n| 7 |\n|   |', 'Eight':'|   |\n| 8 |\n|   |', 
            'Nine':'|   |\n| 9 |\n|   |', 'Ten':'|   |\n|10 |\n|   |', 'Jack':'|   |\n| J |\n|   |', 'Queen':'|   |\n| Q |\n|   |',
          'King':'|   |\n| K |\n|   |', 'Ace':'|   |\n| A |\n|   |'}

di = {'Two':'2 ', 'Three':'3 ', 'Four':'4 ', 'Five':'5 ', 'Six':'6 ', 'Seven':'7 ', 'Eight':'8 ', 
            'Nine':'9 ', 'Ten':'10', 'Jack':'J ', 'Queen':'Q ', 'King':'K ', 'Ace':'A '}

## CREATE Cards
class Cards():
    
    def __init__(self, suits, ranks):
        self.suits = suits
        self.ranks = ranks
        self.values = values[ranks]
        self.di = di[ranks]
        self.display = display[ranks]

        
    def __str__(self):
        return self.ranks + ' of '+ self.suits
    
    ## Displays Cards
    def display_card(self):
        print(self.display)


# In[2]:


##card_a = Cards('Hearts','Three')
##card_b = Cards('Hearts', 'Four')
##print(card_a.values)
##card_b.display_card()


# In[3]:


## CREATE a deck
class Deck():
    
    ## Create deck in order
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Cards(suit, rank)
                self.all_cards.append(created_card)
    
    ## shuffles the deck            
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    ## deals the last card
    def deal_one(self):
        return self.all_cards.pop()
    
    def is_empty(self):
        return len(self.all_cards) == 0


# In[4]:


##new_deck = Deck()
##first_card = new_deck.all_cards[0]
##print(first_card)
##last_card = new_deck.all_cards[-1]
##print(last_card)

##a = new_deck.all_cards[9]
##b = new_deck.all_cards[10]

#new_deck.shuffle()
#first_card = new_deck.all_cards[0]
#print(first_card)
#last_card = new_deck.all_cards[-1]
#print(last_card)

##mycard = new_deck.deal_one()
##print(mycard)
##len(new_deck.all_cards)
##new_deck.is_empty()


# In[5]:


## CREATE Dealers hand
class Dealer():
    def __init__(self):
        self.hand = []
        self.sums = 0
        
    def clear_hand(self):
        while len(self.hand) > 0:
            self.hand.pop()
        self.sums = 0   
        
    ## ask for a card from dealer
    def deal(self, new_card):
        self.hand.append(new_card)
        
    def __str__(self):
        display = ''
        for item in self.hand:
            display = display + '\ ' +str(item)
        
        return f"Dealer has {display}"
    
    def get_sum(self):
        sums = 0
        for item in self.hand:
            sums = sums + item.values
            if sums > 21 and item.ranks == 'Ace':
                sums = sums - 10 
            
            
        self.sums = sums    
        return self.sums

    def display(self):
        line1 = ''
        line2 = ''
        line3 = ''
        for num in self.hand:
            line1 = line1 + ' |  | '
            line2 = line2 + ' |' + str(num.di) + '| '
            line3 = line3 + ' |  | '
        if self.dealer_has_ace() and (self.get_sum() > 12) and (bust(self) == False):
            
            print(f'The Dealer has:  {self.get_sum()} or {self.get_sum()- 10}\n\n{line1}\n{line2}\n{line3}\n')
        
        elif self.dealer_has_ace()and self.get_sum()> 21:
            
            print(f'The Dealer has:  {self.get_sum()}\n\n{line1}\n{line2}\n{line3}\n')
        else:
            
            print(f'The Dealer has:  {self.get_sum()}\n\n{line1}\n{line2}\n{line3}\n')
        
    def display_firsthand(self):
        line1 = ' |  |  |? |'
        line2 = ' |' + self.hand[0].di + '|  |? |'
        line3 = ' |  |  |? |'
            
        print(f'\nThe Dealer is showing:  {self.hand[0].values}\n\n{line1}\n{line2}\n{line3}\n')
        
        
        
    def dealer_has_ace(self):
        for num in self.hand:
            if 'Ace' in num.ranks:
                return True
        return False
    
    def black_jack(self):
        return self.get_sum() == 21


# In[6]:


##dealer = Dealer()
##dealer.deal(b)
##print(dealer)


# In[7]:


## CREAT Players hand
class Player():
    
    ## Testing only
    #def __init__(self, name, amount):
        #self.name = name
        #self.amount = amount
        #self.hand = []
        #self.sums = 0
    
    
    ## Creates a player profile
    def __init__(self):
        
        self.name = '                  '
        self.hand = []
        self.amount = 0
        
        while len(self.name) > 10 :           
            self.name = input("Please enter your name (1-10 charaters): ")
            if len(self.name) > 10:
                print("Please pick a name under 10 charaters")
        while True:
            try:
                self.amount = float(input("Select your starting amount (1-1000): "))
            except:
                print("Sorry that's not a number, please pick again!")
            else:
                if self.amount not in range(0, 1001):
                    print("Sorry that amount is out of range, please pick again (1-1000)")
                else:
                    break
    
    ## Check if player has amount left in his account
    def has_amount(self):
        return self.amount > 0
    
    ## Check to see if bet is less than amount
    def able_to_bet(self, bet):
        return (self.amount - bet)>= 0
           
    ## Clears hand
    def clear_hand(self):
        while len(self.hand) > 0:
            self.hand.pop()
        self.sums = 0
        
    ## ask for a card from dealer
    def hit(self, new_card):
        self.hand.append(new_card)
        
    def __str__(self):
        display = ''
        for item in self.hand:
            display = display + '\ ' +str(item)
        
        return f"{self.name} has {display}"
    
    ## get the sum of players hand
    def get_sum(self):
        sums = 0
        for item in self.hand:
            sums = sums + item.values
            
            if sums > 21 and item.ranks == 'Ace':
                sums = sums - 10                                                                                                                                                                        
            

        self.sums = sums    
        return self.sums
    
    
    
    def playerhand_has_ace(self):
        for num in self.hand:
            if 'Ace' in num.ranks:
                return True
        return False
    
    
    def display(self):
        line1 = ''
        line2 = ''
        line3 = ''
        
        for nums in self.hand:
            ##if has_ace(nums):
                ##ace = True
            line1 = line1 + ' |  | '
            line2 = line2 + ' |' + str(nums.di) + '| '
            line3 = line3 + ' |  | '
        if self.playerhand_has_ace() and (self.get_sum() > 12) and (bust(self) == False):
        
            print(f'The Player has:  {self.get_sum()} or {self.get_sum()- 10}\n\n{line1}\n{line2}\n{line3}\n')
            
        elif self.playerhand_has_ace()and self.get_sum()> 21:
            
            print(f'The Player has:  {self.get_sum()}\n\n{line1}\n{line2}\n{line3}\n')
        
        else:
            print(f'The Player has:  {self.get_sum()}\n\n{line1}\n{line2}\n{line3}\n')
        
    ## H to hit, S to Stay
    def get_input(self):
        input_range = ['h','H','s','S']
        choice = 'Null'
        while choice not in input_range:
            choice = input("'H' to hit, 'S' to stay: ")
        return choice.upper()
    
    def get_bet(self):
        bet = 1000000
        
        while bet > self.amount:
            try:
                bet = float(input(f"Please place your bet (you have $ {self.amount} left) : "))
                if bet > self.amount:
                    print("\nYou don't have that much money")
            except:
                print("\nThat's not a valid input")
                
        return bet
                
    def won(self, bet):
        self.amount = self.amount + bet
        
    def lost(self, bet):
        self.amount = self.amount - bet
        
    def black_jack(self, bet):
        if self.get_sum() == 21:
            self.amount = self.amount + bet*1.5
            print("\nBLACK JACK!")
            #self.clear_hand()
        
            return True
        else:
            return False
        
    def set_amount(self, amounts):
        self.amount = amounts
        
        


# In[8]:


#player = Player('Seven', 100)
##player.has_amount()
##player.able_to_bet(300)
##player.hit(first_card)
##player.hit(last_card)
##player.display()
#four = Cards('Hearts', 'Four')
#ace = Cards('Hearts', 'Ace')
#six = Cards('Hearts', 'Six')
#player.hit(four)
#player.hit(ace)
#player.hit(ace)
#player.hit(six)
#print(bust(player))
#player.display()
#print(player.get_sum())


# In[9]:



## Various conditions
## check if player has busted if have ace, will change the sum value
def bust(hands):
    if hands.get_sum() <= 21:
        return False
    elif hands.get_sum() > 21 and has_ace(hands):
        sums = 0
        ace_count = 0
        for item in hands.hand:
            sums = sums + item.values
            if item.ranks == 'Ace':
                ace_count += 1
            
        sums = sums - (10 * ace_count)
                          
        if sums > 21:
                return True
        
        else:
            return False
    else:
        return True
    
## check if player has ACE
def has_ace(hand):
    for num in hand.hand:
        if 'Ace' in num.ranks:
            return True
    return False

## needs work
def result(player, dealer, bets):
    print(f"player : {player.get_sum()}  dealer : {dealer.get_sum()}")
    if player.get_sum() > dealer.get_sum():
        player.won(bets)
        print('\nYou Won\n')
    elif (player.get_sum() < dealer.get_sum()) and bust(dealer) == False:
        player.lost(bets)
        print('\nYou Lost\n')
    elif bust(dealer):
        player.won(bets)
    else:
        print('\nPUSH\n')
        
def update_screen(player, dealer, bet):
    
    clear_output()
    print('####################\n#                  #\n#    BLACKJACK     #\n#                  #\n####################')
    print(f'\nYou have $ {player.amount - bet}')
    print(f"\nCurrent Bet is $ {bet}")
    
    ##dealer.display()
    ##player.display()
    
    
def ask_for_insurance():
        key = ['y', 'Y', 'n', 'N']
        insurance = 'Null'
        while insurance not in key:
            try:
                insurance = input("\nDealer showing Ace, would you like insurance? (Y or N)").upper()
            except:
                print("\nSorry thats not a valid input")
        return insurance


# In[10]:


##player = Player('Seven', 100)
##player.has_amount()
##player.able_to_bet(300)
##player.hit(first_card)
##player.hit(last_card)
##player.hit(a)
#player.hit(b)
##print(player)
##bust(player)
##print(player.sums)


# In[11]:


## WELCOME MESSAGE
print('####################\n#                  #\n#    BLACKJACK     #\n#                  #\n####################')

## VARIABLE TO KEEP GAME GOING
game_on = True



while game_on:
    
    ## SET UP a new deck
    new_deck = Deck()
    new_deck.shuffle()    
    
    ## SET UP a dealer
    dealer = Dealer()
    
    ## set up a player
    ##player = Player('Seven', 100)
    
    player = Player()
    
    
    while player.has_amount():
        
        bet = player.get_bet()
        player_turn = True
        dealer_turn = False
        cont = True
        dealer.deal(new_deck.deal_one())
        dealer.deal(new_deck.deal_one())
        ##print(len(new_deck.all_cards))
        ##dealer.display_firsthand()
        ##print(dealer.get_sum())
        ##aler.display()
        
        player.hit(new_deck.deal_one())
        player.hit(new_deck.deal_one())
        ##print(len(new_deck.all_cards))
        ##player.display()
        ##print(player.get_sum())
    
        
        if player.black_jack(bet):
            dealer.display()
            player.display()
            player.clear_hand()
            dealer.clear_hand()
            cont = False
            
        elif (player.black_jack(bet) == False) and dealer.hand[0].ranks == 'Ace':
            
            insurance = ask_for_insurance()
            if insurance == 'Y':
                insurance_bet = bet/2
                if dealer.black_jack():
                    player.won(bet)
                else:
                    player.lost(insurance_bet)
                
            else:
                pass
            
    
        if (player.black_jack(bet) == False) and dealer.black_jack():
            print('\nDealer BLACK JACK\n')
            player.lost(bet)
            dealer.display()
            player.display()
            player.clear_hand()
            dealer.clear_hand()
            cont = False

            
            
        
        while player_turn and (new_deck.is_empty() == False) and cont:
            
            ##clear_output()
            update_screen(player, dealer, bet)
            dealer.display_firsthand()
            player.display()
            player_choice = player.get_input()
            if player_choice == 'H':
                clear_output()
                ##dealer.display_firsthand()
                player.hit(new_deck.deal_one())
                ##player.display()
                
                if bust(player) == True:
                    print('player bug')
                    dealer.display_firsthand()
                    player.display()
                    print('\nSorry, you have busted!\n')
                    player.lost(bet)
                    player_turn = False
                    dealer_turn = True
                    player.clear_hand()
                    cont = False
                    dealer.clear_hand()
                else:
                    pass
                    
                        
            elif player_choice == 'S':
                print('a')
                ##clear_output()
                ##dealer.display()
                ##player.display()
                player_turn = False
                dealer_turn = True
                cont = True
                
            else:
                print('why am i here')
            
            
                
                               
        while dealer_turn and (new_deck.is_empty() == False) and cont:
            ##update_screen(player, dealer, bet)
            ##clear_output()
            dealer.display()
            player.display()
            
            if dealer.get_sum()in range (17,22):
                result(player,dealer, bet)
                dealer_turn = False
                player_turn = True
                ##clear_output()
                ##dealer.display()
                ##player.display()
                dealer.clear_hand()
                player.clear_hand()
                cont = False
                
                
            elif bust(dealer) == True:
                
                result(player,dealer, bet)
                dealer_turn = False
                player_turn = True
                ##clear_output()
                ##dealer.display()
                ##player.display()
                dealer.clear_hand()
                player.clear_hand()
                cont = False
                print("Dealer Bust\n")
                
                
            elif (bust(dealer) == False) and dealer.get_sum() < 17:
                
                ##clear_output()
                dealer.deal(new_deck.deal_one())
                ##dealer.display()
                ##player.display()
                
            else: 
                dealer.deal(new_deck.deal_one())
                print(dealer.get_sum())
                print("\n some other condition still not checked ")
        
        
            
        if len(new_deck.all_cards) < 10:
            reshuffle = "Null"
            while reshuffle not in ['N','Y']:
                try:
                    reshuffle = input("\nThis Deck is low on Cards, Would you like to keep playing? (Y or N)").upper()
                except:
                    print("\nSorry thats not a valid input")
                    
            if reshuffle == 'Y':
                new_deck = Deck()
                new_deck.shuffle()
            else:
                game_on = False
        
        
        if player.amount == 0:
            key = ['y', 'Y', 'n', 'N']
            add_money = 'Null'
            while add_money not in key:
                try:
                    add_money = input("\nYou are out of Money, Would you like to add more fund? (Y or N)")
                except:
                    print("\nSorry thats not a valid input")
            add_money = add_money.upper()
            if add_money == 'Y':
                while True:
                    try:
                        money = float(input("Select your starting amount (1-1000): "))
                    except:
                        print("Sorry that's not a number, please pick again!")
                    else:
                        if player.amount not in range(0, 1001):
                            print("Sorry that amount is out of range, please pick again (1-1000)")
                        else:
                            break
                player.set_amount(money)
                        
                            
            else:
                game_on = False
                clear_output()
                print("\nThanks For Playing")
                
            
        
        ##break
    
    
    break
                                                                 
    
    
    


# In[ ]:





# In[ ]:




