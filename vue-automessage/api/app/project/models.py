from app import db

class Project(db.Model):
    __tablename__ = 'project'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_name = db.Column(db.String(20))
    created = db.Column(db.DateTime, server_default=db.func.now())
    versions = db.relationship('Version',backref='Project',cascade="all, delete-orphan")

    def __init__(self, project_name, versions=[]):
      self.project_name = project_name
      self.versions = versions

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
