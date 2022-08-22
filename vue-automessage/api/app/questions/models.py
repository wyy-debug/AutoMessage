from app import db

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_msg = db.Column(db.String(50))
    question_type = db.Column(db.String(50))
    question_author = db.Column(db.String(50))
    version_id = db.Column(db.Integer, db.ForeignKey('versions.id'))

    def __init__(self, question_msg, question_type, question_author, version_id=None):
        self.question_msg = question_msg
        self.question_type = question_type
        self.question_author = question_author
        self.version_id = version_id

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
