import pymysql 
pymysql.install_as_MySQLdb()
import MySQLdb
from flaskext.mysql import MySQL

db_connection = pymysql.connect(host = 'cs467-instance.cnm3wt0bg4mw.us-west-1.rds.amazonaws.com',
                        user = 'admin',
                        passwd = 'OregonCS467', 
                        db = 'adoptionproject')

def execute_query(db_connection = None, query = None, query_params = ()):
    '''
    executes a given SQL query on the given db connection and returns a Cursor object
    db_connection: a MySQLdb connection object created by connect_to_database()
    query: string containing SQL query
    returns: A Cursor object as specified at https://www.python.org/dev/peps/pep-0249/#cursor-objects.
    You need to run .fetchall() or .fetchone() on that object to actually acccess the results.
    '''

    if db_connection is None:
        print("No connection to the database found! Have you called connect_to_database() first?")
        return None

    if query is None or len(query.strip()) == 0:
        print("query is empty! Please pass a SQL query in query")
        return None

    print("Executing %s with %s" % (query, query_params));
    # Create a cursor to execute query. Why? Because apparently they optimize execution by retaining a reference according to PEP0249
    cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)

    '''
    params = tuple()
    #create a tuple of paramters to send with the query
    for q in query_params:
        params = params + (q)
    '''
    #TODO: Sanitize the query before executing it!!!
    cursor.execute(query, query_params)
    # this will actually commit any changes to the database. without this no
    # changes will be committed!
    db_connection.commit();
    return cursor

if __name__ == '__main__':
    print("Executing a sample query on the database using the credentials from db_credentials.py")
    query = 'INSERT INTO Customers(email, password) VALUES ("yinli@oregonstate.edu", "123")'
    # query = 'SELECT * FROM Customers'
    results = execute_query(db_connection, query);
    print("Printing results of %s" % query)

    for r in results.fetchall():
        print(r)