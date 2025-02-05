from player import Player

class PlayerRecord(Player):
    def __init__(self, player_name: str, character_race: str, year_old: int, nationality: str, money: int, body_type: str,
                 strength: int, dexterity: int, intelligence: int, preparation: int, luck: int,
                 interpersonal: int, medicine: int, cooking: int, perception: int, constitution: int):
        super().__init__(player_name, character_race, year_old, nationality, money, body_type)
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.preparation = preparation
        self.luck = luck
        self.interpersonal = interpersonal
        self.medicine = medicine
        self.cooking = cooking
        self.perception = perception
        self.constitution = constitution
