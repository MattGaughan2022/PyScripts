main_loops = 0

class Recipe(object):
    all_ingredients = []
    all_recipes = []

    def __init__(self, name, ingredients={None}, cooking_time=0, difficulty=''):
        self.name = name
        self.ingredients = ingredients
        if(self.ingredients is not None):
            for d in self.ingredients:
                if d not in Recipe.all_ingredients:
                    Recipe.update_all_ingredients(d)
        self.cooking_time = cooking_time
        self.difficulty = difficulty
        Recipe.all_recipes.append(self.name)
    
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name

    def get_cooking_time(self):
        return self.cooking_time
    def set_cooking_time(self, time):
        self.cooking_time = time

    def add_ingredients(self, ingreds):
        if(self.ingredients is None):
            self.ingredients = set(ingreds)
            self.calculate_difficulty()
        else: 
            for i in ingreds:
                if not i in self.ingredients:
                    self.ingredients.update(i)
                    Recipe.update_all_ingredients(i)
            self.calculate_difficulty()

    def get_ingredients(self):
        return self.ingredients
    
    def print_ingredients(self):
        if(self.ingredients):
            p = list(self.ingredients)
            ingreds = ''
            for i in p:
                if p.index(i) < len(p) - 1:
                    ingreds += (i + ', ')
                else:
                    ingreds += ('and ' + i)
            return ingreds

    def calculate_difficulty(self):
        if(self.ingredients):
            if (self.cooking_time < 10 and len(self.ingredients) < 4):
                self.difficulty = 'easy'
            elif (self.cooking_time < 10 and len(self.ingredients) >= 4):
                self.difficulty = 'medium'
            elif (self.cooking_time >= 10 and len(self.ingredients) < 4):
                self.difficulty = 'intermediate'
            elif (self.cooking_time >= 10 and len(self.ingredients) >= 4):
                self.difficulty = 'hard'
            else:
                self.difficulty = 'Not enough info here'
        else:
            self.difficulty = 'Not enough info'
        return self.difficulty

    def get_difficulty(self):
        if not self.difficulty or self.difficulty == '' or self.difficulty == None:
            return self.calculate_difficulty()
        else:
            return self.difficulty

    def update_all_ingredients(d):
        if not d in Recipe.all_ingredients:
            Recipe.all_ingredients.append(d)

    def recipe_search(data, search_term):
        for i in data:
            if search_term in i.ingredients:
                print(i)
            else:
                print(search_term, 'is not in ', i.name)
                print('====')
    
    def __str__(self):
        print(" ",'>>> name:', self.get_name())
        print(" ",'>>> cooking time:', self.get_cooking_time())
        print(" ",'>>> ingredients:', self.get_ingredients())
        print(" ",'>>> difficulty:', self.get_difficulty())
        return '===='

    

banana_shake = Recipe('Banana Smoothie', {'Milk', 'Peanut Butter', 'Bananas', 'Sugar', 'Ice Cubes'}, 5, '')
tea = Recipe('Tea', None, 5, '')
coffee = Recipe('Coffee', {'Coffee Powder', 'Sugar', 'Water'}, 5, '')
cake = Recipe('Cake', {'Sugar', 'Butter', 'Eggs','Vanilla Essence', 'Flour', 'Baking Powder', 'Milk'}, 50, '')
print("  vInitialize tea (no ingredients or cooking time)v ")
print(tea)
print("  vSet tea ingredients, cookingtime, and display stringv ")
tea.add_ingredients({'Tea Leaves', 'Water', 'Sugar'})
print(tea)
print(" v============== ALL RECIPES (Names) ==============v ")
print(Recipe.all_recipes)
print(" v============== INGREDIENT SEARCH ==============v ")
Recipe.recipe_search({tea, coffee, cake, banana_shake}, 'Water')
Recipe.recipe_search({tea, coffee, cake, banana_shake}, 'Sugar')
Recipe.recipe_search({tea, coffee, cake, banana_shake}, 'Bananas')

