from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):
    """Dynamic kivy app for building making labels"""
    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)
        self.names = ["Bob", "Mary", "Suzy"]

    def build(self):
        """Build dynamic labels app from file"""
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    #
    def create_widgets(self):
        """Create label widgets from list of names"""
        # print('Creating widgets')
        for name in self.names:
            temp_label = Label(text=name, font_size=30, color=(0, 0, 1, 1))
            self.root.ids.main.add_widget(temp_label)


DynamicLabels().run()
