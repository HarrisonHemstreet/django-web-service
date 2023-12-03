from rest_framework import viewsets
from .models import Card
from .serializers import CardSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class CardCreateView(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    
    def create(self, request, *args, **kwargs):
        card = Card.objects.create(
            name=request.data['name'],
            mana_cost=request.data['mana_cost'],
            card_art=request.data['card_art'],
            card_type=request.data['card_type'],
            expansion_symbol=request.data['expansion_symbol'],
            rarity=request.data['rarity'],
            description=request.data['description'],
            abilities=request.data['abilities'],
            effects=request.data['effects'],
            flavor_text=request.data['flavor_text'],
            power_toughness=request.data['power_toughness'],
            artist=request.data['artist'],
            number=request.data['number']
        )
        card.save()
        return Response(CardSerializer(card).data)

class CardRetrieveView(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    def retrieve(self, request, *args, **kwargs):
        cards = Card.objects.all()
        return Response(CardSerializer(cards, many=True).data)

class CardUpdateView(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    def update(self, request, *args, **kwargs):
        card = Card.objects.get(id=request.data['id'])
        card.name = request.data['name']
        card.mana_cost = request.data['mana_cost']
        card.card_art = request.data['card_art']
        card.card_type = request.data['card_type']
        card.expansion_symbol = request.data['expansion_symbol']
        card.rarity = request.data['rarity']
        card.description = request.data['description']
        card.abilities = request.data['abilities']
        card.effects = request.data['effects']
        card.flavor_text = request.data['flavor_text']
        card.power_toughness = request.data['power_toughness']
        card.artist = request.data['artist']
        card.number = request.data['number']
        card.save()
        return Response(CardSerializer(card).data)

class CardDeleteView(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    def destroy(self, request, *args, **kwargs):
        card = Card.objects.get(id=request.data['id'])
        card.delete()
        return Response(CardSerializer(card).data)
