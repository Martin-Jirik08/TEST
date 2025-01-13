### GUI imports
from guizero import *
from main_jirik import *


### GUI functions
def appear():
    pass
def my_first_gui_function():
    try:
        hmotnost = float(txtbox_weight.value)
        af = float(txtbox_af.value)
        cml = calculate_cml(hmotnost, af)
        text_cml.value = cml
    except ValueError:
        text_cml.value = "Zadaná hodnota musí být číslo"
def gui_choice():
    us_choice = choice.value
    #print(choice.value)
    user_text_choice.value = user_choice(us_choice)



    
### GUI App
app = App(title="My App",
          width=1075,
          height=1050,
          layout="auto"
          )

## Window 1
window1 = Box(app, visible=True)

# Welcome text
text_welcome = Text(window1, text=(f"Hi, user!"))

# Input activity factor
text_af = Text(
    window1,
    text=("Please enter your activity factor for today:")
)
txtbox_af = TextBox(window1)

# Input weight
text_weight = Text(
    window1,
    text=(f"Please enter your weight in kilograms (kg):")
)
txtbox_weight = TextBox(window1)

# Output calorie maintenance level
text_cml = Text(window1)

# Display an image
image_widget = Picture(
    window1,
    image="resources_jirik/images/calculating_cml.png",
    width=80,
    height=80,
    align="bottom"
)

button = PushButton(window1, text = "Odeslat", command=my_first_gui_function)

choice = ButtonGroup(app, options=["cheese", "ham", "jam"], selected="ham", command=appear)

user_button = PushButton(
    app,
    text="vybrat",
    command=gui_choice
)
user_text_choice = Text(app, text = "")
picture = Picture(app, image="resources_jirik/images/python_snake.png")

app.display()

