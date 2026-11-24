<h1>Student & Course Management System</h1>

A lightweight CRUD web application built with Flask and Flask-SQLAlchemy to manage student records, available courses, and student course enrollments using an SQLite database.

<h3>Features:</h3>
<ul>
  <li>View All Students: Display a list of registered students on the home page (/).</li>
  <li>Create Student & Enroll: Add new students with unique roll numbers and assign them to one or more courses (/student/create).</li>
  <li>Student Details: View a student's personal information and their enrolled courses (/student/<int:student_id>).</li>
  <li>Update Student: Edit a student's first name, last name, and course enrollments (/student/<int:student_id>/update).</li>
  <li>Delete Student: Remove a student record and associated enrollments from the database (/student/<int:student_id>/delete).</li>
</ul
<h3>Tech Stack:</h3>
<ul>
   <li> Backend: Python, Flask, Flask-SQLAlchemy</li>
   <li> Frontend: HTML5, Jinja2 Templates</li>
    <li> Database: SQLite (database.sqlite3)</li>
</ul>
<h3>Project Structure:</h3>

 ```   
├── app.py                        # Main Flask application and routes
├── model.py                      # SQLAlchemy database models (Student, Course, Enrolments)
├── instance/
│   └── database.sqlite3          # SQLite database (auto-generated on first run)
├── templates/
│   ├── index.html                # Home page listing all students
│   ├── create.html               # Form to add a new student
│   ├── update.html               # Form to update student details and courses
│   ├── exists.html               # Notice page when a roll number already exists
│   └── Student details page.html # Detailed view of a student and their courses
└── README.md                     # Project documentation
```
<h3>Database Schema:</h3>
<ol>
  <li>student:</li>
  <ul>
    <li>student_id (Integer, Primary Key, Auto-increment)</li>
    <li>roll_number (String, Unique, Not Null)Project Structure</li>
    <li>first_name (String, Not Null)</li>
    <li>last_name (String, Nullable)</li>
  </ul>
   <li>course:</li>
   <ul>
     <li>course_id (Integer, Primary Key, Auto-increment)</li>
     <li>course_code (String, Unique, Not Null)</li>
     <li>course_name (String, Not Null)</li>
     <li>course_description (String, Nullable)</li>
   </ul>
   <li>enrolments:</li>
   <ul>
      <li>enrolment_id (Integer, Primary Key, Auto-increment)</li>
      <li>estudent_id (Integer, Foreign Key → student.student_id)</li>
      <li>ecourse_id (Integer, Foreign Key → course.course_id)</li>
</ol>
<h3>Routes:</h3>
<table>
  <caption>Overview in details: </caption>
  <tr>
    <th>Method</th>	
    <th>URL</th>
    <th>Description</th>
  </tr>
  <tr>
     <td>GET</td>
     <td>/</td>
     <td>List all students</td>
  </tr>
  <tr>
     <td>GET,POST</td> 
     <td>/student/create</td>	
     <td>Show/submit the add student form</td>
  </tr>
  <tr>
     <td>GET, POST</td>	
     <td>/student/<int:student_id>/update</td>	
     <td> Show / submit the update form</td>
  </tr>
  <tr>
     <td>GET</td>
    <td>/student/<int:s>/delete</td>	
     <td>Delete a student and their enrolments</td>
  </tr>
  <tr>
      <td>GET</td>
      <td> /student/<int:st> </int:st></td>	
      <td>Student details and enrolled courses</td>
  </tr>
</table>
<h3>Getting Started:</h3>
<ol>
  <li>Git Clone:</li>
  
  ```
    https://github.com/MILIHAZRA/Student_Data.git
    cd Student_Data
```
  <li>Create a virtual environment:</li>

  ```
   python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```
   <li>Install dependencies:</li>

```
pip install flask flask-sqlalchemy
```
   <li>Run the application:</li>

  ```
python app.py
```
   <li>Open in browser: Navigate to http://127.0.0.1:5000/ in your web browser.The SQLite database file is created automatically the first time the app runs.</li>
</ol>
<h3>Usage: </h3>
<ul>
   <li>Click + Add Student, enter a roll number and name, tick the courses, and submit.</li>
   <li>Click a roll number on the home page to see that student's details and enrolments.</li>
   <li>Use Update to change a student's name or courses, or Delete to remove the student.</li>
</ul>
<p>Roll numbers must be unique. Adding a duplicate roll number shows an error page.</p>
<h3>Notes:</h3>
<ul>
  <li>The app runs with debug=True, which is only suitable for development.</li>
  <li>Add *.sqlite3 and instance/ to your .gitignore so the local database is not committed.</li>
</ul>

