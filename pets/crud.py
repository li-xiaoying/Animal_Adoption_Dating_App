from flask import Flask, render_template, session
from flask import request, redirect, url_for
from flask import jsonify
from flaskext.mysql import MySQL
from flask import Blueprint
import database.db_connector as db
import base64


# import tkinter as tk
# import tkinter.messagebox

# import time    


import os  #debug

crud_api = Blueprint('crud_api', __name__)

# Routes
# Admin protocol
# Admin add new pet page
@crud_api.route('/admin_new_pets', methods=['GET', 'POST'])
def admin_new_pets():
   if request.method == 'GET':
        return render_template('admin_new_pets.j2')
   elif request.method == 'POST':
      # print(request.json);
      # print(request.form);
        db_connection = db.db_connection
        query = 'INSERT INTO Pets(type, name, img, breed, age, size, gender, goodWithKids, goodWithDogs, goodWithCats, mustBeLeashed, availability) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        type = request.form['type']
        name = request.form['name']
        img = request.files['img'].read()
        breed = request.form['breed']
        age = request.form['age']
        size = request.form['size']
        gender = request.form['gender']
        goodWithKids = request.form['goodWithKids']
        goodWithDogs = request.form['goodWithDogs']
        goodWithCats = request.form['goodWithCats']
        mustBeLeashed = request.form['mustBeLeashed']
        availability = request.form['availability']
        data = (type, name, img, breed, age, size, gender, goodWithKids, goodWithDogs, goodWithCats, mustBeLeashed, availability)
        cursor = db.execute_query(db.db_connection, query, data)



      #   def show_warning(msg):    
      #      top = tkinter.Tk()    
      #      top.withdraw()    
      #      top.update()    
      #      tk.messagebox.showwarning("title", msg)    
      #      top.destroy()

      #   if __name__ == '__main__':    
      #      show_warning('example')

      #      print("Printed immediately.")
      #      time.sleep(2.4)
      #      print("Printed after 2.4 seconds.")

        return redirect("%s%s" % ("admin_view_details/", cursor.lastrowid))
               #   return render_template('admin_add_new_pet_result.j2', newPet=results, base64=base64)
               #   print(cursor.lastrowid)
               #   return jsonify("success")      
      #   return redirect(url_for('admin_add_new_pet_result'))


# Admin find a dog page
@crud_api.route('/admin_find_a_dog', methods=['GET', 'POST'])
def admin_find_a_dog():

   # get all existing dog's breeds from database
   if request.method == 'GET':
      db_connection = db.db_connection
      query = 'SELECT breed FROM Pets WHERE type = "%s"' % ("dog")
      cursor = db.execute_query(db_connection, query)
      results = cursor.fetchall()
       
      breeds = [result['breed'] for result in results]
      # print("query result: %s" % breeds)
      return render_template('admin_find_a_dog.j2', breeds = breeds)

   elif request.method == 'POST':
        db_connection = db.db_connection

        base_query = 'SELECT * FROM Pets WHERE type = "%s"' % ("dog")

      #   if request.form['name'].strip():  #check the name, todo
      #      base_query = base_query + ' AND name LIKE "% + request.form['name'].strip() + %" '


        if request.form['name'].strip():  #check the name
           base_query = base_query + ' AND name =  "%s" ' % request.form['name'].strip()

        if request.form['breed'].strip(): #check the breed
           base_query = base_query + ' AND breed =  "%s" ' % request.form['breed'].strip()

        if request.form['age'].strip(): #check the age
           base_query = base_query + ' AND age =  %s ' % ((request.form['age']))
        
        if request.form['size'].strip(): #check the size
           base_query = base_query + ' AND size =  "%s" ' % (request.form['size'].strip())
        
        if request.form['gender'].strip(): #check the gender
           base_query = base_query + ' AND gender =  "%s" ' % (request.form['gender'].strip())
        
        if request.form['goodWithKids'].strip(): #check if good with kids
           base_query = base_query + ' AND goodWithKids =  %s ' % (request.form['goodWithKids'].strip())
        
        if request.form['goodWithDogs'].strip(): #check the good with dogs
           base_query = base_query + ' AND goodWithDogs =  %s ' % (request.form['goodWithDogs'].strip())
        
        if request.form['goodWithCats'].strip(): #check if good with cats
           base_query = base_query + ' AND goodWithCats =  %s ' % (request.form['goodWithCats'].strip())

        if request.form['mustBeLeashed'].strip(): #check if must be leashed
           base_query = base_query + ' AND mustBeLeashed =  %s ' % (request.form['mustBeLeashed'].strip())
          
        if request.form['availability'].strip(): #check if availability
           base_query = base_query + ' AND availability =  "%s" ' % (request.form['availability'].strip())

        base_query + ";"
        cursor = db.execute_query(db_connection, base_query)
        results = cursor.fetchall()
        return render_template('admin_detailed_find_your_dog.j2', dogs=results, base64=base64)

