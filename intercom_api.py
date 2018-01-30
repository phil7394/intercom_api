import requests
import MySQLdb
import json

hostname = 'localhost'
username = 'root'
password = 'admin123'
database = 'intercomDB'

def doQuery( conn ) :
    cur = conn.cursor()
    cur.execute( "SELECT id, name, email FROM user" )
    
    return cur.fetchall()
        

if __name__ == '__main__':

	myConnection = MySQLdb.connect(host=hostname, user=username, passwd=password, db=database)
	result_set = doQuery(myConnection)
	myConnection.close()
	headers = {'Authorization': 'Bearer <Your access token>', 'Accept': 'application/json', 'Content-type': 'application/json'}
	for id, email, name in result_set:
		requests.post('https://api.intercom.io/users', headers=headers, json={"user_id": id, "email": email, "name": name})
