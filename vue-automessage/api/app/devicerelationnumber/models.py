from app import db

class DeviceRelationNumber(db.Model):
    __tablename__ = 'devicerelationnumber'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    device_id = db.Column(db.Integer)
    number_id = db.Column(db.Integer)

    def __init__(self, device_id, number_id):
      self.device_id = device_id
      self.number_id = number_id

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
