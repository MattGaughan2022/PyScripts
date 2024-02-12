from sqlalchemy import create_engine

engine = create_engine("mysql://cf-python:password@localhost/task_database1")


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
Session = sessionmaker(bind=engine)
session=Session()

from sqlalchemy import Column
from sqlalchemy.types import Integer, String

class Recipe(Base):
    __tablename__ = "task_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(50))

    def __repr__(self):
        return "<" + str(self.id) + ", " + self.name + ", " + self.difficulty + ">"
    def __str__(self):
        return "ID: " + str(self.id) + " | Name: " + self.name + " | Ingredients: " + self.ingredients + " | cooking_time: " + str(self.cooking_time) + " | Difficulty: " + self.difficulty
    

Base.metadata.create_all(engine)

def calculate_difficulty(time, ingredients):
    if (time < 10 and len(ingredients) < 4):
            difficulty = 'easy'
    elif (time < 10 and len(ingredients) >= 4):
        difficulty = 'medium'
    elif (time >= 10 and len(ingredients) < 4):
        difficulty = 'intermediate'
    elif (time >= 10 and len(ingredients) >= 4):
        difficulty = 'hard'
    return difficulty


def create_recipe():
    print("===== CREATE RECIPE =====")
    r_name = input("Name of recipe: ")
    r_cooking_time = input("Cooking time for recipe: ")
    try:
        r_cooking_time = int(r_cooking_time)
    except:
        input("cooking time that is entered is not an integer value. Returning...")
        return None
    r_ingredients = []
    sql_ingredients = ""
    m = int(input("How many ingredients are in " + r_name + "? "))
    for x in range (0, m):
        p = str(input(f"Ingredient #{x + 1}: "))
        r_ingredients.append(p)
        if(x+1 == m):
            sql_ingredients += (p)
        else:
            sql_ingredients += (p + ",")
    r_diff = calculate_difficulty(r_cooking_time, r_ingredients)

    recipe = Recipe(
        name = r_name,
        cooking_time = r_cooking_time,
        ingredients = sql_ingredients,
        difficulty = r_diff
    )
    session.add(recipe)
    session.commit()

    print("Recipe for " + r_name + " was added successfully.")


def view_recipes():
    result = session.query(Recipe).all()
    i = 0
    for row in result:
        print(row)
    input("Press enter to return...")

def search_ingredients():
    all_ingreds_list = []
    i = 0
    recipes_list = session.query(Recipe.ingredients).all()
    for x in recipes_list:
        for y in x:
            y = str(y).split(',')
            for z in y:
                if not z in all_ingreds_list:
                    i+=1
                    print(str(i) + '.', z)
                    all_ingreds_list.append(z)
    choice = int(input("Which ingredient would you like to search for? (ID Input) "))
    print(all_ingreds_list[choice-1])
    result = session.query(Recipe.name, Recipe.ingredients).filter(Recipe.ingredients.like("%" + all_ingreds_list[choice-1] + "%")).all()
    for x in result:
        print("Name: " + x[0] + " | " + "Ingredients: " + x[1])
    input("Press enter to return to the main menu...")
    

def update_recipe():
    result = session.query(Recipe).all()
    i = []
    try:
        result[0]
    except:
        input("Empty table. Please choose to create a recipe. Press enter to return...")
        return None
    for row in result:
        i.append(row.id)
        print(row)
    id_update = input("Select the ID of a recipe you wish to UPDATE: ")
    try: 
        id_update = int(id_update)
        if(id_update in i):
            next
        else:
            input("Bad input. Back to main loop...")
            return 1
    except:
        input("Bad input. Back to main loop...")
        return 1

    column_update = input("Which category/column did you want to update? (name, ingredients, cooking_time): ")
    if(column_update == ('name' or 'Name')):
        change = input("What would you like to change the name of [" + row.name + "] to? ")
        if(len(change) > 0 and len(change) < 50):
            session.query(Recipe).filter(Recipe.name == row.name).update({Recipe.name: change})
            session.commit
        else:
            print("Please enter a name length less than 50")
            update_recipe()

    elif(column_update == ('ingredients' or 'Ingredients')):
        r_ingredients = []
        sql_ingredients = ""
        m = int(input("[UPDATING] How many ingredients are in " + row.name + "? "))
        for x in range (0, m):
            p = str(input(f"Ingredient #{x + 1}: "))
            r_ingredients.append(p)
            if(x+1 == m):
                sql_ingredients += (p)
            else:
                sql_ingredients += (p + ",")
        r_diff = calculate_difficulty(row.cooking_time, r_ingredients)
        session.query(Recipe).filter(Recipe.name == row.name).update({Recipe.ingredients: sql_ingredients, Recipe.difficulty: r_diff})
        session.commit
        
    elif(column_update == ('cooking_time')):
        change = input("What would you like to change [" + row.name + "]'s cooking time to? ")
        try:
            r_cooking_time = int(r_cooking_time)
        except:
            print("cooking time that is entered is not an integer value.")
            return 1
        r_diff = calculate_difficulty(change, row.ingredients)
        session.query(Recipe).filter(Recipe.name == row.name).update({Recipe.cooking_time: change, Recipe.difficulty: r_diff})
        session.commit



def delete_recipe():
    result = session.query(Recipe).all()
    i = []
    try:
        result[0]
    except:
        input("Empty table. Please choose to create a recipe. Press enter to return...")
        return None
    for row in result:
        i.append(row.id)
        print(row)
        print("ID:", row.id, " |  RECIPE: " + row.name, " |  INGREDIENTS: "+  row.ingredients)
    id_delete = input("Select the ID of a recipe you wish to delete: ")
    try: 
        if(id_delete in i):
            try:
                to_delete = session.query(Recipe).filter(Recipe.id == id_delete).one()
                check = input("Are you sure you want to delete " + to_delete.name + "? (Y or N)")
                if(check == "Y" or "y"):
                    session.delete(to_delete)
                    session.commit()
                    return None
                else:
                    input("Not deleting. Returning...")
                    return None
            except:
                print("Error. Potentially an empty ID. Please try again with an existing ID...")
                return None
        else:
            print("Bad input. Back to main loop")
            return None
    except:
        print("Bad input. Back to main loop")
        return None


def main_loop():
    recipes_list = session.query(Recipe).all()
    if(len(recipes_list) > 0):
        print(recipes_list)
    choice = None
    while choice == None or 1 or 2 or 3 or 4 or 5:
        print("Main Menu")
        print("============================")
        print("Pick a choice:")
        print("     1. Create New Recipe")
        print("     2. View all recipes")
        print("     3. Search for a recipe by ingredient")
        print("     4. Update an existing recipe")
        print("     5. Delete a recipe")
        print("     6. Quit the program...")
        choice = input("Your choice: ")
        if choice == '1':
            create_recipe()
        elif choice == '2':
            view_recipes()
        elif choice == '3':
            search_ingredients()
        elif choice == '4':
            update_recipe()
        elif choice == '5':
            delete_recipe()
        else:
            print("Exiting...")
            return False





main_loop()