"""Flask app for Cupcakes"""
import os

<<<<<<< HEAD
from flask import Flask, render_template, flash, redirect, request, jsonify
=======
from flask import Flask, render_template, flash, redirect, jsonify, request
>>>>>>> 26e8905a99c7c62e721f8689a73952fbe75ed42f
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, Cupcake

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///cupcakes")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get("/api/cupcakes")
def show_all_cupcakes():
<<<<<<< HEAD
    """Get data about all cupcakes.
    Respond with JSON like:
    {cupcakes: [{id, flavor, size, rating, image_url}, ...]}"""
=======
    #TODO add to docstring, what func recieves,what func returns
    """Get data about all cupcakes"""
>>>>>>> 26e8905a99c7c62e721f8689a73952fbe75ed42f

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)

@app.get("/api/cupcakes/<int:cupcake_id>")
def show_single_cupcake(cupcake_id):
<<<<<<< HEAD
    """Get data about a single cupcake via cupcake_id
    Respond with JSON like:
    {cupcakes: [{id, flavor, size, rating, image_url}, ...]}"""
=======
        #TODO add to docstring, what func recieves,what func returns
    """Get data about a single cupcake"""
>>>>>>> 26e8905a99c7c62e721f8689a73952fbe75ed42f

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.post("/api/cupcakes")
def create_cupcake():
    """Create a cupcake with flavor, size, rating and image data from the body of the request.
    Respond with JSON like:
    {cupcake: {id, flavor, size, rating, image_url}}"""

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image_url = request.json["image_url"] or None

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image_url=image_url)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)

@app.patch("/api/cupcakes/<int:cupcake_id>")
def update_cupcake(cupcake_id):
    """Update a cupcake using the id passed in the URL and the cupcake data passed in the body of the request.
    Respond with JSON of the newly-updated cupcake, like this:
    {cupcake: {id, flavor, size, rating, image_url}}"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    flavor = request.json.get("flavor", cupcake.flavor)
    size = request.json.get("size", cupcake.size)
    rating = request.json.get("rating", cupcake.rating)
    image_url = request.json.get("image_url", cupcake.image_url)

    cupcake.flavor = flavor
    cupcake.size = size
    cupcake.rating = rating
    cupcake.image_url = image_url

    db.session.commit()
    serialized = cupcake.serialize()

    return (jsonify(cupcake=serialized), 200)

@app.delete("/api/cupcakes/<int:cupcake_id>")
def delete_cupcake(cupcake_id):
    """Delete cupcake with the id passed in the URL.
    Respond with JSON like
    {deleted: [cupcake-id]}"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return (jsonify(deleted=cupcake_id))
