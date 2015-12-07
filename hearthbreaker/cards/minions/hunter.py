from hearthbreaker.cards.base import MinionCard
from hearthbreaker.constants import CHARACTER_CLASS, CARD_RARITY, MINION_TYPE
from hearthbreaker.game_objects import Minion
from hearthbreaker.tags.action import Draw, Summon, AddCard, Give, Kill
from hearthbreaker.tags.base import Effect, Aura, Deathrattle, Battlecry, ActionTag
from hearthbreaker.tags.card_source import CollectionSource
from hearthbreaker.tags.condition import IsType, Not, GreaterThan, MinionIsNotTarget
from hearthbreaker.tags.event import MinionPlaced, MinionDied, Damaged, CharacterDamaged
from hearthbreaker.tags.selector import MinionSelector, SelfSelector, PlayerSelector, UserPicker, Count, \
    HeroSelector, CardSelector, BothPlayer, TargetSelector
from hearthbreaker.tags.status import Add, CHARACTER_STATUS, SetTrue, PLAYER_STATUS, Multiply


class TimberWolf(MinionCard):
    def __init__(self):
        super().__init__("Timber Wolf", 1, CHARACTER_CLASS.HUNTER, CARD_RARITY.FREE, minion_type=MINION_TYPE.BEAST)

    def create_minion(self, player):
        return Minion(1, 1, auras=[Aura(Add(CHARACTER_STATUS.ATTACK, 1), MinionSelector(IsType(MINION_TYPE.BEAST)))])


class Hyena(MinionCard):
    def __init__(self):
        super().__init__("Hyena", 2, CHARACTER_CLASS.HUNTER, CARD_RARITY.RARE, False, minion_type=MINION_TYPE.BEAST)

    def create_minion(self, player):
        return Minion(2, 2)


class SavannahHighmane(MinionCard):
    def __init__(self):
        super().__init__("Savannah Highmane", 6, CHARACTER_CLASS.HUNTER, CARD_RARITY.RARE,
                         minion_type=MINION_TYPE.BEAST)

    def create_minion(self, player):
        return Minion(6, 5, deathrattle=Deathrattle(Summon(Hyena(), 2), PlayerSelector()))


class Houndmaster(MinionCard):
    def __init__(self):
        super().__init__("Houndmaster", 4, CHARACTER_CLASS.HUNTER, CARD_RARITY.FREE, minion_type=MINION_TYPE.NONE,
                         battlecry=Battlecry(Give([Add(CHARACTER_STATUS.HEALTH, 2), Add(CHARACTER_STATUS.ATTACK, 2),
                                                   SetTrue(CHARACTER_STATUS.TAUNT)]),
                                             MinionSelector(IsType(MINION_TYPE.BEAST), picker=UserPicker())))

    def create_minion(self, player):
        return Minion(4, 3)


class KingKrush(MinionCard):
    def __init__(self):
        super().__init__("King Krush", 9, CHARACTER_CLASS.HUNTER, CARD_RARITY.LEGENDARY, minion_type=MINION_TYPE.BEAST)

    def create_minion(self, player):
        return Minion(8, 8, charge=True)


class StarvingBuzzard(MinionCard):
    def __init__(self):
        super().__init__("Starving Buzzard", 5, CHARACTER_CLASS.HUNTER, CARD_RARITY.COMMON,
                         minion_type=MINION_TYPE.BEAST)

    def create_minion(self, player):
        return Minion(3, 2,
                      effects=[Effect(MinionPlaced(IsType(MINION_TYPE.BEAST)), ActionTag(Draw(), PlayerSelector()))])


class TundraRhino(MinionCard):
    def __init__(self):
        super().__init__("Tundra Rhino", 5, CHARACTER_CLASS.HUNTER, CARD_RARITY.COMMON, minion_type=MINION_TYPE.BEAST)

    def create_minion(self, player):
        return Minion(2, 5, charge=True,
                      auras=[Aura(SetTrue(CHARACTER_STATUS.CHARGE), MinionSelector(IsType(MINION_TYPE.BEAST)))])


class ScavengingHyena(MinionCard):
    def __init__(self):
        super().__init__("Scavenging Hyena", 2, CHARACTER_CLASS.HUNTER, CARD_RARITY.COMMON,
                         minion_type=MINION_TYPE.BEAST)

    def create_minion(self, player):
        return Minion(2, 2,
                      effects=[Effect(MinionDied(IsType(MINION_TYPE.BEAST)),
                                      ActionTag(Give(Add(CHARACTER_STATUS.ATTACK, 2)), SelfSelector())),
                               Effect(MinionDied(IsType(MINION_TYPE.BEAST)),
                                      ActionTag(Give(Add(CHARACTER_STATUS.HEALTH, 1)), SelfSelector()))])


