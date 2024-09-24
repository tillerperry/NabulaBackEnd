from datetime import datetime
from tkinter import Grid
import uuid


class User:
    def __init__(self, fullName, age, occupation, nationality, maritalStatus, email, createdAt,id:str,student_id:str,cohort):
        self.fullName = fullName
        self.age = age
        self.occupation = occupation
        self.nationality = nationality
        self.maritalStatus = maritalStatus
        self.email = email
        self.id = id,
        self.student_id = student_id,
        self.cohort = cohort
        self.createdAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.id = str(uuid.uuid4())
        self.student_id = str(uuid.uuid4())
        
        

    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'fullName': self.fullName,
            'age': self.age,
            'occupation': self.occupation,
            'nationality': self.nationality,
            'maritalStatus': self.maritalStatus,
            'email': self.email,
            'createdAt': self.createdAt,
            'cohort': self.cohort
            
        }
