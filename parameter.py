def greet_user(name): #(parameters)
    print(f"hi {name}!")
    print("welcome broad")


def greet_user2(first_name,last_name):
    print(f"hi {first_name}, {last_name}")

print ("start")
greet_user("vivi") #(argument)
greet_user("Mohan")
greet_user("Adhish")
greet_user2("Adhish", "chandra") #position argument
greet_user2(last_name= "Rajasekaran", first_name="Vivekanandhi") # keyword argument mostly used in numerical arguments
greet_user2("mohan", last_name=" Chandrasekaran") # first position arg and then keyword arg.it will not work if it is vise vera
print("Finish")
