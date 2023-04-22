from dataclasses import dataclass, field
from typing import List, Optional, Literal
from dotenv import load_dotenv, find_dotenv
import mongoDBRequests as mongo
import json

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
    ingredientNotes: Optional[List[str]] = None
    
    
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
    recipeDescription: str 
    recipeSource: str # Either web article link or cookbook
    recipeVideoLink: Optional[str]
    recipeCategory: str # Seasoning, Appetizer, Base, Side, Snack, Drink, Breakfast, Lunch, Dinner, Dessert
    recipeCuisineType: str # Asian, American, Mexican, Italian, Greek, German
    recipeGlutenType: str # Glutenfree, Not GF translate to Icons for funsies
    recipeDietType: List[str] # Vegan, Vegetarian, Onmivore, translate to Icons for funsies
    recipeServings: int
    recipePrepTime: int
    recipeCookTime: int
    recipeRestTime: int
    recipeTotalTime: int = field(init=False)
    recipeDifficulty: str
    recipeSeason: Optional[str] # Summer, Winter, Fall, Christmas, Thanksgiving
    cookingMethod: List[str] # PressureCooker, SlowCooker, Air-fry, Oven, Skillet, Grill
    recipeIngredientsSections: List[object]
    recipeStepsSections: List[object]
    recipeNotes: List[str] # Special tips
    recipeKeywords: List[str]
    
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
                 "This easy jerk chicken marinade is Caribbean-inspired and full of spice and flavor",
                 "https://www.asweetpeachef.com/best-chicken-marinades/#wprm-recipe-container-22000",
                 None,
                 "Marinade",
                 "Caribbean",
                 "Gluten Free",
                 "Omnivore",
                 2,
                 5,
                 5,
                 30,
                 "Easy",
                 "All",
                 None,
                 [IngredientsSection("Spices", [ingred1.__dict__, ingred2.__dict__, ingred3.__dict__, ingred4.__dict__]).__dict__, IngredientsSection("Proteins", [ingred10.__dict__]).__dict__],
                 [StepsSection("Jerk Chicken", steps1).__dict__, StepsSection("Garlic Chicken", steps2).__dict__],
                 ["Absolutely smashin","Smashing cause good"],
                 ["Chicken", "Marinade"])

recipe2 = Recipe("Garlic Chicken Marinade",
                 "Lacey Baier",
                 "This easy jerk chicken marinade is Caribbean-inspired and full of spice and flavor",
                 "https://www.asweetpeachef.com/best-chicken-marinades/#wprm-recipe-container-22000",
                 None,
                 "Marinade",
                 "American",
                 "Gluten Free",
                 "Omnivore",
                 2,
                 5,
                 5,
                 30,
                 "Easy",
                 "All",
                 None,
                 [IngredientsSection("Jerk Chicken", [ingred6, ingred7, ingred8, ingred9]), IngredientsSection("Garlic Chicken", [ingred10])],
                 [StepsSection("Jerk Chicken", steps1), StepsSection("Garlic Chicken", steps2)],
                 ["Absolutely smashin","Smashing cause good"],
                 ["Chicken", "Marinade"])

recipeList = [recipe1, recipe2]
# print(recipeList)
#aggregateIngredients(recipeList)
# print(recipe1)

json = json.dumps(recipe1.__dict__, indent=3)
print(json)

#mongo.insertSingleRecord("RecipeGenerator", "Recipes", recipe1.__dict__)
    
    
    
# Chocolate chip cookies recipe
ingredSectionC = IngredientsSection(
    None,
    [
        Ingredient("Cake Flour", "2", "cups", "King Arthur", ["Measurement is 2 cups minus 2 tbsp"]).__dict__,
        Ingredient("Bread Flour", "1 2/3", "cups").__dict__,
        Ingredient("Baking Soda", "1 1/4", "tsp").__dict__,
        Ingredient("Baking Powder", "1 1/2", "tsp").__dict__,
        Ingredient("Kosher Salt", "1 1/2", "tsp").__dict__,
        Ingredient("Unsalted Butter", "20", "tbsp", None, ["2 1/2 sticks of butter","Room Temperature"]).__dict__,
        Ingredient("Light Brown Sugar", "1 1/4", "cups").__dict__,
        Ingredient("Granulated Sugar", "1", "cup", None, ["Measurement is 1 cup plus 2 tbsp"]).__dict__,
        Ingredient("Large Eggs", "2", None).__dict__,
        Ingredient("Vanilla Extract", "2", "tsp").__dict__,
        Ingredient("Bittersweet Chocolate", "1 1/4", "lbs", None, ["Chocolate discs work best", "At least 60% cacao"]).__dict__,
        Ingredient("Sea Salt", None, None, None, "To Taste").__dict__
    ]
)
stepSectionC = StepsSection(
    None,
    [
        "Sift flours, baking soda, baking powder and kosher salt into a bowl. Set aside.",
        "Using a stand mixer fitted with paddle attachment, cream butter and sugars together until very light, about 5 minutes.",
        "Add the eggs, one at a time, mixing well after each addition. Stir in the vanilla.",
        "Reduce speed to low, add the flour mixture and mix until just combined, 5 to 10 seconds.",
        "Drop the chocolate chunks in and incorporate them without breaking them. You may have to do this by hand with a spatula. ",
        "Press plastic wrap against dough and refrigerate for 24 to 36 hours. (I vote 36 hours.) Dough may be used in batches, and can be refrigerated for up to 72 hours.",
        "When you’re ready to bake, fire up the oven to 350° (176°C). Line a baking sheet with parchment paper or a nonstick baking mat. Set aside.",
        "Scoop six 3 1/2-ounce mounds of dough (the size of generous golf balls) onto a baking sheet, making sure to turn horizontally any chocolate pieces that are poking up; it will make for a more attractive cookie. You can also freeze the balls in a resealable plastic bag.) Sprinkle lightly with sea salt.",
        "Bake the cookies until golden brown but still soft, 18 to 20 minutes. You’ll know the cookies are done when the tops have the caramel folds of a Shar Pei.",
        "Transfer sheet to a wire rack for 10 minutes, then slip cookies onto another wire rack to cool a bit more. Repeat with the remaining dough. Eat warm, with a big napkin."
    ]
)