# Admin find a cat page
@crud_api.route('/admin_find_a_cat', methods=['GET', 'POST'])
def admin_find_a_cat():

   # Get all existing cat's breeds from database
   if request.method == 'GET':
      db_connection = db.db_connection
      query = 'SELECT breed FROM Pets WHERE type = "%s"' % ("cat")
      cursor = db.execute_query(db_connection, query)
      results = cursor.fetchall()
       
      breeds = [result['breed'] for result in results]
      # print("query result: %s" % breeds)
      return render_template('admin_find_a_cat.j2', breeds = breeds)

   elif request.method == 'POST':
        db_connection = db.db_connection

        base_query = 'SELECT * FROM Pets WHERE type = "%s"' % ("cat")

      #   if request.form['name'].strip():  #check the name, todo
      #      base_query = base_query + ' AND name LIKE "% + request.form['name'].strip() + %" '


        if request.form['name'].strip():  #check the name
           base_query = base_query + ' AND name =  "%s" ' % request.form['name'].strip()

        if request.form['breed'].strip(): #check the breed
           base_query = base_query + ' AND breed =  "%s" ' % request.form['breed'].strip()

        if request.form['age'].strip(): #check the age
           base_query = base_query + ' AND age =  %s ' % ((request.form['age']))
        
        if request.form['size'].strip(): #check the size
           base_query = base_query + ' AND size =  "%s" ' % (request.form['size'].strip())
        
        if request.form['gender'].strip(): #check the gender
           base_query = base_query + ' AND gender =  "%s" ' % (request.form['gender'].strip())
        
        if request.form['goodWithKids'].strip(): #check if good with kids
           base_query = base_query + ' AND goodWithKids =  %s ' % (request.form['goodWithKids'].strip())
        
        if request.form['goodWithDogs'].strip(): #check the good with dogs
           base_query = base_query + ' AND goodWithDogs =  %s ' % (request.form['goodWithDogs'].strip())
        
        if request.form['goodWithCats'].strip(): #check if good with cats
           base_query = base_query + ' AND goodWithCats =  %s ' % (request.form['goodWithCats'].strip())

        if request.form['mustBeLeashed'].strip(): #check if must be leashed
           base_query = base_query + ' AND mustBeLeashed =  %s ' % (request.form['mustBeLeashed'].strip())
          
        if request.form['availability'].strip(): #check if availability
           base_query = base_query + ' AND availability =  "%s" ' % (request.form['availability'].strip())

        base_query + ";"
        cursor = db.execute_query(db_connection, base_query)
        results = cursor.fetchall()
        return render_template('admin_detailed_find_your_cat.j2', cats=results, base64=base64)


