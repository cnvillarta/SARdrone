# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomepageAlt.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1071, 739)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1071, 739))
        MainWindow.setMaximumSize(QtCore.QSize(1071, 739))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Resources/logo_svg.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table_pilots = QtWidgets.QTableWidget(self.centralwidget)
        self.table_pilots.setGeometry(QtCore.QRect(30, 130, 1011, 551))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_pilots.sizePolicy().hasHeightForWidth())
        self.table_pilots.setSizePolicy(sizePolicy)
        self.table_pilots.setAutoFillBackground(False)
        self.table_pilots.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_pilots.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_pilots.setRowCount(2)
        self.table_pilots.setColumnCount(4)
        self.table_pilots.setObjectName("table_pilots")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        item.setFont(font)
        item.setBackground(QtGui.QColor(203, 203, 203))
        self.table_pilots.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        item.setFont(font)
        item.setBackground(QtGui.QColor(203, 203, 203))
        self.table_pilots.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        item.setFont(font)
        item.setBackground(QtGui.QColor(203, 203, 203))
        self.table_pilots.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        item.setFont(font)
        item.setBackground(QtGui.QColor(203, 203, 203))
        self.table_pilots.setHorizontalHeaderItem(3, item)
        self.table_pilots.horizontalHeader().setVisible(True)
        self.table_pilots.horizontalHeader().setCascadingSectionResizes(False)
        self.table_pilots.horizontalHeader().setHighlightSections(True)
        self.table_pilots.horizontalHeader().setSortIndicatorShown(True)
        self.table_pilots.horizontalHeader().setStretchLastSection(True)
        self.table_pilots.verticalHeader().setVisible(False)
        self.table_pilots.verticalHeader().setSortIndicatorShown(False)
        self.table_pilots.verticalHeader().setStretchLastSection(False)
        self.table_pilots.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.table_pilots.setColumnWidth(0,100)
        self.table_pilots.horizontalHeader().setSectionResizeMode(0,QtWidgets.QHeaderView.Fixed)
        self.table_pilots.horizontalHeader().setSectionResizeMode(1,QtWidgets.QHeaderView.Stretch)
        self.table_pilots.horizontalHeader().setSectionResizeMode(2,QtWidgets.QHeaderView.Stretch)
        self.table_pilots.horizontalHeader().setSectionResizeMode(3,QtWidgets.QHeaderView.Stretch)
        #create buttons inside table cell
        layout = QtWidgets.QHBoxLayout()
        btn_view = QtWidgets.QPushButton()
        btn_delete = QtWidgets.QPushButton()
        #btn_view.setText('View')
        btn_view.setFixedHeight(34)
        btn_delete.setFixedHeight(34)
        btn_delete.setIcon(QtGui.QIcon("C:/Users/Hanjuu/Documents/AIDS (GUI)/Resources/trash_delete_2.png"))
        btn_delete.setIconSize(QtCore.QSize(22,22))
        btn_view.setIcon(QtGui.QIcon("C:/Users/Hanjuu/Documents/AIDS (GUI)/Resources/file_view.png"))
        btn_view.setIconSize(QtCore.QSize(22,22))
        #btn_delete.setText('Delete')
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        btn_view.setFont(font)
        btn_delete.setFont(font)
        btn_delete.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"background-color: #E53935;\n"
