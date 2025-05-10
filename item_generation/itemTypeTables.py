import random
import item_generation.rollDice as rollDice


if __name__ == "__main__":
    print("This is a module file for the main program. Open main.py instead.")


### Weapons

SimpleSlashing = (
    "Handaxe", "Sickle"
)
MartialSlashing = (
    "Battleaxe", "Greataxe",
    "Greatsword", "Longsword",
    "Glaive", "Halberd",
    "Scimitar", "Whip"
)

SimpleBludgeoning = (
    "Club", "Greatclub",
    "Light Hammer", "Mace",
    "Quarterstaff"
)
MartialBludgeoning = (
    "Maul", "Warhammer",
    "Flail"
)

SimplePiercing = (
    "Javelin", "Spear",
    "Dagger"
)
MartialPiercing = (
    "Rapier", "Shortsword",
    "Morningstar", "War pick",
    "Lance", "Pike", 
    "Trident"
)

SimpleRanged = (
    "Sling", "Shortbow", "Light Crossbow"
)
MartialRanged = (
    "Blowgun", "Longbow", "Hand Crossbow", "Heavy Crossbow"
)

def rollWeaponType() -> str:
    isMartial = bool(random.getrandbits(1))
    damageTypeRoll = rollDice.d20()
    if damageTypeRoll < 7:
        if isMartial:
            return random.choice(MartialSlashing)
        else:
            return random.choice(SimpleSlashing)
    if damageTypeRoll < 13:
        if isMartial:
            return random.choice(MartialBludgeoning)
        else:
            return random.choice(SimpleBludgeoning)
    if damageTypeRoll < 17:
        if isMartial:
            return random.choice(MartialPiercing)
        else:
            return random.choice(SimplePiercing)
    if damageTypeRoll < 20:
        if isMartial:
            return random.choice(MartialRanged)
        else:
            return random.choice(SimpleRanged)
    return "Shield"


### Tools

ArtisanTools = (
    "Alchemist's supplies", "Brewer's supplies", "Calligrapher's supplies",
    "Carpenter's tools", "Cartographer's tools", "Cobbler's tools",
    "Cook's utensils", "Glassblower's tools", "Jeweler's tools",
    "Leatherworker's tools", "Mason's tools", "Painter's supplies",
    "Potter's tools", "Smith's tools", "Tinker's tools",
    "Weaver's tools", "Woodcarver's tools"
)
MusicalInstrument = (
    "Bagpipes", "Drum", "Dulcimer", "Flute"
    "Lute", "Lyre", "Horn", "Pan flute",
    "Shawm", "Viol"
)
MiscTools = (
    "Disguise kit", "Forgery kit", "Herbalism kit",
    "Navigator's tools", "Poisoner's kit", "Thieves' tools",
    "Dice set", "Dragonchess set",
    "Playing card set", "Three-Dragon Ante set"
)

def rollToolType() -> str:
    roll = rollDice.d20()
    if roll < 9:
        return "Lamp"
    if roll == 9:
        return "Quiver"
    if roll < 12:
        return "Wand"
    if roll < 16:
        return random.choice(ArtisanTools)
    if roll < 18:
        return random.choice(MusicalInstrument)
    if roll < 20:
        return random.choice(MiscTools)
    return "Common tool"


### Jewellery

def rollJewelleryType() -> str:
    roll = rollDice.d20()
    if roll < 8:
        return "Ring"
    if roll < 14:
        return "Necklace"
    if roll < 17:
        return "Bracelet"
    if roll < 19:
        return "Crown"
    if roll == 19:
        return "Piercing"
    return "Earring"

def rollJewelleryMaterial() -> str:
    roll = rollDice.d20()
    if roll < 6:
        return "Copper"
    if roll < 9:
        return "Iron"
    if roll < 14:
        return "Silver"
    if roll < 18:
        return "Gold"
    if roll == 18:
        return "Ivory"
    return "Other"


### Armor/Clothes

def rollBodypart() -> str:
    roll = rollDice.d20()
    if roll < 3:
        return "Helmet"
    if roll < 10:
        return "Armor/Shirt"
    if roll < 13:
        return "Cloak"
    if roll < 15:
        return "Gloves"
    if roll < 17:
        return "Belt"
    if roll < 20:
        return "Boots"
    if roll == 20:
        return "Pants/Skirt"


def rollMaterial() -> str:
    roll = rollDice.d20()
    if roll < 6:
        return "Cloth"
    if roll < 11:
        return "Light Armor"
    if roll < 15:
        return "Medium Armor"
    if roll < 18:
        return "Heavy Armor"
    if roll == 18:
        return "Wood/Bone"
    if roll == 19:
        return "Stone/Gemstone"
    if roll == 20:
        return "Wild Card"


### Misc

def rollMiscItem() -> str:
    roll = rollDice.d20()
    if roll < 7:
        return "Gem"
    if roll < 10:
        return "Potion"
    if roll < 12:
        return "Book/Scroll"
    if roll == 12:
        return "Inscription/Rune"
    if roll == 13:
        return "Contraption"
    if roll == 14:
        return "Bone/Skull"
    if roll == 15:
        return "Orb"
    if roll == 16:
        return "Hand/Finger"
    if roll == 17:
        return "Heart"
    if roll == 18:
        return "Rock"
    if roll == 19:
        return "Stick"
    if roll == 20:
        return "Other common object"

