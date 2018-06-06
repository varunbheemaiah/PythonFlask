from flask import Flask, render_template, request, redirect

app=Flask(__name__)

@app.route('/home')
def index():
    fruits=['apple','banana','orange']
    return render_template('home.html', fruits=fruits)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=["post","get"])
def login():
    error= None
    if request.method=="POST":
        if request.form['email']!="varunbheemaiah9@gmail.com" or request.form['password']!="donkeykong":
            error="Email or Password incorrect"
        else:
            return redirect("/home")
        return render_template("login.html", error=error)
    return render_template('login.html')

if __name__=='__main__':
    app.jinja_env.globals.update(chr=chr)
    app.run(host="0.0.0.0", port=8000, debug=True, threaded=True)
