# -*- encoding=utf8 -*-
from airtest.core.api import *
from airtest.cli.parser import cli_setup

class Poco:

  def __init__(self,port):
    auto_setup(__file__, devices=["android:///121.5.154.203:"+ port +"?cap_method=javacap&touch_method=adb", ])
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

  # part 1区 xxx区
  # sim 1 - 12
  #
  def change_call(self, part, sim):
    try:
      if self.poco(text="SIM 卡应用1").exists():
        self.poco(text="SIM 卡应用1").click()
      sleep(4.0)
      if self.poco(text=part + "换号").exists():
        self.poco(text=part + "换号").click()
      else:
        self.poco("android:id/list").swipe([0, -0.3])
        sleep(1.0)
        self.poco(text=part + "换号").click()
      if self.poco(text="*SIM-" + sim).exists():
        self.poco("android:id/up").click()
        return True
      if self.poco(text=" SIM-" + sim).exists():
        self.poco(text=" SIM-" + sim).click()
      else:
        self.poco("android:id/list").swipe([0, -0.3])
        sleep(1.0)
        if self.poco(text="*SIM-" + sim).exists():
          self.poco("android:id/up").click()
          return True
        self.poco(text=" SIM-" + sim).click()
      sleep(10)
      if self.poco(text="SIM 卡应用1").exists():
        self.poco(text="SIM 卡应用1").click()
      if self.poco(text=part + "换号").exists():
        self.poco(text=part + "换号").click()
      else:
        self.poco("android:id/list").swipe([0, -0.3])
        sleep(1.0)
        self.poco(text=part + "换号").click()
      if self.poco(text="*SIM-" + sim).exists():
        self.poco("android:id/up").click()
        return True
      return False
    except:
      return False
