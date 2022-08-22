from app import db

class Version(db.Model):
    __tablename__ = 'versions'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50))
    questions = db.relationship('Question', backref='Version', cascade="all, delete-orphan")
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

    def __init__(self,name,questions=[],project_id=None):
        self.name = name
        self.questions = questions
        self.project_id = project_id

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
