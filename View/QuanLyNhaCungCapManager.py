# Form implementation generated from reading ui file 'QuanLyNhaCungCap.ui'
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
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QMessageBox
from Controller.NhaCungCapController import NhaCungCapController
class Ui_Dialog(object):
    def __init__(self, main_window):
      self.main_window = main_window
    def setupUi(self, Dialog):
      # Ẩn thanh hiện thông báo DiaLog
        Dialog.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        Dialog.setObjectName("Dialog")
        Dialog.resize(911, 695)
        Dialog.setStyleSheet("background-color: #D0F9FD;")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(230, 20, 511, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.tblDuLieu = QtWidgets.QTableView(parent=Dialog)
        self.tblDuLieu.setGeometry(QtCore.QRect(0, 100, 911, 431))
        self.tblDuLieu.setStyleSheet("background-color:white;\n"
"color:black;")
        self.tblDuLieu.setObjectName("tblDuLieu")
        (self.tblDuLieu.setSelectionBehavior
         (QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows))
        self.line = QtWidgets.QFrame(parent=Dialog)
        self.line.setGeometry(QtCore.QRect(0, 80, 911, 16))
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(parent=Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 540, 911, 16))
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.btnThemNhaCungCap = QtWidgets.QPushButton(parent=Dialog)
        self.btnThemNhaCungCap.setGeometry(QtCore.QRect(30, 580, 211, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btnThemNhaCungCap.setFont(font)
        self.btnThemNhaCungCap.setObjectName("btnThemNhaCungCap")
        self.btnSuaNhaCungCap = QtWidgets.QPushButton(parent=Dialog)
        self.btnSuaNhaCungCap.setGeometry(QtCore.QRect(290, 580, 211, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btnSuaNhaCungCap.setFont(font)
        self.btnSuaNhaCungCap.setObjectName("btnSuaNhaCungCap")
        self.btnXoaNhaCungCap = QtWidgets.QPushButton(parent=Dialog)
        self.btnXoaNhaCungCap.setGeometry(QtCore.QRect(550, 580, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btnXoaNhaCungCap.setFont(font)
        self.btnXoaNhaCungCap.setObjectName("btnXoaNhaCungCap")
        self.btnQuayVe = QtWidgets.QPushButton(parent=Dialog)
        self.btnQuayVe.setGeometry(QtCore.QRect(844, 642, 61, 51))
        self.btnQuayVe.setStyleSheet("")
        self.btnQuayVe.setText("")
        self.btnQuayVe.setObjectName("btnQuayVe")
        self.Favicon = QtWidgets.QLabel(parent=Dialog)
        self.Favicon.setGeometry(QtCore.QRect(10, 10, 121, 71))
        self.Favicon.setText("")
        self.Favicon.setObjectName("Favicon")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #============================CSS===================================
        #CSS Label
        self.label.setStyleSheet("""color: #FF4500;
                                    font-weight: bold;
                                 """)
        # Thêm hình ảnh Favicon
        pixmap = QPixmap("../Access/Icon/favicon.jpg")
        self.Favicon.setPixmap(pixmap)
        self.Favicon.setScaledContents(True)

        #Thêm icon vào btn

        self.btnQuayVe.setIcon(QIcon("../Access/Icon/back.png"))
        self.btnQuayVe.setIconSize(QSize(40,40))

        self.btnSuaNhaCungCap.setIcon(QIcon("../Access/Icon/update.png"))
        self.btnSuaNhaCungCap.setIconSize(QSize(40,40))

        self.btnThemNhaCungCap.setIcon(QIcon("../Access/Icon/plus.png"))
        self.btnThemNhaCungCap.setIconSize(QSize(40,40))

        self.btnXoaNhaCungCap.setIcon(QIcon("../Access/Icon/delete.png"))
        self.btnXoaNhaCungCap.setIconSize(QSize(40,40))

        #CSS Button
        self.btnThemNhaCungCap.setStyleSheet("""
                                              background-color:#FFFF00;
                                              border-radius: 10px;
                                            """)
        self.btnSuaNhaCungCap.setStyleSheet("""
                                              background-color:#FFFF00;
                                              border-radius: 10px;
                                            """)
        self.btnXoaNhaCungCap.setStyleSheet("""
                                              background-color:#FFFF00;
                                              border-radius: 10px;
                                            """)
        self.btnQuayVe.setStyleSheet("""
                                              background-color:#FFFF00;
                                              border-radius: 25px;
                                    """)
    #============================SỰ KIỆN===============================
        self.loaddata()
        self.Dialog = Dialog
        self.tblDuLieu.clicked.connect(self.row_clicked)
        # self.tblDuLieu.clicked.connect(self.double_clicked)
        self.btnQuayVe.clicked.connect(self.quayve)
        self.btnSuaNhaCungCap.clicked.connect(self.openSuaNhaCungCap)
        self.btnThemNhaCungCap.clicked.connect(self.openthemNhaCungCap)
        self.btnXoaNhaCungCap.clicked.connect(self.xoaNhaCungCap)
    #============================HÀM===================================
    def quayve(self):
      from View.UiManager import Ui_MainWindow
      self.main_window = QtWidgets.QMainWindow()  # tạo một instance mới của QMainWindow
      self.ui = Ui_MainWindow(self.main_window)  # truyền self.main_window như là MainWindow
      self.ui.setupUi(self.main_window)
      self.main_window.show()
      self.Dialog.hide()

    def loaddata(self):
      model = QStandardItemModel()
      model.setHorizontalHeaderLabels(['ID_NhàCungCấp',
                                       'Tên_Nhà_Cung_Cấp', 'Địa_Chỉ',
                                       'Số_Điện_Thoại', 'Email'])
      controller = NhaCungCapController()
      data = controller.getAllNhaCungCap()
      for row in data:
        items = [QStandardItem(str(field)) for field in row]
        model.appendRow(items)
      self.tblDuLieu.setModel(model)

      (self.tblDuLieu.horizontalHeader().setSectionResizeMode
       (QHeaderView.ResizeMode.Stretch))

    def openSuaNhaCungCap(self):
      from SuaNhaCungCap import Ui_Dialog as Ui_Dialog_SuaNhaCungCap
      self.window = QtWidgets.QDialog()
      self.ui = Ui_Dialog_SuaNhaCungCap(self.window)
      self.ui.setupUi(self.window)
      self.window.show()
      self.Dialog.hide()
      # Truyền dữ liệu từ selected_row_data vào các trường nhập liệu
      global selected_row_data
      self.ui.txtTaiKhoan.setText(selected_row_data[0])
      self.ui.txtMatKhau.setText(selected_row_data[1])
      self.ui.txtDiaChi.setText(selected_row_data[2])
      self.ui.txtSoDienThoai.setText(selected_row_data[3])
      self.ui.txtEmail.setText(selected_row_data[4])

    def openthemNhaCungCap(self):
      from ThemNhaCungCap import Ui_Dialog as Ui_Dialog_ThemNhaCungCap
      self.window = QtWidgets.QDialog()
      self.ui = Ui_Dialog_ThemNhaCungCap(self.window)
      self.ui.setupUi(self.window)
      self.window.show()
      self.Dialog.hide()


    def xoaNhaCungCap(self):
        selected_row_data = []
        index = self.tblDuLieu.currentIndex()
        for i in range(self.tblDuLieu.model().columnCount()):
          selected_row_data.append(self.tblDuLieu.model().index(index.row(), i).data())
        confirm = QMessageBox.question(self.Dialog, "Xác nhận", "Bạn có chắc chắn muốn xóa tài khoản này không?",
                                       QMessageBox.StandardButton.Yes |
                                       QMessageBox.StandardButton.No )
        if confirm == QMessageBox.StandardButton.Yes:
          id = selected_row_data[0]
          controller = NhaCungCapController()
          controller.deleteNhaCungCap(id)
          QMessageBox.information(self.Dialog, "Thông báo", "Xóa tài khoản thành công")
          self.loaddata()


    #Lấy dữ liệu của dòng lưu vào selected row data
    def row_clicked(self, index):
      global selected_row_data
      selected_row_data = []
      for i in range(self.tblDuLieu.model().columnCount()):
        selected_row_data.append(self.tblDuLieu.model().index(index.row(), i).data())
      print("Selected row data:", selected_row_data)





    #==================================================================


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Quản Lý Danh Sách Nhà Cung Cấp"))
        self.btnThemNhaCungCap.setText(_translate("Dialog", "Thêm Nhà Cung Cấp"))
        self.btnSuaNhaCungCap.setText(_translate("Dialog", "Sửa Nhà Cùng Cấp"))
        self.btnXoaNhaCungCap.setText(_translate("Dialog", "Xoá Nhà Cung Cấp"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(Dialog)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
