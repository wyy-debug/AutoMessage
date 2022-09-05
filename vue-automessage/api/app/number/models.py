from app import db

class Number(db.Model):
    __tablename__ = 'numbers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 分区
    number_parition = db.Column(db.String(20))
    # 分号
    number_semicolon = db.Column(db.String(20))
    # 手机号码
    number_phone = db.Column(db.Integer)

    def __init__(self, number_parition, number_semicolon, number_phone):
      self.number_parition = number_parition
      self.number_semicolon = number_semicolon
      self.number_phone = number_phone

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
