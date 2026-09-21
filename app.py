from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stud.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# -------- DATABASE --------
class Stud(db.Model):
    email = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100), nullable=False)

# -------- ROUTES --------

@app.route("/")
def home():
    return render_template("logn.html")

# LOGIN API
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    roll = data.get("roll")
    password = data.get("password")

    user = Stud.query.filter_by(email=roll, password=password).first()

    if user:
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "fail"})

@app.route("/chat")
def chat():
    return render_template("indexx.html")

# CHATBOT API
@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.json
    msg = data['message'].lower()

    if "exam" in msg:
        reply = "Exams are conducted at the end of each semester."
    elif "syllabus" in msg:
        reply = "The syllabus is available on the university website."

    elif "training" in msg:
        reply = "Industrial training gives practical exposure."
    elif "attendance" in msg:
        reply = "Students should maintain at least 75% attendance."
    else:
        reply = "Please ask questions related to academics."
    

    return jsonify({"reply": reply})

@app.route("/notice")
def notice():
    return render_template("notice.html")


# -------- RUN --------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
        # Check if user already exists before adding
        existing_user = Stud.query.filter_by(email="12345").first()
        
        if not existing_user:
            user = Stud(email="12345", password="admin")
            db.session.add(user)
            db.session.commit()
            print("Test user created!")
        else:
            print("User '12345' already exists in the database.")

    app.run(debug=True)