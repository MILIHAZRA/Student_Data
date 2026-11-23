from flask import Flask,render_template,request,redirect
from model import *

# configuration setting:
def setup_app():
    app=Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database.sqlite3 "
    db.init_app(app)  #linked app and db
    with app.app_context():
        db.create_all()
    print("DB is configured successfully!!")
    return app

app=setup_app() #calling function

@app.route("/")
def home():
    all_std=Student.query.all() # all the records for the student table(list of object)
    print(all_std)
    return render_template("index.html",all_std=all_std)

@app.route("/student/create",methods=['GET','POST'])
def create():
    if request.method=="GET":
        return render_template("create.html")
    if request.method=="POST":
        roll=request.form.get('roll')
        s=Student.query.filter_by(roll_number=roll).first()
        # as we know that primary key is the roll number, if i will query in the database using primary key
        # i'm only gettling i row always
        if s:
            return render_template("exists.html")
        else:
            f_name = request.form.get('f_name')
            l_name = request.form.get('l_name')
            courses=request.form.getlist('courses')
            new_s=Student(roll_number=roll,first_name=f_name,last_name=l_name)
            db.session.add(new_s)
            db.session.flush()
            for course in courses:
                s_id=new_s.student_id
                new_e=Enrolments(estudent_id=s_id,ecourse_id=int(course))
                db.session.add(new_e)
                db.session.commit()
        return redirect("/")
    
@app.route('/student/<int:student_id>/update',methods=['GET','POST'])
def up_add(student_id):
    to_update=Student.query.filter_by(student_id=student_id).first()
    if not to_update:
        return "Student not found"
    if request.method=='GET':
        return render_template('update.html',to_update=to_update)
    if request.method=='POST':
        f_name = request.form.get('f_name')
        l_name = request.form.get('l_name')
        courses=request.form.getlist('courses')
        to_update.first_name=f_name
        to_update.last_name=l_name
        # Clear existing enrollments for this student before adding updated ones
        Enrolments.query.filter_by(estudent_id=to_update.student_id).delete()
        for course in courses:
            s_id=to_update.student_id
            new_e=Enrolments(estudent_id=s_id,ecourse_id=int(course))
            db.session.add(new_e)
            db.session.commit()
    return redirect("/")


@app.route('/student/<int:s>/delete')
def Del(s):
    to_delete=Student.query.get(s) #search for primary key
    if not to_delete:
        return "Student not found"
    Enrolments.query.filter_by(estudent_id=s).delete()
    db.session.delete(to_delete)
    db.session.commit()
    return redirect("/")

@app.route('/student/<int:st>')
def details(st):
    # student info and they are enrolled in courses
    infor=Student.query.get(st)
    courses=infor.courses
    print(courses)
    return render_template("Student details page.html",infor=infor,courses=courses)


# main program
if __name__=="__main__":
    app.run(debug=True)
