from PyQt5 import QtWidgets
from Views.mainwindowView import Ui_Form
from PyQt5.QtGui import QIntValidator
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

class mainwindowmanager(QtWidgets.QWidget , Ui_Form):
    def __init__(self):
        super(mainwindowmanager,self).__init__()
        self.initui()
        self.answer = []
    def initui(self):
        self.setupUi(self)
        self.age_lin.setValidator(QIntValidator())
        self.sp_lin.setValidator(QIntValidator())
        self.al_lin.setValidator(QIntValidator())
        self.su_lin.setValidator(QIntValidator())
        self.bp_lin.setValidator(QIntValidator())
        self.show()
        self.resultbtn.clicked.connect(self.btnclicked)
    def refreshText(self):

        self.al_lin.setText('')
        self.age_lin.setText('')
        self.su_lin.setText('')
        self.sp_lin.setText('')
        self.bp_lin.setText('')
    def btnclicked(self):
        self.get_age = self.age_lin.text()
        self.get_bp = self.bp_lin.text()
        self.get_sg = self.sp_lin.text()
        self.get_al = self.al_lin.text()
        self.get_su = self.su_lin.text()
        if(len(self.get_age) > 0 and len(self.get_bp) > 0 and len(self.get_sg) > 0
         and len(self.get_al) > 0 and len(self.get_su)):

            xtest = [self.get_age , self.get_bp , self.get_sg , self.get_al ,self.get_su]
            xtest = np.array(xtest).reshape(1,-1)

            data = pd.read_csv('kidney_disease.csv', header=None, skiprows=1)
            df = pd.DataFrame(data)
            df2 = df.dropna(axis=0)

            X = df2.iloc[:, 1:6]
            Y = df2.iloc[:, -1]
            clf = svm.SVC(kernel='linear')

            x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, stratify=Y)

            clf.fit(x_train, y_train)
            clf.predict(xtest)
            preds = clf.predict(xtest)

            print(preds)
            if preds == 'ckd':
                self.refreshText()
                msg = QtWidgets.QMessageBox()
                msg.setText('Positive')
                msg.exec()

            else:
                self.refreshText()
                msg = QtWidgets.QMessageBox()
                msg.setText('Negative')
                msg.exec()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setText('Incorrect input , please try again !!!')
            msg.exec()
