from kivy.app import App
from kivy.lang import Builder


class Products(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total_price = 0
        self.products = [Product("Test", 1)]
        # load products here

    def build(self):
        self.title = "Hello world!"
        self.root = Builder.load_file('products.kv')
        return self.root

    def handle_reset(self, button):
        self.total_price = 0

    def handle_button(self, button):
        pass


# create and start the App running
Products().run()
