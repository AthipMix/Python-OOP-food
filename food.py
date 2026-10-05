from recipe import Recipe


class Food:
    def __init__(self, name, category):
        self.nameTh = name
        self.category = category
        self.recipeList = []

    def display(self):
        return {
            "name": self.nameTh,
            "category": self.category,
            "recipeList": self.recipeList
        }

    def addRecipe(self, recipe):
        self.recipeList.append(recipe)