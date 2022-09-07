from app import db

class NumberRelationMessage(db.Model):
    __tablename__ = 'numberrelationmessage'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    device_id = db.Column(db.Integer)
    message_id = db.Column(db.Integer)

    def __init__(self, device_id, message_id):
      self.device_id = device_id
      self.message_id = message_id

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self

    @classmethod
    def add_relation(cls, device_id, message_id):
      test = cls(device_id, message_id)
      db.session.add(test)
      db.session.commit()

    @classmethod
    def get_messages_id(cls, device_id):
      fetched = cls.query.order_by(cls.id.desc()).filter(cls.device_id == device_id).limit(2)
      return fetched
