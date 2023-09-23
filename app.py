## Flask App Routing

from flask import Flask,render_template,request,redirect,url_for

## create a simple flask application
app=Flask(__name__) #entry point of the program

@app.route("/",methods=["GET"])
def welcome():
    return"<h1>Welcome to my flask demo</h1>"

@app.route("/index",methods=["GET"])
def index():
    return "<h2>Welcome to the index page</h2>"
## Variable rule
@app.route('/success/<score>')
def success(score):
    return "<h3>The person has passed and the score is: </h3>"+ score

@app.route('/fail/<score>')
def fail(score):
    return "<h3>The person has failed and the score is: </h3>"+ score

@app.route('/form', methods=["GET","POST"])
def form():
    if request.method =="GET":
        return render_template("form.html")
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])

        average_marks = (maths+science+history)/3
        res=""
        if average_marks >= 50:
            res = "success"

        else:
            res = "fail"
        
        # return render_template("form.html", score = average_marks)
        return redirect(url_for(res,score=average_marks))


if __name__ == '__main__':
    app.run(debug=True) #if not True,, we have to stop the server incase of code changes
