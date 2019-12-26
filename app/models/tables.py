from app import database

class User(database.Model):
    __tablename__ = "users"

    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, unique=True)
    password = database.Column(database.String)
    name = database.Column(database.String)
    email = database.Column(database.String, unique=True)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.username

class Post(database.Model):
    __tablename__ = "posts"

    id = database.Column(database.Integer, primary_key=True)
    content = database.Column(database.Text)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'))

    user = database.relationship('User', foreign_keys=user_id)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return "<Post %r>" % self.id

class Follow(database.Model):
    __tablename__ = "follow"

    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'))
    follower_id = database.Column(database.Integer, database.ForeignKey('users.id'))

    user = database.relationship('User', foreign_keys=user_id)
    follower = database.relationship('User', foreign_keys=follower_id)