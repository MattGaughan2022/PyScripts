import pickle
main_loops = 0
recipes_list = []
ingredients_list = []

inputFile = str

def take_recipe(iteration):
    print(f"=====[ iteration #{iteration}]=====")
    name = str(input("Name of recipe: "))
    cooking_time = int(input("Cooking time for the recipe: "))
    addIngredients =  []
    difficulty = str
    m = int(input("How many ingredients are in " + name + "? "))
    for m in range (0, m):
        p = str(input(f"Ingredient #{m + 1}:"))
        addIngredients.append(p)
    print(addIngredients)
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': addIngredients, 'difficulty': difficulty}
    return recipe


def hardcode_testing():
    n = int(input("How many recipes would you like to enter? " ))
    global recipes_list, ingredients_list

    for i in range(0, n):
        recipe = take_recipe((i+1)) ##counter for total loops to user
        for ingredient in recipe['ingredients']:
            if ingredient not in ingredients_list:
                ingredients_list.append(ingredient)
            else:
                continue
        recipes_list.append(recipe)
    print("==============================")
    calc_difficulty(recipes_list)
    print("==============================")
    ingredients_list.sort()
    print("ingredients available across all recipes: ", ingredients_list)
    return True

def calc_difficulty(list):
    global recipes_list
    for i in list:
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
        i['difficulty'] = difficulty
        recipes_list = list
        for m in i['ingredients']:
            print(m)
        print("Difficulty level: ", i['difficulty'])

def display_recipe(data):
    for i in data['recipes_list']:
        print(">>>", i['name'])
    hey = 0
    search_recipe = input("Which recipe would you like to display? (name) ")
    for i in data['recipes_list']:
        if i['name'] == search_recipe:
            print(" ",'>>> name:', i['name'])
            print(" ",'>>> cooking time:', i['cooking_time'])
            print(" ",'>>> ingredients:', i['ingredients'])
            print(" ",'>>> difficulty:', i['difficulty'])
            hey = 1
            return hey
        else:
            continue
    if(hey == 0):
        print("No matches. Returning to main loop...")

def search_ingredient(data):
    for count, i in enumerate(data['all_ingredients']):
        print(">>> #%s" % (count), i)
    hey = 0
    try:
        search_ingredient = int(input("Which ingredient would you like to display? (number) "))
        search_ingredient = data['all_ingredients'][search_ingredient]
    except:
        print(search_ingredient)
        print("Input is incorrect. Returning to main loop...")
    else:
        for i in data['recipes_list']:
            if (search_ingredient in i['ingredients']):
                print(search_ingredient, "is in" , i['name'])
                print(" ",'>>> name:', i['name'])
                print(" ",'>>> cooking time:', i['cooking_time'])
                print(" ",'>>> ingredients:', i['ingredients'])
                print(" ",'>>> difficulty:', i['difficulty'])
                hey = 1
                continue
            else:
                continue
        if(hey == 0):
            print("No matches. Returning to main loop...")

def open_file():
    global recipes_list, ingredients_list, inputFile
    try:
        inputFile = input("Enter a filename (current demo file is 'cooking')... ")
        file = open("%s.bin" % (inputFile), 'rb')
        data = pickle.load(file)
    except FileNotFoundError:
        print("File not found.")
        file = open("%s.bin" % (inputFile), 'wb')
        data = {
            'recipes_list': recipes_list,
            'all_ingredients': ingredients_list
            }
        pickle.dump(data, file)
        file.close()
    except:
        data = {
            'recipes_list': recipes_list,
            'all_ingredients': ingredients_list
            }
    else:
        file.close()
    finally:
        recipes_list= data['recipes_list']
        ingredients_list=data['all_ingredients']
        main_loop(data)
        data['recipes_list'] = recipes_list
        data['all_ingredients'] = ingredients_list
        file = open("%s.bin" % (inputFile), 'wb')
        pickle.dump(data, file)
        file.close()
        print("============FIN============")

def check_recipes():
    with open("%s.bin" % (inputFile), 'rb') as file:
            data = pickle.load(file)
            x=1
            for i in data['recipes_list']:
                print("Recipe #%s" % (x))
                print(" ",'>>> name:', i['name'])
                print(" ",'>>> cooking time:', i['cooking_time'])
                print(" ",'>>> ingredients:', i['ingredients'])
                print(" ",'>>> difficulty:', i['difficulty'])
                x+=1
    file.close()
    return True

def check_choice(user_choice):
    return (0 < user_choice < 7) 

def main_loop(data):
    while True:
        global main_loops 
        print("============MAIN LOOP #%s============" % (main_loops))
        main_loops +=1
        print("1. Add recipes ")
        print("2. Check current recipes (testing demo is cooking.bin) ")
        print("3. NYE")
        print("4. Display recipe")
        print("5. Search ingredient")
        print("6. Exit")
        choice = int(input("What would you like to do? (1-6)  "))
        if(check_choice(choice)):
            match choice:
                case 1:
                    hardcode_testing()
                case 2:
                    check_recipes()
                case 3:
                    print("this option is extra! looping...")
                case 4:
                    display_recipe(data)
                case 5:
                    search_ingredient(data)
                case 6:
                    print("Exiting...")
                    return False
        else:
            print("Not working")




open_file() # init start
