import tkinter as tk
from tkinter import ttk


if __name__ == "__main__":
    print("This is a module file for the main program. Open main.py instead.")


class View(tk.Tk):
    
    padding = 10

    button_captions = [
        "Item Type", "Item Subtype", "Item Material",
        "Rarity", "Creator", "Source", 
        "Age", "History", "Property", 
        "Quirk", "Element", "El. Properties"
    ]


    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        # self.textbox_var = tk.StringVar()

        self.title("Eri's Virtual Mindforge™ :3")
        # self.resizable(1, 0)

        self._make_main_frame()
        self._make_side_frame()
        self._make_main_textbox()
        self._make_buttons()

      
    def main(self):
        self.mainloop()
    

    def _make_main_frame(self):
        self.main_frame = ttk.Frame(self, width=800).pack(pady=5)
    
        side_label = ttk.Label(self, text="Reroll:")
        side_label.pack(fill='x', padx=self.padding)


    def _make_side_frame(self):
        self.side_frame = ttk.Frame(self.main_frame, width=50)
        self.side_frame.pack(padx=self.padding, side='left', anchor='nw')


    def _make_main_textbox(self):
        self.textbox = tk.Text(self.main_frame, height=21, width=10)
        self.textbox.pack(fill='x', padx=self.padding)
    

    # This just works O.o
    def _update_main_textbox(self, text):
        self.textbox.delete("1.0", "end-1c")
        self.textbox.insert("end-1c", text)


    def _make_buttons(self):

        for caption in self.button_captions:
            button = ttk.Button(
                self.side_frame, text=caption, width=15,
                command=(lambda button=caption: self.controller.on_button_click(button))
            )
            button.pack()
        
        reroll_button = ttk.Button(
            self.side_frame, text="New Item", width=15,
            command=(lambda : self.controller.reroll_button_click())
        )
        reroll_button.pack(fill='x', pady=self.padding)
        


    



