from PyQt4 import QtCore,QtGui
import gui
import sys
import sysinfo


class MainUiClass(QtGui.QMainWindow, gui.Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainUiClass, self).__init__(parent)
		self.setupUi(self)
		self.threadclass=ThreadClass()
		self.threadclass.start() 
		self.connect(self.threadclass, QtCore.SIGNAL('cpuvalue'),self.updateValue)  
		
	def updateValue(self,val):
		self.lineEdit_temp.setText(str(val))
		
class ThreadClass(QtCore.QThread):
	def __init__(self, parent=None):
		super(ThreadClass, self).__init__(parent)
		
	def __del__(self):
		self.wait(200000)
	
	def run(self):
		while 1:
			val=sysinfo.getCPU()
			self.emit(QtCore.SIGNAL('cpuvalue'),val)

class ThreadClass(QtCore.QThread):
	def __init__(self, parent=None):
		super(ThreadClass, self).__init__(parent)
	
	def run(self):
		while 1:
			val=sysinfo.getCPU()
			self.emit(QtCore.SIGNAL('cpuvalue'),val)
		
if __name__=='__main__':
	a=QtGui.QApplication(sys.argv)
	app=MainUiClass()
	app.show()
	a.exec_()
