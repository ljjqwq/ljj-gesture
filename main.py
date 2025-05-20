import sys
import os
import logging
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtGui import QIcon

# ---------------------- 优先初始化QApplication ----------------------
# 创建应用程序实例（必须在所有GUI组件之前）
app = QApplication(sys.argv)

# ---------------------- 禁用日志和标准输出 ----------------------
sys.stdout = open(os.devnull, 'w')
logging.disable(logging.CRITICAL)

# ---------------------- 添加自定义路径 ----------------------
sys.path.append("D:/YOLOGESTURE")
sys.path.append(os.path.join(os.getcwd(), "ui"))

# ---------------------- 延迟导入GUI相关模块 ----------------------
# 注意：确保在QApplication实例化后再导入包含QWidget的模块
from core.login_register import UiLoginRegisterQDialog
from yologesture.Window import YOLOGESTUREWindow as yologestureWindow
from yologesture.Window import YOLOGESTUREVSWindow as yologestureVSWindow
from yologesture.ChangeWindow import yologesture2vs, vs2yologesture
from utils import glo
from static.resources_rc import qInitResources
qInitResources()  # 加载资源

# ---------------------- 主启动类 ----------------------
class StartupMainWindow:
    def __init__(self):
        # 初始化登录界面
        self.login_dialog = UiLoginRegisterQDialog()
        self._setup_login_ui()
        1
        # 登录验证通过后进入主界面
        if self.login_dialog.exec() == QDialog.Accepted:
            username = self.login_dialog.logged_in_username
            self._setup_main_ui(username)

    def _setup_login_ui(self):
        """配置登录界面样式"""
        qss_file = QFile(':/QSS/qss/login_register.qss')
        if qss_file.open(QFile.ReadOnly | QFile.Text):
            try:
                style = qss_file.readAll().data().decode('UTF-8')
                self.login_dialog.setStyleSheet(style)
            finally:
                qss_file.close()

    def _setup_main_ui(self, username):
        """配置主窗口"""
        # 全局样式和图标设置
        app.setWindowIcon(QIcon('images/logo.ico'))
        app.setStyleSheet("QFrame { border: none; }")

        # 初始化YOLOGESTURE双模式窗口
        yshow = yologestureWindow(username=username)
        yshow_vs = yologestureVSWindow(username=username)
        
        # 全局变量管理
        glo._init()
        glo.set_value('yologesture', yshow)
        glo.set_value('yologesturevs', yshow_vs)

        # 窗口切换信号连接
        yshow.ui.src_vsmode.clicked.connect(yologesture2vs)
        yshow_vs.ui.src_singlemode.clicked.connect(vs2yologesture)

        # 显示主窗口
        yshow.show()

if __name__ == '__main__':
    # 启动主逻辑
    main_window = StartupMainWindow()
    sys.exit(app.exec())