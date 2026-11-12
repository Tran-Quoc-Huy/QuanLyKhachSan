from operator import truediv

from QuanLyDoiTuongKhachSan import *
from QuanLyTaiKhoanKhachSan import *


DSDatPhong = {}
DSPhong = {}

class PhongKhachSan:
    def __init__(self, maPhong, dienTich, soGiuong, giaThueMotNgay, trangThai):
        self.maPhong = maPhong
        self.dienTich = dienTich
        self.soGiuong = soGiuong
        self.giaThueMotNgay = giaThueMotNgay
        self.trangThai = trangThai

    def __str__(self):
        return f"Ma phong: {self.maPhong} - Dien tich: {self.dienTich} - So giuong: {self.soGiuong} - Gia thue mot ngay: {self.giaThueMotNgay:,.0f} - Trang thai: {self.trangThai}"


    @staticmethod
    def thongKe():
        if not DSPhong:
            print("Danh sach rong!")
            return
        soPhongTrong = 0
        soPhongDaThue = 0
        for value in DSPhong.values():
            if (value.trangThai == "Da thue"):
                soPhongDaThue += 1
            else :
                soPhongTrong += 1
        print(f"So phong trong: {soPhongTrong} \nSo phong da thue: {soPhongDaThue}")


    @staticmethod
    def inDanhSachPhong():
        if not DSPhong:
            print("Danh sach rong!")
            return

        print("Danh sach phong:")
        for value in DSPhong.values():
            print(f"{value}")

    @staticmethod
    def xoaPhong():
        if not DSPhong:
            print("Danh sach rong!")
            return

        for value in DSPhong.values():
            print(f"{value}")

        maPhong = input("Nhap ma phong muon xoa: ").strip()
        while maPhong == "" or maPhong not in DSPhong:
            if maPhong == "":
                maPhong = input("Ma phong khong duoc de trong! nhap lai: ").strip()
            else:
                maPhong = input("Ma phong chua ton tai! nhap lai: ").strip()

        DSPhong.pop(maPhong)
        print("Xoa thanh cong!")


    @staticmethod
    def updatePhong():

        for value in DSPhong.values():
            print(f"{value}")

        maPhong = input("Nhap ma phong: ").strip()
        while maPhong == "" or maPhong  not in DSPhong:
            if maPhong == "":
                maPhong = input("Ma phong khong duoc de trong! nhap lai: ").strip()
            else:
                maPhong = input("Ma phong chua ton tai! nhap lai: ").strip()

        print(f"Thong tin phong hien tai: {DSPhong[maPhong]}")


        dienTich = float(input("Nhap dien tich moi: "))
        while dienTich == "" or dienTich < 0:

            if dienTich == "":
                dienTich = float(input("Khong duoc bo trong! nhap lai: "))
            else:
                dienTich = float(input("Phai lon hon 0! nhap lai: "))

        soGiuong = int(input("Nhap so giuong moi: "))
        while soGiuong == "" or soGiuong < 0 or soGiuong > 10:
            if soGiuong == "":
                soGiuong = int(input("Khong the nho hon 0! nhap lai: "))
            else:
                soGiuong = int(input("So giuong khong hop le! nhap lai (0-10): "))

        giaThueMotNgay = float(input("Nhap gia thue mot ngay moi: "))
        while giaThueMotNgay == "" or giaThueMotNgay < 0:
            if giaThueMotNgay == "":
                giaThueMotNgay = float(input("Khong the bo trong! nhap lai: "))
            else:
                giaThueMotNgay = float(input("Khong the < 0! nhap lai: "))

        trangThai = input("Nhap trang thai moi (Trong / Da thue): ")
        while trangThai not in ["Trong", "Da thue"]:
            if trangThai == "":
                trangThai = input("Khong the bo trong! nhap lai: ")

            else :
                trangThai = input("Trang thai chi co the nhap (Trong / Da thue):")

        phong = PhongKhachSan(
            maPhong,
            dienTich,
            soGiuong,
            giaThueMotNgay,
            trangThai
        )

        DSPhong[maPhong] = phong
        print("Cap nhat phong thanh cong!")


    @staticmethod
    def thongKePhongTrong():
        if not DSPhong:
            print("Danh sach rong!")
            return 0

        print("Phong trong")
        soPhongTrong = 0

        for value in DSPhong.values():
            if value.trangThai != "Da thue":
                print(value)
                soPhongTrong += 1

        return soPhongTrong


    @staticmethod
    def themPhong():

        # ==========================================
        # 1. KIEM TRA DANG NHAP QUAN LY
        # ==========================================

        ten_tai_khoan = PHIEN_DANG_NHAP["ten_tai_khoan"]

        # Neu chua dang nhap hoac khong phai tai khoan quan ly
        if ten_tai_khoan not in DSQuanLyTheoTaiKhoan:

            while True:
                print("\n===== XAC THUC TAI KHOAN QUAN LY =====")
                print("1. Dang nhap")
                print("2. Dang ky tai khoan moi")
                print("0. Thoat them phong")

                lua_chon = input("Lua chon cua ban: ").strip()

                if lua_chon == "1":

                    ten_tai_khoan = login_QuanLy()

                    if ten_tai_khoan is not None:
                        break

                elif lua_chon == "2":
                    register_QuanLy()

                    ten_tai_khoan = PHIEN_DANG_NHAP["ten_tai_khoan"]

                    if ten_tai_khoan is not None:
                        break

                elif lua_chon == "0":
                    print("Da thoat chuc nang them phong!")
                    return

                else:
                    print("Lua chon khong hop le!")

        maPhong = input("Nhap ma phong: ").strip()
        while maPhong == "" or maPhong in DSPhong:
            if maPhong == "":
                maPhong = input("Ma phong khong duoc de trong! nhap lai: ").strip()
            else:
                maPhong = input("Ma phong da ton tai! nhap lai: ").strip()

        while True:
            dienTich = input("Nhap dien tich: ").strip()

            if dienTich == "":
                print("Khong the bo trong!")
                continue

            try:
                dienTich = float(dienTich)

                if dienTich <= 0:
                    print("Dien tich phai lon hon 0!")
                else:
                    break

            except ValueError:
                print("Dien tich khong hop le! Chi duoc nhap so.")


        soGiuong = int(input("Nhap so giuong: "))
        while soGiuong == "" or soGiuong < 0 or soGiuong > 10:
            if soGiuong == "":
                soGiuong = int(input("Khong the nho hon 0! nhap lai: "))
            else :
                soGiuong = int(input("So giuong khong hop le! nhap lai (0-10): "))

        giaThueMotNgay = float(input("Nhap gia thue mot ngay: "))
        while giaThueMotNgay == "" or giaThueMotNgay < 0:
            if giaThueMotNgay == "":
                giaThueMotNgay = float(input("Khong the bo trong! nhap lai: "))
            else :
                giaThueMotNgay = float(input("Khong the < 0! nhap lai: "))

        trangThai = input("Nhap trang thai (Trong / Da thue): ")
        while trangThai not in ["Trong", "Da thue"]:
            if trangThai == "":
                trangThai = input("Khong the bo trong! nhap lai: ")

            else :
                trangThai = input("Trang thai chi co the nhap (Trong / Da thue): ")

        phong = PhongKhachSan(
            maPhong,
            dienTich,
            soGiuong,
            giaThueMotNgay,
            trangThai
        )

        DSPhong[maPhong] = phong
        print("Them phong thanh cong!")



