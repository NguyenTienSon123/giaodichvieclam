import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="quanlygiaodichvieclam"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE QuanLyGiaoDichViecLam")

# mycursor.execute("CREATE TABLE taikhoan ("
#                  "manguoidung INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
#                  "tendangnhap VARCHAR(50) NOT NULL,"
#                  "matkhau VARCHAR(30) NOT NULL,"
#                  "level INT(6)"
#                  ");")
# mycursor.execute("CREATE TABLE nhatuyendung ("
#                  "manhatuyendung INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
#                  "manguoidung INT(6) UNSIGNED,"
#                  "ten VARCHAR(100) NOT NULL,"
#                  "sdt VARCHAR(10) NOT NULL,"
#                  "mail VARCHAR(70) NOT NULL,"
#                  "thanhpho VARCHAR(30),"
#                  "FOREIGN KEY (manguoidung) REFERENCES taikhoan(manguoidung)"
#                  ");")
#
# mycursor.execute("CREATE TABLE nguoitimviec ("
#                  "manguoitimviec INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
#                  "manguoidung INT(6) UNSIGNED,"
#                  "ten VARCHAR(100) NOT NULL,"
#                  "sdt VARCHAR(10) NOT NULL,"
#                  "mail VARCHAR(70) NOT NULL,"
#                  "thanhpho VARCHAR(30),"
#                  "FOREIGN KEY (manguoidung) REFERENCES taikhoan(manguoidung)"
#                  ");")
#
# mycursor.execute("CREATE TABLE hoso ("
#                  "mahoso INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
#                  "manguoitimviec INT(6) UNSIGNED,"
#                  "kinhnghiemlamviec VARCHAR(500),"
#                  "trinhdohocvan VARCHAR(500) NOT NULL,"
#                  "hoatdong VARCHAR(500),"
#                  "giaykhen VARCHAR(100),"
#                  "duan VARCHAR(100),"
#                  "chungchi VARCHAR(100),"
#                  "gioitinh VARCHAR(4),"
#                  "FOREIGN KEY (manguoitimviec) REFERENCES nguoitimviec(manguoitimviec)"
#                  ");")
#
# mycursor.execute("CREATE TABLE congviec ("
#                  "macongviec INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
#                  "manhatuyendung INT(6) UNSIGNED,"
#                  "trinhdohocvan VARCHAR(500) NOT NULL,"
#                  "tencongviec VARCHAR(50),"
#                  "loaicongviec VARCHAR(50),"
#                  "chitieu INT(100),"
#                  "songuoiungtuyen INT(100),"
#                  "mota VARCHAR(500),"
#                  "vitri VARCHAR(30),"
#                  "tinhtrang VARCHAR(60),"
#                  "FOREIGN KEY (manhatuyendung) REFERENCES nhatuyendung(manhatuyendung),"
#                  "luong VARCHAR(9)"
#                  ");")
#
# mycursor.execute("CREATE TABLE chitietungtuyen ("
#                  "machitietungtuyen INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
#                  "macongviec INT(6) UNSIGNED,"
#                  "manguoitimviec INT(6) UNSIGNED,"
#                  "FOREIGN KEY (manguoitimviec) REFERENCES nguoitimviec(manguoitimviec),"
#                  "FOREIGN KEY (macongviec) REFERENCES congviec(macongviec),"
#                  "trangthai VARCHAR(20)"
#                  ");")
#
# mycursor.execute("CREATE TABLE tbtontv ("
#                  "matb INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
#                  "manhatuyendung INT(6) UNSIGNED,"
#                  "manguoitimviec INT(6) UNSIGNED,"
#                  "FOREIGN KEY (manguoitimviec) REFERENCES nguoitimviec(manguoitimviec),"
#                  "FOREIGN KEY (manhatuyendung) REFERENCES nhatuyendung(manhatuyendung),"
#                  "noidung VARCHAR(300)"
#                  ");")
#
# mycursor.execute("CREATE TABLE tbtontd ("
#                  "matb INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
#                  "manhatuyendung INT(6) UNSIGNED,"
#                  "manguoitimviec INT(6) UNSIGNED,"
#                  "FOREIGN KEY (manguoitimviec) REFERENCES nguoitimviec(manguoitimviec),"
#                  "FOREIGN KEY (manhatuyendung) REFERENCES nhatuyendung(manhatuyendung),"
#                  "noidung VARCHAR(300);"
#                  ");")


