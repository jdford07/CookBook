from dataclasses import dataclass, field
from typing import List, Optional
from dotenv import load_dotenv, find_dotenv
import mongoTest

@dataclass
class IngredientsSection:
    """ """
    sectionTitle: str
    ingredients: list[object] # Dictionary of ingredients and measurements

@dataclass
class Ingredient:
    """ """
    ingredientName: str
    ingredientAmount: str # 1/2, 1/3, 1...100+
    ingredientMeasurement: str # tsp, tbsp, cup, mg, g, kg, ml, l
    ingredientSuggestedBrand: Optional[str] = None
    
@dataclass
class StepsSection:
    """ """
    sectionTitle: str
    steps: list[str] # Dictionary of ingredients and measurements

@dataclass
class Recipe:
    """Class that defines all notable elements of a given Recipe"""
    recipeTitle: str
    recipeAuthor: str
    recipeCategory: str
    recipeDescription: str
    recipeArticleLink: str
    recipeVideoLink: str
    recipeIngredientsSections: List[object]
    recipeStepsSections: List[object]
    recipeNotes: List[str]
    recipeServings: str
    recipeGlutenClass: str
    recipeDietClass: str
    recipePrepTime: int
    recipeCookTime: int
    recipeRestTime: int
    recipeTotalTime: int = field(init=False)
    recipeDifficulty: str
    
    def __post_init__(self):
        self.recipeTotalTime = self.recipePrepTime + self.recipeCookTime + self.recipeRestTime
        if(self.recipeTotalTime == None):
            self.recipeTotalTime = 0
   
        
        

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

ingred1 = Ingredient("Dried Thyme", "1", "tsp")
ingred2 = Ingredient("Ground Allspice", "1/2", "tsp")
ingred3 = Ingredient("Sugar", "1 1/2", "tbsp")
ingred4 = Ingredient("Sea Salt", "1/2", "tsp", "Morton")
ingred5 = Ingredient("Chicken Breast", "2", "breasts", "Perdue")
ingredSection1a = IngredientsSection("Spices", [ingred1, ingred2, ingred3, ingred4])
ingredSection1b = IngredientsSection("Proteins", [ingred5])

steps1 = ["Add the thyme, allspice, coconut sugar, sea salt, black pepper, garlic powder, cinnamon, cayenne, olive oil, and freshly squeezed lime juice in a mixing bowl. Stir to combine.", 
          "Add the chicken to a 1 quart freezer-safe sealable bag, followed by the jerk spice marinade. Press the air out of the bag and seal tightly, making sure to press the marinade around the chicken to coat.", 
          "Place in the fridge to marinate at least 30 minutes, up to overnight."]
stepSection1 = (None, steps1)


ingred6 = Ingredient("Dried Thyme", "2", "tsp")
ingred7 = Ingredient("Ground Allspice", "3/4", "tsp")
ingred8 = Ingredient("Sugar", "4", "tbsp")
ingred9 = Ingredient("Sea Salt", "2", "tsp", "Morton")
ingred10 = Ingredient("Chicken Breast", "4", "breasts", "Perdue")
ingredSection2a = IngredientsSection("Spices", [ingred6, ingred7, ingred8, ingred9])
ingredSection2b = IngredientsSection("Proteins", [ingred10])
steps2 = ["Add the thyme, allspice, coconut sugar, sea salt, black pepper, garlic powder, cinnamon, cayenne, olive oil, and freshly squeezed lime juice in a mixing bowl. Stir to combine.", 
          "Add the chicken to a 1 quart freezer-safe sealable bag, followed by the jerk spice marinade. Press the air out of the bag and seal tightly, making sure to press the marinade around the chicken to coat."]
stepSection2 = ("Combine it all", steps2)

ingreds3 = {'All Purpose Flour':'3 cups', 
            'Salt':'1 tsp',
            'Baking Powder':'1 tsp',
            'Vegetable Oil':'1/3 cup',
            'Hot Water':'1 cup'}
step3 = [""
    
]

recipe1 = Recipe("Jerk Chicken Marinade",
                 "Lacey Baier",
                 "Sauce",
                 "This easy jerk chicken marinade is Caribbean-inspired and full of spice and flavor",
                 "https://www.asweetpeachef.com/best-chicken-marinades/#wprm-recipe-container-22000",
                 None,
                 [IngredientsSection("Spices", [ingred1, ingred2, ingred3, ingred4]), IngredientsSection("Proteins", [ingred10])],
                 [StepsSection("Jerk Chicken", steps1), StepsSection("Garlic Chicken", steps2)],
                 ["Absolutely smashin","Smashing cause good"],
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
                 [IngredientsSection("Jerk Chicken", [ingred6, ingred7, ingred8, ingred9]), IngredientsSection("Garlic Chicken", [ingred10])],
                 [StepsSection("Jerk Chicken", steps1), StepsSection("Garlic Chicken", steps2)],
                 ["Absolutely smashin","Smashing cause good"],
                 "2 Chicken Breasts",
                 "GlutenFree",
                 "Regular",
                 5,
                 5,
                 30,
                 "Easy")

recipeList = [recipe1, recipe2]
print(recipeList)
#aggregateIngredients(recipeList)
print(recipe1)

