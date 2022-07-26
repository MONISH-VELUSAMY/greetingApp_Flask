from flask import *
app=Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route('/hello')
def index():
    flash('Hi,What is your name?')
    return render_template('index.html')



@app.route('/greet',methods=['GET','POST'])
def greet():
    flash("Hi, "+str(request.form['nm'])+" ,great to see you!!!")
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)