from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

# Created app instance and passed import name
app=Flask(__name__)
# Setting the SQLAlchemy database URI. For this, I have passed through the connection string to my SQL database. In this instance, the user is 'postgres' and the password is 'password123'
app.config["SQLALCHEMY_DATABASE_URI"]='postgresql://postgres:password123@localhost/recipes'
# Needed to set 'SQLALCHEMY_TRACK_MODIFICATIONS' to false in order to fix error and run app properly
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

# Created db SQLAlchemy instance
db=SQLAlchemy(app)

# For each recipe, we will include the following:
# 1. Unique id
# 2. Name of recipe
# 3. Description of recipe

# Created recipe class, which will inherit from SQLAlchemy
class Recipe(db.Model):
    # Now creating the unique id which will be an integer. This will also be the primary key, hence the attribute
    id=db.Column(db.Integer(), primary_key=True)
    # We then create the name column, max characters of 250, and it mustn't be null, so we set nullable to false
    name=db.Column(db.String(250), nullable=False)
    # Then we create the description column. This will be text, so we set it as such. Again we set nullable to false
    description=db.Column(db.Text(), nullable=False)

    # We now need to create methods to assist with querying our database
    # Our first method will help return a string representation of our objects. We do this by creating the following function using __repr__, and passing in itself (the current object)
    def __repr__(self):
        # This function will now return its own name, which will be the name of the recipe
        return self.name
    
    # The following function will allow us to query for ALL recipes within the database
    # To do this we will use @classmethod
    @classmethod
    # Then we create a function called get_all, and we then pass in the class
    def get_all(cls):
        # We then use the '.query' method to actually query the model classes, and finally we add '.all()' to specify that we would like to query ALL objects of this class in our database
        return cls.query.all()
    
    # This function will allow us to specify and select one single recipe through the recipes id
    @classmethod
    # As such, we will need to pass in the class and id
    def get_by_id(cls, id):
        # This will then return the specified recipe with the corresponding id. We do this by using '.get_or_404(id)' - this method will first look for the object with the specified id, but if it does not exist the server will then return a '404 not found' error
        return cls.query.get_or_404(id)
    
    # We will now create methods that are specific to the objects themselves 
    # The following 'save' method will allow us to commit changes to our database. What this method will do is it will get our recipe object and add it to our SQLAlchemy session as well as save it to our database
    def save(self):
        # '.session' will add it to our session first, then '.add(self)' will add our current object (self)
        db.session.add(self)
        # We finally commit it to our database through the following
        db.session.commit()
    
    # Our next 'delete' method will allow us to delete any recipe objects that we wish to delete.
    def delete(self):
        # Similar to above, only difference is we instead use the '.delete(self)' method (which obviously will delete the recipe object)
        db.session.delete(self)
        # Similar to above again, we must commit the changes to our database
        db.session.commit()

# We are now going to create a serialiser class using Marshmallow. This class will allow us to serialise our recipe objects and convert them into data that we can receive as JSON. We will call this class RecipeSchema, which will be the schema from which we will serialise our recipe model - this will inherit from Schema (in Marshmallow)
class RecipeSchema(Schema):
    # We will now sepcify the fields for this class, first is id (which is an integer), then name (which is a string), then description (also a string)
    id=fields.Integer()
    name=fields.String()
    description=fields.String()

# Next, we will need to create routes that will allow us to create, read, update and delete (CRUD) resources
# Our first route will be used to get all recipes, using the 'GET' method. In CRUD, this is a READ command.
@app.route('/recipes', methods=['GET'])
def get_all_recipes():
    # Here we are referring back to our '.get_all()' method we created under the Recipe class and assigning it to 'recipes'
    recipes=Recipe.get_all()

    # We will now create an instance of our RecipeSchema class that we created earlier - this will act as a serialiser, hence we will assign this to 'serialiser'
    # We also need to specify that we want it to return a list, or else it will return our data as an object in JSON - we do this by passing 'many=True'
    serialiser=RecipeSchema(many=True)

    # We now want our serialiser to return the data stored in recipes. Therefore, we will utilise the '.dump()' method and then pass through recipes to do exactly this
    data=serialiser.dump(recipes)

    # In order to return the data in JSON format, we will need to utilise the 'jsonify' function that comes with flask
    return jsonify(
        data
    )

