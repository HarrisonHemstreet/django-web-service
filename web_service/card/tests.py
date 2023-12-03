from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Card

class CardTests(APITestCase):
    def setUp(self):
        self.card = Card.objects.create(
            name='Test Card',
            mana_cost={
                "Red": 0,
                "Blue": 0,
                "Green": 0,
                "Black": 0,
                "White": 0,
                "Any": 0,
            },
            card_art='Test Art',
            card_type='Test Type',
            expansion_symbol='Test Symbol',
            rarity='Common',
            description='Test Description',
            abilities='Test Abilities',
            effects='Test Effects',
            flavor_text='Test Flavor Text',
            power_toughness={"power": 0, "toughness": 0},
            artist='Test Artist',
            number='1'
        )

    def test_list_cards(self):
        url = reverse('card-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
