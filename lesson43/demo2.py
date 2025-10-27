class fruits:
    def __init__(self, name, color):
        self.name = name
        self.color = color

apple_obj = fruits("Apple", "Red")
banana_obj = fruits("Banana", "Yellow")
grape_obj = fruits("Grape", "Purple")
guvava_obj = fruits("Guava", "Green")

print(f'Fruit: {apple_obj.name}, Color: {apple_obj.color}')
print(f'Fruit: {banana_obj.name}, Color: {banana_obj.color}')
print(f'Fruit: {grape_obj.name}, Color: {grape_obj.color}')
print(f'Fruit: {guvava_obj.name}, Color: {guvava_obj.color}')