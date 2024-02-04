from tkinter import Tk, Canvas, Frame, Label, Entry, Button, PhotoImage

from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/danielaiello/Desktop/Qhacks2024/assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def create_gradient(canvas, start_color, end_color, width, height):
    for i in range(height):
        # Interpolate between start and end colors
        r = int((start_color[0] * (height - i) + end_color[0] * i) / height)
        g = int((start_color[1] * (height - i) + end_color[1] * i) / height)
        b = int((start_color[2] * (height - i) + end_color[2] * i) / height)

        # Convert RGB to hexadecimal color code
        color = f'#{r:02x}{g:02x}{b:02x}'

        # Draw a line with the interpolated color
        canvas.create_line(0, i, width, i, fill=color, width=1)


window = Tk()
window.geometry("400x500")
window.title("Nice Tkinter Frontend")

# Create a gradient canvas
gradient_canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=500,
    width=400,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
gradient_canvas.place(x=0, y=0)

# Draw a pink to blue gradient on the canvas
create_gradient(gradient_canvas, (255, 192, 203), (173, 216, 230), 400, 500)

# Create a frame for organization
frame = Frame(
    window,
    bg="#FFFFFF",
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=150)

# Add a label for the prompt
prompt_label = Label(
    frame,
    text="Prompt:",
    bg="#FFFFFF",
    font=("SecularOne Regular", 12),
    justify="left"
)
prompt_label.place(x=10, y=10)

# Add an entry widget for input
prompt_entry = Entry(
    frame,
    font=("SecularOne Regular", 12),
    bd=2,
    relief="flat"
)
prompt_entry.place(x=10, y=40, width=280)

# Load the original image
original_image = PhotoImage(file=str(relative_to_assets("button_1.png")))

# Calculate the new width and height for resizing
new_width, new_height = 100, 100

# Resize the image using subsample
resized_image = original_image.subsample(int(original_image.width() / new_width), int(original_image.height() / new_height))

# Add a button with the resized image and no border
button_1 = Button(
    window,
    image=resized_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print(f"Prompt entered: {prompt_entry.get()}"),
    relief="flat"
)
button_1.place(relx=0.5, rely=0.8, anchor="center", width=100, height=100)

# Add the text elements
gradient_canvas.create_text(
    200,
    50,
    anchor="center",
    text="sneaQy",
    fill="#000000",
    font=("SecularOne Regular", 20)
)

gradient_canvas.create_text(
    200,
    150,
    anchor="center",
    text="Created by Daniel Aiello and Ryan Scomazzon",
    fill="#000000",
    font=("SecularOne Regular", 10)
)

window.mainloop()
