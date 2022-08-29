from app import db

class Number(db.Model):
    __tablename__ = 'numbers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number_type = db.Column(db.String(20))
    number = db.Column(db.Integer)
    partition_id = db.Column(db.Integer, db.ForeignKey('partitions.id'))
    messages = db.relationship('Message', backref='Number', cascade="all, delete-orphan")

    def __init__(self, number, message=[], partition_id=None):
      self.number = number
      self.messages = message
      self.partition_id = partition_id

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
