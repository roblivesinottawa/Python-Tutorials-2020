# def yell(word):
#     return word.upper() + "!"


# result = yell("leave me alone")
# print(result)


# def marvel(name="Steve Rogers", is_hero=True):
#     if name == "Steve Rogers" and is_hero:
#         return "Welcome back Cap!"
#     elif name == "Steve Rogers":
#         return "We thought you were a hero"
#     return f"Hello {name}"


# print(marvel())


def speak(animal="dog"):
    noises = {"pig": "oink", "dog": "woof", "cat": "meow", "duck": "quack"}
    return noises.get(animal, '?')


print(speak("pig"))