# Admin find other pet page
@crud_api.route('/admin_find_other_pet', methods=['GET', 'POST'])
def admin_find_other_pet():

   # get all existing cat's breeds from database
   if request.method == 'GET':
      db_connection = db.db_connection
      query = 'SELECT breed FROM Pets WHERE type = "%s"' % ("others")
      cursor = db.execute_query(db_connection, query)
      results = cursor.fetchall()
       
      breeds = [result['breed'] for result in results]
      # print("query result: %s" % breeds)
      return render_template('admin_find_other_pet.j2', breeds = breeds)

   elif request.method == 'POST':
        db_connection = db.db_connection

        base_query = 'SELECT * FROM Pets WHERE type = "%s"' % ("others")

      #   if request.form['name'].strip():  #check the name, todo
      #      base_query = base_query + ' AND name LIKE "% + request.form['name'].strip() + %" '


        if request.form['name'].strip():  #check the name
           base_query = base_query + ' AND name =  "%s" ' % request.form['name'].strip()

        if request.form['breed'].strip(): #check the breed
           base_query = base_query + ' AND breed =  "%s" ' % request.form['breed'].strip()

        if request.form['age'].strip(): #check the age
           base_query = base_query + ' AND age =  %s ' % ((request.form['age']))
        
        if request.form['size'].strip(): #check the size
           base_query = base_query + ' AND size =  "%s" ' % (request.form['size'].strip())
        
        if request.form['gender'].strip(): #check the gender
           base_query = base_query + ' AND gender =  "%s" ' % (request.form['gender'].strip())
        
        if request.form['goodWithKids'].strip(): #check if good with kids
           base_query = base_query + ' AND goodWithKids =  %s ' % (request.form['goodWithKids'].strip())
        
        if request.form['goodWithDogs'].strip(): #check the good with dogs
           base_query = base_query + ' AND goodWithDogs =  %s ' % (request.form['goodWithDogs'].strip())
        
        if request.form['goodWithCats'].strip(): #check if good with cats
           base_query = base_query + ' AND goodWithCats =  %s ' % (request.form['goodWithCats'].strip())

        if request.form['mustBeLeashed'].strip(): #check if must be leashed
           base_query = base_query + ' AND mustBeLeashed =  %s ' % (request.form['mustBeLeashed'].strip())
          
        if request.form['availability'].strip(): #check if availability
           base_query = base_query + ' AND availability =  "%s" ' % (request.form['availability'].strip())

        base_query + ";"
        cursor = db.execute_query(db_connection, base_query)
        results = cursor.fetchall()
        return render_template('admin_detailed_find_other_pet.j2', others=results, base64=base64)


# @crud_api.route('/admin_add_new_pet_result', methods=['GET', 'POST'])
# def admin_add_new_pet_result():
#     return render_template('admin_add_new_pet_result.j2')


# Admin views pets details, give id is petsID in Pets table
@crud_api.route('/admin_view_details/<int:id>')
def view_details(id):
   db_connection = db.db_connection
   query = 'SELECT * FROM Pets WHERE petsID = %d;' % (id)
   cursor = db.execute_query(db_connection, query)
   results = cursor.fetchall()
   return render_template('admin_view_details.j2', dogs=results, base64=base64)

# Admin updates pets details, give id is petsID in Pets table
@crud_api.route('/admin_update_details/<int:id>', methods=['POST', 'GET'])
def update_details(id):
   petsID = id
   db_connection = db.db_connection
   query = 'SELECT * FROM Pets WHERE petsID = %d;' % (id)
   cursor = db.execute_query(db_connection, query)
   results = cursor.fetchall()
   if request.method == 'GET':
      return render_template('admin_update_pets.j2', dogs=results, value=petsID)
   elif request.method == 'POST':
      type = request.form['type']
      name = request.form['name']
      breed = request.form['breed']
      age = request.form['age']
      size = request.form['size']
      gender = request.form['gender']
      goodWithKids = request.form['goodWithKids']
      goodWithDogs = request.form['goodWithDogs']
      goodWithCats = request.form['goodWithCats']
      mustBeLeashed = request.form['mustBeLeashed']
      availability = request.form['availability']
      query = "UPDATE Pets SET type='%s', name='%s', breed='%s', age='%s', size='%s', gender='%s', goodWithKids='%s', goodWithDogs='%s', goodWithCats='%s', mustBeLeashed='%s', availability='%s' WHERE petsID=%d;" % (type, name, breed, age, size, gender, goodWithKids, goodWithDogs, goodWithCats, mustBeLeashed, availability, petsID)
      db.execute_query(db.db_connection, query)
      query = 'SELECT * FROM Pets WHERE petsID = %d;' % (petsID)
      cursor = db.execute_query(db_connection, query)
      results = cursor.fetchall()
      return render_template('admin_view_details.j2', dogs=results, base64=base64)

