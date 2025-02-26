# Form implementation generated from reading ui file 'Suadonhang.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from Controller.DơnHangController import DonhangController

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(774, 429)
        Dialog.setStyleSheet("background-color: #D0F9FD;")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(300, 10, 381, 41))
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
        self.line.setGeometry(QtCore.QRect(0, 60, 771, 16))
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.txtTenkhach = QtWidgets.QTextEdit(parent=Dialog)
        self.txtTenkhach.setGeometry(QtCore.QRect(310, 90, 131, 31))
        self.txtTenkhach.setObjectName("txtTenkhach")
        self.iconTaiKhoan = QtWidgets.QLabel(parent=Dialog)
        self.iconTaiKhoan.setGeometry(QtCore.QRect(120, 90, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.iconTaiKhoan.setFont(font)
        self.iconTaiKhoan.setObjectName("iconTaiKhoan")
        self.btnSuadonhang = QtWidgets.QPushButton(parent=Dialog)
        self.btnSuadonhang.setGeometry(QtCore.QRect(280, 360, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnSuadonhang.setFont(font)
        self.btnSuadonhang.setObjectName("btnSuadonhang")
        self.btnQuayVe = QtWidgets.QPushButton(parent=Dialog)
        self.btnQuayVe.setGeometry(QtCore.QRect(650, 360, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnQuayVe.setFont(font)
        self.btnQuayVe.setObjectName("btnQuayVe")
        self.iconTaiKhoan_4 = QtWidgets.QLabel(parent=Dialog)
        self.iconTaiKhoan_4.setGeometry(QtCore.QRect(120, 150, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.iconTaiKhoan_4.setFont(font)
        self.iconTaiKhoan_4.setObjectName("iconTaiKhoan_4")
        self.txtIDNhanVien = QtWidgets.QTextEdit(parent=Dialog)
        self.txtIDNhanVien.setGeometry(QtCore.QRect(310, 140, 131, 31))
        self.txtIDNhanVien.setObjectName("txtIDNhanVien")
        self.iconTaiKhoan_7 = QtWidgets.QLabel(parent=Dialog)
        self.iconTaiKhoan_7.setGeometry(QtCore.QRect(120, 200, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.iconTaiKhoan_7.setFont(font)
        self.iconTaiKhoan_7.setObjectName("iconTaiKhoan_7")
        self.txtSDT = QtWidgets.QTextEdit(parent=Dialog)
        self.txtSDT.setGeometry(QtCore.QRect(310, 200, 131, 31))
        self.txtSDT.setObjectName("txtSDT")
        self.iconTaiKhoan_2 = QtWidgets.QLabel(parent=Dialog)
        self.iconTaiKhoan_2.setGeometry(QtCore.QRect(120, 260, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.iconTaiKhoan_2.setFont(font)
        self.iconTaiKhoan_2.setObjectName("iconTaiKhoan_2")
        self.txtIDdonhang = QtWidgets.QTextEdit(parent=Dialog)
        self.txtIDdonhang.setGeometry(QtCore.QRect(310, 260, 131, 31))
        self.txtIDdonhang.setObjectName("txtIDdonhang")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.btnQuayVe.clicked.connect(Dialog.close)
        self.btnSuadonhang.clicked.connect(self.sua)

    def sua(self):
        tenkhach = self.txtTenkhach.toPlainText()
        idnhanvien = self.txtIDNhanVien.toPlainText()
        sdt = self.txtSDT.toPlainText()
        iddonhang = self.txtIDdonhang.toPlainText()
        controller = DonhangController()
        controller.updateDonHang(idnhanvien,tenkhach,sdt, iddonhang)

    def close(self):
        self.close()



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Thông tin đơn hàng"))
        self.iconTaiKhoan.setText(_translate("Dialog", "Tên khách"))
        self.btnSuadonhang.setText(_translate("Dialog", "Sửa"))
        self.btnQuayVe.setText(_translate("Dialog", "Quay Về"))
        self.iconTaiKhoan_4.setText(_translate("Dialog", "IDĐơn hàng"))
        self.iconTaiKhoan_7.setText(_translate("Dialog", "SĐT"))
        self.iconTaiKhoan_2.setText(_translate("Dialog", "ID_Nhân Viên"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