class Webspinner(MinionCard):
    def __init__(self):
        super().__init__("Webspinner", 1, CHARACTER_CLASS.HUNTER, CARD_RARITY.COMMON, minion_type=MINION_TYPE.BEAST)

    def create_minion(self, player):
        return Minion(1, 1, deathrattle=Deathrattle(AddCard(CollectionSource([IsType(MINION_TYPE.BEAST)])),
                                                    PlayerSelector()))


class Hound(MinionCard):
    def __init__(self):
        super().__init__("Hound", 1, CHARACTER_CLASS.HUNTER, CARD_RARITY.COMMON, False, minion_type=MINION_TYPE.BEAST)

    def create_minion(self, player):
        return Minion(1, 1, charge=True)


class Huffer(MinionCard):
    def __init__(self):
        super().__init__("Huffer", 3, CHARACTER_CLASS.HUNTER, CARD_RARITY.COMMON, False, minion_type=MINION_TYPE.BEAST)

    def create_minion(self, player):
        return Minion(4, 2, charge=True)


class Misha(MinionCard):
    def __init__(self):
        super().__init__("Misha", 3, CHARACTER_CLASS.HUNTER, CARD_RARITY.COMMON, False, minion_type=MINION_TYPE.BEAST)

    def create_minion(self, player):
        return Minion(4, 4, taunt=True)


class Leokk(MinionCard):
    def __init__(self):
        super().__init__("Leokk", 3, CHARACTER_CLASS.HUNTER, CARD_RARITY.COMMON, False, minion_type=MINION_TYPE.BEAST)

    def create_minion(self, player):
        return Minion(2, 4, auras=[Aura(Add(CHARACTER_STATUS.ATTACK, 1), MinionSelector())])


class Snake(MinionCard):
    def __init__(self):
        super().__init__("Snake", 0, CHARACTER_CLASS.HUNTER, CARD_RARITY.COMMON, False, minion_type=MINION_TYPE.BEAST)

    def create_minion(self, player):
        return Minion(1, 1)


class MetaltoothLeaper(MinionCard):
    def __init__(self):
        super().__init__("Metaltooth Leaper", 3, CHARACTER_CLASS.HUNTER, CARD_RARITY.RARE, minion_type=MINION_TYPE.MECH,
                         battlecry=Battlecry(Give(Add(CHARACTER_STATUS.ATTACK, 2)),
                                             MinionSelector(IsType(MINION_TYPE.MECH))))

    def create_minion(self, player):
        return Minion(3, 3)


class KingOfBeasts(MinionCard):
    def __init__(self):
        super().__init__("King of Beasts", 5, CHARACTER_CLASS.HUNTER, CARD_RARITY.RARE, minion_type=MINION_TYPE.BEAST,
                         battlecry=Battlecry(Give(Add(CHARACTER_STATUS.ATTACK, Count(MinionSelector(IsType(
                             MINION_TYPE.BEAST))))), SelfSelector()))

    def create_minion(self, player):
        return Minion(2, 6, taunt=True)


class Gahzrilla(MinionCard):
    def __init__(self):
        super().__init__("Gahz'rilla", 7, CHARACTER_CLASS.HUNTER, CARD_RARITY.LEGENDARY, minion_type=MINION_TYPE.BEAST)

    def create_minion(self, player):
        return Minion(6, 9, effects=[Effect(Damaged(), ActionTag(Give(Multiply(CHARACTER_STATUS.ATTACK, 2)),
                                                                 SelfSelector()))])


class SteamwheedleSniper(MinionCard):
    def __init__(self):
        super().__init__("Steamwheedle Sniper", 2, CHARACTER_CLASS.HUNTER, CARD_RARITY.EPIC)

    def create_minion(self, player):
        return Minion(2, 3, auras=[Aura(SetTrue(PLAYER_STATUS.POWER_TARGETS_MINIONS), HeroSelector())])


class CoreRager(MinionCard):
    def __init__(self):
        super().__init__("Core Rager", 4, CHARACTER_CLASS.HUNTER, CARD_RARITY.RARE, minion_type=MINION_TYPE.BEAST,
                         battlecry=(Battlecry(Give([Add(CHARACTER_STATUS.ATTACK, 3), Add(CHARACTER_STATUS.HEALTH, 3)]),
                                              SelfSelector(),
                                              Not(GreaterThan(Count(CardSelector()), value=0)))))

    def create_minion(self, player):
        return Minion(4, 4)


class Acidmaw(MinionCard):
    def __init__(self):
        super().__init__("Acidmaw", 7, CHARACTER_CLASS.HUNTER, CARD_RARITY.LEGENDARY, minion_type=MINION_TYPE.BEAST)

    def create_minion(self, player):
        return Minion(4, 2, effects=[Effect(CharacterDamaged(MinionIsNotTarget(), BothPlayer()),
                                            [ActionTag(Kill(), TargetSelector())])])
