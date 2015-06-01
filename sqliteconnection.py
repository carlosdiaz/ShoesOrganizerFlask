import sqlite3

with sqlite3.connect("shoesorganizer.db") as connection:
	c = connection.cursor()
	#c.execute(""" DROP TABLE shoescatalog""")
	#First version will only store the path of the image
	
	c.execute(""" CREATE TABLE shoescatalog (Name TEXT, Description TEXT, Model TEXT, Image TEXT)""")
	c.execute(' INSERT INTO shoescatalog VALUES("Zapatos rojos", "Estan en buena condicion", "Andrea", "http://zapachic.com/wp-content/uploads/2014/05/6-zapatos-Andrea-por-cat%C3%A1logo-con-botines-rojos-y-azules--1024x481.jpg") ')
	c.execute(' INSERT INTO shoescatalog VALUES("Tennis rosas", "No estan tan buenos", "Nike", "http://zapachic.com/wp-content/uploads/2014/05/6-zapatos-Andrea-por-cat%C3%A1logo-con-botines-rojos-y-azules--1024x481.jpg") ')
	c.execute(' INSERT INTO shoescatalog VALUES("Sandalias negras", "Estan en buena condicion", "Ay caramba", "http://zapachic.com/wp-content/uploads/2014/05/6-zapatos-Andrea-por-cat%C3%A1logo-con-botines-rojos-y-azules--1024x481.jpg") ')
	c.execute(' INSERT INTO shoescatalog VALUES("Tennis rojos", "Estan tan buenos", "Polo", "http://zapachic.com/wp-content/uploads/2014/05/6-zapatos-Andrea-por-cat%C3%A1logo-con-botines-rojos-y-azules--1024x481.jpg") ')
	
	