# Admin views adopter details, give parameter is customer email
@crud_api.route('/admin_view_adopter/<string:email>')
def view_adopter(email):
   db_connection = db.db_connection
   query = 'SELECT * FROM Customers WHERE email = %s'
   data = (email)
   cursor = db.execute_query(db_connection, query, data)
   results = cursor.fetchall()
   return render_template('admin_view_adopter.j2', adopters=results)

# Adopter protocol
# Adopter browse pet details, give id is petsID
@crud_api.route('/browse_details/<int:id>', methods=['POST', 'GET'])
def browse_detail(id):
   db_connection = db.db_connection
   if request.method == 'GET':
      query = 'SELECT * FROM Pets WHERE petsID = %d;' % (id)
      cursor = db.execute_query(db_connection, query)
      results = cursor.fetchall()


      for pet in results:
        pet['isLiked'] = False

    # check if this pet is liked by this customer  
      query = 'SELECT * FROM CustomerLikePet WHERE customerID = "%s" And petsID = "%s";' % (session['userID'],id)
      cursor = db.execute_query(db_connection, query)
      likedPetResult = cursor.fetchall()

      if likedPetResult:  #if this pet is liked by this customer
         pet['isLiked'] = True
   
      return render_template('customer_browse_details.j2', pets=results, base64=base64)
   elif request.method == 'POST':
      # Customer click "adopt" button, pet becomes "pending"
      query = "UPDATE Pets SET availability='pending' WHERE petsID=%d;" % (id)
      db.execute_query(db.db_connection, query)

      petsID = id
      customerEmail = session['username']
      # First check if row existed IN AdminMsg
      query = 'SELECT * FROM AdminMsg WHERE customerEmail = %s AND petsID=%s'
      data = (customerEmail, petsID)
      cursor = db.execute_query(db_connection, query, data)
      results = cursor.fetchall()
      if results:
         # Update corresponding message
         query = 'UPDATE AdminMsg SET status="pending" WHERE customerEmail = %s AND petsID=%s'
         data = (customerEmail, petsID)
         cursor = db.execute_query(db_connection, query, data)
      else:   
         # Send message to AdminMsg table
         query = 'INSERT IGNORE INTO AdminMsg(petsID, customerEmail, status) VALUES (%s, %s, %s)'
         status = "pending"
         data = (petsID, customerEmail, status)
         cursor = db.execute_query(db_connection, query, data)
      return render_template('customer_request_ok.j2', userID=session['userID'])







      
