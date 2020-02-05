# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginAlt.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        MainWindow.setBaseSize(QtCore.QSize(600, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Resources/logo_svg.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.app_logo = QtWidgets.QLabel(self.centralwidget)
        self.app_logo.setGeometry(QtCore.QRect(70, 20, 135, 114))
        self.app_logo.setText("")
        self.app_logo.setPixmap(QtGui.QPixmap("../Resources/aids_logo.png"))
        self.app_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.app_logo.setObjectName("app_logo")
        self.hline = QtWidgets.QFrame(self.centralwidget)
        self.hline.setGeometry(QtCore.QRect(30, 310, 531, 20))
        self.hline.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hline.setObjectName("hline")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(370, 270, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 176, 6);\n"
"border: 1.2px solid #ff9d07;\n"
"outline: none;}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 157, 7);\n"
"outline: none;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(254, 140, 8);\n"
"outline: none;\n"
"border: none;\n"
"}\n"
"\n"
"\n"
"")
        self.btn_login.setObjectName("btn_login")
        self.lbl_response = QtWidgets.QLabel(self.centralwidget)
        self.lbl_response.setGeometry(QtCore.QRect(180, 130, 311, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.lbl_response.sizePolicy().hasHeightForWidth())
        self.lbl_response.setSizePolicy(sizePolicy)
        self.lbl_response.setMinimumSize(QtCore.QSize(311, 20))
        self.lbl_response.setMaximumSize(QtCore.QSize(311, 20))
        self.lbl_response.setBaseSize(QtCore.QSize(5, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_response.setFont(font)
        self.lbl_response.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_response.setObjectName("lbl_response")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(200, 40, 293, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.aids_logo = QtWidgets.QLabel(self.layoutWidget)
        self.aids_logo.setMinimumSize(QtCore.QSize(291, 43))
        self.aids_logo.setMaximumSize(QtCore.QSize(291, 43))
        font = QtGui.QFont()
        font.setFamily("Audiowide")
        font.setPointSize(28)
        font.setKerning(True)
        self.aids_logo.setFont(font)
        self.aids_logo.setObjectName("aids_logo")
        self.verticalLayout.addWidget(self.aids_logo)
        self.app_name = QtWidgets.QLabel(self.layoutWidget)
        self.app_name.setMinimumSize(QtCore.QSize(291, 20))
        self.app_name.setMaximumSize(QtCore.QSize(291, 20))
        font = QtGui.QFont()
        font.setFamily("Barlow Medium")
        font.setPointSize(12)
        font.setKerning(True)
        self.app_name.setFont(font)
        self.app_name.setObjectName("app_name")
        self.verticalLayout.addWidget(self.app_name)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(130, 157, 344, 33))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.username_layout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.username_layout.setContentsMargins(0, 0, 0, 0)
        self.username_layout.setObjectName("username_layout")
        self.user_icon = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_icon.sizePolicy().hasHeightForWidth())
        self.user_icon.setSizePolicy(sizePolicy)
        self.user_icon.setMinimumSize(QtCore.QSize(66, 31))
        self.user_icon.setMaximumSize(QtCore.QSize(66, 31))
        self.user_icon.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.user_icon.setFont(font)
        self.user_icon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.user_icon.setText("")
        self.user_icon.setPixmap(QtGui.QPixmap("../Resources/user_icon.png"))
        self.user_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.user_icon.setObjectName("user_icon")
        self.username_layout.addWidget(self.user_icon)
        self.txt_username = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_username.sizePolicy().hasHeightForWidth())
        self.txt_username.setSizePolicy(sizePolicy)
        self.txt_username.setMinimumSize(QtCore.QSize(270, 31))
        self.txt_username.setMaximumSize(QtCore.QSize(270, 31))
        self.txt_username.setSizeIncrement(QtCore.QSize(5, 0))
        self.txt_username.setBaseSize(QtCore.QSize(5, 0))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.txt_username.setFont(font)
        self.txt_username.setStyleSheet("padding-left: 4px;")
        self.txt_username.setObjectName("txt_username")
        self.username_layout.addWidget(self.txt_username)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(150, 210, 321, 33))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.password_layout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.password_layout.setContentsMargins(0, 0, 0, 0)
        self.password_layout.setObjectName("password_layout")
        self.password_icon = QtWidgets.QLabel(self.layoutWidget2)
        self.password_icon.setText("")
        self.password_icon.setPixmap(QtGui.QPixmap("../Resources/padlock_icon.png"))
        self.password_icon.setObjectName("password_icon")
        self.password_layout.addWidget(self.password_icon)
        self.txt_password = QtWidgets.QLineEdit(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.txt_password.sizePolicy().hasHeightForWidth())
        self.txt_password.setSizePolicy(sizePolicy)
        self.txt_password.setMinimumSize(QtCore.QSize(270, 31))
        self.txt_password.setMaximumSize(QtCore.QSize(270, 31))
        self.txt_password.setSizeIncrement(QtCore.QSize(5, 0))
        self.txt_password.setBaseSize(QtCore.QSize(5, 0))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.txt_password.setFont(font)
        self.txt_password.setStyleSheet("padding-left: 4px;")
        self.txt_password.setText("")
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setObjectName("txt_password")
        self.password_layout.addWidget(self.txt_password)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(110, 343, 364, 33))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.forgotpass_layout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.forgotpass_layout.setContentsMargins(0, 0, 0, 0)
        self.forgotpass_layout.setObjectName("forgotpass_layout")
        self.lbl_forgot = QtWidgets.QLabel(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_forgot.sizePolicy().hasHeightForWidth())
        self.lbl_forgot.setSizePolicy(sizePolicy)
        self.lbl_forgot.setMinimumSize(QtCore.QSize(187, 31))
        self.lbl_forgot.setMaximumSize(QtCore.QSize(187, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_forgot.setFont(font)
        self.lbl_forgot.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_forgot.setObjectName("lbl_forgot")
        self.forgotpass_layout.addWidget(self.lbl_forgot)
        self.btn_forgot = QtWidgets.QPushButton(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_forgot.sizePolicy().hasHeightForWidth())
        self.btn_forgot.setSizePolicy(sizePolicy)
        self.btn_forgot.setMinimumSize(QtCore.QSize(169, 31))
        self.btn_forgot.setMaximumSize(QtCore.QSize(169, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.btn_forgot.setFont(font)
        self.btn_forgot.setStyleSheet("QPushButton {\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(201, 201, 201);\n"
"border: 1.2px solid #ABABAB;\n"
"outline: none;}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(171, 171, 171);\n"
"outline: none;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(129, 129, 129);\n"
"outline: none;\n"
"border: none;\n"
"}\n"
"\n"
"\n"
"")
        self.btn_forgot.setObjectName("btn_forgot")
        self.forgotpass_layout.addWidget(self.btn_forgot)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txt_username, self.txt_password)
        MainWindow.setTabOrder(self.txt_password, self.btn_login)
        MainWindow.setTabOrder(self.btn_login, self.btn_forgot)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AIDS Login"))
        self.btn_login.setText(_translate("MainWindow", "Login"))
        self.lbl_response.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.aids_logo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#2c365d;\">AIDS</span></p></body></html>"))
        self.app_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#2c365d;\">Air-based Inspection Deployment System</span></p></body></html>"))
        self.txt_username.setPlaceholderText(_translate("MainWindow", "User ID"))
        self.txt_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lbl_forgot.setText(_translate("MainWindow", "Forgot Password?"))
        self.btn_forgot.setText(_translate("MainWindow", "Reset Password"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
