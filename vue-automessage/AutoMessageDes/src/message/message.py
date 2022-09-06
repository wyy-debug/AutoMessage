from src.number import number


class Message(number.Number):
    def __init__(self, device_id, number_id, number_phone, message_id, message_text, device_name, device_number,
                 number_parition, number_semicolon):
        super().__init__(device_id, device_name, device_number, number_id, number_parition, number_semicolon,
                         number_phone)
        self.message_id = message_id
        self.message_text = message_text