recipeC = Recipe(
    "David Leite's Chocolate Chip Cookies",
    "David Leite",
    "Say hello to the chocolate chip cookie recipe that started an Internet craze and made bakers rethink how to make cookies. They originally appeared in the July 9, 2008 edition of the New York Times in an article written by our Fearless Leader, David Leite. What makes them so damn special is the dough is refrigerated for 24 to 36 hours for a more complex flavor and greater variation in texture. Sea salt is the finishing touch.",
    "https://leitesculinaria.com/9951/recipes-perfect-chocolate-chip-cookies.html",
    None,
    "Dessert",
    "American",
    "Not Gluten Free",
    "Omnivore",
    18,
    15,
    20,
    8640,
    "Easy",
    "All",
    ["Oven"],
    ingredSectionC.__dict__,
    stepSectionC.__dict__,
    None,
    ["Chocolate Chip", "Cookies", "Baked"]
)

# mongo.insertSingleRecord("RecipeGenerator", "Recipes", recipeC.__dict__)


# # Souffle recipe
ingredSectionDa = IngredientsSection(
    "Ramekin Lining",
    [
        Ingredient("Unsalted Butter", "2", "tbsp", None, ["Melted butter"]).__dict__,
        Ingredient("Granulated Sugar", "2", "tbsp", None, None).__dict__
    ]
)
ingredSectionDb = IngredientsSection(
    "Souffles",
    [
        Ingredient("Unsweetened Chocolate", "2", "oz", None, ["Chopped up"]).__dict__,
        Ingredient("Semisweet Chocolate Chips", "1/3", "cup", None, None).__dict__,
        Ingredient("All Purpose Flour", "1/3", "cup", None, ["Can subsitute with Bread Flour", "Measurement is 1/3 cup plus 1 tbsp"]).__dict__,
        Ingredient("Unsalted Butter", "3", "tbsp", None, ["Room Temperature"]).__dict__,
        Ingredient("Milk", "1", "cup", None, "Cold milk").__dict__,
        Ingredient("Large Eggs", "6", None, None, ["6 egg yolks", "5 egg whites"]).__dict__,
        Ingredient("Vanilla Extract", "1", "tsp", None, None).__dict__,
        Ingredient("Granulated Sugar", "1/3", "cup", None, ["Measurement is 1/3 cup plus 1 tbsp"]).__dict__,
        Ingredient("Powdered Sugar", "1/4", "Cup", None, None).__dict__
    ]
)
stepSectionD = StepsSection(
    None,
    [
        "Preheat oven to 375 F. Line a baking sheet with parchment paper.",
        "To prepare the ramekins: Brush the bottoms and sides of eight 5-ounce ramekins with the melted butter. Divide the granulated sugar among the ramekins and turn them to thoroughly coat the bottoms and sides. Discard any extra sugar.",
        "To make the souffles: In a small stainless steel bowl or the top of a double boiler, combine the chopped chocolate and chocolate chips. Nest the bowl over a pot of barely simmering water (the bowl should not touch the water) and stir the chocolate until melted (taking care not to get any water in the bowl), Set the bowl aside off the heat.",
        "In a medium saucepan, melt the butter over medium heat. Sprinkle in the flour and whick until the flour is incorporated and the mixture thickens, about 1 minute. Reduce the heat to low and whisk in the milk. Continue whisking until the mixture becomes smooth, 2 to 3 minutes. Remove the saucepan from the heat. Transfer the mixture to the bowl with the melted chocolate and stir to combine. Slowly stir the egg yolks into the chocolate mixture. Set aside.",
        "In a bowl, with an electric mixer fitted with the whisk, whip the egg whites and vanilla until the whites start to get foamy, then sprinkle in the sugar. Continue whipping the egg whites on medium speed until they form soft peaks and the consistency resembles whipped cream, about 3 minutes.",
        "Use a spatula to fold about one-third of egg whites into the chocolate mixture, carefully lifting from the bottom and folding over. Fold in half the remaining egg whites, then the last of the egg whites, taking care not to deflate the mixture.",
        "Divide the mixture among the prepared ramekins and place them on the prepared baking sheet.",
        "Bake the souffles undisturbed until they have risen over the top of the rims, 12 to 15 minutes.",
        "Pour the powdered sugar into a sifter or fine-mesh sieve and gently tap over each souffle immediately as it comes out of the oven.",
        "Serve immediately"
    ]
)

