# Connect to the database.
import sys
import pymysql
from collections import OrderedDict

# connect to db
# pymysql.connect def makeConnection():
def makeConnection():

	file = open(sys.path[0]+"/dbconfig.txt", "r")   
	dbStr = file.readline().strip() 
	userStr = file.readline().strip() 
	passwdStr = file.readline().strip() 
	hostStr = file.readline().strip() 

	conn = pymysql.connect(
		db=dbStr,
		user=userStr,
		passwd=passwdStr,
		host=hostStr)
	return conn

# str 	getPwd(login):
def getPwd(login):
	conn = makeConnection()
	c = conn.cursor()

	print("login: %s" %login)
	rows_count = c.execute("Call get_userPwd(%s) ;" ,  (login,))
	if rows_count > 0:
		rs = c.fetchall()
		print("rs = %s" % rs)
		for i, r in enumerate(rs):
			pwd = r[0]		
# 		print("pwd = %s" % pwd)
	else:
		pwd = None
# 		print("no rs = %s" % rs)
	conn.close()		
	return pwd
# void def createRecord(**studentRec):
def createRecord(**studentRec):
	BookName = studentRec['BookName'].strip()
	Author = studentRec['Author'].strip()
	Publisher = studentRec['Publisher'].strip()
	Pubdate = studentRec['Pubdate'].strip()
	Price = studentRec['Price'].strip()
	Sellingprice = studentRec['Sellingprice'].strip()
	BookCName = studentRec['BookCName'].strip()

	conn = makeConnection()
	c = conn.cursor()

	# Insert student data.
	query = "CALL add_ebook ('%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (BookName, Author, Publisher, Pubdate, Price, Sellingprice, BookCName)
	c.execute(query)
	conn.commit()
	conn.close()
	

# list-of-list 	getEnrollmentRecords():	
def getEnrollmentRecords():
	conn = makeConnection()
	c = conn.cursor()

	# Print the contents of the db table.
	c.execute("CALL get_book_record();")	

	# Fetch all the rows in a list of lists.
	results = c.fetchall()

	conn.close()
	return results

# [] getCourses():	
def getCourses():
	conn = makeConnection()
	c = conn.cursor()	

	# Print the contents of the db table.
	c.execute("CALL get_category();")	

	# Fetch all the rows in a list of lists.
	results = c.fetchall()

	records = []
	for i, r in enumerate(results):
		records.append(r[0])
# 		print ("%d: %s" % (i+1,  r[0]))

	conn.close()
	return records	

def deleted(**deleteRec):
	BookId = deleteRec['BookId'].strip()
	conn = makeConnection()
	c = conn.cursor()

	# Print the contents of the db table.	
	query = "CALL delete_inventory ('%s');" % (BookId)
	# Fetch all the rows in a list of lists.
	c.execute(query)
	conn.commit()
	conn.close()