# Adopter find a dog page
@crud_api.route('/adopter_find_a_dog', methods=['GET', 'POST'])
def adopter_find_a_dog():

   # Get all existing dog's breeds from database
   if request.method == 'GET':
      db_connection = db.db_connection
      query = 'SELECT breed FROM Pets WHERE type = "%s"' % ("dog")
      cursor = db.execute_query(db_connection, query)
      results = cursor.fetchall()
       
      breeds = [result['breed'] for result in results]
      # print("query result: %s" % breeds)
      return render_template('adopter_find_a_dog.j2', breeds = breeds)

   elif request.method == 'POST':
        db_connection = db.db_connection

        base_query = 'SELECT * FROM Pets WHERE type = "%s"' % ("dog")

      #   if request.form['name'].strip():  #check the name, todo
      #      base_query = base_query + ' AND name LIKE "% + request.form['name'].strip() + %" '


        if request.form['name'].strip():  #check the name
           base_query = base_query + ' AND name =  "%s" ' % request.form['name'].strip()

        if request.form['breed'].strip(): #check the breed
           base_query = base_query + ' AND breed =  "%s" ' % request.form['breed'].strip()

        if request.form['age'].strip(): #check the age
           base_query = base_query + ' AND age =  %s ' % ((request.form['age']))
        
        if request.form['size'].strip(): #check the size
           base_query = base_query + ' AND size =  "%s" ' % (request.form['size'].strip())
        
        if request.form['gender'].strip(): #check the gender
           base_query = base_query + ' AND gender =  "%s" ' % (request.form['gender'].strip())
        
        if request.form['goodWithKids'].strip(): #check if good with kids
           base_query = base_query + ' AND goodWithKids =  %s ' % (request.form['goodWithKids'].strip())
        
        if request.form['goodWithDogs'].strip(): #check the good with dogs
           base_query = base_query + ' AND goodWithDogs =  %s ' % (request.form['goodWithDogs'].strip())
        
        if request.form['goodWithCats'].strip(): #check if good with cats
           base_query = base_query + ' AND goodWithCats =  %s ' % (request.form['goodWithCats'].strip())

        if request.form['mustBeLeashed'].strip(): #check if must be leashed
           base_query = base_query + ' AND mustBeLeashed =  %s ' % (request.form['mustBeLeashed'].strip())
          
        if request.form['availability'].strip(): #check if availability
           base_query = base_query + ' AND availability =  "%s" ' % (request.form['availability'].strip())

        base_query + ";"
        cursor = db.execute_query(db_connection, base_query)
        results = cursor.fetchall()

        if results:
 
           for pet in results:
             pet['isLiked'] = False

           AllPetsIdList = [pet['petsID'] for pet in results]

               # Get all pet is liked by this customer  
           query = 'SELECT * FROM CustomerLikePet WHERE customerID = "%s" And petsID IN (%s);' % (session['userID'], ",".join(str(elem) for elem in AllPetsIdList))
           cursor = db.execute_query(db_connection, query)
           likedPetResult = cursor.fetchall()

           if likedPetResult:  #if there are pets is liked by this customer
                  # print("likedOtherPetResult: ", likedOtherPetResult) # petId, customerId
              for likedPet in likedPetResult:
                    for pet in results: 
                       if pet['petsID'] == likedPet['petsID']:
                          pet['isLiked'] = True

           return render_template('adopter_detailed_find_your_dog.j2', dogs=results, base64=base64)
        else:
           return render_template('customer_find_a_pet_empty.j2')


