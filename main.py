from QuanLyDoiTuongKhachSan import *
from QuanLyThietBiKhachSan import *
from QuanLyTaiKhoanADMinKhachSan import *
from QuanLyPhongKhachSan import *

def menu():
    ql_human = QuanLyHuman()
    ql_tb = QuanLyThietBi()

    while True:

        print("\n===== QUAN LY KHACH SAN =====")
        print("1. Quan ly nguoi")
        print("2. Quan ly thiet bi")
        print("3. Quan ly phong")
        print("4. Them Tai Khoan ADMin")
        print("5. Doi Tai Khoan ADMin")
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

            while True:

                print("\n===== QUAN LY PHONG =====")

                print("1. Them phong")

                print("2. Dat phong")

                print("3. In phieu dat phong")

                print("0. Quay lai")

                chose = input("Nhap lua chon: ")

                if chose == "1":

                    PhongKhachSan.themPhong()


                elif chose == "2":

                    tenKhachHang = input("Nhap ten khach hang: ").strip()

                    while tenKhachHang == "" or tenKhachHang.isdigit():
                        if tenKhachHang == "":
                            print("Khong the bo trong!")
                        else:
                            print("Ten khach hang khong the chi gom so!")

                        tenKhachHang = input("Nhap lai ten khach hang: ").strip()

                    phieu = PhieuDatPhong(tenKhachHang, 0)
                    phieu.datPhong()


                elif chose == "3":

                    PhieuDatPhong.inToanBoPhieuDatPhong()


                elif chose == "0":

                    break


                else:

                    print("Lua chon khong hop le!")

        elif chon == "4":
            register()

        elif chon == "5":
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