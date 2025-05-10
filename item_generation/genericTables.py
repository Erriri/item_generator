import random
import item_generation.rollDice as rollDice


if __name__ == "__main__":
    print("This is a module file for the main program. Open main.py instead.")


### Rarity

def rollRarity() -> str:
    roll = rollDice.d20()
    if roll < 7:
        return "Common"
    if roll < 13:
        return "Uncommon"
    if roll < 17:
        return "Rare"
    if roll < 20:
        return "Very rare"
    return "Legendary"


### Creator

CreatorList = (
    "Aberration", "Human", "Human", "Human", # Yes, you get Human for 3 rolls
    "Celestial", "Dragon", "Drow", "Dwarf", "Dwarf", # There are several duplicates in these tables
    "El. Air", "El. Earth", "El. Fire", "El. Water",
    "Elf", "Elf", "Fey", "Fiend",
    "Giant", "Gnome", "Undead"
)

def rollCreator() -> str:
    return random.choice(CreatorList)


### Source of Power

SourceList = (
    "Masterfully crafted", "Empowered by the Arcane", "Empowered by Psionics",
    "Empowered by Nature", "Empowered by Nature",
    "Fueled by Antimagic", "Fueled by Hate", "Fueled by Undeath",
    "Powered by Celestials", "Powered by Celestials",
    "Powered by Fiends", "Powered by Fiends",
    "Powered by Elements", "Powered by Elements", "Powered by Elements",
    "Powered by the Feywild", "Powered by the Feywild",
    "Powered by the Shadowfell", "Powered by the Shadowfell",
    "Powered by the Unknown"
)

def rollSource() -> str:
    return random.choice(SourceList)


### Age

def rollAge() -> str:
    roll = rollDice.d20()
    if roll < 4:
        return "Several years old"
    if roll < 9:
        return "Decades old"
    if roll < 16:
        return "Centuries old"
    if roll < 19:
        return "Millenia old"
    return "Times immemorial"


### Detail from History

DetailList = (
    "Arcane", "Bane", "Heroic", "Ornament", "Prophecy", "Religious", 
    "Sinister", "Symbol of Power", "Neglect", "Symbol of Change"
)

def rollDetail() -> str:
    return random.choice(DetailList)


### Minor Property

PropertyList = (
    "Beacon", "Compass", "Conscientious", "Delver", "Gleaming",
    "Guardian", "Harmonious", "Hidden Message", "Key", "Language",
    "Sentinel", "Song Craft", "Strange Material", "Temperate", "Unbreakable",
    "War Leader", "Waterborne", "Wicked", "Illusion", "REROLL"
)

def rollProperty() -> str:
    randProperty = random.choice(PropertyList)
    if randProperty == "REROLL":
        randProperty1 = random.choice(PropertyList)
        while randProperty1 == "REROLL":
            randProperty1 = random.choice(PropertyList)

        randProperty2 = random.choice(PropertyList)
        while randProperty2 == "REROLL":
            randProperty2 = random.choice(PropertyList)
        
        return randProperty1 + " and " + randProperty2
    return randProperty


### Quirk

QuirkList = (
    "Blissful", "Confident", "Covetous", "Frail", "Hungry",
    "Loud", "Metamorphic", "Muttering", "Painful", "Possessive",
    "Repulsive", "Slothful", "Sentient", "Item Set", "Elusive",
    "Clinging", "Shifting", "Unfinished", "Transformative", "REROLL"
)

def rollQuirk() -> str:
    quirk = random.choice(QuirkList)
    if quirk == "REROLL":
        quirk1 = random.choice(QuirkList)
        while quirk1 == "REROLL":
            quirk1 = random.choice(QuirkList)

        quirk2 = random.choice(QuirkList)
        while quirk2 == "REROLL":
            quirk2 = random.choice(QuirkList)
        
        return quirk1 + " and " + quirk2
    return quirk


### Element

def rollElement() -> str:
    roll = rollDice.d20()
    if roll < 3:
        return "Acid"
    if roll < 5:
        return "Lightning"
    if roll < 7:
        return "Cold"
    if roll < 9:
        return "Fire"
    if roll == 9:
        return "Physical"
    if roll < 12:
        return "Force"
    if roll == 12:
        return "Psychic"
    if roll < 15:
        return "Poison"
    if roll < 17:
        return "Necrotic"
    if roll < 19:
        return "Radiant"
    if roll == 19:
        return "Thunder"
    # this is the fun part. Potentially infinite recursion
    return rollElement() + " and " + rollElement()


propertyFromElement = (
    "Protection", "Damage", "Utility", "Casting"
)

def propertiesFromElement() -> list:
    properties = []
    propertyCount = 0
    roll = rollDice.d20()
    if roll < 4:
        propertyCount = 1
    elif roll < 10:
        propertyCount = 2
    elif roll < 16:
        propertyCount = 3
    elif roll < 20:
        propertyCount = 4
    else:
        propertyCount = 5
    for i in range(propertyCount):
        properties.append(random.choice(propertyFromElement))
    return properties