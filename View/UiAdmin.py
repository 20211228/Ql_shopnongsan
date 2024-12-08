# Form implementation generated from reading ui file 'UiAdmin.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from QuanLyNhaCungCap import Ui_Dialog as Ui_Dialog_NhaCungCap
from QuanLySanPham import Ui_Dialog as Ui_Dialog_SanPham
from ThongKeDoanhThu import Ui_Dialog as Ui_Dialog_ThongKe
from QuanLyTaiKhoan import Ui_Dialog as Ui_Dialog_TaiKhoan
from QuanLyDonHang import Ui_Dialog as Ui_Dialog_DonHang
from ChucNangKhac import Ui_Dialog as Ui_Dialog_ChucNangKhac
import dialog_manager

class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1265, 912)
        MainWindow.setStyleSheet("background-color: #D0F9FD;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1271, 111))
        self.widget.setObjectName("widget")
        self.Favicon = QtWidgets.QLabel(parent=self.widget)
        self.Favicon.setGeometry(QtCore.QRect(80, 0, 131, 91))
        self.Favicon.setText("")
        self.Favicon.setObjectName("Favicon")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(420, 10, 501, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(parent=self.widget)
        self.line.setGeometry(QtCore.QRect(0, 100, 1261, 16))
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.widget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(0, 120, 231, 801))
        self.widget_2.setObjectName("widget_2")
        self.btnTaiKhoan = QtWidgets.QPushButton(parent=self.widget_2)
        self.btnTaiKhoan.setGeometry(QtCore.QRect(0, 10, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.btnTaiKhoan.setFont(font)
        self.btnTaiKhoan.setObjectName("btnTaiKhoan")
        self.btnThongKe = QtWidgets.QPushButton(parent=self.widget_2)
        self.btnThongKe.setGeometry(QtCore.QRect(0, 120, 221, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.btnThongKe.setFont(font)
        self.btnThongKe.setObjectName("btnThongKe")
        self.btnSanPham = QtWidgets.QPushButton(parent=self.widget_2)
        self.btnSanPham.setGeometry(QtCore.QRect(0, 230, 221, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.btnSanPham.setFont(font)
        self.btnSanPham.setObjectName("btnSanPham")
        self.btnNhaCungCap = QtWidgets.QPushButton(parent=self.widget_2)
        self.btnNhaCungCap.setGeometry(QtCore.QRect(0, 340, 221, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.btnNhaCungCap.setFont(font)
        self.btnNhaCungCap.setObjectName("btnNhaCungCap")
        self.btnDonHang = QtWidgets.QPushButton(parent=self.widget_2)
        self.btnDonHang.setGeometry(QtCore.QRect(0, 450, 221, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.btnDonHang.setFont(font)
        self.btnDonHang.setObjectName("btnDonHang")
        self.btnDangXuat = QtWidgets.QPushButton(parent=self.widget_2)
        self.btnDangXuat.setGeometry(QtCore.QRect(0, 680, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.btnDangXuat.setFont(font)
        self.btnDangXuat.setObjectName("btnDangXuat")
        self.line_3 = QtWidgets.QFrame(parent=self.widget_2)
        self.line_3.setGeometry(QtCore.QRect(-10, 100, 231, 16))
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_7 = QtWidgets.QFrame(parent=self.widget_2)
        self.line_7.setGeometry(QtCore.QRect(0, 210, 231, 16))
        self.line_7.setLineWidth(2)
        self.line_7.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_6 = QtWidgets.QFrame(parent=self.widget_2)
        self.line_6.setGeometry(QtCore.QRect(-10, 320, 241, 16))
        self.line_6.setLineWidth(2)
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_5 = QtWidgets.QFrame(parent=self.widget_2)
        self.line_5.setGeometry(QtCore.QRect(0, 430, 231, 16))
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_4 = QtWidgets.QFrame(parent=self.widget_2)
        self.line_4.setGeometry(QtCore.QRect(0, 660, 231, 16))
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_9 = QtWidgets.QFrame(parent=self.widget_2)
        self.line_9.setGeometry(QtCore.QRect(0, 540, 231, 16))
        self.line_9.setLineWidth(2)
        self.line_9.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_9.setObjectName("line_9")
        self.btnChucNangKhac = QtWidgets.QPushButton(parent=self.widget_2)
        self.btnChucNangKhac.setGeometry(QtCore.QRect(0, 570, 221, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.btnChucNangKhac.setFont(font)
        self.btnChucNangKhac.setObjectName("btnChucNangKhac")
        self.line_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(220, 110, 31, 781))
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.Images = QtWidgets.QLabel(parent=self.centralwidget)
        self.Images.setGeometry(QtCore.QRect(240, 110, 1021, 801))
        self.Images.setText("")
        self.Images.setObjectName("Images")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #================================CSS===========================================

        #Css Label
        self.label.setStyleSheet("""
                    color: #FF4500;
                    font-weight: bold;
                """)

        # Thêm hình ảnh vào giao diện
        pixamp = QPixmap("../Access/Icon/favicon.jpg")
        self.Favicon.setPixmap(pixamp)
        self.Favicon.setScaledContents(True)

        pixamp = QPixmap("../Access/Images/CoHaiLua.png")
        self.Images.setPixmap(pixamp)
        self.Images.setScaledContents(True)

        #Thêm Icon cho button

        self.btnTaiKhoan.setIcon(QIcon("../Access/Icon/account.png"))
        self.btnTaiKhoan.setIconSize(QSize(40, 40))
        self.btnThongKe.setIcon(QIcon("../Access/Icon/statistical.png"))
        self.btnThongKe.setIconSize(QSize(40, 40))
        self.btnSanPham.setIcon(QIcon("../Access/Icon/vegetables.png"))
        self.btnSanPham.setIconSize(QSize(40, 40))
        self.btnNhaCungCap.setIcon(QIcon("../Access/Icon/NhaCungCap.png"))
        self.btnNhaCungCap.setIconSize(QSize(40, 40))
        self.btnDonHang.setIcon(QIcon("../Access/Icon/oder.png"))
        self.btnDonHang.setIconSize(QSize(40, 40))
        self.btnDangXuat.setIcon(QIcon("../Access/Icon/log-out.png"))
        self.btnDangXuat.setIconSize(QSize(40, 40))
        self.btnChucNangKhac.setIcon(QIcon("../Access/Icon/other.png"))
        self.btnChucNangKhac.setIconSize(QSize(40, 40))

        #CSS Button
        self.btnTaiKhoan.setStyleSheet("""
                                        background-color:#FFFF00;
                                        border-radius: 10px;
                                        border: 2px solid #00FF00;
                                       """)
        self.btnThongKe.setStyleSheet("""
                                        background-color:#FFFF00;
                                        border-radius: 10px;
                                        border: 2px solid #00FF00;
                                     """)
        self.btnSanPham.setStyleSheet("""
                                        background-color:#FFFF00;
                                        border-radius: 10px;
                                        border: 2px solid #00FF00;
                                      """)
        self.btnNhaCungCap.setStyleSheet("""
                                        background-color:#FFFF00;
                                        border-radius: 10px;
                                        border: 2px solid #00FF00;
                                      """)
        self.btnDonHang.setStyleSheet("""
                                        background-color:#FFFF00;
                                        border-radius: 10px;
                                        border: 2px solid #00FF00;
                                      """)
        self.btnDangXuat.setStyleSheet("""
                                        background-color:#FFFF00;
                                        border-radius: 10px;
                                        border: 2px solid #00FF00;
                                      """)
        self.btnChucNangKhac.setStyleSheet("""
                                        background-color:#FFFF00;
                                        border-radius: 10px;
                                        border: 2px solid #00FF00;
                                      """)

        #=================================Sự Kiện=====================================
        self.btnDangXuat.clicked.connect(self.openLogin)
        self.btnNhaCungCap.clicked.connect(self.openNhaCungCap)
        self.btnSanPham.clicked.connect(self.openSanPham)
        self.btnThongKe.clicked.connect(self.openThongKe)
        self.btnTaiKhoan.clicked.connect(self.openTaiKhoan)
        self.btnDonHang.clicked.connect(self.openDonHang)
        self.btnChucNangKhac.clicked.connect(self.openChucNangKhac)


    #=================================Hàm=========================================
    def openLogin(self):
        from Login import Ui_Dialog as Ui_Dialog_Login
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog_Login(self.window)
        self.ui.setupUi(self.window)
        self.window.show()
        self.MainWindow.hide()

    def openNhaCungCap(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog_NhaCungCap(self.window)
        self.ui.setupUi(self.window)
        self.window.show()
        self.MainWindow.hide()

    def openThongKe(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog_ThongKe(self.window)
        self.ui.setupUi(self.window)
        self.window.show()
        self.MainWindow.hide()

    def openSanPham(self):

        self.window = QtWidgets.QDialog()  # tạo một instance mới của QDialog chỉ khi nó chưa tồn tại
        self.ui = Ui_Dialog_SanPham(self.window)
        self.ui.setupUi(self.window)
        self.window.show()
        self.MainWindow.hide()

    def openDonHang(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog_DonHang(self.window)
        self.ui.setupUi(self.window)
        self.window.show()
        self.MainWindow.hide()
    def openTaiKhoan(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog_TaiKhoan(self.window)
        self.ui.setupUi(self.window)
        self.window.show()
        self.MainWindow.hide()

    def openChucNangKhac(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog_ChucNangKhac(self.window)
        self.ui.setupUi(self.window)
        self.window.show()
        self.MainWindow.hide()


    #=============================================================================
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Cửa Hàng Nông Sản __ Cô Hai Lúa"))
        self.btnTaiKhoan.setText(_translate("MainWindow", "Tài Khoản"))
        self.btnThongKe.setText(_translate("MainWindow", "Thống Kê"))
        self.btnSanPham.setText(_translate("MainWindow", "Sản Phẩm"))
        self.btnNhaCungCap.setText(_translate("MainWindow", "Nhà Cung Cấp"))
        self.btnDonHang.setText(_translate("MainWindow", "Đơn Hàng"))
        self.btnDangXuat.setText(_translate("MainWindow", "Đăng Xuất"))
        self.btnChucNangKhac.setText(_translate("MainWindow", "Chức Năng Khác"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
