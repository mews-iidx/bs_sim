import random
class Card:
    def __init___(self, name, img):
        self.name = card_name
        self.img = card_img

class Trash:
    def __init__(self):
        self.cards = []
        self.core = 0


class Reserve:
    def __init__(self):
        self.core = 3
        self.soulcore = 1

class Burst:
    def __init__(self):
        self.burst = None
        self.is_set = False

def CardListDebug(deck_id):
    card_list = []
    for i in range(40):
        card = {'name' : 'yamauchi', 'img_path': 'yamauchi.png'}
        card['name'] = card['name'] + str(i)
        card_list.append(card)
    return  card_list

def get_deck(deck_id):
    #TODO fix it, for debug
    card_list = CardListDebug(deck_id)
    return card_list
    
    

class Player:
    def __init__(self, user_id, deck_id):
        self.user_id = user_id
        self.deck_id = deck_id
        self.deck = get_deck(deck_id)
        self.hand = []
        self.burst = Burst()
        self.life = 5
        self.reserve = Reserve()
        self.trash = Trash()

        #TODO fix it, for debug
        card_list = get_deck(deck_id)
    def __repr__(self):
        return '''
            user_id : %d
            deck_id : %d
            life : %d
            hand : %s
            ''' % (self.user_id, self.deck_id, self.life, self.hand)

#def player_info(player):
    

class Game:
    def __init__(self):
        #TODO fix it, for debug
        self.p1 = Player(0, 0)
        self.p2 = Player(0, 0)
        self.turn_seq = ['start', 'core', 'draw', 'refresh', 'main', 'attack', 'end']
        self._confirm_turn_player()

    def _confirm_turn_player(self):
        if random.randrange(2) == 0:
            self.turn_player = self.p1
            self.enemy_player = self.p2
        else:
            self.turn_player = self.p2
            self.enemy_player = self.p1
        
    def toggle_player(self):
        if self.turn_player == self.p1:
            self.turn_player = self.p2
            self.enemy_player = self.p1
        else:
            self.turn_player = self.p1
            self.enemy_player = self.p2

    def game_init(self):
        FIRST_DRAW = 4
        random.shuffle(self.p1.deck)
        random.shuffle(self.p2.deck)

        for i in range(FIRST_DRAW):
            self.draw(self.p1)
            self.draw(self.p2)

        
    def draw(self, player):
        draw_card = player.deck.pop(0)
        player.hand.append(draw_card)


if __name__ == '__main__':
    game_master = Game()
    game_master.game_init()
    print(game_master.p1)
