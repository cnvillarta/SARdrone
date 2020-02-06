# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ForgotPasswordAlt.ui'
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Resources/logo_svg.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_forgot = QtWidgets.QLabel(self.centralwidget)
        self.lbl_forgot.setGeometry(QtCore.QRect(200, 130, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(19)
        self.lbl_forgot.setFont(font)
        self.lbl_forgot.setStyleSheet("padding-left:9px;\n"
"padding-bottom: 4px;")
        self.lbl_forgot.setObjectName("lbl_forgot")
        self.lbl_sub1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sub1.setGeometry(QtCore.QRect(140, 170, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_sub1.setFont(font)
        self.lbl_sub1.setStyleSheet("padding-left:4px;\n"
"padding-bottom:10px;")
        self.lbl_sub1.setObjectName("lbl_sub1")
        self.lbl_sub2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sub2.setGeometry(QtCore.QRect(190, 190, 261, 18))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_sub2.setFont(font)
        self.lbl_sub2.setStyleSheet("padding-top:4px;\n"
"padding-left:6px;")
        self.lbl_sub2.setObjectName("lbl_sub2")
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(170, 290, 291, 31))
        self.btn_reset.setStyleSheet("QPushButton {\n"
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
        self.btn_reset.setObjectName("btn_reset")
        self.lbl_error = QtWidgets.QLabel(self.centralwidget)
        self.lbl_error.setGeometry(QtCore.QRect(170, 220, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.lbl_error.setFont(font)
        self.lbl_error.setStyleSheet("padding-bottom:7 rem;")
        self.lbl_error.setText("")
        self.lbl_error.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_error.setObjectName("lbl_error")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 330, 521, 16))
        self.line.setStyleSheet("margin-top:4px;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.app_logo = QtWidgets.QLabel(self.centralwidget)
        self.app_logo.setGeometry(QtCore.QRect(70, 20, 135, 114))
        self.app_logo.setText("")
        self.app_logo.setPixmap(QtGui.QPixmap("../Resources/aids_logo.png"))
        self.app_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.app_logo.setObjectName("app_logo")
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
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(112, 240, 351, 33))
        self.widget.setObjectName("widget")
        self.email_layout = QtWidgets.QHBoxLayout(self.widget)
        self.email_layout.setContentsMargins(0, 0, 0, 0)
        self.email_layout.setObjectName("email_layout")
        self.lbl_email = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_email.setFont(font)
        self.lbl_email.setStyleSheet("")
        self.lbl_email.setObjectName("lbl_email")
        self.email_layout.addWidget(self.lbl_email)
        self.txt_email = QtWidgets.QLineEdit(self.widget)
        self.txt_email.setMinimumSize(QtCore.QSize(291, 31))
        self.txt_email.setMaximumSize(QtCore.QSize(291, 31))
        self.txt_email.setStyleSheet("padding-left: 4px;")
        self.txt_email.setObjectName("txt_email")
        self.email_layout.addWidget(self.txt_email)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(90, 350, 371, 33))
        self.widget1.setObjectName("widget1")
        self.remember_layout = QtWidgets.QHBoxLayout(self.widget1)
        self.remember_layout.setContentsMargins(0, 0, 0, 0)
        self.remember_layout.setObjectName("remember_layout")
        self.lbl_remember = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_remember.setFont(font)
        self.lbl_remember.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_remember.setObjectName("lbl_remember")
        self.remember_layout.addWidget(self.lbl_remember)
        self.btn_forgot = QtWidgets.QPushButton(self.widget1)
        self.btn_forgot.setMinimumSize(QtCore.QSize(116, 31))
        self.btn_forgot.setMaximumSize(QtCore.QSize(116, 31))
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
        self.remember_layout.addWidget(self.btn_forgot)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txt_email, self.btn_reset)
        MainWindow.setTabOrder(self.btn_reset, self.btn_forgot)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AIDS – Forgot Password"))
        self.lbl_forgot.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#2c365d;\">Forgot password?</span></p></body></html>"))
        self.lbl_sub1.setText(_translate("MainWindow", "Enter the email address associated with your account below"))
        self.lbl_sub2.setText(_translate("MainWindow", "and we will send you a password reset code"))
        self.btn_reset.setText(_translate("MainWindow", "Request reset code"))
        self.aids_logo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#2c365d;\">AIDS</span></p></body></html>"))
        self.app_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#2c365d;\">Air-based Inspection Deployment System</span></p></body></html>"))
        self.lbl_email.setText(_translate("MainWindow", "Email :"))
        self.lbl_remember.setText(_translate("MainWindow", "Remembered your password?"))
        self.btn_forgot.setText(_translate("MainWindow", "Try logging in"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
