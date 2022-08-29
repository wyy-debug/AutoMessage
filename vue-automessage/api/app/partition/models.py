from app import db

class Partition(db.Model):
    __tablename__ = 'partitions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    partition = db.Column(db.String(20))
    devices_id = db.Column(db.Integer, db.ForeignKey('devices.id'))
    number = db.relationship('Number', backref='Partition', cascade="all, delete-orphan")

    def __init__(self, partition, number=[], devices_id=None):
      self.devices_id = devices_id
      self.partition = partition
      self.number = number

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
