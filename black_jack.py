class Card(object):

    RANKS=[
        'A','2','3','4','5','6','7','8','10','J','Q','K'
    ]
    
    SUITS=[
        'c','d','h','s'
    ]

    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit

    def __str__(self):
        rep=self.rank +self.suit
        return rep

class Unprintable_Card(Card):

     def __str__(self):
        return'<Unprintable>'


class Positionable_Card(Card):
        
    def __init__(self,rank,suit,face__up=True):
        
            super(Positionable_Card,self).__init__(rank,suit)
            self.is__face__up=face__up

    def __str__(self):
        
            if self.is__face__up:
                
                rep=super(Positionable_Card,self).__str__()
                
            else:
                rep='XX'

            return rep
        
    def flip(self):
        
            self.is__face__up= not self.is__face__up

Card1=Card('A','c')
Card2=Unprintable_Card('A','d')
Card3=Positionable_Card('A','h')

print('Print a Card object:')
print(Card1)


print('Print an Unprinatable card object: ')
print(Card2)

print('Print a Positionable Card object:  ')
print(Card3)

print('Flipping the Positionable Card object:  ')
Card3.flip()

print('Printing the Positionable card object: ')
print(Card3)
        
    
