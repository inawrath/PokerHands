from django.shortcuts import render
# from django.http import HttpResponse
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from django.http import JsonResponse
import requests
import json
from .help import Cards


class Deck:
    _url_base = 'https://services.comparaonline.com/dealer'
    _token = None
    _sesion = None
    _retry = 0

    def __init__(self, token=None):
        self._sesion = requests.Session()
        self._retry = 0
        retries = Retry(
            total=10,
            backoff_factor=0.1,
            status_forcelist=[
                500,
                501,
                502,
                503,
                504
            ]
        )

        self._sesion.mount('http://', HTTPAdapter(max_retries=retries))

        if token is None:
            self._token = self.newDeck()
        else:
            self._token = token

    def getToken(self):
        return self._token

    def newDeck(self):
        if self._retry > 5:
            return ''
        request = self._sesion.post(self._url_base + '/deck')
        if request.status_code == 200 and len(request.text) == 36:
            return request.text
        self._retry += 1
        return self.newDeck()

    def newHand(self):
        if self._retry > 5:
            return {
                'end': True,
                'message': 'Max retries'
            }
        url = '{}{}/{}/deal/5'.format(
            self._url_base,
            '/deck',
            self._token
        )
        request = self._sesion.get(url)
        print(str(request.status_code) + ' - ' + str(url))
        if request.status_code == 200:
            hand = json.loads(request.text)
            return {
                'end': False,
                'hand': [
                    {
                        'suit': card['suit'],
                        'number': card['number'],
                        'image': Cards.getImage(card['number'], card['suit'])
                    }
                    for card in hand
                ]
            }
        elif request.status_code == 405:
            return {
                'end': True,
                'message': 'GameOver'
            }
        self._retry += 1
        return self.newHand()

    def getHand(self):
        hand = self.newHand()
        if hand['end']:
            return hand
        hand['ranking'] = Cards.rank(hand['hand'])
        return hand


def index(request):
    return render(request, 'index.html')


def new(request):
    if request.method == 'POST':
        deck = Deck()
        hand1 = deck.getHand()
        hand2 = deck.getHand()
        if hand1['end'] or hand2['end']:
            data = {
                'status': True,
                'end': True,
                'message': 'GameOver'
            }
        else:
            data = {
                'token': deck.getToken(),
                'status': True,
                'end': False,
                'hand1': hand1,
                'hand2': hand2,
                'win_hand': Cards.compareTwoHands(hand1['hand'], hand2['hand'])
            }
    else:
        data = {
            'message': 'Method not allowed',
            'status': False
        }
    return JsonResponse(data)


def newHand(request):
    if request.method == 'POST':
        deck = Deck(request.POST.get('token', None))
        hand1 = hand1 = deck.getHand()
        hand2 = None
        if hand1['end']:
            data = {
                'status': True,
                'end': True,
                'message': 'GameOver'
            }
        else:
            hand2 = deck.getHand()
            if hand2['end']:
                data = {
                    'status': True,
                    'end': True,
                    'message': 'GameOver'
                }
            else:
                data = {
                    'token': deck.getToken(),
                    'status': True,
                    'end': False,
                    'hand1': hand1,
                    'hand2': hand2,
                    'win_hand': Cards.compareTwoHands(hand1['hand'], hand2['hand'])
                }
    else:
        data = {
            'message': 'Method not allowed',
            'status': False
        }
    return JsonResponse(data)
