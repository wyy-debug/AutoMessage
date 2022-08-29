from app import db

class Device(db.Model):
    __tablename__ = 'devices'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    devices_name = db.Column(db.String(20))
    partition = db.relationship('Partition', backref='Device', cascade="all, delete-orphan")

    def __init__(self, devices_name, partition=[]):
      self.devices_name = devices_name
      self.partition = partition

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
