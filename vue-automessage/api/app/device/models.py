from app import db

class Device(db.Model):
    __tablename__ = 'devices'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    devices_id = db.Column(db.String(20))
    phone_number = db.Column(db.Integer)
    messages = db.relationship('Message', backref='Device', cascade="all, delete-orphan")

    def __init__(self, devices_id, phone_number, message=[]):
      self.devices_id = devices_id
      self.phone_number = phone_number
      self.messages = message

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
