import mysql.connector

dataBase = mysql.connector.connect(
	host = '127.0.0.1',
	user = 'root',
	passwd = 'mysqlpassword'

	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE mydatabasename")

# Create a user
cursorObject.execute("CREATE USER 'mydatabaseuser'@'localhost' IDENTIFIED BY 'mysqlpassword'")

# Grant all privileges on database
cursorObject.execute("GRANT ALL PRIVILEGES ON mydatabasename.* TO 'mydatabaseuser'@'localhost'")	

# Flush privileges
cursorObject.execute("FLUSH PRIVILEGES")

print("All Done!")
