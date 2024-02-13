import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password')

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database2")

cursor.execute("USE task_database2")

cursor.execute('''
CREATE TABLE IF NOT EXISTS Recipes(
id              INT PRIMARY KEY AUTO_INCREMENT,
name            VARCHAR(50),
ingredients     VARCHAR(255),
cooking_time    INT,
difficulty      VARCHAR(20)
)
''')

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

def create_recipe(conn, cursor):
    print("===== CREATE RECIPE =====")
    r_name = input("Name of recipe: ")
    r_cooking_time = int(input("Cooking time for recipe: "))
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
    print(sql_ingredients)
    sql = 'INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)'
    val = (r_name, sql_ingredients, r_cooking_time, r_diff)
    cursor.execute(sql, val)
    conn.commit()
    print("Recipe for " + r_name + " was added successfully.")

def search_ingredient(conn, cursor):
    sql = 'SELECT ingredients FROM Recipes'
    cursor.execute(sql)
    result = cursor.fetchall()
    # for count, row in enumerate(result):
    #     print("#" + str(count + 1) + " ",  row)
    all_ingreds_list = []
    for row in result:
        for x in row:
            row = x.split(',')
            for y in row:
                if not y in all_ingreds_list:
                    all_ingreds_list.append(y)
                else:
                    continue
    for x in all_ingreds_list:
        print(x)
    search_val = input("Which ingredient would you like to search for? (enter a string from above): ")
    print("Searching for '" + search_val + "'  .... ")

    sql = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
    val = ("%" + search_val + "%")
    cursor.execute(sql, (val,))
    result = cursor.fetchall()
    for row in result:
        print(row)
    return 1

def update_recipe(conn, cursor):
    sql = "SELECT id, name, cooking_time, ingredients FROM Recipes"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        #print(row)
        print("ID:", row[0], " |  RECIPE: " + row[1], " |  COOKING TIME: ", row[2], " |  INGREDIENTS: ", row[3])
    sql_searchID = int(input("Please enter the ID of the recipe you want to UPDATE: "))
    for row in result:
        if row[0] == sql_searchID: 
            print("ID:", row[0], " |  RECIPE: " + row[1], " |  COOKING TIME: ", row[2], " |  INGREDIENTS: ", row[3])
            choice = input("Which CATEGORY would you like to change? (name, cooking_time, or ingredients?) ")
            if(choice == "cooking_time"):
                choice = int(input("What is the new cooking time of the recipe? "))
                r_diff = calculate_difficulty(choice, row[3])
                print(choice, r_diff)
                cursor.execute('UPDATE recipes SET cooking_time = %s  WHERE id = %s', (choice, row[0]))
                cursor.execute('UPDATE recipes SET difficulty = %s  WHERE id = %s' , (r_diff, row[0]))
                conn.commit()

            elif(choice == "ingredients"):
                r_ingredients = []
                sql_ingredients = ""
                m = int(input("[UPDATING QUERY] How many ingredients are in the new " + row[1] + " recipe? "))
                for x in range (0, m):
                    p = str(input(f"[UPDATING QUERY] Ingredient #{x + 1}: "))
                    r_ingredients.append(p)
                    if(x+1 == m):
                        sql_ingredients += (p)
                    else:
                        sql_ingredients += (p + ",")
                r_diff= calculate_difficulty(row[2], r_ingredients)
                print(r_ingredients, sql_ingredients, r_diff)
                cursor.execute('UPDATE recipes SET ingredients = %s  WHERE id = %s', (sql_ingredients, row[0]))
                cursor.execute('UPDATE recipes SET difficulty = %s  WHERE id = %s', (r_diff, row[0]))
                conn.commit()
                
            elif(choice == "name"):
                choice = input("What is the new name of the recipe? ")
                r_name = choice
                cursor.execute('UPDATE recipes SET name = %s WHERE id = %s', (r_name, row[0]))
                conn.commit()

            else:
                print("something went wrong...")
    return 1

def delete_recipe(conn, cursor):
    sql = "SELECT id, name  FROM Recipes"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print("ID:", row[0], " |  RECIPE: " + row[1])
    sql_searchID = input("Please enter the ID of the recipe you want to DELETE: ")
    cursor.execute('DELETE FROM recipes WHERE id = %s', (sql_searchID,))
    conn.commit()
    return 1


def main_menu(conn, cursor):
    choice = None
    while(choice != '5'):
        print("Main Menu")
        print("============================")
        print("Pick a choice:")
        print("     1. Create New Recipe")
        print("     2. Search for a recipe by ingredient")
        print("     3. Update an existing recipe")
        print("     4. Delete a recipe")
        print("     5. Quit the program...")
        choice = input("Your choice: ")
        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_ingredient(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
        elif choice == '4':
            delete_recipe(conn, cursor)
        else:
            print("Exiting...")
            break

    conn.close()

main_menu(conn, cursor)
