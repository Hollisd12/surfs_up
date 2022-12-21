# Import flask dependency
from flask import Flask

# Create a new flask app instance called app
app = Flask(__name__)

# Create a flask route
@app.route('/')
def hello_world():
    return 'Hello world'

    