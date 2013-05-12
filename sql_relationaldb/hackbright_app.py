import sqlite3

DB = None
CONN = None

# function that will call 
def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    print """\
Student: %s %s
Github account: %s"""%(row[0], row[1], row[2])

def query_for_projects(title):
    query = """SELECT title, description, max_grade FROM Projects WHERE title = ?"""
    DB.execute(query, (title,))
    row = DB.fetchone()
    print """\
    Title: %s 
    Description: %s
    Max Grade: %s""" % (row[0], row[1], row[2])

def query_for_grades(project_title):
    query = """SELECT grade FROM Grades WHERE project_title = ?"""
    DB.execute(query, (project_title,))
    row = DB.fetchone()
    print """\
    Grade: %s""" % (row[0])

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def make_new_student(first_name, last_name, github):
    query = """INSERT into Students values (?, ?, ?)"""
    DB.execute(query, (first_name, last_name, github))
    CONN.commit()
    print "Successfully added student: %s %s"%(first_name, last_name)

def make_new_project(title, description, max_grade):
    query = """INSERT into Projects values (?, ?, ?)"""
    DB.execute(query, (title, description, max_grade))
    CONN.commit()
    print "Successfully added project: %s %s"%(title, description)

def make_new_grade(student_github, project_title, grade):
    query = """INSERT into Grades values (?, ?, ?)"""
    DB.execute(query, (student_github, project_title, grade))
    CONN.commit()
    print "Successfully added grade: %s"%(grade)

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)
        elif command == "project":
            query_for_projects(*args)
        elif command == "new_project":
            make_new_project(*args)
        elif command == "grade":
            query_for_grades(*args)
        elif command == "new_grade":
            make_new_grade(*args)
        elif command == "all_grades":
            query_all_grades(*args)

    CONN.close()

if __name__ == "__main__":
    main()

