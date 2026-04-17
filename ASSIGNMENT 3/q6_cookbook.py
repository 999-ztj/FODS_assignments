"""
This program creates a Dish class with attributes: dish_id, dish_name,
ingredients, and instructions. A Cookbook class manages a collection
of Dish objects with options to add and display dishes.
"""

class Dish:
    def __init__(self, dish_id, dish_name, ingredients, instructions):
        self.dish_id = dish_id
        self.dish_name = dish_name
        self.ingredients = ingredients
        self.instructions = instructions

    def display(self):
        print(f"  Dish ID      : {self.dish_id}")
        print(f"  Dish Name    : {self.dish_name}")
        print(f"  Ingredients  : {self.ingredients}")
        print(f"  Instructions : {self.instructions}")


class Cookbook:
    def __init__(self):
        # List to store all dishes
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)
        print(f"Dish '{dish.dish_name}' added to cookbook.")

    def display_all(self):
        if len(self.dishes) == 0:
            print("No dishes in the cookbook yet.")
        else:
            print("=== All Dishes in Cookbook ===")
            for dish in self.dishes:
                dish.display()
                print()


# Create a cookbook
my_cookbook = Cookbook()

# Add some dishes
print("=== Add Dishes to Cookbook ===")
print()

# Keep adding dishes until user is done
while True:
    choice = input("Do you want to add a dish? (yes/no): ")
    if choice.lower() != "yes":
        break

    dish_id = input("  Dish ID      : ")
    dish_name = input("  Dish Name    : ")
    ingredients = input("  Ingredients  : ")
    instructions = input("  Instructions : ")

    new_dish = Dish(dish_id, dish_name, ingredients, instructions)
    my_cookbook.add_dish(new_dish)
    print()

print()

# Display all dishes in the cookbook
my_cookbook.display_all()
