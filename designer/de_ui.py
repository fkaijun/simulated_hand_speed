# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'de_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(339, 242)
        MainWindow.setWindowOpacity(0.8)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout.addWidget(self.line_6)
        self.add_layout = QtWidgets.QHBoxLayout()
        self.add_layout.setObjectName("add_layout")
        self.verticalLayout.addLayout(self.add_layout)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hour = QtWidgets.QSpinBox(self.centralwidget)
        self.hour.setMinimum(1)
        self.hour.setMaximum(24)
        self.hour.setProperty("value", 10)
        self.hour.setObjectName("hour")
        self.horizontalLayout.addWidget(self.hour)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.minute = QtWidgets.QSpinBox(self.centralwidget)
        self.minute.setMaximum(59)
        self.minute.setObjectName("minute")
        self.horizontalLayout_3.addWidget(self.minute)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.second = QtWidgets.QSpinBox(self.centralwidget)
        self.second.setMaximum(59)
        self.second.setObjectName("second")
        self.horizontalLayout_2.addWidget(self.second)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setObjectName("start_btn")
        self.verticalLayout.addWidget(self.start_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 339, 26))
        self.menubar.setObjectName("menubar")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu_deam_help = QtWidgets.QAction(MainWindow)
        self.menu_deam_help.setObjectName("menu_deam_help")
        self.menuhelp.addAction(self.menu_deam_help)
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HandSpeed"))
        self.label_5.setText(_translate("MainWindow", "?????????????????????????????????????????????????????????"))
        self.label_4.setText(_translate("MainWindow", "???????????????????????????????????????????????????"))
        self.label.setText(_translate("MainWindow", "???"))
        self.label_3.setText(_translate("MainWindow", "???"))
        self.label_2.setText(_translate("MainWindow", "???"))
        self.start_btn.setText(_translate("MainWindow", "??????"))
        self.menuhelp.setTitle(_translate("MainWindow", "help"))
        self.menu_deam_help.setText(_translate("MainWindow", "Deam"))
