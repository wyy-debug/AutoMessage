# -*- encoding=utf8 -*-
from airtest.core.api import *
from airtest.cli.parser import cli_setup

class poco_device:

  def __init__(self):
    auto_setup(__file__, devices=["android:///121.5.154.203:8555?cap_method=javacap&touch_method=adb", ])
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

  # part 1区 xxx区
  # sim 1 - 12
  #
  def change_call(self, part, sim):
    try:
      self.poco(text="SIM 卡应用1").click()
      self.poco(text=part + "换号").click()
      self.poco(text=" SIM-" + sim).click()
      return True
    except:
      return False
