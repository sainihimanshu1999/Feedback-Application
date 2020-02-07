from flask import Flask, render_template , request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


ENV ='dev'
if ENV== 'dev':
    app.debug = True
    app.congif['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Himanshu9716@localhost/lexus'

else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key = True)
    Customer = db.Column(db.String(200), unique = True)






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

        return render_template('success.html')


if __name__ == '__main__':
    
    app.run()
