from flask import Flask, render_template, session
from flask import request, redirect, url_for
from flaskext.mysql import MySQL
import database.db_connector as db
from pets.crud import crud_api
from flask import Blueprint
import base64

cats_api = Blueprint('cats_api', __name__)

# Routes
# Adopter protocol
# Adopter browse all cats
@cats_api.route('/browse_cats')
def browse_cats():
    db_connection = db.db_connection
    query = 'SELECT * FROM Pets WHERE type = "%s";' % ("cat")
    cursor = db.execute_query(db_connection, query)

    allCatslist = cursor.fetchall()

    for pet in allCatslist:
        pet['isLiked'] = False

    AllCatsIdList = [pet['petsID'] for pet in allCatslist]

    # Get all cats are liked by this customer  
    query = 'SELECT * FROM CustomerLikePet WHERE customerID = "%s" And petsID IN (%s);' % (session['userID'], ",".join(str(elem) for elem in AllCatsIdList))
    cursor = db.execute_query(db_connection, query)
    likedCatResult = cursor.fetchall()

    if likedCatResult:  #if there are cats are liked by this customer
        # print("likedCatResult: ", likedCatResult) # petId, customerId
        for likedPet in likedCatResult:
            for pet in allCatslist: 
                if pet['petsID'] == likedPet['petsID']:
                    pet['isLiked'] = True

    return render_template('browse_cats.j2', cats=allCatslist, base64=base64)

# Admin protocol
# Cats Archive page, show all cats
@cats_api.route('/cats_archive')
def cats_archive():
    db_connection = db.db_connection
    query = 'SELECT * FROM Pets WHERE type = "%s";' % ("cat")
    cursor = db.execute_query(db_connection, query)
    results = cursor.fetchall()
    return render_template('cats_archive.j2', cats=results, base64=base64)

# Delete cat, give id is petsID in Pets table
@cats_api.route('/admin_delete_cat/<int:id>')
def delete_cat(id):
   db_connection = db.db_connection

   # Delete selected cat
   query = "DELETE FROM Pets WHERE petsID=%d;" % (id)
   db.execute_query(db_connection, query)

   # Show updated all cats information
   query = 'SELECT * FROM Pets WHERE type = "%s";' % ("cat")
   cursor = db.execute_query(db_connection, query)
   results = cursor.fetchall()
   return redirect(url_for('cats_api.cats_archive'))