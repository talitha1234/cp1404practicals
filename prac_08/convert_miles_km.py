from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_RATIO = 1.60934


class ConvertMilesKm(App):
    message = StringProperty()

    def build(self):
        """Build kivy app from kv file"""
        self.title = "Convert Miles to KM"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = ''
        return self.root

    def calculate_conversion(self):
        """Calculate miles to km and update output"""
        try:
            km = float(self.root.ids.user_input.text) * CONVERSION_RATIO
            self.message = str(km)
        except ValueError:
            self.message = str(0.0)

    def handle_increment(self, increment):
        """Increment miles by increment amount"""
        if self.root.ids.user_input.text == '':
            miles = increment
        else:
            miles = float(self.root.ids.user_input.text) + increment

        self.root.ids.user_input.text = str(miles)
        self.calculate_conversion()


ConvertMilesKm().run()