"border: 1.2px solid #D32F2F;\n"
"outline: none;}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #D32F2F;\n"
"outline: none;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #C62828;\n"
"outline: none;\n"
"border: none;\n"
"}\n"
"\n"
"\n"
"")
        btn_view.setStyleSheet("QPushButton {\n"
"    background-color: #1E88E5;\n"
"    color: rgb(255, 255, 255);\n"
"border: 1.2px solid #1976D2;\n"
"outline: none;}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #1976D2;\n"
"outline: none;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #1565C0;\n"
"outline: none;\n"
"border: none;\n"
"}\n"
"\n"
"\n"
"")
        btn_view.setCursor(QtCore.Qt.PointingHandCursor)
        btn_delete.setCursor(QtCore.Qt.PointingHandCursor)
        layout.addStretch()
        layout.addWidget(btn_view,20)
        layout.addWidget(btn_delete,20)

        cellWidget = QtWidgets.QWidget()
        cellWidget.setLayout(layout)

        self.table_pilots.setCellWidget(0,3,cellWidget) #buttons placement
        self.table_pilots.horizontalHeader().setStyleSheet( "QHeaderView::section{"
            "border-top:0px solid #D8D8D8;"
            "border-left:0px solid #D8D8D8;"
            "border-right:1px solid #D8D8D8;"
            "border-bottom: 1px solid #D8D8D8;"
            "background-color:white;"
            "padding:4px;"
        "}"
        "QTableCornerButton::section{"
            "border-top:0px solid #D8D8D8;"
            "border-left:0px solid #D8D8D8;"
            "border-right:1px solid #D8D8D8;"
            "border-bottom: 1px solid #D8D8D8;"
            "background-color:white;"
        "}" );

        #remove select trigger
        self.table_pilots.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.table_pilots.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        #remove dotted border
        self.table_pilots.setFocusPolicy(QtCore.Qt.NoFocus) 

        self.btn_operations = QtWidgets.QPushButton(self.centralwidget)
        self.btn_operations.setGeometry(QtCore.QRect(820, 690, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.btn_operations.setFont(font)
        self.btn_operations.setStyleSheet("QPushButton {\n"
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
        self.btn_operations.setObjectName("btn_operations")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(30, 90, 121, 31))
        self.btn_add.setMinimumSize(QtCore.QSize(121, 31))
        self.btn_add.setMaximumSize(QtCore.QSize(121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.btn_add.setFont(font)
        self.btn_add.setIcon(QtGui.QIcon("C:/Users/Hanjuu/Documents/AIDS (GUI)/Resources/add_user_2.png"))
        self.btn_add.setIconSize(QtCore.QSize(22,22))
        self.btn_add.setStyleSheet("QPushButton {\n"
"background-color: #4CAF50;\n"
"color: rgb(255, 255, 255);\n"
"border: 1.2px solid #43A047;\n"
"outline: none;}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #43A047;\n"
"outline: none;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #388E3C;\n"
"outline: none;\n"
"border: none;\n"
"}\n"
"\n"
"\n"
"")
        self.btn_add.setObjectName("btn_add")
        self.lbl_registered = QtWidgets.QLabel(self.centralwidget)
        self.lbl_registered.setGeometry(QtCore.QRect(30, 20, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(29)
        self.lbl_registered.setFont(font)
        self.lbl_registered.setObjectName("lbl_registered")
        self.searchbar = QtWidgets.QLineEdit(self.centralwidget)
        self.searchbar.setGeometry(QtCore.QRect(700, 90, 201, 31))
        self.searchbar.setMinimumSize(QtCore.QSize(201, 31))
        self.searchbar.setMaximumSize(QtCore.QSize(201, 31))
        self.searchbar.setStyleSheet("padding-left: 4px;")
        self.searchbar.setText("")
        self.searchbar.setObjectName("searchbar")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(920, 90, 121, 31))
        self.btn_search.setMinimumSize(QtCore.QSize(121, 31))
        self.btn_search.setMaximumSize(QtCore.QSize(121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.btn_search.setFont(font)
        self.btn_search.setIcon(QtGui.QIcon("C:/Users/Hanjuu/Documents/AIDS (GUI)/Resources/search_white.png"))
        self.btn_search.setIconSize(QtCore.QSize(22,22))
        self.btn_search.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
" background-color: #26A69A;\n"
"border: 1.2px solid #009688;\n"
"outline: none;}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #009688;\n"
"outline: none;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #00897B;\n"
"outline: none;\n"
"border: none;\n"
"}\n"
"\n"
"\n"
"")
        self.btn_search.setObjectName("btn_search")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(680, 17, 361, 33))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_user = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lbl_user.setFont(font)
        self.lbl_user.setText("")
        self.lbl_user.setScaledContents(False)
        self.lbl_user.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_user.setObjectName("lbl_user")
        self.horizontalLayout.addWidget(self.lbl_user)
        self.btn_logout = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_logout.setMinimumSize(QtCore.QSize(121, 31))
        self.btn_logout.setMaximumSize(QtCore.QSize(121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.btn_logout.setFont(font)
        self.btn_logout.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"background-color: #E53935;\n"
"border: 1.2px solid #D32F2F;\n"
"outline: none;}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #D32F2F;\n"
"outline: none;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #C62828;\n"
"outline: none;\n"
"border: none;\n"
"}\n"
"\n"
"\n"
"")
        self.btn_logout.setObjectName("btn_logout")
        self.horizontalLayout.addWidget(self.btn_logout)

        ####### Delete Dialog (Delete Pilot)

        """msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Delete Pilot")
        msgBox.setWindowIcon(QtGui.QIcon('../../Resources/logo_svg.svg'))
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setText("Are you sure you want to delete this pilot?")
        msgBox.setInformativeText("This process cannot be undone")
        msgBox.addButton(QtWidgets.QMessageBox.Cancel)
        delete = msgBox.addButton(QtWidgets.QMessageBox.Yes)
        delete.setText('Delete')
        

        msgBox.setDefaultButton(QtWidgets.QMessageBox.Cancel)
        ret = msgBox.exec_()"""

        ########


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_logout, self.btn_add)
        MainWindow.setTabOrder(self.btn_add, self.searchbar)
        MainWindow.setTabOrder(self.searchbar, self.btn_search)
        MainWindow.setTabOrder(self.btn_search, self.table_pilots)
        MainWindow.setTabOrder(self.table_pilots, self.btn_operations)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AIDS – Home [Administrator]"))
        self.table_pilots.setSortingEnabled(True)
        item = self.table_pilots.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.table_pilots.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Last Name"))
        item = self.table_pilots.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "First Name"))
        item = self.table_pilots.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Actions"))
        self.btn_operations.setText(_translate("MainWindow", "Access Previous Operations"))
        self.btn_add.setText(_translate("MainWindow", " Add Pilot"))
        self.lbl_registered.setText(_translate("MainWindow", "REGISTERED PILOTS"))
        self.btn_search.setText(_translate("MainWindow", "Search"))
        self.btn_logout.setText(_translate("MainWindow", "Logout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
