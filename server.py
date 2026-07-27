
from flask import Flask
import datetime
import csv
import random

app = Flask(__name__)

with open("users.csv", "r") as f:
    users = list(csv.DictReader(f))

quotes = [
    "The best way to predict the future is to invent it. - Alan Kay",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "Do not take life too seriously. You will never get out of it alive. - Elbert Hubbard",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson"
]


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
    return response


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/time")
def time():
    return {"current_time": str(datetime.datetime.now())}


@app.route("/users")
def get_users():
    return {"users": users}


@app.route("/quote")
def get_quote():
    return {"quote": random.choice(quotes)}


# Add at least one new endpoint of your own below.
# Make it return JSON.  Get creative — quotes, jokes, a counter, anything.


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
