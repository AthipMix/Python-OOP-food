from flask import Flask, render_template, request, redirect, url_for

from food import Food
from recipe import Recipe


app = Flask(__name__)


# --------------------------------
# Food Data
# --------------------------------

food1 = Food("ผัดกะเพรา", "อาหารจานเดียว")
food1.addRecipe(Recipe("หมูสับ", 100, "กรัม"))
food1.addRecipe(Recipe("ใบกะเพรา", 20, "กรัม"))
food1.addRecipe(Recipe("พริก", 10, "เม็ด"))

food2 = Food("ข้าวผัด", "อาหารจานเดียว")
food2.addRecipe(Recipe("ข้าวสวย", 200, "กรัม"))
food2.addRecipe(Recipe("ไข่ไก่", 1, "ฟอง"))
food2.addRecipe(Recipe("หมู", 100, "กรัม"))


foods = [food1, food2]


# --------------------------------
# Home
# --------------------------------

@app.route("/")
def index():
    return render_template(
        "index.html",
        foods=foods
    )


# --------------------------------
# Add Recipe
# --------------------------------

@app.route("/add-recipe/<int:food_id>", methods=["POST"])
def add_recipe(food_id):

    food = foods[food_id]

    recipe_name = request.form["recipeName"]
    quantity = float(request.form["quantity"])
    unit_name = request.form["unitName"]

    recipe = Recipe(
        recipe_name,
        quantity,
        unit_name
    )

    food.addRecipe(recipe)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)