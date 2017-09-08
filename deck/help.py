
class Cards:
    _path_image = 'https://private-storage-inc.s3.amazonaws.com/cards/'
    _cards = {
        '2': {
            'clubs': {
                'url': '2_of_clubs.png'
            },
            'diamonds': {
                'url': '2_of_diamonds.png'
            },
            'hearts': {
                'url': '2_of_hearts.png'
            },
            'spades': {
                'url': '2_of_spades.png'
            },
            'size': 1,
        },
        '3': {
            'clubs': {
                'url': '3_of_clubs.png'
            },
            'diamonds': {
                'url': '3_of_diamonds.png'
            },
            'hearts': {
                'url': '3_of_hearts.png'
            },
            'spades': {
                'url': '3_of_spades.png'
            },
            'size': 2,
        },
        '4': {
            'clubs': {
                'url': '4_of_clubs.png'
            },
            'diamonds': {
                'url': '4_of_diamonds.png'
            },
            'hearts': {
                'url': '4_of_hearts.png'
            },
            'spades': {
                'url': '4_of_spades.png'
            },
            'size': 3,
        },
        '5': {
            'clubs': {
                'url': '5_of_clubs.png'
            },
            'diamonds': {
                'url': '5_of_diamonds.png'
            },
            'hearts': {
                'url': '5_of_hearts.png'
            },
            'spades': {
                'url': '5_of_spades.png'
            },
            'size': 4,
        },
        '6': {
            'clubs': {
                'url': '6_of_clubs.png'
            },
            'diamonds': {
                'url': '6_of_diamonds.png'
            },
            'hearts': {
                'url': '6_of_hearts.png'
            },
            'spades': {
                'url': '6_of_spades.png'
            },
            'size': 5,
        },
        '7': {
            'clubs': {
                'url': '7_of_clubs.png'
            },
            'diamonds': {
                'url': '7_of_diamonds.png'
            },
            'hearts': {
                'url': '7_of_hearts.png'
            },
            'spades': {
                'url': '7_of_spades.png'
            },
            'size': 6,
        },
        '8': {
            'clubs': {
                'url': '8_of_clubs.png'
            },
            'diamonds': {
                'url': '8_of_diamonds.png'
            },
            'hearts': {
                'url': '8_of_hearts.png'
            },
            'spades': {
                'url': '8_of_spades.png'
            },
            'size': 7,
        },
        '9': {
            'clubs': {
                'url': '9_of_clubs.png'
            },
            'diamonds': {
                'url': '9_of_diamonds.png'
            },
            'hearts': {
                'url': '9_of_hearts.png'
            },
            'spades': {
                'url': '9_of_spades.png'
            },
            'size': 8,
        },
        '10': {
            'clubs': {
                'url': '10_of_clubs.png'
            },
            'diamonds': {
                'url': '10_of_diamonds.png'
            },
            'hearts': {
                'url': '10_of_hearts.png'
            },
            'spades': {
                'url': '10_of_spades.png'
            },
            'size': 9,
        },
        'jack': {
            'clubs': {
                'url': 'jack_of_clubs.png'
            },
            'diamonds': {
                'url': 'jack_of_diamonds.png'
            },
            'hearts': {
                'url': 'jack_of_hearts.png'
            },
            'spades': {
                'url': 'jack_of_spades.png'
            },
            'size': 10,
        },
        'queen': {
            'clubs': {
                'url': 'queen_of_clubs.png'
            },
            'diamonds': {
                'url': 'queen_of_diamonds.png'
            },
            'hearts': {
                'url': 'queen_of_hearts.png'
            },
            'spades': {
                'url': 'queen_of_spades.png'
            },
            'size': 11,
        },
        'king': {
            'clubs': {
                'url': 'king_of_clubs.png'
            },
            'diamonds': {
                'url': 'king_of_diamonds.png'
            },
            'hearts': {
                'url': 'king_of_hearts.png'
            },
            'spades': {
                'url': 'king_of_spades.png'
            },
            'size': 12,
        },
        'ace': {
            'clubs': {
                'url': 'ace_of_clubs.png'
            },
            'diamonds': {
                'url': 'ace_of_diamonds.png'
            },
            'hearts': {
                'url': 'ace_of_hearts.png'
            },
            'spades': {
                'url': 'ace_of_spades.png'
            },
            'size': 13,
        },
    }

    _rules = {}

    @staticmethod
    def get(number, suit):
        return Cards._path_image + Cards._cards.get(number, {}).get(suit, 'black_joker.png')

    @staticmethod
    def size(number):
        return Cards._cards.get(number, {}).get('size', 0)
