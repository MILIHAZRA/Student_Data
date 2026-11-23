from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy() #instance created

class Student(db.Model):
    __tablename__="student"
    student_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    roll_number=db.Column(db.String,nullable=False,unique=True)
    first_name=db.Column(db.String,nullable=False)
    last_name=db.Column(db.String)
    courses=db.relationship("Enrolments",backref="student")


class Course(db.Model):
    __tablename__="course"
    course_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    course_code=db.Column(db.String,nullable=False,unique=True)
    course_name=db.Column(db.String,nullable=False)
    course_description=db.Column(db.String)

class Enrolments(db.Model):
    __tablename__="enrolments"
    enrolment_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    estudent_id=db.Column(db.Integer,db.ForeignKey(Student.student_id),nullable=False)
    ecourse_id=db.Column(db.Integer,db.ForeignKey(Course.course_id),nullable=False)
    course = db.relationship("Course") 
# basic approach:
   #1. I'll search in the enrollments with thw given student_id
   #2. you will get a course id list andyou will query in your course table you'll fetch the properties
# relationships:
   #object to object