from flask import Flask, render_template, session
from flask import request, redirect, url_for
from flaskext.mysql import MySQL
import os
import database.db_connector as db
import base64
from pets.dogs import dogs_api
from pets.cats import cats_api
from pets.others import others_api
from pets.crud import crud_api

# Configuration
app = Flask(__name__)
app.secret_key = 'your secret key'

# Improt dogs.py
app.register_blueprint(dogs_api)

# Improt cats.py
app.register_blueprint(cats_api)

# Improt others.py
app.register_blueprint(others_api)

# Improt crud.py
app.register_blueprint(crud_api)


# Routes
# Landing page
@app.route('/')
def root():
    return render_template('landing_page.j2')

# Adopter home page
@app.route('/adopter_home')
def adpoter_home():
    # Check is user is logged in
    if 'adopter_loggedin' in session:
        # List the newly added pets (4)
        db_connection = db.db_connection
        query = 'SELECT * FROM Pets ORDER BY date DESC LIMIT 4;'
        cursor = db.execute_query(db_connection, query)
        results = cursor.fetchall()
        return render_template('adopter_home.j2', userID=session['userID'], pets=results, base64=base64)
    # User is not logged in
    return render_template('adopter_login.j2') 

# Shelter home page
@app.route('/shelter_home')
def shelter_home():
    # Check is user is logged in
    if 'shelter_loggedin' in session:
        return render_template('shelter_home.j2', userID=session['userID'])
    # User is not logged in
    return render_template('shelter_login.j2') 

# Shelter log in page
@app.route('/shelter_login', methods=['GET', 'POST'])
def shelter_login():
    if request.method == 'GET':
        return render_template('shelter_login.j2')
    elif request.method == 'POST':
        db_connection = db.db_connection
        # Check if account exists 
        query = 'SELECT * FROM Customers WHERE email = %s AND password = %s'
        email = request.form['email']
        psw = request.form['password']
        data = (email, psw)
        cursor = db.execute_query(db_connection, query, data)
        results = cursor.fetchall()
        if results:
            # Successful loggedin
            session['username'] = email
            if email == 'admin@oregonstate.edu': #If user is admin
                session['shelter_loggedin'] = True
                session['userID'] = results[0]["customerID"]
                return redirect(url_for('shelter_home', variable=session['userID']))
            else: # If user is regular customer
                return render_template('shelter_login_error.j2')
        else:
            cursor.close()
            # Account does not exist or username/password incorrect
            return render_template('shelter_login_error.j2')

# Admin: Shelter message page
@app.route('/shelter_message', methods=['GET', 'POST'])
def shelter_mess():
    db_connection = db.db_connection
    if request.method == 'GET':
        query = 'SELECT * FROM AdminMsg'
        cursor = db.execute_query(db_connection, query)
        results = cursor.fetchall()
        return render_template('shelter_message.j2', messages = results)
    elif request.method == 'POST':
        msgID = request.form['messageID']
        petID = request.form['petID']   
        if request.form["action_identifier"] == "Approve":  # Admin approve adopter request, and change pet's status to adopted
            query = "UPDATE AdminMsg SET status='approved' WHERE adminMsgID=%s;" % (msgID)
            db.execute_query(db.db_connection, query)
            query = "UPDATE Pets SET availability='adopted' WHERE petsID=%s;" % (petID)
            db.execute_query(db.db_connection, query)
        elif request.form["action_identifier"] == "Ignore": # Admin ignore adopter request, and change pet's status to available
            query = "UPDATE AdminMsg SET status='ignored' WHERE adminMsgID=%s;" % (msgID)
            db.execute_query(db.db_connection, query)
            query = "UPDATE Pets SET availability='available' WHERE petsID=%s;" % (petID)
            db.execute_query(db.db_connection, query)
        query = 'SELECT * FROM AdminMsg'
        cursor = db.execute_query(db_connection, query)
        results = cursor.fetchall()
        return render_template('shelter_message.j2', messages=results, msgID=msgID)

# Adopter log in page
@app.route('/adopter_login', methods=['GET', 'POST'])
def adopter_login():
    if request.method == 'GET':
        return render_template('adopter_login.j2')
    elif request.method == 'POST':
        db_connection = db.db_connection
        # Check if account exists 
        query = 'SELECT * FROM Customers WHERE email = %s AND password = %s'
        email = request.form['email']
        psw = request.form['password']
        data = (email, psw)
        cursor = db.execute_query(db_connection, query, data)
        results = cursor.fetchall()
        if results:
            # Successful loggedin
            session['username'] = email
            session['userID'] = results[0]["customerID"]
            if email == 'admin@oregonstate.edu': # If user is admin
                return render_template('adopter_login_error.j2')
            else: # If user is regular customer
                session['adopter_loggedin'] = True
                return redirect(url_for('adpoter_home', variable=session['userID']))
        else:
            # Account does not exist or username/password incorrect
            return render_template('adopter_login_error.j2')

# Log out
@app.route('/logout')
def logout():
    # Remove session data
    session.pop('shelter_loggedin', None)
    session.pop('adopter_loggedin', None)
    session.pop('username', None)
    session.pop('userID', None)
    return redirect(url_for('root'))

# Sign up page
@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup_page.j2')
    elif request.method == 'POST':
        db_connection = db.db_connection
        query = 'SELECT * FROM Customers WHERE email = %s'
        email = request.form['email']
        data = (email)
        cursor = db.execute_query(db_connection, query, data)
        results = cursor.fetchall()
        # Check if account exists using MySQL
        if results:
            return render_template('user_already_exists_page.j2')
        else:
            query = 'INSERT INTO Customers(email, password) VALUES (%s, %s)'
            email = request.form['email']
            psw = request.form['psw']
            data = (email, psw)
            db.execute_query(db_connection, query, data)
            return redirect(url_for('adopter_login'))

# Profile page
@app.route('/profile/<int:id>', methods=['GET','POST'])
def profile(id):
    user_id = id
    db_connection = db.db_connection
    if request.method == 'GET':
        query = 'SELECT * FROM Customers WHERE customerID=%d;' % (id)
        cursor = db.execute_query(db_connection, query)
        results = cursor.fetchall()
        cursor.close()
        return render_template('profile_page.j2', users=results, value=user_id)
    elif request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['phone']
        email = request.form['email']
        query = "UPDATE Customers SET firstName='%s', lastName='%s', customerPhone='%s', email='%s' WHERE customerID=%d;" % (fname, lname, phone, email, user_id)
        db.execute_query(db_connection, query)
        return redirect(url_for('adpoter_home', variable=user_id))

# Find your pet page, move to crud.py
# @app.route('/admin_find_your_pet', methods=['GET', 'POST'])
# def admin_find_your_pet():
#     return render_template('admin_find_your_pet.j2')

@app.route('/customer_find_your_pet', methods=['GET', 'POST'])
def customer_find_your_pet():
    return render_template('customer_find_your_pet.j2')

# Other pet page
@app.route('/admin_others', methods=['GET', 'POST'])
def admin_others():
    return render_template('admin_others.j2')


@app.route('/admin_add_new_pet_result', methods=['GET', 'POST'])
def admin_add_new_pet_result():
    return render_template('admin_add_new_pet_result.j2')


#Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 1234))
    app.run(port=port, debug=True, host='0.0.0.0')
