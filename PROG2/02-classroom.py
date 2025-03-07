class Document:
    """
       A class to represent a Docuent.

       ...

       Attributes
       ----------
       title : str
           title of document
       owner : str
           name of owner
       """
    def __init__(self, title, owner):
        self.title = title
        self.owner = owner

class Student:
    """
       A class to represent a Student.

       ...

       Attributes
       ----------
       name : str
           name of student

       Methods
       -------
       add_document(document):
            Appends doc to student
    """
    def __init__(self, name):
        self.name = name
        self.documents = []

    def add_document(self, document):
        self.documents.append(document)

class Table:
    """
       A class to represent a Table.

       ...

       Attributes
       ----------
       table_number : int
           number of table
       students: Student
           students at table

       Methods
       -------
       add_students(student1, student2):
            Adds students to table
    """
    def __init__(self, table_number):
        self.table_number = table_number
        self.students = []

    def add_students(self, student1, student2):
        self.students.extend([student1, student2])

class Blackboard:
    """
       A class to represent a Blackboard.

       ...

       Attributes
       ----------
       content : str
           content of Blackboard

       Methods
       -------
       write(text):
            Write text on blackboard
    """
    def __init__(self):
        self.content = ""

    def write(self, text):
        self.content = text

class Teacher:
    """
       A class to represent a Teacher.

       ...

       Attributes
       ----------
       name : str
           name of teacher

    """
    def __init__(self, name):
        self.name = name

#  Wird nur in dieser Datei ausgeführt in anderen Dateien aber nicht
if __name__ == "__main__":
    teacher = Teacher("Herr Müller")
    blackboard = Blackboard()
    blackboard.write(f"Lehrer: {teacher.name}")

    students = [Student(f"Schüler {i + 1}") for i in range(20)]

    documents = [Document(f"Dokument {i + 1}", students[i]) for i in range(20)]
    for i in range(20):
        students[i].add_document(documents[i])

    tables = [Table(i + 1) for i in range(10)]
    for i, table in enumerate(tables):
        table.add_students(students[i * 2], students[i * 2 + 1])
