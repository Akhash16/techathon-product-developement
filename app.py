from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/')
def main_page():
    return render_template("")

@app.route("/login")
def login():
    return render_template("")

@app.route("/signup")
def signup():
    return render_template("")

@app.route("/qa")
def signup():
    


if __name__ == '__main__':
    app.run(port=5000,debug=True)