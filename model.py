import item_generation.item as Item


if __name__ == "__main__":
    print("This is a module file for the main program. Open main.py instead.")


class Model:
    

    def roll_item(self) -> Item:
        self.item = Item.rollItem()
        return self.item


    def get_item(self) -> Item:
        return self.item


    def change_item_property(self, button):
        match button:
            case "Item Type":
                self.item.change_class()
            case "Item Subtype":
                self.item.set_itemSubtype()
            case "Item Material":
                self.item.set_itemMaterial()
            case "Rarity":
                self.item.set_rarity()
            case "Creator":
                self.item.set_creator()
            case "Source":
                self.item.set_source()
            case "Age":
                self.item.set_age()
            case "History":
                self.item.set_detail()
            case "Property":
                self.item.set_property()
            case "Quirk":
                self.item.set_quirk()
            case "Element":
                self.item.set_element()
            case "El. Properties":
                self.item.set_propertiesFromElements()


            case _:
                pass
