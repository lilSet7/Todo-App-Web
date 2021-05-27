from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login
 
class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(40), index=True, unique=True)
  email = db.Column(db.String(40), index=True, unique=True)
  password_hash = db.Column(db.String(128))
  todo = db.relationship("Todo", backref='autho', lazy="dynamic")
  
  
  def set_password(self, password):
    self.password_hash = generate_password_hash(password)
    
  def check_password(self, password):
    return check_password_hash(self.password_hash, password)
  
class Todo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(20))
  message = db.Column(db.String(100))
  complete = db.Column(db.Boolean)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  
  @login.user_loader
  def load_user(id):
    return User.query.get(int(id))