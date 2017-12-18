# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
import sys
from Ui_my_excel import Ui_MainWindow
from glob import glob
from os.path import join
import os
from xlrd import open_workbook
import re
import shutil

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    my_dir=''
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.my_dir = QtGui.QFileDialog.getExistingDirectory(self,u'打开文件夹','/')
        print u'%s'%self.my_dir
    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet

        print 'ok'
        print unicode(self.my_dir)
        print glob(join(unicode(self.my_dir),'*.xlsx'))#使用glob函数，可以枚举文件
        print unicode(self.lineEdit.text())
        my_list = re.split(' ',self.lineEdit.text())
        """
        for l in my_list:
            print unicode(l)
        """
        number = 0
        for file in glob(join(unicode(self.my_dir),'*.xlsx')):
            print file

            wb = open_workbook(file.replace(u'/',u'\\'))
            for s in wb.sheets():
                for row in range(s.nrows):
                    for col in range(s.ncols):
                        if s.cell(row,col).value:
                            print s.cell(row,col).value,
                            for l in my_list:
                                if unicode(l) in unicode(s.cell(row,col).value):
                                    self.textBrowser.append(file)
                                    self.textBrowser.append(u'%d行 %d列'%(row+1,col+1))
                                    fileList = file.split('\\')
                                    print fileList[-1]
                                    if not os.path.exists(unicode(self.my_dir)+u'\\符合条件\\'+fileList[-1]):
                                        number+=1
                                        if not os.path.exists(unicode(self.my_dir+u'\\符合条件')):
                                            os.mkdir(unicode(self.my_dir)+u'\\符合条件')
                                            self.textBrowser.append(u'创建文件夹成功 %s'%unicode((self.my_dir)+u'\\符合条件'))
                                        else:
                                            self.textBrowser.append(u'文件夹已经存在，不需要重复创建')
                                        self.textBrowser.append(u'正在复制文件')
                                        shutil.copy(file,unicode(self.my_dir)+u'\\符合条件')
                                        self.textBrowser.append(u'一个文件复制完成')
                    print ''
        self.textBrowser.append(u'文件共处理了%s文件'%str(number))
        """
        if os.path.isdir(self.my_dir):
            #print os.listdir(self.my_dir)#返回所有文件
            for file in os.listdir(self.my_dir):
                print file.decode('gbk')
                if file[-5:]=='.xlsx':
                    print 'find file:',file.decode('gbk')
        """

    
    @pyqtSignature("")
    def on_actionOpen_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        
    
    @pyqtSignature("")
    def on_actionClose_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        
    
    @pyqtSignature("")
    def on_actionExit_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        sys.exit(0)
        
    
    @pyqtSignature("")
    def on_actionAbout_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        
    
    @pyqtSignature("")
    def on_actionInstruction_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