# Adopter find a cat page
@crud_api.route('/adopter_find_a_cat', methods=['GET', 'POST'])
def adopter_find_a_cat():

   # Get all existing dog's breeds from database
   if request.method == 'GET':
      db_connection = db.db_connection
      query = 'SELECT breed FROM Pets WHERE type = "%s"' % ("cat")
      cursor = db.execute_query(db_connection, query)
      results = cursor.fetchall()
       
      breeds = [result['breed'] for result in results]
      # print("query result: %s" % breeds)
      return render_template('adopter_find_a_cat.j2', breeds = breeds)

   elif request.method == 'POST':
        db_connection = db.db_connection

        base_query = 'SELECT * FROM Pets WHERE type = "%s"' % ("cat")

      #   if request.form['name'].strip():  #check the name, todo
      #      base_query = base_query + ' AND name LIKE "% + request.form['name'].strip() + %" '


        if request.form['name'].strip():  #check the name
           base_query = base_query + ' AND name =  "%s" ' % request.form['name'].strip()

        if request.form['breed'].strip(): #check the breed
           base_query = base_query + ' AND breed =  "%s" ' % request.form['breed'].strip()

        if request.form['age'].strip(): #check the age
           base_query = base_query + ' AND age =  %s ' % ((request.form['age']))
        
        if request.form['size'].strip(): #check the size
           base_query = base_query + ' AND size =  "%s" ' % (request.form['size'].strip())
        
        if request.form['gender'].strip(): #check the gender
           base_query = base_query + ' AND gender =  "%s" ' % (request.form['gender'].strip())
        
        if request.form['goodWithKids'].strip(): #check if good with kids
           base_query = base_query + ' AND goodWithKids =  %s ' % (request.form['goodWithKids'].strip())
        
        if request.form['goodWithDogs'].strip(): #check the good with dogs
           base_query = base_query + ' AND goodWithDogs =  %s ' % (request.form['goodWithDogs'].strip())
        
        if request.form['goodWithCats'].strip(): #check if good with cats
           base_query = base_query + ' AND goodWithCats =  %s ' % (request.form['goodWithCats'].strip())

        if request.form['mustBeLeashed'].strip(): #check if must be leashed
           base_query = base_query + ' AND mustBeLeashed =  %s ' % (request.form['mustBeLeashed'].strip())
          
        if request.form['availability'].strip(): #check if availability
           base_query = base_query + ' AND availability =  "%s" ' % (request.form['availability'].strip())

        base_query + ";"
        cursor = db.execute_query(db_connection, base_query)
        results = cursor.fetchall()

        if results:
 
           for pet in results:
             pet['isLiked'] = False

           AllPetsIdList = [pet['petsID'] for pet in results]

               # Get all pet is liked by this customer  
           query = 'SELECT * FROM CustomerLikePet WHERE customerID = "%s" And petsID IN (%s);' % (session['userID'], ",".join(str(elem) for elem in AllPetsIdList))
           cursor = db.execute_query(db_connection, query)
           likedPetResult = cursor.fetchall()

           if likedPetResult:  #if there are pets is liked by this customer
                  # print("likedOtherPetResult: ", likedOtherPetResult) # petId, customerId
              for likedPet in likedPetResult:
                    for pet in results: 
                       if pet['petsID'] == likedPet['petsID']:
                          pet['isLiked'] = True

           return render_template('adopter_detailed_find_your_cat.j2', cats=results, base64=base64)
        else:
           return render_template('customer_find_a_pet_empty.j2')

