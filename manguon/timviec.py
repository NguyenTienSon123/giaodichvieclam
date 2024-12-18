# Form implementation generated from reading ui file 'timviec.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector
import subprocess


class Ui_NguoiTimViec(object):
    def chuyenDenDSCongViec(self):
        subprocess.run(["python", "timviec_QuanLyCongViec.py"])

    def chuyenDenDSNhaTuyenDung(self):
        subprocess.run(["python", "timviec_DanhSachNhaTuyenDung.py"])

    def thoat(self):
        NguoiTimViec.destroy()
        subprocess.run(["python", "trangchu.py"])

    def chuyenDenSuaHoSo(self):
        subprocess.run(["python", "timviec_suahoso.py"])

    def setupUi(self, NguoiTimViec):
        NguoiTimViec.setObjectName("NguoiTimViec")
        NguoiTimViec.resize(374, 418)
        self.centralwidget = QtWidgets.QWidget(parent=NguoiTimViec)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_listnhatuyendung = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.chuyenDenDSNhaTuyenDung())
        self.bt_listnhatuyendung.setGeometry(QtCore.QRect(80, 30, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt_listnhatuyendung.setFont(font)
        self.bt_listnhatuyendung.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.bt_listnhatuyendung.setObjectName("bt_listnhatuyendung")
        self.bt_listcongviec = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.chuyenDenDSCongViec())
        self.bt_listcongviec.setGeometry(QtCore.QRect(80, 100, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt_listcongviec.setFont(font)
        self.bt_listcongviec.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.bt_listcongviec.setObjectName("bt_listcongviec")
        self.bt_thoat = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.thoat())
        self.bt_thoat.setGeometry(QtCore.QRect(80, 310, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt_thoat.setFont(font)
        self.bt_thoat.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.bt_thoat.setObjectName("bt_thoat")
        self.bt_thongbao = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_thongbao.setGeometry(QtCore.QRect(80, 240, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt_thongbao.setFont(font)
        self.bt_thongbao.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.bt_thongbao.setObjectName("bt_thongbao")
        self.bt_Hoso = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.chuyenDenSuaHoSo())
        self.bt_Hoso.setGeometry(QtCore.QRect(80, 170, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt_Hoso.setFont(font)
        self.bt_Hoso.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.bt_Hoso.setObjectName("bt_Hoso")
        NguoiTimViec.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=NguoiTimViec)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 374, 26))
        self.menubar.setObjectName("menubar")
        NguoiTimViec.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=NguoiTimViec)
        self.statusbar.setObjectName("statusbar")
        NguoiTimViec.setStatusBar(self.statusbar)

        self.retranslateUi(NguoiTimViec)
        QtCore.QMetaObject.connectSlotsByName(NguoiTimViec)
        self.bt_thongbao.clicked.connect(self.thongBao)

    def retranslateUi(self, NguoiTimViec):
        _translate = QtCore.QCoreApplication.translate
        NguoiTimViec.setWindowTitle(_translate("NguoiTimViec", "Tìm Việc"))
        self.bt_listnhatuyendung.setText(_translate("NguoiTimViec", "Nhà tuyển dụng"))
        self.bt_listcongviec.setText(_translate("NguoiTimViec", "Công việc"))
        self.bt_thoat.setText(_translate("NguoiTimViec", "Thoát"))
        self.bt_thongbao.setText(_translate("NguoiTimViec", "Thông báo"))
        self.bt_Hoso.setText(_translate("NguoiTimViec", "Hồ sơ"))

    def thongBao(self):
        subprocess.run(["python", "thongbao.py"])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NguoiTimViec = QtWidgets.QMainWindow()
    ui = Ui_NguoiTimViec()
    ui.setupUi(NguoiTimViec)
    NguoiTimViec.show()
    sys.exit(app.exec())
