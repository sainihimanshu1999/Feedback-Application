from flask import Flask, render_template , request
from flask_sqlalchemy import SQLAlchemy
from mail import send_mail

app = Flask(__name__)


ENV ='prod'
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Himanshu9716@localhost/Lexus'

else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://wzeeppwrypfkoe:78dbc27d56afcd7f24cc668709f325860bf54a493647f7a5ad1ebb255e73374d@ec2-184-72-236-57.compute-1.amazonaws.com:5432/dc8qc7tka8aqp0'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    Customer = db.Column(db.String(200), unique=True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, Customer, dealer, rating, comments):
        self.Customer = Customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit' , methods = ['POST'])
def submit():
    if request.method == 'POST':
        Customer  = request.form['Customer']
        
        dealer  = request.form['dealer']
        rating  = request.form['rating']
        comments  = request.form['comments']
        #print(Customer , dealer , rating , comments)
        if Customer == '' or dealer == '' :
            return render_template('index.html' , message = 'Please Enter Required Feilds')

        if db.session.query(Feedback).filter(Feedback.Customer == Customer).count()== 0:
            data = Feedback(Customer , dealer, rating, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(Customer, dealer, rating, comments)
            return render_template('success.html')
        return render_template('index.html' , message = 'You have already submitted')


if __name__ == '__main__':
    
    app.run()