recipeD = Recipe(
    "Chocolate Souffles",
    "Joanna Gaines",
    None,
    "Magnolia Table Vol 2, Page 291",
    None,
    "Dessert",
    "American",
    "Not Gluten Free",
    "Omnivore",
    18,
    30,
    15,
    0,
    "Medium",
    "All",
    ["Oven, Stove Top"],
    [ingredSectionDa.__dict__, ingredSectionDb.__dict__],
    stepSectionD.__dict__,
    None,
    ["Souffle", "Chocolate", "Baked"]
)

# mongo.insertSingleRecord("RecipeGenerator", "Recipes", recipeD.__dict__)

# Homemade Gnocchi recipe
ingredSection = IngredientsSection(
    None,
    [
        Ingredient("Kosher Salt", "1/2", "cup", None, ["Measurement is 1/2 cup plus 1 tsp"]).__dict__,
        Ingredient("Russet Potatoes", "2 1/2", "lbs", None, ["About 4 potatoes"]).__dict__,
        Ingredient("Large Eggs", "3", None, None, ["Lightly beaten", "1 egg yolk"]).__dict__,
        Ingredient("All Purpose Flour", "2 1/2", "cups", None, ["Plus more flour for rolling"]).__dict__,
        Ingredient("Canola Oil", "2", "tbsp", None, None).__dict__
    ]
)
stepSectionD = StepsSection(
    None,
    [
        "Preheat the oven to 400F.",
        "Spread the 1/2 cup of salt on a sheet pan, creating a salt bed.",
        "Using a fork, poke each potato all over to allow for steam to vent. Place the potatoes along the salt bed, keeping equal distance between the potatoes. Bake until tender when pierced with a paring knife, about 1 hr 15 minutes.",
        "Carefully halve the potatoes lengthwise and scoop the inside into a bowl to cool, about 15 minutes. Press the insides of the potatoes through a potato ricer into a large bowl. Set aside until cool enough to work with",
        "Create a well on a flat surface. Crack eggs into the center and mix with the potatoes. Working quickly, sprinkle the flour and the remaining 1 teaspoon salt over the potatoes and gently fold in the flour and salt. Turn the dough out onto a lightly floured surface and gently knead just until the dough comes together. Divide the dough into 8 equal portions and cover with a clean kitchen towel.",
        "Working with one portion of dough at a time, use your hands to roll the dough back and forth while moving them outward to elongate the dough into a 3/4-inch-diameter rope. Using a dough scraper or knife, cut the rope into 1- to 2-inch pieces.",
        "Bring a large pot of salted water to boil over high heat. Line a sheet pan with a clean kitchen towel. Working in 3 or 4 batches (so the gnocchi have plenty of room to cook), gently add the gnocchi to the simmering water. (Be sure to let the water return to a simmer between batches). When they rise to the surface,  cook until slightly firm, about 1 minute. UIsing a spider or slotted spoon, transfer the gnocchi to the towel-lined sheet pan. Let cool for 10 minutes.",
        "In a large nonstick skillet, heat 1 tablespoon of the canola oil over medium-high heat. Add half of the gnocchi. Cook, stirring occaisonally, until golden brown, to 4 to 6 minutes. Transfer to a plate and repeat with the remaining canola oil and gnocchi. Return the browned gnocchi to the skillet and toss with the sauce of your choice."
    ]
)

recipeD = Recipe(
    "Homemade Gnocchi",
    "Joanna Gaines",
    None,
    "Magnolia Table Vol 2, Page 34",
    None,
    "Dinner",
    "Italian",
    "Not Gluten Free",
    ["Omnivore", "Vegetarian"],
    4,
    120,
    20,
    0,
    "Medium",
    "All",
    ["Stove Top"],
    [ingredSection.__dict__],
    stepSectionD.__dict__,
    ["You can freeze the gnocchi after step 6 to save for quick dinners.", "If cooking from frozen, start with step 7", "When gnocchi rise tothe surface, cook until slightly firm, about 5 minutes"],
    ["Gnocchi", "Pasta", "homemade", "scratch", "from scratch"]
)

mongo.insertSingleRecord("RecipeGenerator", "Recipes", recipeD.__dict__)