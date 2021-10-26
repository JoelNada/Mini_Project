from flask  import Flask, redirect, url_for, render_template

app  = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/Home")
def Home():
	return render_template("home.html");
@app.route("/Pharmacy")
def Pharmacy():
    return render_template("Pharmacy.html");

@app.route("/Login")
def Login():
    return render_template("Login.html");

@app.route("/DoctorLogin")
def DoctorLogin():
    return render_template("DoctorLogin.html");

@app.route("/PatientLogin")
def PatientLogin():
    return render_template("PatientLogin.html");

@app.route("/SignUp")
def SignUp():
    return render_template("SignUp.html");

@app.route("/docregister")
def docregister():
    return render_template("docregister.html");

@app.route("/PatientRegister")
def PatientRegister():
    return render_template("PatientRegister.html");


if __name__ == "__main__":
    app.run(debug=True)
