from guizero import App,Text,PushButton,Picture
import os

app = App(title='drinker')

welcome = Text(app,text="Drinkser",size = 40, font="Arial",color="blue")


def drinkOne():
    os.system("python3 drink1.py")


app = App(title="drinkser")

logo = Picture(app, image="drinkser.png")

welcome_message = Text(app, text="Select a drink to dispense!", size=16, font="Arial", color="#511314")

drinkOneImage = Picture(app, image="coke.jpg", width=60, height=85)

drinkOneButton = PushButton(app, command=drinkOne, text="Drink 1")


app.display()
