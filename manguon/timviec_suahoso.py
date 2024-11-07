# Form implementation generated from reading ui file 'timviec_suahoso.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector


class Ui_timviec_SuaHoSo(object):
    def setupUi(self, timviec_SuaHoSo):
        timviec_SuaHoSo.setObjectName("timviec_SuaHoSo")
        timviec_SuaHoSo.resize(800, 631)
        self.centralwidget = QtWidgets.QWidget(parent=timviec_SuaHoSo)
        self.centralwidget.setObjectName("centralwidget")
        self.te_ChungChi_shs = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.te_ChungChi_shs.setGeometry(QtCore.QRect(270, 440, 491, 51))
        self.te_ChungChi_shs.setObjectName("te_ChungChi_shs")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 370, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.te_HoatDong_shs = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.te_HoatDong_shs.setGeometry(QtCore.QRect(270, 200, 491, 51))
        self.te_HoatDong_shs.setObjectName("te_HoatDong_shs")
        self.te_GiayKhen_shs = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.te_GiayKhen_shs.setGeometry(QtCore.QRect(270, 280, 491, 51))
        self.te_GiayKhen_shs.setObjectName("te_GiayKhen_shs")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 210, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.bt_SuaHoSo_shs = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_SuaHoSo_shs.setGeometry(QtCore.QRect(320, 520, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt_SuaHoSo_shs.setFont(font)
        self.bt_SuaHoSo_shs.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.bt_SuaHoSo_shs.setObjectName("bt_SuaHoSo_shs")
        self.te_kinhNghiemLamViec_shs = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.te_kinhNghiemLamViec_shs.setGeometry(QtCore.QRect(270, 40, 491, 51))
        self.te_kinhNghiemLamViec_shs.setObjectName("te_kinhNghiemLamViec_shs")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 290, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.te_ThinhDoHocVan_shs = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.te_ThinhDoHocVan_shs.setGeometry(QtCore.QRect(270, 120, 491, 51))
        self.te_ThinhDoHocVan_shs.setObjectName("te_ThinhDoHocVan_shs")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 130, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 50, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.te_DuAn_shs = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.te_DuAn_shs.setGeometry(QtCore.QRect(270, 360, 491, 51))
        self.te_DuAn_shs.setObjectName("te_DuAn_shs")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 450, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        timviec_SuaHoSo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=timviec_SuaHoSo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        timviec_SuaHoSo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=timviec_SuaHoSo)
        self.statusbar.setObjectName("statusbar")
        timviec_SuaHoSo.setStatusBar(self.statusbar)

        self.retranslateUi(timviec_SuaHoSo)
        QtCore.QMetaObject.connectSlotsByName(timviec_SuaHoSo)
        self.loadHoSo()
        self.bt_SuaHoSo_shs.clicked.connect(self.suaHoSo)

    def retranslateUi(self, timviec_SuaHoSo):
        _translate = QtCore.QCoreApplication.translate
        timviec_SuaHoSo.setWindowTitle(_translate("timviec_SuaHoSo", "Tìm việc - Sửa hồ sơ"))
        self.label_6.setText(_translate("timviec_SuaHoSo", "Dự án"))
        self.label_4.setText(_translate("timviec_SuaHoSo", "Hoạt động"))
        self.bt_SuaHoSo_shs.setText(_translate("timviec_SuaHoSo", "Lưu thay đổi"))
        self.label_5.setText(_translate("timviec_SuaHoSo", "Giấy khen"))
        self.label_3.setText(_translate("timviec_SuaHoSo", "Trình độ học vấn"))
        self.label_2.setText(_translate("timviec_SuaHoSo", "Kinh nghiệm làm việc"))
        self.label_7.setText(_translate("timviec_SuaHoSo", "Chứng chỉ"))

    def suaHoSo(self):
        file = open("manguoitimviec.txt", "r")
        manguoitimviec = str(file.read())
        file.close()
        kn = self.te_kinhNghiemLamViec_shs.text()
        td = self.te_ThinhDoHocVan_shs.text()
        hd = self.te_HoatDong_shs.text()
        gk = self.te_GiayKhen_shs.text()
        da = self.te_DuAn_shs.text()
        cc = self.te_ChungChi_shs.text()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="quanlygiaodichvieclam"
        )
        mycursor = mydb.cursor()

        try:
            mycursor.execute("UPDATE hoso SET kinhnghiemlamviec = %s, trinhdohocvan = %s, "
                             "hoatdong = %s, giaykhen=%s, duan = %s, chungchi = %s "
                             "WHERE manguoitimviec = %s;",
                             (kn, td, hd, gk, da, cc, manguoitimviec))
            mydb.commit()
            QtWidgets.QMessageBox.information(self.centralwidget, "Thông báo", "Hồ sơ của bạn đã sửa")
        except Exception as e:
            print("Error:", e)
            QtWidgets.QMessageBox.information(self.centralwidget, "Thông báo", "Có lỗi xảy ra khi sửa hồ sơ.")

    def loadHoSo(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="quanlygiaodichvieclam"
        )
        mycursor = mydb.cursor()

        file = open("manguoitimviec.txt", "r")
        manguoitimviec = str(file.read())
        file.close()

        mycursor.execute(
            "SELECT kinhnghiemlamviec, trinhdohocvan, hoatdong, giaykhen, duan, chungchi FROM hoso WHERE manguoitimviec = %s",
            (manguoitimviec,))
        hoso = mycursor.fetchall()
        self.te_kinhNghiemLamViec_shs.setText(hoso[0][0])
        self.te_ThinhDoHocVan_shs.setText(hoso[0][1])
        self.te_HoatDong_shs.setText(hoso[0][2])
        self.te_GiayKhen_shs.setText(hoso[0][3])
        self.te_DuAn_shs.setText(hoso[0][4])
        self.te_ChungChi_shs.setText(hoso[0][5])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    timviec_SuaHoSo = QtWidgets.QMainWindow()
    ui = Ui_timviec_SuaHoSo()
    ui.setupUi(timviec_SuaHoSo)
    timviec_SuaHoSo.show()
    sys.exit(app.exec())