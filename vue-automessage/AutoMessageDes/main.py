import sys
import json
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QMessageBox
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtCore import *
from ui.untitled import Ui_MainWindow
from src.devicemanage import Devicemanager
from src.utils.httphandle import HttpHandle


class MyThread(QThread):
  my_signal = pyqtSignal(str)  # 1

  def __init__(self,httphandle,data):
    super(MyThread, self).__init__()
    self.count = 0
    self.httphandle = httphandle
    self.data = data

  def run(self):
    changeres = self.httphandle.changenumber(json.dumps(self.data))
    if ("Traceback" not in changeres):
      changeres_json = json.loads(changeres)
      if changeres_json["code"] == "success":
        if changeres_json["mes"] == "succss":
          self.my_signal.emit("succss")
        else:
          self.my_signal.emit("error")
      else:
        self.my_signal.emit("noline")



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


    # 槽初始化
    def connect_init(self):
      self.ui.FindNumberButton.clicked.connect(self.finddevices)
      self.ui.treeWidget.doubleClicked.connect(self.changenumber)
      self.ui.ResButton.clicked.connect(self.getmessage)

    def init_ui(self):
      self.show()


    def set_change(self,changeres):
      if changeres == "success":
        QMessageBox.information(self, "提示", "切号成功")
        self.getmessage()
      elif changeres == "error":
        QMessageBox.information(self, "提示", "切号失败，请等待一会儿重试")
      else:
        QMessageBox.information(self, "提示", "设备不在线")
    # 切号
    def changenumber(self):

      item = self.ui.treeWidget.currentItem()
      if(item.text(1)!=""):
        device_id = self.Devicemanager.numbertodevice[int(item.text(3))]
        device_number = self.Devicemanager.device_dict[device_id].device_number
        data = {'device_number':device_number, 'number_parition': item.text(1), 'number_semicolon': item.text(2)}
        my_thread = MyThread(self.httphandle, data)
        my_thread.start()
        my_thread.my_signal.connect(self.set_change)
        QMessageBox.information(self, "提示", "切号中请等待完成")

        # 判断是否切号成功

    # 获取短信
    def getmessage(self):
      self.ui.listWidget.clear()
      message = self.httphandle.get_messages(self.choose_device)
      message_json = json.loads(message)
      if message_json["code"] == "success":
        for i in message_json["messages"]:
          self.ui.listWidget.addItem(i["message_text"])

    # 查询设备并且添加在列表树中
    def finddevices(self):
        phone_number = self.ui.FindNumberEdit.text()
        if phone_number == "":
          self.changebox()
        try:
          device_id = self.Devicemanager.numbertodevice[int(phone_number)]
          self.choose_device = device_id
          Device = self.Devicemanager.device_dict[device_id]
          self.ui.treeWidget.clear()
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








