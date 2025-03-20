class Animal:
    def __init__(self, name, group, number_of_legs, skills):
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills

    def __repr__(self):
        return f"Animal(name='{self.name}', group='{self.group}', number_of_legs={self.number_of_legs}, skills={self.skills})"
 
lion = Animal('Lion', 'Mammals', 4, ['Roaring', 'Hunting'])
dolphin = Animal('Dolphin', 'Mammals', 0, ['Swimming', 'Jumping'])
parrot = Animal('Parrot', 'Birds', 2, ['Flying', 'Mimicking'])
crocodile = Animal('Crocodile', 'Reptiles', 4, ['Swimming', 'Hunting'])
elephant = Animal('Elephant', 'Mammals', 4, ['Trunk Usage', 'Swimming'])

animals = [lion, dolphin, parrot, crocodile, elephant]

for animal in animals:
    print(animal)
