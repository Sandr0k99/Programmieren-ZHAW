class Person:
    """
       A class to represent a Person.

       ...

       Attributes
       ----------
       name : str
           name of person
       age: int
           age of person
       hair_color : str
           hair color of person

       Methods
       -------
       speak(text):
            person speaking text
       birthday():
            adds 1 to the age of the person
    """
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