# Then we will create a route to create a recipe, using the 'POST' method. In CRUD, this is a CREATE command.
@app.route('/recipes', methods=['POST'])
def create_a_recipe():
    # Firstly, we will need to get the data that our client wishes to post as JSON. We will do this via the request object (from flask) and using the '.get_json()' method (assuming the client will input the data as JSON)
    data=request.get_json()

    # Once we receive the JSON data, we will need to create an object of our Recipe model class (see above for reference to the Recipe class)
    new_recipe=Recipe(
        # We utilise the '.get()' method to retrieve our 'name' and 'description' attributes from our data
        name=data.get('name'),
        description=data.get('description'),
    )

    # We will now call our 'save' method (that we created above) on 'new_recipe' in order to save our newly created recipe
    new_recipe.save()

    # And finally, we will call our RecipeSchema class to serialise and return our object as JSON and show our request has been successfully executed
    serialiser=RecipeSchema()

    # Again, I'll use the '.dump()' method to return our data, passing through our newly created recipe
    data=serialiser.dump(new_recipe)

    # Then it will return a JSON response, using jsonify again. It will also return the successful http status code (201)
    return jsonify(
        data 
    ), 201

# Next will will create a route to get only one recipe via it's id (hence the '<int:id>'. In CRUD, this is a READ command.
@app.route('/recipes/<int:id>', methods=['GET'])
def get_one_recipe(id):
    # Firstly, we need to query the database for the specific id of the recipe we would like to look up, and then return that object as JSON. We will do this via the 'get_by_id()' method that I created above
    recipe=Recipe.get_by_id(id)

    # Again, we need to create a serialiser variable based on the RecipeSchema class created above
    serialiser=RecipeSchema()

    # And our data will need to be returned via the dump method
    data=serialiser.dump(recipe)

    # Using jsonify again, we will return this data in the form of JSON. I'll also return the relevant (200) status code to signify it has been successfully executed
    return jsonify(
        data
    ), 200

# Then we use the 'PUT' method to create an update function. In CRUD, this is an UPDATE command.
@app.route('/recipes/<int:id>', methods=['PUT'])
def update_recipe(id):
    # Firstly, I'll create a variable called recipe_to_update, then call the 'get_by_id()' method I created earlier and passing through the id of the specific recipe
    recipe_to_update=Recipe.get_by_id(id)

    # The data that we want to update will be retrieved as JSON, again via using the '.get_json()' method
    data=request.get_json()

    # We now need to update the name and description, and set it to the newly assigned values from the client
    recipe_to_update.name=data.get('name')
    recipe_to_update.description=data.get('description')

    # Now that the changes have been made above, we need to save these changes to our database using 'db.session.commit()'
    db.session.commit()

    # Again, we need to create a JSON response using our RecipeSchema class
    serialiser=RecipeSchema()

    # As done previously, we'll use the '.dump()' method to return our 'recipe_to_update' data
    recipe_data=serialiser.dump(recipe_to_update)

    # And finally, our recipe_data can be returned as JSON along with the 200 status code
    return jsonify(
        recipe_data
    ), 200

# Finally, we will create a route to delete a recipe via its id using the 'DELETE' method. In CRUD, this is a DELETE command.
@app.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    # First, I'll query the specific recipe I'd like to delete - this is done via the 'get_by_id' method I created earlier
    recipe_to_delete=Recipe.get_by_id(id)

    # Now we apply the 'delete()' method I created earlier
    recipe_to_delete.delete()

    # Finally, we'll send the client a messga to confirm the recipe has been delete, along with the relevant 204 status code
    return jsonify(
        {"message": "Recipe successfully deleted."}
    ), 204

# In case we encounter any error, we'll need to handle these appropriately using the flask errorhandler method
@app.errorhandler(500)
def internal_server_error(error):
    return jsonify(
        {"message": "Error! You have encountered an internal server error."}
    ), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify(
        {"message": "Error! Resource not found."}
    ), 404

# Our server is ran via the following statement. Debug is also set to True
if __name__ == '__main__':
    app.run(debug=True)