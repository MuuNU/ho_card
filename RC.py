# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(340, 410)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(340, 410))
        MainWindow.setMaximumSize(QSize(340, 410))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 3, 321, 401))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAcceptDrops(False)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.checkBox_2 = QCheckBox(self.layoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_2.addWidget(self.checkBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_5 = QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_3.addWidget(self.lineEdit_5)

        self.checkBox = QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_3.addWidget(self.checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(True)

        self.horizontalLayout_7.addWidget(self.comboBox)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_7.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_7.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.listWidget = QListWidget(self.layoutWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.lineEdit)
        self.label_2.setBuddy(self.lineEdit_2)
        self.label_3.setBuddy(self.lineEdit_5)
        self.label_8.setBuddy(self.comboBox)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineEdit_2, self.lineEdit_5)
        QWidget.setTabOrder(self.lineEdit_5, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.checkBox_2)
        QWidget.setTabOrder(self.checkBox_2, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.listWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.lineEdit.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Select group", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Create Rocket-Chat account", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
    # retranslateUi
