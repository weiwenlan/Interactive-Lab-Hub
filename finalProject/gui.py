from guizero import App, Text, PushButton, Picture, Box
import os


def drink1():
        os.system('python3 drink.py 1 4')
        print("test 1")

def drink2():
        os.system('python3 drink.py 2 4')
        print("test 2")

def drink3():
        os.system('python3 drink.py 3 4')
        print("test 3")

def drink12():
        os.system('python3 drink.py 1 4')
        os.system('python3 drink.py 2 4')
        print("test 12")

def drink13():
        os.system('python3 drink.py 1 4')
        os.system('python3 drink.py 3 4')
        print("test 13")

def drink23():
        os.system('python3 drink.py 2 4')
        os.system('python3 drink.py 3 4')
        print("test 23")

def drink123():
        os.system('python3 drink.py 1 4')
        os.system('python3 drink.py 2 4')
        os.system('python3 drink.py 3 4')
        print("test 123")


app = App(title="drinkser", layout="grid")

logo = Picture(app, image="drinkser.png",width=160, height=80, grid=[1, 0])
welcome_message = Text(app, text="Select a drink to dispense", size=12, font="Arial", color="#511314", grid=[1, 1])

one_drink = Text(app, text="Choose 1 drink!", size=12, font="Arial", color="#511314", grid=[1, 2])

# drink1Image = Picture(app, image="coke3.jpg", width=60, height=85, grid=[0, 3])
drink1Button = PushButton(app, image="coke3.jpg", width=40, height=60, command=drink1, text="Coke", grid=[0, 3])

# drink2Image = Picture(app, image="sprite.jpg", width=60, height=85, grid=[1, 3])
drink2Button = PushButton(app, image="sprite.jpg", width=40, height=60, command=drink2, text="Sprite", grid=[1, 3])

# drink3Image = Picture(app, image="fanta.png", width=60, height=85, grid=[2, 3])
drink3Button = PushButton(app, image="fanta.png", width=40, height=60, command=drink3, text="Fanta", grid=[2, 3])

two_drinks = Text(app, text="Mix 2 drinks!", size=12, font="Arial", color="#511314", grid=[1, 4])

drink13Button = PushButton(app, image="coke_and_fanta.png", width=80, height=60, command=drink13, text="Coke + Fanta", grid=[0, 5])
drink12Button = PushButton(app, image="coke_and_sprite.png", width=80, height=60, command=drink12, text="Coke + Sprite", grid=[1, 5])
drink23Button = PushButton(app, image="sprite_and_fanta.png", width=80, height=60, command=drink23, text="Sprite + Fanta", grid=[2, 5])

three_drinks = Text(app, text="Put all 3 together!", size=12, font="Arial", color="#511314", grid=[1, 6])


drink123Button = PushButton(app, image="all_three.png", width=120, height=60, command=drink123, text="All Together!", grid=[1, 7])

#box = Box(app, grid=[2,3],  align="top", width=300, height=400)
#box2 = Box(app, grid=[1,3], align="top", width=300, height=400)



app.display()
