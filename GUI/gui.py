# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new3.ui'
#
# Created: Mon Feb 19 14:57:30 2018
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(657, 380)
        MainWindow.setMinimumSize(QtCore.QSize(657, 380))
        MainWindow.setMaximumSize(QtCore.QSize(657, 380))
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(162, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_ConBrok = QtGui.QPushButton(self.centralwidget)
        self.pushButton_ConBrok.setMinimumSize(QtCore.QSize(125, 23))
        self.pushButton_ConBrok.setObjectName(_fromUtf8("pushButton_ConBrok"))
        self.gridLayout.addWidget(self.pushButton_ConBrok, 0, 1, 1, 1)
        self.Status = QtGui.QLineEdit(self.centralwidget)
        self.Status.setMinimumSize(QtCore.QSize(130, 20))
        self.Status.setReadOnly(True)
        self.Status.setObjectName(_fromUtf8("Status"))
        self.gridLayout.addWidget(self.Status, 0, 2, 1, 2)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(201, 291))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_temp = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_temp.setGeometry(QtCore.QRect(80, 30, 41, 20))
        self.lineEdit_temp.setAcceptDrops(False)
        self.lineEdit_temp.setReadOnly(True)
        self.lineEdit_temp.setObjectName(_fromUtf8("lineEdit_temp"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 61, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_hum = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_hum.setGeometry(QtCore.QRect(80, 80, 41, 20))
        self.lineEdit_hum.setReadOnly(True)
        self.lineEdit_hum.setObjectName(_fromUtf8("lineEdit_hum"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_motion = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_motion.setGeometry(QtCore.QRect(80, 140, 81, 20))
        self.lineEdit_motion.setReadOnly(True)
        self.lineEdit_motion.setObjectName(_fromUtf8("lineEdit_motion"))
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(201, 291))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.lineEdit_smoke = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_smoke.setGeometry(QtCore.QRect(80, 30, 51, 20))
        self.lineEdit_smoke.setAcceptDrops(False)
        self.lineEdit_smoke.setText(_fromUtf8(""))
        self.lineEdit_smoke.setReadOnly(True)
        self.lineEdit_smoke.setObjectName(_fromUtf8("lineEdit_smoke"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_motion_2 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_motion_2.setGeometry(QtCore.QRect(80, 80, 81, 20))
        self.lineEdit_motion_2.setReadOnly(True)
        self.lineEdit_motion_2.setObjectName(_fromUtf8("lineEdit_motion_2"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 80, 46, 13))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 2)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setMinimumSize(QtCore.QSize(211, 291))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit_GPSLoc = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_GPSLoc.setGeometry(QtCore.QRect(10, 60, 191, 81))
        self.lineEdit_GPSLoc.setReadOnly(True)
        self.lineEdit_GPSLoc.setObjectName(_fromUtf8("lineEdit_GPSLoc"))
        self.pushButton_Loc = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_Loc.setGeometry(QtCore.QRect(10, 160, 75, 23))
        self.pushButton_Loc.setObjectName(_fromUtf8("pushButton_Loc"))
        self.pushButton_FB = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_FB.setGeometry(QtCore.QRect(70, 250, 75, 23))
        self.pushButton_FB.setObjectName(_fromUtf8("pushButton_FB"))
        self.gridLayout.addWidget(self.groupBox_3, 1, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_ConBrok, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_ConBrok.toggle)
        QtCore.QObject.connect(self.pushButton_Loc, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_Loc.toggle)
        QtCore.QObject.connect(self.pushButton_FB, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_FB.toggle)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "                                                                                   Surviellance", None))
        self.label.setText(_translate("MainWindow", "Connect to the Broker", None))
        self.pushButton_ConBrok.setText(_translate("MainWindow", "Connect", None))
        self.Status.setText(_translate("MainWindow", "statuscon", None))
        self.Status.setPlaceholderText(_translate("MainWindow", "Status", None))
        self.groupBox.setTitle(_translate("MainWindow", "Node 1", None))
        self.label_2.setText(_translate("MainWindow", "Temperature:", None))
        self.lineEdit_temp.setPlaceholderText(_translate("MainWindow", "*C", None))
        self.label_3.setText(_translate("MainWindow", "Humidity:", None))
        self.lineEdit_hum.setPlaceholderText(_translate("MainWindow", "%", None))
        self.label_4.setText(_translate("MainWindow", "Motion:", None))
        self.lineEdit_motion.setPlaceholderText(_translate("MainWindow", "Neutral", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Node 2", None))
        self.lineEdit_smoke.setPlaceholderText(_translate("MainWindow", "Normal", None))
        self.label_5.setText(_translate("MainWindow", "Smoke", None))
        self.lineEdit_motion_2.setPlaceholderText(_translate("MainWindow", "Neutral", None))
        self.label_6.setText(_translate("MainWindow", "Motion:", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Node 3", None))
        self.label_7.setText(_translate("MainWindow", "GPS Location", None))
        self.lineEdit_GPSLoc.setPlaceholderText(_translate("MainWindow", "                        Location", None))
        self.pushButton_Loc.setText(_translate("MainWindow", "Get Location", None))
        self.pushButton_FB.setText(_translate("MainWindow", "Fall Back", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

