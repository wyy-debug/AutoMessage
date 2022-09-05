class Devices:
    def __init___(self,device_id,device_name,device_number):
        self.device_id = device_id,
        self.device_name = device_name  
        self.device_number = device_number
    
    def add_devices(self):
        pass

    def get_devices_list(self):
        pass

    def update_devices(self):
        pass

    def del_devices(self):
        DeviceRelationNumber.del_device_id()
        pass

class DeviceRelationNumber:
    def __init__(self,id,device_id,number_id):
        self.id = id
        self.device_id = device_id
        self.number_id = number_id
    
    def add_devices_relation_number(self):
        pass

    def get_number_id(self):
        pass

    def get_device_id(self):
        pass

    def del_number_id(self):
        pass

    def del_device_id(self):
        pass


class Numbers:
    def __init__(self,number_id,number_partition,number_semicolon,number_phone):
        self.number_id = number_id
        self.number_parition = number_partition
        self.number_semicolon = number_semicolon
        self.number_phone = number_phone
    
    def add_numbers(self):
        DeviceRelationNumber.add_devices_relation_number()
        pass

    def get_numbers_list(self):
        DeviceRelationNumber.get_number_id()
        pass

    def update_numbers(self):
        pass

    def del_numbers(self):
        DeviceRelationNumber.del_device_id()
        NumbeRelationMessage.del_number_id
        pass

class NumbeRelationMessage:
    def __init__(self,id,number_id,message_id):
        self.id = id
        self.number_id = number_id
        self.message_id = message_id
    
    def add_number_relation_message(self):
        pass

    def get_message_id(self):
        pass

    def get_number_id(self):
        pass

    def del_message_id(self):
        pass

    def del_number_id(self):
        pass

    
class Messages:
    def __init__(self,message_id,creat_time):
        self.message_id = message_id
        self.creat_time = creat_time

    def add_messages(self):
        NumbeRelationMessage.add_number_relation_message()
        pass

    def get_messages_list(self):
        NumbeRelationMessage.get_number_id()
        pass

    def del_messages(self):
        DeviceRelationNumber.del_message_id()
        pass


class User:
    def __init__(self,user_id,user_name,user_password,user_identity):
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_identity = user_identity