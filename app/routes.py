from flask import render_template, url_for, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
from app.models import User, Todo
from app import app, db
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/home')
@login_required
def home():
  todo_list = Todo.query.all()
  return render_template("home.html", title="Seja bem vindo", todo_list = todo_list)
 
@app.route("/add", methods=["POST"])
def add():
  title = request.form.get("title")
  message = request.form.get("message")
  new_todo = Todo(title=title, message=message, complete= False)
  db.session.add(new_todo)
  db.session.commit()
  return redirect(url_for("home"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
  todo= Todo.query.filter_by(id=todo_id).first()
  todo.complete = not todo.complete
  db.session.commit()
  return redirect(url_for("home"))
  
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
  todo = Todo.query.filter_by(id=todo_id).first()
  db.session.delete(todo)
  db.session.commit()
  return redirect(url_for("home"))
  
  
@app.route('/register', methods=["GET", "POST"])
def register():
  if current_user.is_authenticated:
    redirect(url_for("home"))
  if request.method == "POST":
    username = request.form["name"]
    email = request.form["email"]
    pas = request.form["password"]
    pas2 = request.form["password2"]
    if pas == pas2:
      user = User(username=username, email=email)
      user.set_password(pas)
      db.session.add(user)
      db.session.commit()
      flash('Usuario Cadastrado com Sucesso')
      return redirect(url_for("login"))
    else:
      flash("senha ou email invalido!")
  return render_template("register.html", title="Registro")
  
@app.route('/login', methods=["GET", "POST"])
def login():
  if current_user.is_authenticated:
    return redirect(url_for("home"))
  if request.method == "POST":
    email_form = request.form["email"]
    email = User.query.filter_by(email=email_form).first()
    password = request.form["password"]
    if email is None or not email.check_password(password):
      flash("Senha ou Nome de Usuario Invalido")
      return redirect(url_for("login"))
    login_user(email, remember = request.form.get("remember_me"))
    next_page = request.args.get("next")
    if not next_page or url_parse(next_page).netloc != ' ':
      next_page = url_for("home")
      return redirect(next_page)
  return render_template("login.html", title="Login")

@app.route('/profile')
def perfil():
  return "ola user"
  
@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for("login"))
  
db.create_all()