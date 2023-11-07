from kivy.app import App
from kivy.lang import Builder


class Products(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total_price = 0
        self.product_to_price = {"test": 10, "test2": 15}
        # load products here

    def build(self):
        self.title = "Hello world!"
        self.root = Builder.load_file('products.kv')
        return self.root

    def handle_button_press(self, button):
        if button.text == "Reset":
            self.total_price = 0
        else:
            self.total_price += self.product_to_price[button.text]


# create and start the App running
Products().run()
