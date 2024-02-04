from pathlib import Path
from tkinter import Tk, Canvas, Frame, Label, Entry, Button, PhotoImage
import localvars

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = localvars.ASSETS_PATH


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class GUI:
    def __init__(self):
        window = Tk()
        window.geometry("400x500")
        window.title("Nice Tkinter Frontend")

        # Create a gradient canvas with a darker pink color
        gradient_canvas = Canvas(
            window,
            bg="#D2691E",  # Darker pink color
            height=500,
            width=400,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        gradient_canvas.place(x=0, y=0)

        # Draw a pink to blue gradient on the canvas
        for i in range(500):
            r = int((255 * (500 - i) + 173 * i) / 500)
            g = int((182 * (500 - i) + 216 * i) / 500)
            b = int((193 * (500 - i) + 230 * i) / 500)
            color = f'#{r:02x}{g:02x}{b:02x}'
            gradient_canvas.create_line(0, i, 400, i, fill=color, width=1)

        # Create a transparent frame for organization
        frame = Frame(
            window,
            bg="#FFA500",  # Orange color
            bd=2,  # Borderwidth
            relief="ridge"  # Relief type for the border
        )
        frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=150)

        # Add a label for the prompt with transparency
        prompt_label = Label(
            frame,
            text="Prompt:",
            bg="#FFA500",  # Orange color
            font=("Segoe UI", 12),  # Fluent design-inspired font
            justify="left",
            fg="white",  # White text
            bd=0,  # No border
        )
        prompt_label.place(x=10, y=10)

        # Add a transparent entry widget for input
        prompt_entry = Entry(
            frame,
            font=("Segoe UI", 12),  # Fluent design-inspired font
            bd=2,
            relief="flat"
        )
        prompt_entry.place(x=10, y=40, width=280)

        original_image = PhotoImage(file=str(relative_to_assets("button_1.png")))

        new_width, new_height = 100, 100
        resized_image = original_image.subsample(int(original_image.width() / new_width), int(original_image.height() / new_height))

        # Increase the font size and add a glowing effect to "sneaQy"
        sneaQy_text = gradient_canvas.create_text(
            200,
            50,
            anchor="center",
            text="sneaQy",
            fill="#FFFFFF",  # White text
            font=("Segoe UI", 30, "bold"),  # Larger and bold
            justify="center"
        )

        # Add a glowing effect to "sneaQy"
        gradient_canvas.itemconfig(sneaQy_text, font=("Segoe UI", 30, "bold"), fill="#FFFFFF")  # Gold color for glow
        gradient_canvas.itemconfig(sneaQy_text, tag="glow")

        button_1 = Button(
            window,
            image=resized_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print(f"Prompt entered: {prompt_entry.get()}"),
            relief="ridge"
        )
        button_1.place(relx=0.5, rely=0.8, anchor="center", width=100, height=100)

        gradient_canvas.create_text(
            200,
            150,
            anchor="center",
            text="Created by Daniel Aiello and Ryan Scomazzon",
            fill="white",  # White text
            font=("Segoe UI", 10)  # Fluent design-inspired font
        )

        self.window = window

    
        

if __name__ == "__main__":
    ui = GUI()
    ui.window.mainloop()