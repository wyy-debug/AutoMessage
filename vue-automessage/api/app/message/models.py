from app import db

class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    message_text = db.Column(db.String(500))
    creat_time = db.Column(db.DateTime)

    def __init__(self, message_text, creat_time):
        self.message_text = message_text
        self.creat_time = creat_time

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
