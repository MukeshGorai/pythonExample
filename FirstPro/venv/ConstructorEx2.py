class Person:
    def __init__(self, name):
        self.name=name

    def talk(self):
        print(f"Hi, I am {self.name}")


mukesh=Person("Mukesh Gorai")
mukesh.talk()

gorai=Person("Gorai Muku")
gorai.talk()