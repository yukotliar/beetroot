# Doggy age
#
# Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.
class Dog:
    def __init__(self, name, breed, dog_age):
        self.name = name
        self.breed = breed
        self.age_factor = 7
        self.dog_age = dog_age

    def human_age(self, dog_age):
        return self.dog_age * self.age_factor


dog1 = Dog('Sidor', 'Scotish', 3)
human_eq = dog1.human_age(dog1.dog_age)
print(f'{dog1.name} of a {dog1.breed} breed, age {dog1.dog_age}, it\'s {human_eq} in human equivalent.')
