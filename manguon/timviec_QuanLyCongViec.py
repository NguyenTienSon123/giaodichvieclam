# Form implementation generated from reading ui file 'timviec_QuanLyCongViec.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector


class Ui_timviec_DanhSachCongViec(object):
    def setupUi(self, timviec_DanhSachCongViec):
        timviec_DanhSachCongViec.setObjectName("timviec_DanhSachCongViec")
        timviec_DanhSachCongViec.resize(763, 425)
        self.centralwidget = QtWidgets.QWidget(parent=timviec_DanhSachCongViec)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 0, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.te_tencongviec_TimViec_dsCongViec = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.te_tencongviec_TimViec_dsCongViec.setGeometry(QtCore.QRect(290, 60, 171, 31))
        self.te_tencongviec_TimViec_dsCongViec.setObjectName("te_tencongviec_TimViec_dsCongViec")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 50, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.table_dsCongViec = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.table_dsCongViec.setGeometry(QtCore.QRect(50, 110, 661, 201))
        self.table_dsCongViec.setObjectName("table_dsCongViec")
        self.table_dsCongViec.setColumnCount(11)
        self.table_dsCongViec.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.table_dsCongViec.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dsCongViec.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dsCongViec.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dsCongViec.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dsCongViec.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dsCongViec.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dsCongViec.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dsCongViec.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dsCongViec.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dsCongViec.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dsCongViec.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dsCongViec.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dsCongViec.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dsCongViec.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dsCongViec.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dsCongViec.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dsCongViec.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dsCongViec.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dsCongViec.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dsCongViec.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dsCongViec.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_dsCongViec.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dsCongViec.setItem(0, 2, item)
        self.bt_UngTuyen_TimViec_DSCongViec = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_UngTuyen_TimViec_DSCongViec.setGeometry(QtCore.QRect(530, 330, 141, 41))
        self.bt_UngTuyen_TimViec_DSCongViec.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 170, 255);")
        self.bt_UngTuyen_TimViec_DSCongViec.setObjectName("bt_UngTuyen_TimViec_DSCongViec")
        self.te_macongviec_TimViec_dsCongViec = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.te_macongviec_TimViec_dsCongViec.setGeometry(QtCore.QRect(240, 330, 201, 31))
        self.te_macongviec_TimViec_dsCongViec.setObjectName("te_macongviec_TimViec_dsCongViec")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 329, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.bt_TimKiem_TimViec_dsCongViec = QtWidgets.QPushButton(parent=self.centralwidget)
        self.bt_TimKiem_TimViec_dsCongViec.setGeometry(QtCore.QRect(560, 50, 101, 41))
        self.bt_TimKiem_TimViec_dsCongViec.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 170, 255);")
        self.bt_TimKiem_TimViec_dsCongViec.setObjectName("bt_TimKiem_TimViec_dsCongViec")
        timviec_DanhSachCongViec.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=timviec_DanhSachCongViec)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 763, 26))
        self.menubar.setObjectName("menubar")
        timviec_DanhSachCongViec.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=timviec_DanhSachCongViec)
        self.statusbar.setObjectName("statusbar")
        timviec_DanhSachCongViec.setStatusBar(self.statusbar)

        self.retranslateUi(timviec_DanhSachCongViec)
        QtCore.QMetaObject.connectSlotsByName(timviec_DanhSachCongViec)

        self.bt_TimKiem_TimViec_dsCongViec.clicked.connect(self.timCongViecTheoTen)
        self.bt_UngTuyen_TimViec_DSCongViec.clicked.connect(self.ungTuyen)
        self.loadCongViec()

    def retranslateUi(self, timviec_DanhSachCongViec):
        _translate = QtCore.QCoreApplication.translate
        timviec_DanhSachCongViec.setWindowTitle(_translate("timviec_DanhSachCongViec", "Tìm việc - Danh sách công việc"))
        self.label.setText(_translate("timviec_DanhSachCongViec", "Danh sách công việc"))
        self.label_2.setText(_translate("timviec_DanhSachCongViec", "Tên công việc"))
        item = self.table_dsCongViec.horizontalHeaderItem(0)
        item.setText(_translate("timviec_DanhSachCongViec", "Mã công việc"))
        item = self.table_dsCongViec.horizontalHeaderItem(1)
        item.setText(_translate("timviec_DanhSachCongViec", "Nhà tuyển dụng"))
        item = self.table_dsCongViec.horizontalHeaderItem(2)
        item.setText(_translate("timviec_DanhSachCongViec", "Tên công việc "))
        item = self.table_dsCongViec.horizontalHeaderItem(3)
        item.setText(_translate("timviec_DanhSachCongViec", "Mô tả"))
        item = self.table_dsCongViec.horizontalHeaderItem(4)
        item.setText(_translate("timviec_DanhSachCongViec", "Vị trí"))
        item = self.table_dsCongViec.horizontalHeaderItem(5)
        item.setText(_translate("timviec_DanhSachCongViec", "Trình độ"))
        item = self.table_dsCongViec.horizontalHeaderItem(6)
        item.setText(_translate("timviec_DanhSachCongViec", "Loại công việc"))
        item = self.table_dsCongViec.horizontalHeaderItem(7)
        item.setText(_translate("timviec_DanhSachCongViec", "Chỉ tiêu"))
        item = self.table_dsCongViec.horizontalHeaderItem(8)
        item.setText(_translate("timviec_DanhSachCongViec", "Số người ứng tuyển"))
        item = self.table_dsCongViec.horizontalHeaderItem(9)
        item.setText(_translate("timviec_DanhSachCongViec", "Lương"))
        item = self.table_dsCongViec.horizontalHeaderItem(10)
        item.setText(_translate("timviec_DanhSachCongViec", "Tình Trạng"))
        __sortingEnabled = self.table_dsCongViec.isSortingEnabled()
        self.table_dsCongViec.setSortingEnabled(False)
        self.table_dsCongViec.setSortingEnabled(__sortingEnabled)
        self.bt_UngTuyen_TimViec_DSCongViec.setText(_translate("timviec_DanhSachCongViec", "Ứng tuyển"))
        self.label_3.setText(_translate("timviec_DanhSachCongViec", "Mã công việc"))
        self.bt_TimKiem_TimViec_dsCongViec.setText(_translate("timviec_DanhSachCongViec", "Tìm kiếm"))

    def timCongViecTheoTen(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="quanlygiaodichvieclam"
            )
            tencongviec = self.te_tencongviec_TimViec_dsCongViec.text()
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM congviec WHERE tencongviec like %s", (tencongviec, ))
            rows = mycursor.fetchall()
            col_count = len(mycursor.description)

            self.table_dsCongViec.setColumnCount(col_count)
            self.table_dsCongViec.setRowCount(len(rows))

            for tablerow, row in enumerate(rows):
                for col in range(col_count):
                    self.table_dsCongViec.setItem(tablerow, col, QtWidgets.QTableWidgetItem(str(row[col])))
            self.te_tencongviec_TimViec_dsCongViec.setText("")
            mycursor.close()
            mydb.close()
        except Error as e:
            print(f"Database error: {e}")
            self.te_tencongviec_TimViec_dsCongViec.setText("")
        except Exception as e:
            print(f"Error: {e}")
            self.te_tencongviec_TimViec_dsCongViec.setText("")

    def ungTuyen(self):
        file = open("manguoitimviec.txt", "r")
        manguoitimviec = str(file.read())
        file.close()
        macongviec = self.te_macongviec_TimViec_dsCongViec.text()

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="quanlygiaodichvieclam"
            )

            mycursor = mydb.cursor()

            # Kiểm tra nếu người tìm việc đã ứng tuyển công việc này
            mycursor.execute("SELECT * FROM chitietungtuyen WHERE manguoitimviec = %s AND macongviec = %s",
                             (manguoitimviec, macongviec))
            t = bool(mycursor.fetchall())
            if t:
                QtWidgets.QMessageBox.information(self.centralwidget, "Thông báo",
                                                  "Bạn đã đăng ký ứng tuyển công việc này")
            else:
                # kiểm tra xem đã đủ chỉ tiêu chưa
                mycursor.execute("SELECT chitieu, songuoiungtuyen FROM congviec WHERE macongviec = %s",
                                 (macongviec, ))
                kq = mycursor.fetchall()
                chitieu = int(kq[0][0])
                songuoiungtuyen = int(kq[0][1])
                if chitieu > songuoiungtuyen:
                    # Thêm 1 chitiettuyendung
                    mycursor.execute("INSERT INTO chitietungtuyen (macongviec, manguoitimviec, trangthai)"
                                     " VALUES (%s, %s, %s);",
                                     (macongviec, manguoitimviec, "Chưa phê duyệt"))
                    mydb.commit()

                    # Thêm 1 thông báo gửi cho nhà tuyển dụng
                    mycursor.execute("SELECT manhatuyendung FROM congviec WHERE macongviec = %s", (macongviec,))
                    manhatuyendung = mycursor.fetchone()[0]  # Lấy giá trị duy nhất

                    mycursor.execute("INSERT INTO tbtontd (manhatuyendung, manguoitimviec, noidung)"
                                     " VALUES (%s, %s, %s);",
                                     (manhatuyendung, manguoitimviec,
                                      f"Người tìm việc có mã là {manguoitimviec} đã đăng ký công việc của bạn, "
                                      f"hãy phê duyệt!"))
                    mydb.commit()

                    # Sửa số lượng người ứng tuyển của công việc
                    mycursor.execute("SELECT songuoiungtuyen FROM congviec WHERE macongviec = %s", (macongviec,))
                    songuoiungtuyen = mycursor.fetchone()[0]  # Lấy giá trị duy nhất
                    songuoiungtuyen += 1
                    mycursor.execute("UPDATE congviec SET songuoiungtuyen = %s WHERE macongviec = %s;",
                                     (songuoiungtuyen, macongviec))
                    mydb.commit()
                    QtWidgets.QMessageBox.information(self.centralwidget, "Thông báo",
                                                      "Bạn đã đăng ký ứng tuyển thành công.")
                    self.loadCongViec()
                    self.te_macongviec_TimViec_dsCongViec.setText('')
                else:
                    QtWidgets.QMessageBox.information(self.centralwidget, "Thông báo",
                                                      "Công việc này đã có đủ người đăng ký ứng tuyên, "
                                                      "hãy chờ nhà tuyển dụng phê duyệt họ để có thể ứng tuyển.")
            mycursor.close()
            mydb.close()
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            QtWidgets.QMessageBox.critical(self.centralwidget, "Lỗi", f"Lỗi cơ sở dữ liệu: {e}")
        except Exception as e:
            print(f"Error: {e}")
            QtWidgets.QMessageBox.critical(self.centralwidget, "Lỗi", f"Lỗi: {e}")

    def loadCongViec(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="quanlygiaodichvieclam"
            )

            mycursor = mydb.cursor()
            mycursor.execute("SELECT macongviec, manhatuyendung, tencongviec, mota, vitri, trinhdohocvan, "
                             "loaicongviec, chitieu, songuoiungtuyen, luong, tinhtrang FROM congviec")
            rows = mycursor.fetchall()
            col_count = len(mycursor.description)

            self.table_dsCongViec.setColumnCount(col_count)
            self.table_dsCongViec.setRowCount(len(rows))

            for tablerow, row in enumerate(rows):
                for col in range(col_count):
                    self.table_dsCongViec.setItem(tablerow, col, QtWidgets.QTableWidgetItem(str(row[col])))

            mycursor.close()
            mydb.close()
        except Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    timviec_DanhSachCongViec = QtWidgets.QMainWindow()
    ui = Ui_timviec_DanhSachCongViec()
    ui.setupUi(timviec_DanhSachCongViec)
    timviec_DanhSachCongViec.show()
    sys.exit(app.exec())
