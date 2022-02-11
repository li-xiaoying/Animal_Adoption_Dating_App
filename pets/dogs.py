from flask import Flask, render_template, session
from flask import request, redirect, url_for
from flaskext.mysql import MySQL
import database.db_connector as db
from pets.crud import crud_api
from flask import Blueprint
import base64

dogs_api = Blueprint('dogs_api', __name__)

# Routes
# Adopter protocol
# Adopter browse all dogs
@dogs_api.route('/browse_dogs')
def browse_dogs():
    db_connection = db.db_connection
    query = 'SELECT * FROM Pets WHERE type = "%s";' % ("dog")
    cursor = db.execute_query(db_connection, query)

    allDogslist = cursor.fetchall()

    for pet in allDogslist:
        pet['isLiked'] = False

    AllDogsIdList = [pet['petsID'] for pet in allDogslist]

    # Get all dogs are liked by this customer  
    query = 'SELECT * FROM CustomerLikePet WHERE customerID = "%s" And petsID IN (%s);' % (session['userID'], ",".join(str(elem) for elem in AllDogsIdList))
    cursor = db.execute_query(db_connection, query)
    likedDogResult = cursor.fetchall()

    if likedDogResult:  #if there are dogs are liked by this customer
        for likedPet in likedDogResult:
            for pet in allDogslist: 
                if pet['petsID'] == likedPet['petsID']:
                    pet['isLiked'] = True

    return render_template('browse_dogs.j2', dogs=allDogslist, base64=base64)

# Admin protocol
# Dogs Archive page, show all dogs
@dogs_api.route('/dogs_archive')
def dogs_archive():
    db_connection = db.db_connection
    query = 'SELECT * FROM Pets WHERE type = "%s";' % ("dog")
    cursor = db.execute_query(db_connection, query)
    results = cursor.fetchall()
    return render_template('dogs_archive.j2', dogs=results, base64=base64)

# Delete dog, give id is petsID in Pets table
@dogs_api.route('/admin_delete_dog/<int:id>')
def delete_dog(id):
   db_connection = db.db_connection

   # Delete selected dog
   query = "DELETE FROM Pets WHERE petsID=%d;" % (id)
   db.execute_query(db_connection, query)

   # Show updated all dogs information
   query = 'SELECT * FROM Pets WHERE type = "%s";' % ("dog")
   cursor = db.execute_query(db_connection, query)
   results = cursor.fetchall()
   return redirect(url_for('dogs_api.dogs_archive'))