class PhieuDatPhong:
    def __init__(self, khachHang, soNgayThue):
        self.ma_phieu = ""
        self.khachHang = khachHang
        self.soNgayThue = soNgayThue
        self.phong = None
        self.trang_thai = "Dang thue"

    def tinhTien(self):
        if self.phong is None:
            return 0

        return self.soNgayThue * self.phong.giaThueMotNgay

    def __str__(self):
        return (
            f"Ma phieu: {self.ma_phieu}\n"
            f"Khach hang: {self.khachHang.ho_ten}\n"
            f"Ma khach hang: {self.khachHang.ma_khach_hang}\n"
            f"CCCD: {self.khachHang.so_cccd}\n"
            f"So dien thoai: {self.khachHang.so_dien_thoai}\n"
            f"Phong: {self.phong.maPhong}\n"
            f"So ngay thue: {self.soNgayThue}\n"
            f"Don gia: {self.phong.giaThueMotNgay}\n"
            f"Tong tien: {self.tinhTien()}\n"
            f"Trang thai: {self.trang_thai}"
        )


    def tinhTien(self):
        if self.phong is None:
            return 0

        return self.soNgayThue * self.phong.giaThueMotNgay

    def __str__(self):
        return (
            f"Ma phieu: {self.ma_phieu}\n"
            f"Khach hang: {self.khachHang.ho_ten}\n"
            f"Ma khach hang: {self.khachHang.ma_khach_hang}\n"
            f"CCCD: {self.khachHang.so_cccd}\n"
            f"So dien thoai: {self.khachHang.so_dien_thoai}\n"
            f"Phong: {self.phong.maPhong}\n"
            f"So ngay thue: {self.soNgayThue}\n"
            f"Don gia: {self.phong.giaThueMotNgay}\n"
            f"Tong tien: {self.tinhTien()}\n"
            f"Trang thai: {self.trang_thai}"
        )


    @staticmethod
    def datPhong():

        # ==========================================
        # 1. KIEM TRA DANG NHAP
        # ==========================================

        ten_tai_khoan = PHIEN_DANG_NHAP["ten_tai_khoan"]

        # Neu chua dang nhap hoac khong phai tai khoan khach hang
        if ten_tai_khoan not in DSKhachHangTheoTaiKhoan:

            while True:
                print("\n===== XAC THUC TAI KHOAN =====")
                print("1. Dang nhap")
                print("2. Dang ky tai khoan moi")
                print("0. Thoat dat phong")

                lua_chon = input("Lua chon cua ban: ").strip()

                if lua_chon == "1":

                    ten_tai_khoan = login_KhachHang()

                    if ten_tai_khoan is not None:
                        break

                elif lua_chon == "2":

                    register_KhachHang()

                    ten_tai_khoan = PHIEN_DANG_NHAP["ten_tai_khoan"]

                    if ten_tai_khoan is not None:
                        break

                elif lua_chon == "0":
                    print("Da thoat chuc nang dat phong!")
                    return

                else:
                    print("Lua chon khong hop le!")

        # ==========================================
        # 2. LAY THONG TIN KHACH HANG TU DSHuman
        # ==========================================

        ma_khach_hang = DSKhachHangTheoTaiKhoan[ten_tai_khoan]

        khach_hang = DSHuman.get(ma_khach_hang)

        if not isinstance(khach_hang, KhachHang):
            print("Khong tim thay thong tin khach hang!")
            return

        print("\n===== THONG TIN KHACH HANG =====")
        print(f"Ho ten: {khach_hang.ho_ten}")
        print(f"Ma khach hang: {khach_hang.ma_khach_hang}")
        print(f"So CCCD: {khach_hang.so_cccd}")
        print(f"So dien thoai: {khach_hang.so_dien_thoai}")

        # ==========================================
        # 3. KIEM TRA PHONG TRONG
        # ==========================================

        if not DSPhong:
            print("Danh sach phong rong!")
            return

        danh_sach_phong_trong = []

        for phong in DSPhong.values():
            if phong.trangThai == "Trong":
                danh_sach_phong_trong.append(phong)

        if not danh_sach_phong_trong:
            print("Khong con phong trong!")
            return

        print("\n===== DANH SACH PHONG TRONG =====")

        for phong in danh_sach_phong_trong:
            print(phong)

        # ==========================================
        # 4. CHON PHONG
        # ==========================================

        maPhong = input("\nNhap ma phong muon dat: ").strip()

        while (
                maPhong == ""
                or maPhong not in DSPhong
                or DSPhong[maPhong].trangThai != "Trong"
        ):

            if maPhong == "":
                print("Ma phong khong duoc de trong!")

            elif maPhong not in DSPhong:
                print("Ma phong khong ton tai!")

            else:
                print("Phong da duoc thue!")

            maPhong = input("Vui long chon lai ma phong: ").strip()

        phong = DSPhong[maPhong]

        # ==========================================
        # 5. NHAP SO NGAY THUE
        # ==========================================

        soNgayThue = input("Nhap so ngay thue: ").strip()

        while not soNgayThue.isdigit() or int(soNgayThue) <= 0:
            soNgayThue = input(
                "So ngay thue phai la so nguyen lon hon 0, nhap lai: "
            ).strip()

        soNgayThue = int(soNgayThue)

        # ==========================================
        # 6. TAO PHIEU DAT PHONG
        # ==========================================

        dem = 1

        ma_phieu = f"DP{dem:03d}"

        while ma_phieu in DSDatPhong:
            dem += 1
            ma_phieu = f"DP{dem:03d}"

        phieu = PhieuDatPhong(khach_hang, soNgayThue)

        phieu.ma_phieu = ma_phieu
        phieu.phong = phong
        phieu.trang_thai = "Dang thue"

        # Luu phieu theo ma phieu
        DSDatPhong[ma_phieu] = phieu

        # Cap nhat trang thai phong
        phong.trangThai = "Da thue"

        # ==========================================
        # 7. XUAT KET QUA
        # ==========================================

        print("\n===== DAT PHONG THANH CONG =====")
        print(f"Ma phieu: {ma_phieu}")
        print(phieu)

    def tinhTien(self):
        if self.phong is None:
            return 0
        return self.soNgayThue * self.phong.giaThueMotNgay

    def __str__(self):
        return (
            f"Khach hang: {self.khachHang.ho_ten}\n"
            f"CCCD: {self.khachHang.so_cccd}\n"
            f"Phong: {self.phong.maPhong}\n"
            f"So ngay thue: {self.soNgayThue}\n"
            f"Tong tien: {self.tinhTien()}"
        )

    @staticmethod
    def inToanBoPhieuDatPhong():
        if not DSDatPhong:
            print("Danh sach phieu dat phong rong!")
            return

        print("\n===== DANH SACH PHIEU DAT PHONG =====")

        for key, value in DSDatPhong.items():
            print(value)
            print("-" * 40)