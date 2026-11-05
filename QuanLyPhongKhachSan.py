
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
        return f"Ma phong: {self.maPhong} - Dien tich: {self.dienTich} - So giuong: {self.soGiuong} - Gia thue mot ngay: {self.giaThueMotNgay}"

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

        trangThai = input("Nhap trang thai: ")
        while trangThai == "":
            trangThai = input("Khong the bo trong! nhap lai: ")

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
    def __init__(self, tenKhachHang, soNgayThue):
        self.tenKhachHang = tenKhachHang
        self.soNgayThue = soNgayThue
        self.phong = None

    def datPhong(self):
        maPhong = input("Nhap ma phong muon dat: ").strip()

        while True:
            if maPhong not in DSPhong:
                maPhong = input("Ma phong chua ton tai! Nhap lai: ").strip()
                continue

            phong = DSPhong[maPhong]

            if phong.trangThai == "daThue":
                maPhong = input("Phong da duoc thue! Chon lai: ").strip()
                continue

            break

        self.phong = phong

        self.soNgayThue = int(input("Nhap so ngay thue: "))

        DSDatPhong[maPhong] = self

        phong.trangThai = "daThue"

        print("Dat phong thanh cong!")
        print(f"Tong tien: {self.tinhTien()}")

    def tinhTien(self):
        if self.phong is None:
            return 0
        return self.soNgayThue * self.phong.giaThueMotNgay

    def __str__(self):
        return (
            f"Khach hang: {self.tenKhachHang}\n"
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