# Adopter find other pet page
@crud_api.route('/adopter_find_other_pet', methods=['GET', 'POST'])
def adopter_find_other_pet():


   # Get all existing dog's breeds from database
   if request.method == 'GET':
      db_connection = db.db_connection
      query = 'SELECT breed FROM Pets WHERE type = "%s"' % ("others")
      cursor = db.execute_query(db_connection, query)
      results = cursor.fetchall()
       
      breeds = [result['breed'] for result in results]
      # print("query result: %s" % breeds)
      return render_template('adopter_find_other_pet.j2', breeds = breeds)

   elif request.method == 'POST':
        db_connection = db.db_connection

        base_query = 'SELECT * FROM Pets WHERE type = "%s"' % ("others")

      #   if request.form['name'].strip():  #check the name, todo
      #      base_query = base_query + ' AND name LIKE "% + request.form['name'].strip() + %" '


        if request.form['name'].strip():  #check the name
           base_query = base_query + ' AND name =  "%s" ' % request.form['name'].strip()

        if request.form['breed'].strip(): #check the breed
           base_query = base_query + ' AND breed =  "%s" ' % request.form['breed'].strip()

        if request.form['age'].strip(): #check the age
           base_query = base_query + ' AND age =  %s ' % ((request.form['age']))
        
        if request.form['size'].strip(): #check the size
           base_query = base_query + ' AND size =  "%s" ' % (request.form['size'].strip())
        
        if request.form['gender'].strip(): #check the gender
           base_query = base_query + ' AND gender =  "%s" ' % (request.form['gender'].strip())
        
        if request.form['goodWithKids'].strip(): #check if good with kids
           base_query = base_query + ' AND goodWithKids =  %s ' % (request.form['goodWithKids'].strip())
        
        if request.form['goodWithDogs'].strip(): #check the good with dogs
           base_query = base_query + ' AND goodWithDogs =  %s ' % (request.form['goodWithDogs'].strip())
        
        if request.form['goodWithCats'].strip(): #check if good with cats
           base_query = base_query + ' AND goodWithCats =  %s ' % (request.form['goodWithCats'].strip())

        if request.form['mustBeLeashed'].strip(): #check if must be leashed
           base_query = base_query + ' AND mustBeLeashed =  %s ' % (request.form['mustBeLeashed'].strip())
          
        if request.form['availability'].strip(): #check if availability
           base_query = base_query + ' AND availability =  "%s" ' % (request.form['availability'].strip())

        base_query + ";"
        cursor = db.execute_query(db_connection, base_query)
        results = cursor.fetchall()

        if results:
 
           for pet in results:
             pet['isLiked'] = False

           AllPetsIdList = [pet['petsID'] for pet in results]

               # Get all pet is liked by this customer  
           query = 'SELECT * FROM CustomerLikePet WHERE customerID = "%s" And petsID IN (%s);' % (session['userID'], ",".join(str(elem) for elem in AllPetsIdList))
           cursor = db.execute_query(db_connection, query)
           likedPetResult = cursor.fetchall()

           if likedPetResult:  #if there are pets is liked by this customer
                  # print("likedOtherPetResult: ", likedOtherPetResult) # petId, customerId
              for likedPet in likedPetResult:
                    for pet in results: 
                       if pet['petsID'] == likedPet['petsID']:
                          pet['isLiked'] = True

           return render_template('adopter_detailed_find_other_pet.j2', others=results, base64=base64)
        else:
           return render_template('customer_find_a_pet_empty.j2')






# Adopter like a pet, give id is petsID
@crud_api.route('/customer_like_pet/<int:id>', methods=['POST', 'DELETE'])  
def customer_like_pet(id):
   db_connection = db.db_connection
  
   if request.method == 'POST':
      # Customer click "LIKE" button
      query = 'INSERT IGNORE INTO CustomerLikePet(petsID, customerID) VALUES (%s, %s)'
      petsID = id
      customerID = session['userID']
      
      data = (petsID, customerID)
      cursor = db.execute_query(db_connection, query, data)
      return "success"
      # return render_template('customer_like_pet_result.j2', customerID=session['userID'])

   if request.method == 'DELETE':
      # Customer click the "LIKE" button again when the pet is liked
      query = 'DELETE FROM CustomerLikePet WHERE petsID = %d AND customerID = %d;'% (id,session['userID'])
      cursor = db.execute_query(db_connection, query)
      return "success"


    # Adopter browse liked pet list
@crud_api.route('/customer_like_pet_list', methods=['POST', 'GET'])
def customer_like_pet_list():
   db_connection = db.db_connection
   # user_id = session['userID']
   query = 'SELECT * FROM CustomerLikePet WHERE customerID = %d;' % (session['userID'])
   # query = "UPDATE AdminMsg SET status='approved' WHERE adminMsgID=%s;" % (msgID)
   cursor = db.execute_query(db_connection, query)
   likedResult = cursor.fetchall()
   if likedResult:
      # print(likedResult)

      likedPetsIdList = [pet['petsID'] for pet in likedResult]
      # print(likedPetsIdList)
      query = 'SELECT * FROM Pets WHERE petsID IN (%s);' % (",".join(str(elem) for elem in likedPetsIdList))

      cursor = db.execute_query(db_connection, query)
      results = cursor.fetchall()
      return render_template('customer_like_pet_list.j2', likePets=results, base64=base64)
   else:
      return render_template('customer_like_pet_list_empty.j2')
   
   
   # likedPetsIdList = [pet['petsID'] for pet in likedResult]
   # print(likedPetsIdList)

   # return render_template('customer_like_pet_list.j2', pets=likedResult, base64=base64)
