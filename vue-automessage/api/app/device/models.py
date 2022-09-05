from app import db

class Device(db.Model):
    __tablename__ = 'devices'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    device_name = db.Column(db.String(20))
    device_number = db.Column(db.String(20))

    def __init__(self, device_name, device_number):
      self.device_name = device_name
      self.device_number = device_number

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
