class DeviceManager():

  def __init__(self):
    # 服务器启动时，进行切号
    self.devicerelationnumber = {}

  def get_number_id(self, device_id):
    return self.devicerelationnumber[device_id]

  def set_number_id(self, device_id, number_id):
    self.devicerelationnumber[device_id] = number_id
