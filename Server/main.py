from PyQt4 import QtCore,QtGui
import gui
import sys
#import sysinfo
import simple_mqtt_test


class MainUiClass(QtGui.QMainWindow, gui.Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainUiClass, self).__init__(parent)
		self.setupUi(self)
		self.threadclass=ThreadClass()
		self.threadclass.start() 
		self.threadclass2=ThreadClass2()
		self.threadclass2.start() 
		self.threadclass3=ThreadClass3()
		self.threadclass3.start()
		self.connect(self.threadclass, QtCore.SIGNAL('temp1'),self.updateValue)  
		self.connect(self.threadclass, QtCore.SIGNAL('hum1'),self.updateValue2) 
		self.connect(self.threadclass, QtCore.SIGNAL('motion1'),self.updateValue3) 
		self.connect(self.threadclass2, QtCore.SIGNAL('gas2'),self.updateValue4) 
		self.connect(self.threadclass2, QtCore.SIGNAL('motion2'),self.updateValue5)
		self.connect(self.threadclass3, QtCore.SIGNAL('lat1'),self.updateValue6)
		self.connect(self.threadclass3, QtCore.SIGNAL('lon1'),self.updateValue7)
		self.connect(self.threadclass3, QtCore.SIGNAL('dis1'),self.updateValue8)
		  
		
	def updateValue(self,temp):
		self.lineEdit_temp.setText(str(temp))
		
	def updateValue2(self,hum):
		self.lineEdit_hum.setText(str(hum))
		
	def updateValue3(self,md1):
		self.lineEdit_motion.setText(str(md1))
	
	def updateValue4(self,gas):
		self.lineEdit_smoke.setText(str(gas))
	
	def updateValue5(self,md2):
		self.lineEdit_motion_2.setText(str(md2))
		
	def updateValue6(self,lat):
		self.lineEdit_GPSLoc.setText(str(lat))

	def updateValue7(self,lon):
		self.lineEdit_GPSLon.setText(str(lon))
		
	def updateValue8(self,dis):
		self.lineEdit_GPSDis.setText(str(dis))
		
class ThreadClass(QtCore.QThread):
	def __init__(self, parent=None):
		super(ThreadClass, self).__init__(parent)
	
	def run(self):
		while 1:
			temp=simple_mqtt_test.main1()
			hum=simple_mqtt_test.main2()
			md1=simple_mqtt_test.main3()
			self.emit(QtCore.SIGNAL('temp1'),temp)
			self.emit(QtCore.SIGNAL('hum1'),hum)
			self.emit(QtCore.SIGNAL('motion1'),md1)
			
class ThreadClass2(QtCore.QThread):
	def __init__(self, parent=None):
		super(ThreadClass2, self).__init__(parent)
	
	def run(self):
		while 1:
			gas = simple_mqtt_test.main4()
			md2=simple_mqtt_test.main5()
			self.emit(QtCore.SIGNAL('gas2'),gas)
			self.emit(QtCore.SIGNAL('motion2'),md2)



class ThreadClass3(QtCore.QThread):
	def __init__(self, parent=None):
		super(ThreadClass3, self).__init__(parent)
	
	def run(self):
		while 1:
			lat=simple_mqtt_test.main7()
			lon=simple_mqtt_test.main8()
			dis=simple_mqtt_test.main9()
			self.emit(QtCore.SIGNAL('lat1'),lat)
			self.emit(QtCore.SIGNAL('lon1'),lon)
			self.emit(QtCore.SIGNAL('dis1'),dis)


		
		
if __name__=='__main__':
	a=QtGui.QApplication(sys.argv)
	app=MainUiClass()
	app.show()
	a.exec_()
