#!/usr/bin/python

import MySQLdb

class Driver(object):

	"""Class for describing sql commands with python"""

	def connect(self, host, user_name, password, db):
		"""Connecting to database"""
		self.db = MySQLdb.connect(host, user_name, password, db)

		#Preparing using cursor() method
		self.cursor = self.db.cursor(MySQLdb.cursors.Cursor)

	def execute_query(self, query):
		"""Execute a sql query"""
		try:
			#Executing a sql query with execute() method
			self.cursor.execute(query)

			#Finalizing the changes using commit() method
			self.db.commit()

			#Returning all fetched values
			self.cursor.fetchall()
		except:
			#Rollback in case of error
			print "Error"
			self.db.rollback()

	#def input_transform(self, value):
	#	"""Returns a dict of appropriate values"""
	#	result_tuple = ()
	#	
	#	for i in value:
	#		if isinstance(i, (int, str)):
	#			result_tuple = result_tuple + (i, )
	#
	#	return result_tuple



	def insert(self, table_name, columns, attrs):
		"""Inserts new records in a table"""
		insert_query = "INSERT INTO %s (%s) VALUES %s" \
			% (table_name, (', ').join(columns), attrs)
			
		#Use execute_query() method
		self.execute_query(insert_query)

	def select(self, table_name, columns):
		"""Read the result of query"""
		select_query = "SELECT %s FROM %s" % ((', ').join(columns), table_name)
		
		try:
			#Executing query 
			self.cursor.execute(select_query)

			#Fetching output of executing
			self.select_result = self.cursor.fetchall()

			#Returning result
			return self.select_result
		except:
			#Rollback in case of error
			self.db.rollback()

	def update(self, table_name, changes, condition):
		"""Update records in a table"""
		update_query = "UPDATE %s SET %s WHERE %s" % (table_name, changes, condition)
		self.execute_query(update_query)

	def delete(self, table_name, condition):
		"""Delete selected records"""
		delete_query = "DELETE FROM %s WHERE %s" % (table_name, condition)
		self.execute_query(delete_query)		


if __name__ == '__main__':
	tmpDB = Driver()

	#Works
	tmpDB.connect("localhost", "denny", "isurrender", "local_db")

	#Works
	#print('Executing any query')
	#tmpDB.execute_query('DROP TABLE IF EXISTS Test')
	#tmpDB.execute_query('CREATE TABLE Test (Name VARCHAR(30))')

	print('Inserting values')
	tmpDB.insert('Test', ('Name'), ('Nick', 'FRE'))
	#tmpDB.insert('Test', '(Name, Age, Role)', "'Oleksiy', 20, 'Student'")
	#tmpDB.insert('Schools', ('name', 'address'), ('School 23', 'st. Green'))

	#Works
	#print('Reading data')
	#print tmpDB.select('EMPLOYEE', ('FIRST_NAME', 'LAST_NAME'))
	
	#Works
	#print('Updating data')
	#tmpDB.update('EMPLOYEE', 'FIRST_NAME = "Denis"', 'LAST_NAME = "Mohan"')

	#Works
	#print('Deleting data')
	#tmpDB.delete('EMPLOYEE', 'AGE = 21')

