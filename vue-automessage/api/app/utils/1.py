# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, devices=["android:///121.5.154.203:8555?cap_method=javacap&touch_method=adb",])


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

poco(text="SIM 卡应用1").click()
poco(text="1区换号").click()
poco(text=" SIM-3").click()


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
