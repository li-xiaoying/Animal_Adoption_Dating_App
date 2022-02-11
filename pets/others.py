from flask import Flask, render_template, session
from flask import request, redirect, url_for
from flaskext.mysql import MySQL
import database.db_connector as db
from pets.crud import crud_api
from flask import Blueprint
import base64

others_api = Blueprint('others_api', __name__)


# Routes
# Adopter protocol
# Adopter browse all other pets.
@others_api.route('/browse_others')
def browse_others():
    
    db_connection = db.db_connection
    query = 'SELECT * FROM Pets WHERE type = "%s";' % ("others")
    cursor = db.execute_query(db_connection, query)
    allOtherPetlist = cursor.fetchall()

    for pet in allOtherPetlist:
        pet['isLiked'] = False

    AllOtherPetsIdList = [pet['petsID'] for pet in allOtherPetlist]

    # Get all other type of pet is liked by this customer  
    query = 'SELECT * FROM CustomerLikePet WHERE customerID = "%s" And petsID IN (%s);' % (session['userID'], ",".join(str(elem) for elem in AllOtherPetsIdList))
    cursor = db.execute_query(db_connection, query)
    likedOtherPetResult = cursor.fetchall()

    if likedOtherPetResult:  #if there is other type of pet is liked by this customer
        # print("likedOtherPetResult: ", likedOtherPetResult) # petId, customerId
        for likedPet in likedOtherPetResult:
            for pet in allOtherPetlist: 
                if pet['petsID'] == likedPet['petsID']:
                    pet['isLiked'] = True

    return render_template('browse_others.j2', others=allOtherPetlist,base64=base64)
   

    # return render_template('browse_others.j2', others=results, base64=base64)



# Admin protocol
#Other pets Archive page, show all other pets.
@others_api.route('/others_archive')
def others_archive():
    db_connection = db.db_connection
    query = 'SELECT * FROM Pets WHERE type = "%s";' % ("others")
    cursor = db.execute_query(db_connection, query)
    results = cursor.fetchall()
    return render_template('others_archive.j2', others=results, base64=base64)


# Delete selected pet, given id is petsID in Pets table
@others_api.route('/admin_delete_other/<int:id>')
def delete_other(id):
   db_connection = db.db_connection

   # Delete selected pet
   query = "DELETE FROM Pets WHERE petsID=%d;" % (id)
   db.execute_query(db_connection, query)

   # Show updated other pets information
   query = 'SELECT * FROM Pets WHERE type = "%s";' % ("others")
   cursor = db.execute_query(db_connection, query)
   results = cursor.fetchall()
   return redirect(url_for('others_api.others_archive'))



