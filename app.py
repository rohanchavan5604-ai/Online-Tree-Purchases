from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "nursery_secret_key"

# ---------------- DATABASE ----------------
def db():
    return sqlite3.connect("database.db")

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("home.html")

# ---------------- CATEGORY ----------------
@app.route("/category")
def category():
    return render_template("category.html")

# ---------------- PLANTS ----------------
@app.route("/plants/<category>")
def plants(category):
    con = db()
    cur = con.cursor()
    cur.execute("SELECT * FROM plants WHERE category=?", (category,))
    data = cur.fetchall()
    con.close()
    return render_template("plants.html", plants=data, category=category)

# ---------------- PLANT DETAIL ----------------
@app.route("/plant/<int:id>")
def plant_detail(id):
    con = db()
    cur = con.cursor()
    cur.execute("SELECT * FROM plants WHERE id=?", (id,))
    plant = cur.fetchone()
    con.close()
    return render_template("plant_detail.html", plant=plant)

# ================= USER AUTH =================

@app.route("/user_login", methods=["GET", "POST"])
def user_login():
    error = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        con = db()
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cur.fetchone()
        con.close()

        if user:
            session.clear()                # VERY IMPORTANT
            session["user"] = username     # SAVE LOGIN
            return redirect("/")
        else:
            error = "Invalid username or password"

    return render_template("user_login.html", error=error)


# -------- USER REGISTER --------
@app.route("/register", methods=["GET", "POST"])
def register():
    msg = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        try:
            con = db()
            cur = con.cursor()
            cur.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, password))
            con.commit()
            con.close()
            return redirect("/user_login")
        except:
            msg = "Username already exists!"

    return render_template("register.html", msg=msg)




# -------- USER LOGOUT --------
@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("admin", None)
    return redirect("/")

# ================= BOOKING =================

@app.route("/book/<int:id>", methods=["GET", "POST"])
def book(id):
    # USER MUST LOGIN BEFORE BOOKING
    if not session.get("user"):
        return redirect("/user_login")

    con = db()
    cur = con.cursor()
    cur.execute("SELECT * FROM plants WHERE id=?", (id,))
    plant = cur.fetchone()

    if request.method == "POST":
        phone = request.form["phone"]
        address = request.form["address"]
        quantity = int(request.form["quantity"])
        date = request.form["date"]
        time = request.form["time"]

        total_price = quantity * plant[3]

        cur.execute("""
            INSERT INTO bookings
            (plant_name, user_name, phone, address, quantity, total_price, date, time)
            VALUES (?,?,?,?,?,?,?,?)
        """, (plant[2], session["user"], phone, address, quantity, total_price, date, time))

        con.commit()
        con.close()
        return redirect("/booking-success")

    return render_template("booking.html", plant=plant)

# -------- SUCCESS PAGE --------
@app.route("/booking-success")
def booking_success():
    return render_template("booking_success.html")

# ================= ADMIN AUTH =================

ADMIN_USER = "aniketjadhav"
ADMIN_PASS = "aniket@123"

@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    error = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == ADMIN_USER and password == ADMIN_PASS:
            session["admin"] = True
            return redirect("/admin")
        else:
            error = "Invalid admin credentials"

    return render_template("admin_login.html", error=error)

@app.route("/admin")
def admin():
    if not session.get("admin"):
        return redirect("/admin-login")

    con = db()
    cur = con.cursor()
    cur.execute("SELECT * FROM bookings")
    bookings = cur.fetchall()
    con.close()
    return render_template("admin.html", bookings=bookings)

# ---------------- CONTACT ----------------
@app.route("/contact")
def contact():
    return render_template("contact.html")

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
