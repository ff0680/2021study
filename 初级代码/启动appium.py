# 初始化参数
"""
掌握内容：
appium自动化
步骤
    1.系统
    2.系统版本号
    3.设备名称 adb device
    4.app的包名
    5.app的启动名（进入app的哪个页面）
运行代码之前：
    1.手机和appium已连接
    2.运行appium service

"""
import time

#参数
caps = {
    "platformName": "Android",
    "platformVersion": "6.0",
    "deviceName": "192.168.56.101:5555",
    "appPackage": "com.xueqiu.android",  # aapt dump badging apk
    "appActivity": ".view.WelcomeActivityAlias",
    "noReset": False
}

from appium.webdriver import Remote

driver = Remote(desired_capabilities=caps,
                command_executor='http://127.0.0.1:4723/wd/hub')  # 初始化Remote

# 退出会话
# driver.quit()

# 打印desired_capabilities
# print(driver.desired_capabilities)
#
# # 查看当前的包名
# print(driver.current_package)
#
# # 查看当前的页面入口，利用这个去切换页面
# print(driver.current_activity)

# 查看当前的上下文（环境） native  web
# print(driver.current_context)
#
# # 查看源码（在web环境下面，打印html源代码  在native中，打印xml）
# print(driver.page_source)
#
# # 设备时间
# print(driver.device_time)
time.sleep(4)

driver.find_element_by_id("com.xueqiu.android:id/tv_agree").click()

# 跳转到其他页面上 启动app
# driver.start_activity("com.xueqiu.android","com.xueqiu.gear.common.js.SnowballWebViewActivity")

# time.sleep(10)






