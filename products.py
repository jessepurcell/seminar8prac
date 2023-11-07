from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button

from product import Product


class Products(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total_price = 0
        self.products = [Product("Apple", 1.0), Product("Pear", 2.0), Product("Orange", 2.25)]

    def build(self):
        self.title = "Products"
        self.root = Builder.load_file('products.kv')
        self.create_widgets()
        self.root.ids.total_price.text = f"Total Price: ${self.total_price}"
        return self.root

    def create_widgets(self):
        """Create buttons from data and add them to the GUI."""
        for product in self.products:
            # create a button for each data entry, specifying the text
            temp_button = Button(text=product.__str__())
            temp_button.product = product
            temp_button.bind(on_press=self.handle_button)
            # add the button to the "entries_box" layout widget
            self.root.ids.products.add_widget(temp_button)

    def handle_reset(self):
        self.total_price = 0
        self.update_total_price()

    def handle_button(self, button):
        self.total_price += button.product.price
        self.update_total_price()

    def update_total_price(self):
        self.root.ids.total_price.text = f"Total Price: ${self.total_price}"


# create and start the App running
Products().run()
