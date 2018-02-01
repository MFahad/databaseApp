import sqlite3

class Database:
	
	def __init__(self,db):		#this function should be executed when the object is created so to make sure our database is created also known as constructor in C++
		self.conn=sqlite3.connect(db) #the connection stays open till the destructor is called
		self.cur=self.conn.cursor()	#the cursor method of the connection object of sqlite3 library
		self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text , author text, year integer, isbn integer)")# id set to mandotry item just to keep count 
		self.conn.commit()
		
		
	def insert(self,title, author, year, isbn):
		self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
		self.conn.commit()
		
		
	def view(self):
		self.cur.execute("SELECT * FROM book") #self gets replaced by backend which is the database object created in the frontend 
		rows=self.cur.fetchall()
		return rows

	def search(self,title="", author="", year="",isbn=""):
		self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
		rows=self.cur.fetchall()
		
		return rows
		
	def delete(self,id):
	#	conn=sqlite3.connect("books.db")
	#	cur=conn.cursor()
		self.cur.execute("DELETE FROM book WHERE id=?",(id,))
		self.conn.commit()
		

	def update(self,id,title,author,year,isbn):
		self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
		self.conn.commit()
		
	def __del__(self):	 #so this is just like destructor in C++
		self.conn.close()  # instead of closing the db in each method we close it when the object is delted
		
		
#insert("the sun","muhammad fahad", 1928, 458345328092834)
#delete(2)
#update(3,"the moon","john smooth",1928,39209320)
#print(view())
#print(search(author="john smith"))
