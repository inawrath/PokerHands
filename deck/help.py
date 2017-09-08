CLUBS = 'clubs'
DIAMONDS = 'diamonds'
HEARTS = 'hearts'
SPADES = 'spades'


class Cards:
    _path_image = 'https://private-storage-inc.s3.amazonaws.com/cards/'
    _cards = {
        '2': {
            CLUBS: {
                'url': '2_of_clubs.png'
            },
            DIAMONDS: {
                'url': '2_of_diamonds.png'
            },
            HEARTS: {
                'url': '2_of_hearts.png'
            },
            SPADES: {
                'url': '2_of_spades.png'
            },
            'size': 1,
        },
        '3': {
            CLUBS: {
                'url': '3_of_clubs.png'
            },
            DIAMONDS: {
                'url': '3_of_diamonds.png'
            },
            HEARTS: {
                'url': '3_of_hearts.png'
            },
            SPADES: {
                'url': '3_of_spades.png'
            },
            'size': 2,
        },
        '4': {
            CLUBS: {
                'url': '4_of_clubs.png'
            },
            DIAMONDS: {
                'url': '4_of_diamonds.png'
            },
            HEARTS: {
                'url': '4_of_hearts.png'
            },
            SPADES: {
                'url': '4_of_spades.png'
            },
            'size': 3,
        },
        '5': {
            CLUBS: {
                'url': '5_of_clubs.png'
            },
            DIAMONDS: {
                'url': '5_of_diamonds.png'
            },
            HEARTS: {
                'url': '5_of_hearts.png'
            },
            SPADES: {
                'url': '5_of_spades.png'
            },
            'size': 4,
        },
        '6': {
            CLUBS: {
                'url': '6_of_clubs.png'
            },
            DIAMONDS: {
                'url': '6_of_diamonds.png'
            },
            HEARTS: {
                'url': '6_of_hearts.png'
            },
            SPADES: {
                'url': '6_of_spades.png'
            },
            'size': 5,
        },
        '7': {
            CLUBS: {
                'url': '7_of_clubs.png'
            },
            DIAMONDS: {
                'url': '7_of_diamonds.png'
            },
            HEARTS: {
                'url': '7_of_hearts.png'
            },
            SPADES: {
                'url': '7_of_spades.png'
            },
            'size': 6,
        },
        '8': {
            CLUBS: {
                'url': '8_of_clubs.png'
            },
            DIAMONDS: {
                'url': '8_of_diamonds.png'
            },
            HEARTS: {
                'url': '8_of_hearts.png'
            },
            SPADES: {
                'url': '8_of_spades.png'
            },
            'size': 7,
        },
        '9': {
            CLUBS: {
                'url': '9_of_clubs.png'
            },
            DIAMONDS: {
                'url': '9_of_diamonds.png'
            },
            HEARTS: {
                'url': '9_of_hearts.png'
            },
            SPADES: {
                'url': '9_of_spades.png'
            },
            'size': 8,
        },
        '10': {
            CLUBS: {
                'url': '10_of_clubs.png'
            },
            DIAMONDS: {
                'url': '10_of_diamonds.png'
            },
            HEARTS: {
                'url': '10_of_hearts.png'
            },
            SPADES: {
                'url': '10_of_spades.png'
            },
            'size': 9,
        },
        'J': {
            CLUBS: {
                'url': 'jack_of_clubs.png'
            },
            DIAMONDS: {
                'url': 'jack_of_diamonds.png'
            },
            HEARTS: {
                'url': 'jack_of_hearts.png'
            },
            SPADES: {
                'url': 'jack_of_spades.png'
            },
            'size': 10,
        },
        'Q': {
            CLUBS: {
                'url': 'queen_of_clubs.png'
            },
            DIAMONDS: {
                'url': 'queen_of_diamonds.png'
            },
            HEARTS: {
                'url': 'queen_of_hearts.png'
            },
            SPADES: {
                'url': 'queen_of_spades.png'
            },
            'size': 11,
        },
        'K': {
            CLUBS: {
                'url': 'king_of_clubs.png'
            },
            DIAMONDS: {
                'url': 'king_of_diamonds.png'
            },
            HEARTS: {
                'url': 'king_of_hearts.png'
            },
            SPADES: {
                'url': 'king_of_spades.png'
            },
            'size': 12,
        },
        'A': {
            CLUBS: {
                'url': 'ace_of_clubs.png'
            },
            DIAMONDS: {
                'url': 'ace_of_diamonds.png'
            },
            HEARTS: {
                'url': 'ace_of_hearts.png'
            },
            SPADES: {
                'url': 'ace_of_spades.png'
            },
            'size': 13,
        },
    }

    _rules = {
        'Royal Flush': ['10', 'A', 'J', 'K', 'Q']
    }

    _rank = {
        0: 'Without rank',
        2: 'One Pair',
        3: 'Two Pairs',
        4: 'Three of a Kind',
        5: 'Straight',
        6: 'Flush',
        7: 'Full House',
        8: 'Four of a Kind',
        9: 'Straight Flush',
        10: 'Royal Flush',
    }

    @staticmethod
    def getImage(number, suit):
        return Cards._path_image + Cards._cards.get(number, {}).get(suit, {}).get('url', 'black_joker.png')

    @staticmethod
    def size(number):
        return Cards._cards.get(number, {}).get('size', 0)

    @staticmethod
    def sizeHand(list_cards):
        list_values = [
            Cards.size(card['number'])
            for card in list_cards
        ]
        list_values.sort(reverse=True)
        return list_values

    @staticmethod
    def getNumberSameSuit(list_cards):
        suits = {
            CLUBS: 0,
            DIAMONDS: 0,
            HEARTS: 0,
            SPADES: 0,
        }
        for card in list_cards:
            suits[card['suit']] += 1

        return dict(
            filter(lambda result: result[1] > 0, suits.items())
        )

    @staticmethod
    def getNumberCardsSameValue(list_cards):
        values = {}
        for card in list_cards:
            number = card['number'].upper()
            if values.get(number, False):
                values[number] += 1
            else:
                values[number] = 1
        return values

    @staticmethod
    def allSameSuit(list_cards):
        list_suits = Cards.getNumberSameSuit(list_cards)
        if len(list_suits) == 1:
            return list_suits[list(list_suits.keys())[0]] == 5
        return False

    @staticmethod
    def allConsecutiveCards(list_cards):
        list_values = list(
            set(
                Cards.size(card['number'])
                for card in list_cards
            )
        )
        if len(list_values) == 5:
            for index, value in enumerate(list_values):
                index_next = index + 1
                if index_next <= 4:
                    if value + 1 == list_values[index_next]:
                        continue
                    else:
                        return False

                elif index == 4:
                    return True
        return False

    @staticmethod
    def isRoyalFlush(list_cards):
        if Cards.allSameSuit(list_cards):
            cards = list(Cards.getNumberCardsSameValue(list_cards).keys())
            cards.sort()
            return cards in list(Cards._rules['Royal Flush'])
        return False

    @staticmethod
    def isStraightFlush(list_cards):
        return Cards.allConsecutiveCards(list_cards) and Cards.allSameSuit(list_cards)

    @staticmethod
    def isFourOfAKing(list_cards):
        return 4 in Cards.getNumberCardsSameValue(list_cards).values()

    @staticmethod
    def isFullHouse(list_cards):
        numbers_values = Cards.getNumberCardsSameValue(list_cards).values()
        return 3 in numbers_values and 2 in numbers_values

    @staticmethod
    def isFlush(list_cards):
        return Cards.allSameSuit(list_cards)

    @staticmethod
    def isStraight(list_cards):
        return Cards.allConsecutiveCards(list_cards)

    @staticmethod
    def isThreeOfAKing(list_cards):
        return 3 in Cards.getNumberCardsSameValue(list_cards).values()

    @staticmethod
    def isTwoPairs(list_cards):
        return list(Cards.getNumberCardsSameValue(list_cards).values()).count(2) == 2

    @staticmethod
    def isOnePair(list_cards):
        return 2 in Cards.getNumberCardsSameValue(list_cards).values()

    @staticmethod
    def HighHand(cards_hand1, cards_hand2):
        list_values_hand1 = Cards.sizeHand(cards_hand1)
        list_values_hand2 = Cards.sizeHand(cards_hand2)
        for i in range(0, 5):
            if list_values_hand1[i] == list_values_hand2[i]:
                continue
            return 1 if list_values_hand1[i] > list_values_hand2[i] else 2
        return 0

    @staticmethod
    def rankHand(list_cards):
        if Cards.isRoyalFlush(list_cards):
            return 10
        if Cards.isStraightFlush(list_cards):
            return 9
        if Cards.isFourOfAKing(list_cards):
            return 8
        if Cards.isFullHouse(list_cards):
            return 7
        if Cards.isFlush(list_cards):
            return 6
        if Cards.isStraight(list_cards):
            return 5
        if Cards.isThreeOfAKing(list_cards):
            return 4
        if Cards.isTwoPairs(list_cards):
            return 3
        if Cards.isOnePair(list_cards):
            return 2
        return 0

    @staticmethod
    def rank(list_cards):
        return Cards._rank[Cards.rankHand(list_cards)]

    @staticmethod
    def compareTwoHands(cards_hand1, cards_hand2):
        rank_hand1 = Cards.rankHand(cards_hand1)
        rank_hand2 = Cards.rankHand(cards_hand2)

        if rank_hand1 > rank_hand2:
            return 1
        if rank_hand2 > rank_hand1:
            return 2
        if rank_hand1 == rank_hand2:
            return Cards.HighHand(cards_hand1, cards_hand2)
