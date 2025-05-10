import item_generation.itemTypeTables as itemTypeTables
import item_generation.genericTables as genericTables
import item_generation.rollDice as rollDice


if __name__ == "__main__":
    print("This is a module file for the main program. Open main.py instead.")


def rollItem():
    roll = rollDice.d20()
    if roll < 9:
        return Weapon()
    if roll < 11:
        return Tool()
    if roll < 15:
        return Jewellery()
    if roll < 19:
        return Clothes()
    return Misc()


class Item:
    
    # I would probably be hanged for doing this
    # But it's for science
    def change_class(self):
        self.__class__ = type(rollItem())

        self.set_itemSubtype()
        self.set_itemMaterial()

        # print(vars(self))
        


    def __init__(self):
        self.set_rarity()
        self.set_creator()
        self.set_source()
        self.set_age()
        self.set_detail()
        self.set_property()
        self.set_quirk()
        self.set_element()
        self.set_propertiesFromElements()

        self.set_itemSubtype()
        self.set_itemMaterial()
        
    
    def set_rarity(self):
        self.rarity = genericTables.rollRarity()

    def set_creator(self):
        self.creator = genericTables.rollCreator()

    def set_source(self):
        self.source = genericTables.rollSource()

    def set_age(self):
        self.age = genericTables.rollAge()

    def set_detail(self):
        self.detail = genericTables.rollDetail()

    def set_property(self):
        self.property = genericTables.rollProperty()

    def set_quirk(self):
        self.quirk = genericTables.rollQuirk()

    def set_element(self):
        self.element = genericTables.rollElement()

    def set_propertiesFromElements(self):
        self.propertiesFromElements = genericTables.propertiesFromElement()
    

    def set_itemSubtype(self):
        self.itemType = None

    def set_itemMaterial(self):
        self.itemMaterial = None
    


    def __str__(self):
        return f"""Rarity: {self.rarity}
Creator: {self.creator}
Source of Power: {self.source}
Age: {self.age}
Detail from History: {self.detail}
Minor Property: {self.property}
Quirk: {self.quirk}
Element: {self.element}
Properties from elements: {self.propertiesFromElements}"""




class Weapon(Item):
    def __init__(self):
        Item.__init__(self)
    

    def set_itemSubtype(self):
        self.itemType = itemTypeTables.rollWeaponType()


    def __str__(self):
        return f"Weapon: {self.itemType}\n" + Item.__str__(self)



class Tool(Item):
    def __init__(self):
        Item.__init__(self)

 
    def set_itemSubtype(self):
        self.itemType = itemTypeTables.rollToolType()


    def __str__(self):
        return f"Tool: {self.itemType}\n" + Item.__str__(self)



class Jewellery(Item):
    def __init__(self):
        Item.__init__(self)
    

    def set_itemSubtype(self):
        self.itemType = itemTypeTables.rollJewelleryType()

    def set_itemMaterial(self):
        self.itemMaterial = itemTypeTables.rollJewelleryMaterial()
  

    def __str__(self):
        return f"""Jewellery: {self.itemType}
Material: {self.itemMaterial}
""" + Item.__str__(self)



class Clothes(Item):
    def __init__(self):
        Item.__init__(self)
    

    def set_itemSubtype(self):
        self.itemType = itemTypeTables.rollBodypart()

    def set_itemMaterial(self):
        self.itemMaterial = itemTypeTables.rollMaterial()
    
    
    def __str__(self):
        return f"""Clothes: {self.itemType}
Material: {self.itemMaterial}
""" + Item.__str__(self)



class Misc(Item):
    def __init__(self):
        Item.__init__(self)
    

    def set_itemSubtype(self):
        self.itemType = itemTypeTables.rollMiscItem()
      

    def __str__(self):
        return f"Misc: {self.itemType}\n" + Item.__str__(self)