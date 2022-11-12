from flask import Flask
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
    pass

# Then we will create a route to create a recipe, using the 'POST' method. In CRUD, this is a CREATE command.
@app.route('/recipes', methods=['POST'])
def create_a_recipe():
    pass

# Next will will create a route to get only one recipe via it's id (hence the '<int:id>'. In CRUD, this is a READ command.
@app.route('/recipes/<int:id>', methods=['GET'])
def get_one_recipe(id):
    pass

# Then we use the 'PUT' method to create an update function. In CRUD, this is an UPDATE command.
@app.route('/recipes/<int:id>', methods=['PUT'])
def update_recipe(id):
    pass

# Finally, we will create a route to delete a recipe via its id using the 'DELETE' method. In CRUD, this is a DELETE command.
@app.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    pass

# Our server is ran via the following statement. Debug is also set to True
if __name__ == '__main__':
    app.run(debug=True)