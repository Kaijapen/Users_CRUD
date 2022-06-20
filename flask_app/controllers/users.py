# users.py
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User


@app.route("/")
def start_page():
    users_list = User.get_all()
    return render_template("result.html", users_list=users_list)


@app.route("/result/commit", methods=["POST"])
def results():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.create(data)
    return redirect("/")


@app.route("/add/user")
def new_user():
    return render_template("index.html")


@app.route("/user/<int:id>")
def user_page_get(id):
    data = {
        "id": id
    }
    user = User.get_one(data)
    return render_template("user_info.html", user=user)


@app.route("/delete/<int:id>")
def user_delete(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect("/")


@app.route("/edit/<int:id>")
def user_edit(id):
    data = {
        "id": id,
    }
    user = User.get_one(data)
    return render_template("edit_user.html", user=user)


@app.route("/edit/commit/<int:id>", methods=["POST"])
def updating(id):
    data = {
        "id": id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.update(data)
    return redirect("/")
