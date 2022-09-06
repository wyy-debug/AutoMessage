from src.device import device
class Number(device.Device):
    def __init__(self, device_id, device_name, device_number, number_id, number_parition, number_semicolon,
                 number_phone):
        super().__init__(device_id, device_name, device_number)
        self.number_id = number_id
        self.number_parition = number_parition
        self.number_semicolon = number_semicolon
        self.number_phone = number_phone
