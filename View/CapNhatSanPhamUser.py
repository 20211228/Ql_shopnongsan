# Form implementation generated from reading ui file 'CapNhatSanPham.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QHeaderView
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox

class Ui_Dialog(object):
    def __init__(self, main_window):
        self.main_window = main_window
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(627, 429)
        Dialog.setStyleSheet("background-color: #D0F9FD;")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(210, 10, 281, 41))
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
        self.idSanPham = QtWidgets.QTextEdit(parent=Dialog)
        self.idSanPham.setGeometry(QtCore.QRect(230, 90, 191, 31))
        self.idSanPham.setObjectName("idSanPham")
        self.idSanPham.setReadOnly(True)
        self.txtSoLuong = QtWidgets.QTextEdit(parent=Dialog)
        self.txtSoLuong.setGeometry(QtCore.QRect(230, 150, 191, 31))
        self.txtSoLuong.setObjectName("txtSoLuong")
        self.txtTenSanPham = QtWidgets.QTextEdit(parent=Dialog)
        self.txtTenSanPham.setGeometry(QtCore.QRect(230, 210, 191, 31))
        self.txtTenSanPham.setObjectName("txtTenSanPham")
        self.iconTaiKhoan = QtWidgets.QLabel(parent=Dialog)
        self.iconTaiKhoan.setGeometry(QtCore.QRect(40, 90, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.iconTaiKhoan.setFont(font)
        self.iconTaiKhoan.setObjectName("iconTaiKhoan")
        self.iconMatKhau = QtWidgets.QLabel(parent=Dialog)
        self.iconMatKhau.setGeometry(QtCore.QRect(180, 189, 21, 21))
        self.iconMatKhau.setText("")
        self.iconMatKhau.setObjectName("iconMatKhau")
        self.iconRole = QtWidgets.QLabel(parent=Dialog)
        self.iconRole.setGeometry(QtCore.QRect(180, 250, 21, 20))
        self.iconRole.setText("")
        self.iconRole.setObjectName("iconRole")
        self.btnCapNhatSanPham = QtWidgets.QPushButton(parent=Dialog)
        self.btnCapNhatSanPham.setGeometry(QtCore.QRect(230, 370, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnCapNhatSanPham.setFont(font)
        self.btnCapNhatSanPham.setObjectName("btnCapNhatSanPham")
        self.btnQuayVe = QtWidgets.QPushButton(parent=Dialog)
        self.btnQuayVe.setGeometry(QtCore.QRect(510, 390, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnQuayVe.setFont(font)
        self.btnQuayVe.setObjectName("btnQuayVe")
        self.iconTaiKhoan_2 = QtWidgets.QLabel(parent=Dialog)
        self.iconTaiKhoan_2.setGeometry(QtCore.QRect(40, 150, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.iconTaiKhoan_2.setFont(font)
        self.iconTaiKhoan_2.setObjectName("iconTaiKhoan_2")
        self.iconTaiKhoan_3 = QtWidgets.QLabel(parent=Dialog)
        self.iconTaiKhoan_3.setGeometry(QtCore.QRect(40, 210, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.iconTaiKhoan_3.setFont(font)
        self.iconTaiKhoan_3.setObjectName("iconTaiKhoan_3")
        self.iconTaiKhoan_4 = QtWidgets.QLabel(parent=Dialog)
        self.iconTaiKhoan_4.setGeometry(QtCore.QRect(40, 270, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.iconTaiKhoan_4.setFont(font)
        self.iconTaiKhoan_4.setObjectName("iconTaiKhoan_4")
        self.iconTaiKhoan_5 = QtWidgets.QLabel(parent=Dialog)
        self.iconTaiKhoan_5.setGeometry(QtCore.QRect(40, 330, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.iconTaiKhoan_5.setFont(font)
        self.iconTaiKhoan_5.setObjectName("iconTaiKhoan_5")
        self.txtDonGia = QtWidgets.QTextEdit(parent=Dialog)
        self.txtDonGia.setGeometry(QtCore.QRect(230, 270, 191, 31))
        self.txtDonGia.setObjectName("txtDonGia")
        self.txtNhaCungCap = QtWidgets.QTextEdit(parent=Dialog)
        self.txtNhaCungCap.setGeometry(QtCore.QRect(230, 330, 191, 31))
        self.txtNhaCungCap.setObjectName("txtNhaCungCap")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
#===============================================================================
        #CSS Label
        self.label.setStyleSheet("""color: #FF4500;
                                    font-weight: bold;
                                 """)
        # Thêm hình ảnh Favicon
        pixmap = QPixmap("../Access/Icon/favicon.jpg")
        self.Favicon.setPixmap(pixmap)
        self.Favicon.setScaledContents(True)

        #CSS txt
        self.txtDonGia.setStyleSheet("""
            background-color: white;
            color: black;
        """)
        self.txtSoLuong.setStyleSheet("""
            background-color: white;
            color: black;
        """)
        self.txtNhaCungCap.setStyleSheet("""
            background-color: white;
            color: black;
        """)
        self.txtTenSanPham.setStyleSheet("""
            background-color: white;
            color: black;
        """)
        self.idSanPham.setStyleSheet("""
            background-color: white;
            color: black;
        """)
        #Css icon button
        self.btnQuayVe.setIcon(QIcon("../Access/Icon/Quayve.png"))
        self.btnQuayVe.setIconSize(QSize(30,30))
        self.btnCapNhatSanPham.setIcon(QIcon("../Access/Icon/update.png"))
        self.btnCapNhatSanPham.setIconSize(QSize(30,30))
        #CSS Button
        self.btnQuayVe.setStyleSheet("""
                                              background-color:#FFFF00;
                                              border-radius: 20px;
                                    """)
        self.btnCapNhatSanPham.setStyleSheet("""
                                              background-color:#FFFF00;
                                              border-radius: 10px;
                                    """)
#=================================Sự Kiện=======================================
        self.Dialog = Dialog
        self.btnQuayVe.clicked.connect(self.quayve)
        self.btnCapNhatSanPham.clicked.connect(self.capNhatSanPham)



#==================================Hàm==========================================
    def quayve(self):
        from QuanLySanPhamUser import Ui_Dialog as Ui_Dialog_QuanLySanPham
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog_QuanLySanPham(self.window)
        self.ui.setupUi(self.window)
        self.window.show()
        self.Dialog.hide()

    def capNhatSanPham(self):
        from Controller.SanPhamController import SanPhamController
        idSanPham = self.idSanPham.toPlainText()
        soLuong = self.txtSoLuong.toPlainText()
        tenSanPham = self.txtTenSanPham.toPlainText()
        donGia = self.txtDonGia.toPlainText()
        idNhaCungCap = self.txtNhaCungCap.toPlainText()
        if idSanPham == '' or soLuong == '' or tenSanPham == '' or donGia == '' or idNhaCungCap == '':
            QMessageBox.warning(self.Dialog, "Lỗi", "Vui lòng nhập đầy đủ thông tin")
        else:
            sanPham = SanPhamController()
            sanPham.updateSanPham(idSanPham, soLuong, tenSanPham, donGia, idNhaCungCap)
            QMessageBox.information(self.Dialog, "Thông báo", "Cập nhật sản phẩm thành công")
            self.quayve()

#===============================================================================
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Cập Nhật Sản Phẩm"))
        self.iconTaiKhoan.setText(_translate("Dialog", "ID_SảnPhẩm"))
        self.btnCapNhatSanPham.setText(_translate("Dialog", "Cập Nhật Sản Phẩm"))
        self.btnQuayVe.setText(_translate("Dialog", "Quay Về"))
        self.iconTaiKhoan_2.setText(_translate("Dialog", "Số_Lượng"))
        self.iconTaiKhoan_3.setText(_translate("Dialog", "Tên_Sẩn_Phẩm"))
        self.iconTaiKhoan_4.setText(_translate("Dialog", "Đơn_Giá"))
        self.iconTaiKhoan_5.setText(_translate("Dialog", "ID_Nhà_Cung_Cấp"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(Dialog)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
