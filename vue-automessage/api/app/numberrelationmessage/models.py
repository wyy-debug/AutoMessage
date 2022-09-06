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

    @classmethod
    def add_relation(cls, number_id, message_id):
      data = {"number_id": number_id, "message_id": message_id}
      db.session.add(data)
      db.session.commit()

    @classmethod
    def get_messages_id(cls, number_id):
      fetched = cls.query.filter(cls.number_id == number_id).all()
      return fetched
