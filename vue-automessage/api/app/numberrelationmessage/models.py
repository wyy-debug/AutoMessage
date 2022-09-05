from app import db

class NumberRelationMessage(db.Model):
    __tablename__ = 'numberrelationmessage'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number_id = db.Column(db.Integer)
    message_id = db.Column(db.Integer)

    def __init__(self, device_id, message_id):
      self.device_id = device_id
      self.message_id = message_id

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
