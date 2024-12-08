# Form implementation generated from reading ui file 'ThemTaiKhoan.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox
from Controller.TaiKhoanController import TaiKhoanController

class Ui_Dialog(object):
    def __init__(self, main_window):
        self.main_window = main_window
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(627, 429)
        Dialog.setStyleSheet("background-color: #D0F9FD;")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(220, 20, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Favicon = QtWidgets.QLabel(parent=Dialog)
        self.Favicon.setGeometry(QtCore.QRect(40, 0, 71, 61))
        self.Favicon.setText("")
        self.Favicon.setObjectName("Favicon")
        self.line = QtWidgets.QFrame(parent=Dialog)
        self.line.setGeometry(QtCore.QRect(0, 60, 621, 16))
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.txtTaiKhoan = QtWidgets.QTextEdit(parent=Dialog)
        self.txtTaiKhoan.setGeometry(QtCore.QRect(210, 110, 191, 31))
        self.txtTaiKhoan.setObjectName("txtTaiKhoan")
        self.txtMatKhau = QtWidgets.QTextEdit(parent=Dialog)
        self.txtMatKhau.setGeometry(QtCore.QRect(210, 180, 191, 31))
        self.txtMatKhau.setObjectName("txtMatKhau")
        self.txtRole = QtWidgets.QTextEdit(parent=Dialog)
        self.txtRole.setGeometry(QtCore.QRect(210, 250, 191, 31))
        self.txtRole.setObjectName("txtRole")
        self.iconTaiKhoan = QtWidgets.QLabel(parent=Dialog)
        self.iconTaiKhoan.setGeometry(QtCore.QRect(180, 116, 21, 20))
        self.iconTaiKhoan.setText("")
        self.iconTaiKhoan.setObjectName("iconTaiKhoan")
        self.iconMatKhau = QtWidgets.QLabel(parent=Dialog)
        self.iconMatKhau.setGeometry(QtCore.QRect(180, 189, 21, 21))
        self.iconMatKhau.setText("")
        self.iconMatKhau.setObjectName("iconMatKhau")
        self.iconRole = QtWidgets.QLabel(parent=Dialog)
        self.iconRole.setGeometry(QtCore.QRect(180, 250, 21, 20))
        self.iconRole.setText("")
        self.iconRole.setObjectName("iconRole")
        self.btnThemTaiKhoan = QtWidgets.QPushButton(parent=Dialog)
        self.btnThemTaiKhoan.setGeometry(QtCore.QRect(220, 340, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnThemTaiKhoan.setFont(font)
        self.btnThemTaiKhoan.setObjectName("btnThemTaiKhoan")
        self.btnQuayVe = QtWidgets.QPushButton(parent=Dialog)
        self.btnQuayVe.setGeometry(QtCore.QRect(510, 390, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnQuayVe.setFont(font)
        self.btnQuayVe.setObjectName("btnQuayVe")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #================================CSS===========================================
        #CSS Favicon
        qixmap = QPixmap("../Access/Icon/favicon.jpg")
        self.Favicon.setPixmap(qixmap)
        self.Favicon.setScaledContents(True)

        qixmap = QPixmap("../Access/Icon/user-solid.svg")
        self.iconTaiKhoan.setPixmap(qixmap)
        self.iconTaiKhoan.setScaledContents(True)

        qixmap = QPixmap("../Access/Icon/password-solid.svg")
        self.iconMatKhau.setPixmap(qixmap)
        self.iconMatKhau.setScaledContents(True)

        qixmap = QPixmap("../Access/Icon/role.png")
        self.iconRole.setPixmap(qixmap)
        self.iconRole.setScaledContents(True)
        #CSS label
        self.label.setStyleSheet("""
                    color: #FF4500;
                    font-weight: bold;
                """)
        #Css button
        self.btnThemTaiKhoan.setIcon(QIcon("../Access/Icon/update.png"))
        self.btnThemTaiKhoan.setIconSize(QSize(30, 30))
        self.btnQuayVe.setIcon(QIcon("../Access/Icon/Quayve.png"))
        self.btnQuayVe.setIconSize(QSize(30, 30))
        #CSS textedit

        self.txtTaiKhoan.setStyleSheet("""
                                        background-color: white;
                                        color: black;
        """)
        self.txtMatKhau.setStyleSheet("""
                                        background-color: white;
                                        color: black;
        """)
        self.txtRole.setStyleSheet("""
                                        background-color: white;
                                        color: black;
        """)
        #CSS button
        self.btnQuayVe.setStyleSheet("""
                                            background-color:#FFFF00;
                                            border-radius: 20px;
                                    """)
        self.btnThemTaiKhoan.setStyleSheet("""
                                            background-color:#FFFF00;
                                            border-radius: 20px;
        """)
        #============================SỰ KIỆN===========================================
        self.Dialog = Dialog
        self.btnQuayVe.clicked.connect(self.quayve)
        self.btnThemTaiKhoan.clicked.connect(self.themTaiKhoan)

    #================================HÀM===========================================
    def quayve(self):
        from QuanLyTaiKhoan import Ui_Dialog as Ui_Dialog_TaiKhoan
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog_TaiKhoan(self.window)
        self.ui.setupUi(self.window)
        self.window.show()
        self.Dialog.hide()

    def themTaiKhoan(self):
        username = self.txtTaiKhoan.toPlainText()
        password = self.txtMatKhau.toPlainText()
        role = self.txtRole.toPlainText()
        taiKhoanController = TaiKhoanController()
        taiKhoanController.addTaiKhoan(username, password, role)
        QMessageBox.information(self.Dialog, "Thông báo", "Thêm tài khoản thành công")
        self.quayve()




    #==============================================================================
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Thêm Tài Khoản"))
        self.btnThemTaiKhoan.setText(_translate("Dialog", "Thêm Tài Khoản"))
        self.btnQuayVe.setText(_translate("Dialog", "Quay Về"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(Dialog)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())