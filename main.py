from view import View
from model import Model


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)
        self.reroll_button_click()


    def main(self):
        self.view.main()
    

    def reroll_button_click(self):
        result = self.model.roll_item()
        self.view._update_main_textbox(result)
    

    def on_button_click(self, button):
        self.model.change_item_property(button)
        result = self.model.get_item()
        self.view._update_main_textbox(result)



if __name__ == "__main__":
    controller = Controller()
    controller.main()
