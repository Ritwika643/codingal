class Animals:
    def __init__(self, color, size):
        self.color = color
        self.size = size

dog_obj = Animals("brown", "medium")
cat_obj = Animals("black", "small")
donkey_obj = Animals("grey", "large")

print(f'Dog - Color: {dog_obj.color}, Size: {dog_obj.size}')
print(f'Cat - Color: {cat_obj.color}, Size: {cat_obj.size}')
print(f'Donkey - Color: {donkey_obj.color}, Size: {donkey_obj.size}')