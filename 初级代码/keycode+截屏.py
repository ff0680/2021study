caps = {
    "platformName": "Android",
    "platformVersion": "6.0",
    "deviceName": "emulator-5554",
    "appPackage": "com.xueqiu.android",  # aapt dump badging apk
    "appActivity": "com.xueqiu.android.view.WelcomeActivityAlias",
    "noReset": False
}

from appium.webdriver import Remote

driver = Remote(desired_capabilities=caps,
                command_executor='http://127.0.0.1:4723/wd/hub')  # 初始化Remote

# Android only  模拟物理按键：返回 拍照 电源 拨号  音量加减
driver.press_keycode(24)  # 按键号
driver.get_screenshot_as_file("保存后的文件名")  # 截屏
driver.background_app("秒")  # 将应用放在后台多长时间 -1：一直置于后台；
driver.lock()  # 锁屏
driver.unlock()  # 解锁
