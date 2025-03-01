class Person:
    def __init__(self, name, age, hair_color):
        self.name = name
        self.age = age
        self.hair_color = hair_color

    def speak(self, text):
        print(f"{self.name} sagt: {text}")

    def birthday(self):
        self.age += 1
        print(f"{self.name} hat jetzt Geburtstag gefeiert und ist {self.age} Jahre alt.")

if __name__ == "__main__":
    person = Person("Anna", 25, "Blond")
    person.speak("Hallo, wie geht's?")
    person.birthday()