## Jinja 2 template
## variable rule
## dynamic url

from flask import Flask,render_template,request
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# @app.route('/form',methods=['GET','POST'])
# def form():
#     if request.method=='POST':
#         name=request.form['name']
#         return f'Hello {name}!'
#     return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route("/success/<int:score>")
def success(score):
    # return "The marks you got is "+str(score)
    res = ''
    if score>=50:
        res='Pass'
    else:
        res="Fail"
    return render_template("result_try.html",results=res)





if __name__=="__main__":
    app.run(debug=True)