from dotenv import load_dotenv, find_dotenv
import mongoTest


class RecipeSection:
    def __init__(self, sectionTitle, ingredients, steps):
        self.sectionTitle = sectionTitle
        self.ingredients = ingredients # Dictionary of ingredients and measurements
        self.steps       = steps # List of instruction steps
        

# Class that defines all notable elements of an OSRS News Article
class Recipe:
    def __init__(self, title, author, category, description, articleLink, videoLink, sections, notes, servings, glutenClass, dietClass, prepTime, cookTime, restTime, difficulty):
        self.title       = title
        self.author      = author
        self.category    = category # Sauce, Soup, Main Course, Side Dish
        self.description = description
        self.articleLink = articleLink
        self.videoLink   = videoLink
        self.sections    = sections # List containing objects of instruction steps and ingredients
        self.notes       = notes
        self.servings    = servings
        self.glutenClass = glutenClass # Gluten Free, Gluten Friendly, Neither
        self.dietClass   = dietClass # Vegan, Vegetarian
        self.prepTime    = prepTime
        self.cookTime    = cookTime
        self.restTime    = restTime
        self.totalTime   = int(prepTime) + int(cookTime) + int(restTime)
        self.difficulty  = difficulty

def aggregateIngredients(recipeList):
    ingredientsDict = {}
    
    for recipe in recipeList:
        for section in recipe.sections:
            for ingredient in section.ingredients.items():
                if(ingredient[0] in ingredientsDict):
                    ingredientsDict[f"{ingredient[0]}"]
                    pass
                else:
                    ingredientsDict[f"{ingredient[0]}"] = ingredient[1]
        
        
    return ingredientsDict

ingreds1 = {'Dried Thyme':'1 tsp', 'Ground Allspice':'1/2tsp', 'Sugar':'1 1/2 tbsp', 'Sea Salt':'1/2tsp'}
steps1 = ["Add the thyme, allspice, coconut sugar, sea salt, black pepper, garlic powder, cinnamon, cayenne, olive oil, and freshly squeezed lime juice in a mixing bowl. Stir to combine.", "Add the chicken to a 1 quart freezer-safe sealable bag, followed by the jerk spice marinade. Press the air out of the bag and seal tightly, making sure to press the marinade around the chicken to coat.", "Place in the fridge to marinate at least 30 minutes, up to overnight."]

ingreds2 = {'Dried Thyme':'2 tsp', 'Ground Allspice':'1 tsp', 'Sugar':'3 tbsp', 'Sea Salt':'2 tsp'}
steps2 = ["Add the thyme, allspice, coconut sugar, sea salt, black pepper, garlic powder, cinnamon, cayenne, olive oil, and freshly squeezed lime juice in a mixing bowl. Stir to combine.", "Add the chicken to a 1 quart freezer-safe sealable bag, followed by the jerk spice marinade. Press the air out of the bag and seal tightly, making sure to press the marinade around the chicken to coat."]

print(ingreds1)

recipe1 = Recipe("Jerk Chicken Marinade",
                 "Lacey Baier",
                 "Sauce",
                 "This easy jerk chicken marinade is Caribbean-inspired and full of spice and flavor",
                 "https://www.asweetpeachef.com/best-chicken-marinades/#wprm-recipe-container-22000",
                 None,
                 [RecipeSection("Jerk Chicken", ingreds1, steps1), RecipeSection("Garlic Chicken", ingreds2, steps2)],
                 "Absolutely smashin",
                 "2 Chicken Breasts",
                 "GlutenFree",
                 "Regular",
                 5,
                 5,
                 30,
                 "Easy")

recipe2 = Recipe("Garlic Chicken Marinade",
                 "Lacey Baier",
                 "Sauce",
                 "This easy jerk chicken marinade is Caribbean-inspired and full of spice and flavor",
                 "https://www.asweetpeachef.com/best-chicken-marinades/#wprm-recipe-container-22000",
                 None,
                 [RecipeSection("Jerk Chicken", ingreds1, steps1), RecipeSection("Garlic Chicken", ingreds2, steps2)],
                 "Absolutely smashin",
                 "2 Chicken Breasts",
                 "GlutenFree",
                 "Regular",
                 5,
                 5,
                 30,
                 "Easy")

recipeList = [recipe1, recipe2]
print(recipeList)
aggregateIngredients(recipeList)
print(recipe1)

