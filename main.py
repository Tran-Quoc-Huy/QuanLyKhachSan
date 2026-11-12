
# ========== IMPORT CAC MODULE ==========

from QuanLyTaiKhoanKhachSan import *
from QuanLyDoiTuongKhachSan import *
from QuanLyPhongKhachSan import *
from QuanLyThietBiKhachSan import *


# ==================================================
# MENU QUAN LY NGUOI
# ==================================================

def menuQuanLyNguoi(ql_human):

    while True:
        print("\n========== QUAN LY NGUOI ==========")
        print("1. Them")
        print("2. Hien thi danh sach")
        print("3. Tim kiem")
        print("4. Sua thong tin")
        print("5. Xoa")
        print("6. Thong ke")
        print("0. Quay lai")

        chon = input("Nhap lua chon: ").strip()

        if chon == "1":
            ql_human.them()

        elif chon == "2":
            ql_human.inDanhSach()

        elif chon == "3":
            ql_human.timTheoDieuKien_MaDoiTuong()

        elif chon == "4":
            ql_human.sua()

        elif chon == "5":
            ql_human.xoa()

        elif chon == "6":
            ql_human.thongKe()

        elif chon == "0":
            break

        else:
            print("Lua chon khong hop le!")


# ==================================================
# MENU QUAN LY THIET BI
# ==================================================

def menuQuanLyThietBi(ql_tb):

    while True:
        print("\n========== QUAN LY THIET BI ==========")
        print("1. Them thiet bi")
        print("2. Hien thi danh sach")
        print("3. Tim kiem")
        print("4. Sua thong tin")
        print("5. Xoa thiet bi")
        print("6. Thong ke")
        print("0. Quay lai")

        chon = input("Nhap lua chon: ").strip()

        if chon == "1":
            ql_tb.them()

        elif chon == "2":
            ql_tb.inDanhSach()

        elif chon == "3":
            ql_tb.menuTimKiem()

        elif chon == "4":
            ql_tb.sua()

        elif chon == "5":
            ql_tb.xoa()

        elif chon == "6":
            ql_tb.menuThongKe()

        elif chon == "0":
            break

        else:
            print("Lua chon khong hop le!")


# ==================================================
# MENU QUAN LY PHONG
# ==================================================

def menuQuanLyPhong():

    while True:
        print("\n========== QUAN LY PHONG ==========")
        print("1. Them phong")
        print("2. Cap nhat phong")
        print("3. Xoa phong")
        print("4. Dat phong")
        print("5. Hien thi danh sach phong")
        print("6. Thong ke phong")
        print("7. In toan bo phieu dat phong")
        print("0. Quay lai")

        chon = input("Nhap lua chon: ").strip()

        if chon == "1":
            PhongKhachSan.themPhong()

        elif chon == "2":
            PhongKhachSan.updatePhong()

        elif chon == "3":
            PhongKhachSan.xoaPhong()

        elif chon == "4":
            PhieuDatPhong.datPhong()

        elif chon == "5":
            PhongKhachSan.inDanhSachPhong()

        elif chon == "6":
            PhongKhachSan.thongKe()

        elif chon == "7":
            PhieuDatPhong.inToanBoPhieuDatPhong()

        elif chon == "0":
            break

        else:
            print("Lua chon khong hop le!")


# ==================================================
# MENU CHINH
# ==================================================

def menu():

    # Khoi tao cac doi tuong quan ly
    ql_human = QuanLyHuman()
    ql_tb = QuanLyThietBi()

    while True:
        print("\n====================================")
        print("         QUAN LY KHACH SAN")
        print("====================================")
        print("1. Quan ly nguoi")
        print("2. Quan ly thiet bi")
        print("3. Quan ly phong")
        print("0. Thoat chuong trinh")

        chon = input("Nhap lua chon: ").strip()

        if chon == "1":
            menuQuanLyNguoi(ql_human)

        elif chon == "2":
            menuQuanLyThietBi(ql_tb)

        elif chon == "3":
            menuQuanLyPhong()

        elif chon == "0":
            print("Tam biet!")
            break

        else:
            print("Lua chon khong hop le!")


# ==================================================
# MAIN
# ==================================================


if __name__ == "__main__":
    menu()
