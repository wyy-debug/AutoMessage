import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem
from ui.untitled import Ui_MainWindow
from src.devicemanage import Devicemanager


class Example(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.Devicemanager = Devicemanager()
        self.Devicemanager.init_device_dict()
        self.TreeInit()
        self.DevicesBoxInit()
        self.connect_init()

    def connect_init(self):
      self.ui.FindNumberButton.clicked.connect(self.finddevices)

    def init_ui(self):
      self.show()

    def finddevices(self):
      self.ui.treeWidget.clear()
      phone_number = self.ui.FindNumberEdit.text()
      try:
        device_id = self.Devicemanager.numbertodevice[int(phone_number)]
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








