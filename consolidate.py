from flask import request
from flask_restful import Resource
from http import HTTPStatus
from flask import Flask
from flask_restful import Api


recipe_list = []

def get_last_id():
       if recipe_list:
           last_recipe = recipe_list[-1]
       else:
           return 1
       return last_recipe.id+1

class Recipe:
    def __init__(self,name,description,num_of_servings,cook_time,directions):
        self.id = get_last_id()
        self.name = name
        self.description = description
        self.num_of_servings = num_of_servings
        self.cook_time = cook_time
        self.directions = directions
        self.is_publish = False

    @property
    def data(self):
         return {
             'id' : delf.id,
             'name': self.name,
             'description':self.description,
             'num_of_servings' :self.num_of_servings,
             'cook_time' : self.cook_time,
             'directions': self.directions

         }


class RecipeListResource(Resource):
    def get(self):

        data = []

        for recipe in recipe_list:
            if recipe.is_publish is True:
                data.append(recipe.data)

        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()

        recipe = Recipe(name=data['name'],
                        description=data['description'],
                        num_of_servings=data['num_of_servings'],
                        cook_time=data['cook_time'],
                        directions=data['directions'])

        recipe_list.append(recipe)

        return recipe.data, HTTPStatus.CREATED


app = Flask(__name__)
api = Api(app)

api.add_resource(RecipeListResource, '/recipes')

if __name__ == '__main__':
    app.run()
    
