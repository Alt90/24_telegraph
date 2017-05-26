from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///post.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(200))
    signature = db.Column(db.String(200))
    body = db.Column(db.String(5000))

    def __init__(self, header, signature, body):
        self.header = header
        self.signature = signature
        self.body = body

    def __repr__(self):
        return '{}'.format(self.header)

@app.route('/', methods=['GET', 'POST']))
def form():
    if request.method == 'POST':
        post = Post(request.form['header'], request.form['signature'], request.form['body'])
        db.session.add(post)
        db.session.commit()
    else:
        return render_template('form.html')

if __name__ == "__main__":
    db.create_all()
    app.run()
