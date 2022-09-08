import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QMessageBox
from ui.untitled import Ui_MainWindow
from src.devicemanage import Devicemanager
from src.utils.httphandle import HttpHandle

class Example(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.httphandle = HttpHandle()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.choose_device = 1
        self.Devicemanager = Devicemanager()
        self.Devicemanager.init_device_dict()
        self.TreeInit()
        self.DevicesBoxInit()
        self.connect_init()


    def connect_init(self):
      self.ui.FindNumberButton.clicked.connect(self.finddevices)
      self.ui.treeWidget.doubleClicked.connect(self.changenumber)
      self.ui.ResButton.clicked.connect(self.getmessage)

    def init_ui(self):
      self.show()

    def changenumber(self):
      item = self.ui.treeWidget.currentItem()
      if(item.text(1)!=""):
        device_id = self.Devicemanager.numbertodevice[int(item.text(3))]
        device_number = self.Devicemanager.device_dict[device_id].device_number
        data = {'device_number':device_number, 'number_parition': item.text(1), 'number_semicolon': item.text(2)}
        changeres = self.httphandle.changenumber(json.dumps(data))
        if("Traceback" not in changeres):
          changeres_json = json.loads(changeres)
          if changeres_json["code"] == "success":
            if changeres_json["mes"] == "succss":
              QMessageBox.information(self, "提示", "切号成功")
            else:
              QMessageBox.information(self, "提示", "切号失败，请等待一会儿重试")
          self.getmessage()
        else:
          QMessageBox.information(self, "提示", "设备不在线")
        # 判断是否切号成功

    def getmessage(self):
      self.ui.listWidget.clear()
      message = self.httphandle.get_messages(self.choose_device)
      message_json = json.loads(message)
      if message_json["code"] == "success":
        for i in message_json["messages"]:
          self.ui.listWidget.addItem(i["message_text"])

    def finddevices(self):
        self.ui.treeWidget.clear()
        phone_number = self.ui.FindNumberEdit.text()
        try:
          device_id = self.Devicemanager.numbertodevice[int(phone_number)]
          self.choose_device = device_id
          Device = self.Devicemanager.device_dict[device_id]
          self.root = QTreeWidgetItem(self.ui.treeWidget)
          self.root.setText(0, Device.device_name)
          for i in Device.number_list:
            if i.number_phone == int(phone_number):
              child = QTreeWidgetItem(self.root)
              child.setText(1, str(i.number_parition))
              child.setText(2, str(i.number_semicolon))
              child.setText(3, str(i.number_phone))
              self.root.addChild(child)
        except:
          print("error")

    def TreeInit(self):
      self.ui.treeWidget.headerItem().setText(0, "设备名")
      self.ui.treeWidget.headerItem().setText(1, "分区")
      self.ui.treeWidget.headerItem().setText(2, "分号")
      self.ui.treeWidget.headerItem().setText(3, "号码")

    def DevicesBoxInit(self):
      self.ui.DevicesBox.currentIndexChanged.connect(self.changebox)
      for i in self.Devicemanager.devicenametoid.keys():
        self.ui.DevicesBox.addItem(i)

    def changebox(self):
      self.ui.treeWidget.clear()
      device = self.ui.DevicesBox.currentText()
      self.SetTree(self.Devicemanager.devicenametoid[device])

    def SetTree(self, device_id):
      Device = self.Devicemanager.device_dict[device_id]
      self.choose_device = device_id
      self.root = QTreeWidgetItem(self.ui.treeWidget)
      self.root.setText(0,Device.device_name)
      for i in Device.number_list:
        child = QTreeWidgetItem(self.root)
        child.setText(1, str(i.number_parition))
        child.setText(2, str(i.number_semicolon))
        child.setText(3, str(i.number_phone))
        self.root.addChild(child)

if __name__ == '__main__':
    e = Example()
    sys.exit(e.app.exec())








