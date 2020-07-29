#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
      # if len(ingredients) < len(recipe):
      #       return 0
            for i in recipe.values():
                  for j in ingredients.values():
                        if len(ingredients) < len(recipe):
                             return 0
                        if j < i:
                            return 0
                        elif j == i:
                            return 1
                        elif j > i:
                              return j // i
              


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
  
 
