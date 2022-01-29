from flask import Flask, jsonify
import json

appFlask = Flask(__name__)

@appFlask.route('/')
def view():
    return 
    


if __name__ == "__main__":
    appFlask.run(debug=True)
    