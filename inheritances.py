class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal): # if nothing to pass/give after the method.simply give pass
    pass

dog1 = Dog()
dog1.bark()
cat1 = Cat()
cat1.walk()