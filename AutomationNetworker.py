from flask import Flask
from flask_restful import Api
from resources.recipe import RecipeListResource, RecipeResource, RecipePublishResource

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return "It is working.  Figure out the issue, Chica"

api.add_resource(RecipeListResource)
api.add_resource(RecipeResource)
api.add_resource(RecipePublishResource)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
