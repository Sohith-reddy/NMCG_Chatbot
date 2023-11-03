from flask import Flask,render_template,redirect,url_for,flash,jsonify
from datetime import timedelta
import sqlalchemy
app=Flask(__name__)
app.secret_key="Team-NMCG"
app.permanent_session_lifetime=timedelta(days=15)
visitor_count=0
@app.route('/',methods=['POST','GET'])
@app.route('/home',methods=['POST','GET'])
def home():
    global visitor_count
    visitor_count += 1 
    return render_template('mainindex.html', visitor_count=visitor_count)
@app.route("/login", methods = ['POST','GET'])
def login():
    return render_template('login.html')
@app.route('/about/action',methods=['POST','GET'])
def about_action():
    return render_template('mainbase.html')
@app.route('/about/anotheraction',methods=['POST','GET'])
def about_another_action():
    return render_template('mainbase.html')
@app.route('/about/something',methods=['POST','GET'])
def about_something():
    return render_template('mainbase.html')
@app.route('/divisions/action',methods=['POST','GET'])
def divisions_action():
    return render_template('mainbase.html')
@app.route('/divisions/anotheraction',methods=['POST','GET'])
def divisions_another_action():
    return render_template('mainbase.html')
@app.route('/divisions/something',methods=['POST','GET'])
def divisions_something():
    return render_template('mainbase.html')
@app.route('/chatbot',methods=['POST','GET'])
def chatbot():
    return render_template('mainbase.html')
@app.route('/chatbot/main',methods=['POST','GET'])
def chatbot_main():
    return render_template('mainbase.html')
@app.route('/chatbot/queries',methods=['POST','GET'])
def chatbot_queries():
    return render_template('mainbase.html')
@app.route('/chatbot/feedback',methods=['POST','GET'])
def chatbot_feedback():
    return render_template('mainbase.html')

@app.route('/signup',methods=['POST','GET'])
def signup():
    return render_template('signup.html')

@app.route('/accounts',methods=['POST','GET'])
def social_accounts():
    return render_template('mainbase.html')

@app.route('/trail',methods=['POST','GET'])
def trial():
    return render_template('chatbot.html')

if __name__=='__main__':
    app.run(debug=True,port=8000)
