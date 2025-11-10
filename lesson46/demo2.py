class Bird:
    def speak(self):
        print("Chirp Chirp")

class Parrot(Bird):
    def speak(self):
        print("Squawk Squawk")

class Crow(Bird):
    def speak(self):
        print("Caw Caw")

for bird in (Parrot(), Crow()), Bird():
    bird.speak()