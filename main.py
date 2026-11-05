from QuanLyDoiTuongKhachSan import *
from QuanLyThietBiKhachSan import *
from QuanLyTaiKhoanADMinKhachSan import *

def menu():
    ql_human = QuanLyHuman()
    ql_tb = QuanLyThietBi()

    while True:

        print("\n===== QUAN LY KHACH SAN =====")
        print("1. Quan ly nguoi")
        print("2. Quan ly thiet bi")
        print("3. Them Tai Khoan ADMin")
        print("4. Doi Tai Khoan ADMin")
        print("0. Thoat")

        chon = input("Nhap lua chon: ")

        if chon == "1":

            while True:

                print("\n===== QUAN LY NGUOI =====")
                print("1. Them")
                print("2. Hien thi")
                print("3. Tim kiem")
                print("4. Sua")
                print("5. Xoa")
                print("6. Thong ke")
                print("0. Quay lai")

                c = input("Nhap lua chon: ")

                if c == "1":
                    ql_human.them()

                elif c == "2":
                    ql_human.inDanhSach()

                elif c == "3":
                    ql_human.timTheoDieuKien_MaDoiTuong()

                elif c == "4":
                    ql_human.sua()

                elif c == "5":
                    ql_human.xoa()

                elif c == "6":
                    ql_human.thongKe()

                elif c == "0":
                    break

        elif chon == "2":

            while True:

                print("\n===== QUAN LY THIET BI =====")
                print("1. Them")
                print("2. Hien thi")
                print("3. Tim kiem")
                print("4. Sua")
                print("5. Xoa")
                print("6. Thong ke")
                print("0. Quay lai")

                c = input("Nhap lua chon: ")

                if c == "1":
                    ql_tb.them()

                elif c == "2":
                    ql_tb.inDanhSach()

                elif c == "3":
                    ql_tb.timTheoMa()

                elif c == "4":
                    ql_tb.sua()

                elif c == "5":
                    ql_tb.xoa()

                elif c == "6":
                    ql_tb.thongKe()

                elif c == "0":
                    break

        elif chon == "3":
            register()

        elif chon == "4":
            login()

        elif chon == "0":
            print("Tam biet!")
            break


if __name__ == "__main__":

    register()

    if login():
        menu()

    else:
        print("Khoi dong chuong trinh that bai!")