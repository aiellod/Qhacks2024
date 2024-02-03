from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class CustomNotification(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Create a label inside the layout
        label = Label(text="This is a custom notification.", font_size=18)
        layout.add_widget(label)

        # Bind the on_touch_down and on_touch_move events
        layout.bind(on_touch_down=self.on_touch_down)
        layout.bind(on_touch_move=self.on_touch_move)

        return layout

    def on_touch_down(self, instance, touch):
        # Check if the touch is inside the layout
        if instance.collide_point(*touch.pos):
            # Store the initial touch position for calculating movement
            touch.ud['start_pos'] = touch.pos
            return True

    def on_touch_move(self, instance, touch):
        # Check if the touch is inside the layout and has a starting position
        if instance.collide_point(*touch.pos) and 'start_pos' in touch.ud:
            # Calculate the movement offset
            dx = touch.pos[0] - touch.ud['start_pos'][0]
            dy = touch.pos[1] - touch.ud['start_pos'][1]

            # Update the window position based on the movement offset
            App.get_running_app().root_window.position = (App.get_running_app().root_window.x + dx,
                                                           App.get_running_app().root_window.y + dy)

            # Update the starting position for the next movement
            touch.ud['start_pos'] = touch.pos

if __name__ == "__main__":
    CustomNotification().run()
