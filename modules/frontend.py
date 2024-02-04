from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class TooltipPopup(Popup):
    def __init__(self, **kwargs):
        super(TooltipPopup, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (200, 100)

class MyFloatLayoutApp(App):
    def build(self):
        # Create a FloatLayout
        layout = FloatLayout()

        # Set the background image
        bg_image = Image(source='bg.jpeg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(bg_image)

        # Create a small text input
        text_input = TextInput(text='Enter text here', size_hint=(None, None), height=30, pos_hint={'center_x': 0.5, 'center_y': 0.8})
        layout.add_widget(text_input)

        # Create a small button
        button1 = Button(text="Push Me!",
                         color=(1, 0, .65, 1),
                         background_normal='button-unpressed.png',
                         background_down='down.png',
                         size_hint=(.3, .3),
                         pos_hint={"x": 0.1, "y": 0.3})
        button1.bind(on_enter=self.show_tooltip)
        layout.add_widget(button1)
    
        return layout

    def show_tooltip():
        process = Popen(['python3', 'settings.py'], stdout=PIPE, stderr=PIPE)


if __name__ == '__main__':
    MyFloatLayoutApp().run()
