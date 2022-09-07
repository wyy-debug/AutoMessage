import json

from src.device.device import Device
from src.message.message import Message
from src.number.number import Number
from src.utils.httphandle import HttpHandle
class Devicemanager:

  def __init__(self):
    self.httphandle = HttpHandle()
    self.device_dict = {}
    self.message_list = []
    self.numbertodevice = {}
    self.devicenametoid = {}
    pass


  def add_device(self,device_name,device_number):
    data = {'device_name':device_name,'device_number':device_number}
    device_data = self.httphandle.add_device(json.dumps(data))
    device_json = json.loads(device_data)
    if device_json["code"] == "success":
      device = Device(int(device_json["device"]["id"]), device_json["device"]["device_name"], device_json["device"]["device_number"])
      self.device_dict[device.device_id] = device
      self.devicenametoid[device.device_name] = device.device_id

  def add_number(self, device_id, number_parition, number_semicolon, number_phone):
    data = {'number_parition':number_parition, 'number_semicolon':number_semicolon,'number_phone':number_phone}
    number_data = self.httphandle.add_number(json.dumps(data),device_id)
    number_json = json.loads(number_data)
    if number_json["code"] == "success":
      device = self.device_dict[device_id]
      number = Number(device.device_id, device.device_name, device.device_number, number_json["result"]["id"], number_json["result"]["number_parition"],
                      number_json["result"]["number_semicolon"], number_json["result"]["number_phone"])
      device.number_list.append(number)
      self.numbertodevice[number.number_phone] = device.device_id

  def init_device_dict(self):
    device_data = self.httphandle.get_devices()
    device_json = json.loads(device_data)
    if device_json["code"] == "success":
      for i in device_json["devices"]:
        device = Device(int(i["id"]), i["device_name"], i["device_number"])
        self.device_dict[device.device_id] = device
        self.devicenametoid[device.device_name] = device.device_id
        self.init_number_dict(device)

  def init_number_dict(self,device):
    number_data = self.httphandle.get_numbers(device.device_id)
    number_json = json.loads(number_data)
    if number_json["code"] == "success":
      for i in number_json["numbers"]:
        number = Number(device.device_id,device.device_name,device.device_number,int(i["id"]), i["number_parition"], i["number_semicolon"],i["number_phone"])
        device.number_list.append(number)
        self.numbertodevice[number.number_phone] = device.device_id
    pass

if __name__=='__main__':
  test = Devicemanager()
  test.init_device_dict()
  test.add_device('12312', '12312312')
  test.add_number(1, "test1", "test1", 13333333333)

