class User:
    def __init__(self, full_name, age, occupation, nationality, marital_status, email, created_at):
        self.full_name = full_name
        self.age = age
        self.occupation = occupation
        self.nationality = nationality
        self.marital_status = marital_status
        self.email = email
        self.created_at = created_at

    def to_dict(self):
        return {
            'full_name': self.full_name,
            'age': self.age,
            'occupation': self.occupation,
            'nationality': self.nationality,
            'marital_status': self.marital_status,
            'email': self.email,
            'created_at': self.created_at
        }
