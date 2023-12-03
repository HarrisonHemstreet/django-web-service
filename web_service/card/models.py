from django.db import models
from django.core.exceptions import ValidationError

class Card(models.Model):
    class CardType(models.TextChoices):
        RED = 'Red', 'Red'
        BLUE = 'Blue', 'Blue'
        GREEN = 'Green', 'Green'
        BLACK = 'Black', 'Black'
        WHITE = 'White', 'White'
        ANY = 'Any', 'Any'

    class ExpansionSymbol(models.TextChoices):
        FIRST = 'First', 'First'

    class Rarity(models.TextChoices):
        COMMON = 'Common', 'Common'
        RARE = 'Rare', 'Rare'
        LEGENDARY = 'Legendary', 'Legendary'
        MYTHIC = 'Mythic', 'Mythic'

    def default_mana_cost(self):
        return {
            "Red": 0,
            "Blue": 0,
            "Green": 0,
            "Black": 0,
            "White": 0,
            "Any": 0,
        }
    
    def default_power_toughness(self):
        return {"power": 0, "toughness": 0}

    name = models.CharField(max_length=40)
    mana_cost = models.JSONField(default=default_mana_cost)
    card_art = models.URLField()
    card_type = models.CharField(max_length=5, choices=CardType.choices)
    expansion_symbol = models.CharField(max_length=5, choices=ExpansionSymbol.choices)
    rarity = models.CharField(max_length=9, choices=Rarity.choices)
    description = models.CharField(max_length=120)
    abilities = models.CharField(max_length=120)
    effects = models.CharField(max_length=120)
    flavor_text = models.CharField(max_length=120)
    power_toughness = models.JSONField(default=default_power_toughness)
    artist = models.CharField(max_length=40)
    number = models.IntegerField(default=-1)

    def clean(self):
        # Validate mana_cost structure
        mana_cost_required_keys = ["Red", "Blue", "Green", "Black", "White", "Any"]
        if not all(key in self.mana_cost for key in mana_cost_required_keys):
            raise ValidationError("All mana cost keys must be present: ('Red', 'Blue', 'Green', 'Black', 'White', 'Any')")
        
        if not all(isinstance(self.mana_cost[key], int) for key in mana_cost_required_keys):
            raise ValidationError("All mana cost values must be integers.")

        # Validation for power_toughness
        power_toughness_required_keys = ["power", "toughness"]
        if not all(key in self.power_toughness for key in power_toughness_required_keys):
            raise ValidationError("Both power and toughness keys must be present.")
        
        if not all(isinstance(self.power_toughness[key], int) for key in power_toughness_required_keys):
            raise ValidationError("Power and toughness values must be integers or None.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
