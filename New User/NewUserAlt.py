# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewUserAlt.ui'
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 160, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("padding-left:6px;\n"
"padding-bottom:10px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 190, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("padding-bottom:6px;\n"
"padding-left:6px;")
        self.label_2.setObjectName("label_2")
        self.lbl_error = QtWidgets.QLabel(self.centralwidget)
        self.lbl_error.setGeometry(QtCore.QRect(180, 220, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.lbl_error.setFont(font)
        self.lbl_error.setStyleSheet("padding-bottom:7 rem;")
        self.lbl_error.setText("")
        self.lbl_error.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_error.setObjectName("lbl_error")
        self.btnChange = QtWidgets.QPushButton(self.centralwidget)
        self.btnChange.setGeometry(QtCore.QRect(180, 340, 291, 31))
        self.btnChange.setStyleSheet("QPushButton {\n"
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
        self.btnChange.setObjectName("btnChange")
        self.lbl_changePass = QtWidgets.QLabel(self.centralwidget)
        self.lbl_changePass.setGeometry(QtCore.QRect(200, 120, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(19)
        self.lbl_changePass.setFont(font)
        self.lbl_changePass.setStyleSheet("padding-left:7px;\n"
"padding-bottom: 4px;")
        self.lbl_changePass.setObjectName("lbl_changePass")
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
        self.widget.setGeometry(QtCore.QRect(73, 240, 401, 33))
        self.widget.setObjectName("widget")
        self.newPass_layout = QtWidgets.QHBoxLayout(self.widget)
        self.newPass_layout.setContentsMargins(0, 0, 0, 0)
        self.newPass_layout.setObjectName("newPass_layout")
        self.lbl_newpass = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_newpass.setFont(font)
        self.lbl_newpass.setStyleSheet("")
        self.lbl_newpass.setObjectName("lbl_newpass")
        self.newPass_layout.addWidget(self.lbl_newpass)
        self.txtNewPass = QtWidgets.QLineEdit(self.widget)
        self.txtNewPass.setMinimumSize(QtCore.QSize(291, 31))
        self.txtNewPass.setMaximumSize(QtCore.QSize(291, 31))
        self.txtNewPass.setStyleSheet("margin-right:4px;\n"
"padding-left: 4px;\n"
"")
        self.txtNewPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtNewPass.setObjectName("txtNewPass")
        self.newPass_layout.addWidget(self.txtNewPass)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(48, 291, 421, 33))
        self.widget1.setObjectName("widget1")
        self.confirmPass_layout = QtWidgets.QHBoxLayout(self.widget1)
        self.confirmPass_layout.setContentsMargins(0, 0, 0, 0)
        self.confirmPass_layout.setObjectName("confirmPass_layout")
        self.lbl_confirmPass = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.lbl_confirmPass.setFont(font)
        self.lbl_confirmPass.setStyleSheet("")
        self.lbl_confirmPass.setObjectName("lbl_confirmPass")
        self.confirmPass_layout.addWidget(self.lbl_confirmPass)
        self.txtConfirmPass = QtWidgets.QLineEdit(self.widget1)
        self.txtConfirmPass.setMinimumSize(QtCore.QSize(291, 31))
        self.txtConfirmPass.setMaximumSize(QtCore.QSize(291, 31))
        self.txtConfirmPass.setStyleSheet("margin-left:4px;\n"
"padding-left: 4px;")
        self.txtConfirmPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtConfirmPass.setObjectName("txtConfirmPass")
        self.confirmPass_layout.addWidget(self.txtConfirmPass)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtNewPass, self.txtConfirmPass)
        MainWindow.setTabOrder(self.txtConfirmPass, self.btnChange)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AIDS – Reset Password"))
        self.label.setText(_translate("MainWindow", "Password must have at least 8 characters, an upper case (A-Z),"))
        self.label_2.setText(_translate("MainWindow", "and a number (0-9). Special Characters are optional"))
        self.btnChange.setText(_translate("MainWindow", "Change Password"))
        self.lbl_changePass.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#2c365d;\">Change Password</span></p></body></html>"))
        self.aids_logo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#2c365d;\">AIDS</span></p></body></html>"))
        self.app_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#2c365d;\">Air-based Inspection Deployment System</span></p></body></html>"))
        self.lbl_newpass.setText(_translate("MainWindow", "New Password :"))
        self.lbl_confirmPass.setText(_translate("MainWindow", "Re-enter Password :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
