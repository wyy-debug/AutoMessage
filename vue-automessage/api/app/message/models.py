from app import db

class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    recv_from_number = db.Column(db.Integer)
    message_text = db.Column(db.String(500))
    recv_time = db.Column(db.DateTime)
    devices_id = db.Column(db.Integer, db.ForeignKey('devices.id'))

    def __init__(self, recv_from_number, message_text, recv_time, devices_id=None):
        self.recv_from_number = recv_from_number
        self.message_text = message_text
        self.recv_time = recv_time
        self.devices_id = devices_id

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
