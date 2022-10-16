import sqlite3
# creating an connection

#Create database and connect on it
db = sqlite3.connect("School.db") 

# Create tables 

db.execute("""
CREATE TABLE Class ( 
id INTEGER primary key   , 
name TEXT ,
floorNumber INTEGER  
) ;
""")

db.execute("""
CREATE TABLE Course ( 
id INTEGER primary key   , 
name TEXT ,
bookName TEXT , 
teacherName TEXT 
) ;
""")

db.execute("""
CREATE TABLE ContactInfo (
id INTEGER primary key   , 
phoneNumber TEXT , 
City TEXT 
) ; 
""" )


db.execute("""
CREATE TABLE student (
id INTEGER primary key ,  
first_name TEXT , 
last_name TEXT , 
age INTEGER CHECK (Age>=16) ,
ContactId INTEGER ,
ClassId INTEGER , 
UNIQUE (first_name,last_name) , 
CONSTRAINT fk_class
    FOREIGN KEY (ClassId)
    REFERENCES Class (id) , 
CONSTRAINT fk_Contact
    FOREIGN KEY (ContactId)
    REFERENCES ContactInfo (id) 
) ;
""")


db.execute("""
CREATE TABLE studentCourses (
studentId INTEGER  , 
courseId INTEGER ,
PRIMARY KEY (studentId, courseId) , 
CONSTRAINT fk_student
    FOREIGN KEY (studentId)
    REFERENCES student (id) ,
CONSTRAINT fk_course
    FOREIGN KEY (courseId)
    REFERENCES course (id) 
) ;

""")

#close database 

db.close()




