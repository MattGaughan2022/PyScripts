recipes_list = []

ingredients_list = []

def take_recipe(iteration):
    print(f"=====[ iteration #{iteration}]=====")
    name = str(input("Name of recipe: "))
    cooking_time = int(input("Cooking time for the recipe: "))
    addIngredients =  []
    m = int(input("How many ingredients are in " + name + "? "))
    for m in range (0, m):
        p = str(input(f"Ingredient #{m + 1}:"))
        addIngredients.append(p)
    print(addIngredients)
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': addIngredients}
    return recipe


n = int(input("How many recipes would you like to enter? " ))

for i in range(0, n):
    recipe = take_recipe((i+1))
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
        else:
            continue
    recipes_list.append(recipe)
print("==============================")
for i in recipes_list:
    if (i['cooking_time'] < 10 and len(i['ingredients']) < 4):
        difficulty = 'easy'
    elif (i['cooking_time'] < 10 and len(i['ingredients']) >= 4):
        difficulty = 'medium'
    elif (i['cooking_time'] >= 10 and len(i['ingredients']) < 4):
        difficulty = 'intermediate'
    elif (i['cooking_time'] >= 10 and len(i['ingredients']) >= 4):
        difficulty = 'hard'
    print("Recipe: ", i['name'])
    print("Cooking Time (min): ", i['cooking_time'])
    print("Ingredients:")
    for m in i['ingredients']:
        print(m)
    print("Difficulty level: ", difficulty)
    print("==============================")
ingredients_list.sort()
print("ingredients available across all recipes: ", ingredients_list)