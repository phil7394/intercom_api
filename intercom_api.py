import requests
import MySQLdb

# db connection details
hostname = 'localhost'
username = 'root'
password = 'admin123'
database = 'intercomDB'

# executes db query
def doQuery( conn ) :
    cur = conn.cursor() # get cursor
    cur.execute( "SELECT id, name, email FROM user" )
    
    return cur.fetchall() # return the result set
        
# main
if __name__ == '__main__':

	myConnection = MySQLdb.connect(host=hostname, user=username, passwd=password, db=database) # open connection
	result_set = doQuery(myConnection)
	myConnection.close() # close connection
	headers = {'Authorization': 'Bearer <Your access token>', 'Accept': 'application/json', 'Content-type': 'application/json'} # request header
	for id, email, name in result_set:
		requests.post('https://api.intercom.io/users', headers=headers, json={"user_id": id, "email": email, "name": name})# send post request with json data
