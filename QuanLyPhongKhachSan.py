from QuanLyDoiTuongKhachSan import *

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
        return f"Ma phong: {self.maPhong} - Dien tich: {self.dienTich} - So giuong: {self.soGiuong} - Gia thue mot ngay: {self.giaThueMotNgay} - Trang thai: {self.trangThai}"


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
        maPhong = input("Nhap ma phong: ").strip()
        while maPhong == "" or maPhong in DSPhong:
            if maPhong == "":
                maPhong = input("Ma phong khong duoc de trong! nhap lai: ").strip()
            else:
                maPhong = input("Ma phong da ton tai! nhap lai: ").strip()

        dienTich = float(input("Nhap dien tich: "))
        while dienTich == "" or dienTich < 0:

            if dienTich == "":
                dienTich = float(input("Khong duoc bo trong! nhap lai: "))
            else :
                dienTich = float(input("Phai lon hon 0! nhap lai: "))

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
        self.khachHang = khachHang
        self.soNgayThue = soNgayThue
        self.phong = None

    @staticmethod
    def datPhong():
        if not DSPhong:
            print("Ds rong!")
            return

        soPhongTrong = PhongKhachSan.thongKePhongTrong()

        if soPhongTrong == 0:
            print("Khong con phong trong!")
            return

        def nhapThongTinKhachHang():

            cccd = input("Nhap CCCD khach hang: ").strip()

            while cccd == "" or not cccd.isdigit():
                cccd = input("CCCD khong hop le! nhap lai: ").strip()

            khach_hang = timKhachHangTheoCCCD(cccd)

            if khach_hang is not None:
                print("Khach hang da ton tai!")
                print(f"Ho ten: {khach_hang.ho_ten}")

                return khach_hang

            print("Khach hang moi!")

            tenKhachHang = input("Nhap ten khach hang: ").strip()

            while tenKhachHang == "" or tenKhachHang.isdigit():
                if tenKhachHang == "":
                    print("Khong the bo trong!")
                else:
                    print("Ten khach hang khong the chi gom so!")

                tenKhachHang = input("Nhap lai ten khach hang: ").strip()

            ma_khach_hang = input("Nhap ma khach hang: ").strip()

            while ma_khach_hang == "" or ma_khach_hang in DSHuman:
                ma_khach_hang = input(
                    "Ma khach hang khong hop le! nhap lai: "
                ).strip()

            ngay_sinh = input("Nhap ngay sinh: ").strip()
            gioi_tinh = input("Nhap gioi tinh: ").strip()
            so_dien_thoai = input("Nhap so dien thoai: ").strip()
            dia_chi = input("Nhap dia chi: ").strip()
            email = input("Nhap email: ").strip()
            quoc_tich = input("Nhap quoc tich: ").strip()

            khach_hang = KhachHang(
                tenKhachHang,
                ngay_sinh,
                gioi_tinh,
                so_dien_thoai,
                ma_khach_hang,
                dia_chi,
                email,
                cccd,
                quoc_tich
            )

            DSHuman[ma_khach_hang] = khach_hang

            print("Da them khach hang moi!")

            return khach_hang

        khach_hang = nhapThongTinKhachHang()

        maPhong = input("Nhap ma phong muon dat: ").strip()

        while maPhong not in DSPhong:
            maPhong = input("Ma phong chua ton tai! nhap lai: ").strip()

        phong = DSPhong[maPhong]

        while phong.trangThai == "daThue":
            maPhong = input("Phong da duoc thue! Chon lai: ").strip()

            while maPhong not in DSPhong:
                maPhong = input("Ma phong chua ton tai! nhap lai: ").strip()

            phong = DSPhong[maPhong]

        soNgayThue = int(input("Nhap so ngay thue: "))

        phieu = PhieuDatPhong(khach_hang, soNgayThue)
        phieu.phong = phong

        DSDatPhong[maPhong] = phieu

        phong.trangThai = "Da thue"

        print("Dat phong thanh cong!")
        print(f"Tong tien: {phieu.tinhTien()}")

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