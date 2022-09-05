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


    @classmethod
    def delete_number_id(cls,device_id):
      device = cls.query.filter(cls.device_id == device_id).all()
      if device:
        device.delete()
        db.session.commit()

    @classmethod
    def add_relation(cls, device_id, number_id):
      data = {"device_id":device_id,"number_id":number_id}
      db.session.add(data)
      db.session.commit()


    @classmethod
    def get_numbers_id(cls, device_id):
      fetched = cls.query.filter(cls.device_id == device_id).all()

      return fetched
