# ========== REGISTER ==========

def register():
    ten_tk = input("DANG KY! \nEnter your nick name: ")
    mat_khau_tk = input("Enter your password: ")
    return  ten_tk, mat_khau_tk

# ========== LOGIN ==========

def login(ten_tk, mat_khau_tk):
    so_lan_thu = 0

    print("DANG NHAP!")

    while so_lan_thu < 3:
        nick_name = input("Enter your nick name: ")
        mat_khau = input("Enter your password: ")

        if nick_name == ten_tk and mat_khau == mat_khau_tk:
            print("Dang nhap thanh cong")
            return True
        else:
            so_lan_thu += 1
            print(f"Dang nhap that bai (so lan thu con {3 - so_lan_thu})")

    print("Dang nhap that bai!")
    return False


# ========== CLASS CƠ SỞ ==========

class Human:
    def __init__(self, ho_ten, ngay_sinh, gioi_tinh, so_dien_thoai):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.gioi_tinh = gioi_tinh
        self.so_dien_thoai = so_dien_thoai


# ========== CLASS KẾ THỪA - LỄ TÂN ==========

class LeTan(Human):
    def __init__(
        self,
        ho_ten,
        ngay_sinh,
        gioi_tinh,
        so_dien_thoai,
        ma_le_tan,
        ca_lam,
        luong,
        chuc_vu,
        ten_dang_nhap
    ):
        super().__init__(
            ho_ten,
            ngay_sinh,
            gioi_tinh,
            so_dien_thoai
        )

        self.ma_le_tan = ma_le_tan
        self.ca_lam = ca_lam
        self.luong = luong
        self.chuc_vu = chuc_vu
        self.ten_dang_nhap = ten_dang_nhap

#===========dung de in value===========
    def __str__(self):
        return f"Ho & ten: {self.ho_ten} - Ngay sinh: {self.ngay_sinh} - Gioi tinh:  {self.gioi_tinh} - So dien thoai: {self.so_dien_thoai} - Ca lam: {self.ca_lam} - Luong(k/h): {self.luong} - Chuc vu: {self.chuc_vu} - Ten dang nhap: {self.ten_dang_nhap}"


# ========== CLASS KẾ THỪA - KHÁCH HÀNG ==========

class KhachHang(Human):
    def __init__(
        self,
        ho_ten,
        ngay_sinh,
        gioi_tinh,
        so_dien_thoai,
        ma_khach_hang,
        dia_chi,
        email,
        so_cccd,
        quoc_tich
    ):
        super().__init__(
            ho_ten,
            ngay_sinh,
            gioi_tinh,
            so_dien_thoai
        )

        self.ma_khach_hang = ma_khach_hang
        self.dia_chi = dia_chi
        self.email = email
        self.so_cccd = so_cccd
        self.quoc_tich = quoc_tich

    def __str__(self):
        return f"Ho & ten: {self.ho_ten} - Ngay sinh: {self.ngay_sinh} - Gioi tinh: {self.gioi_tinh} - So dien thoai: {self.so_dien_thoai} - Ma khach hang: {self.ma_khach_hang} - Dia chi: {self.dia_chi} - Email: {self.email} - So CCCD: {self.so_cccd} - Quoc tich: {self.quoc_tich}"



# ========== CLASS QUẢN LÝ KHÁCH SẠN ==========

class QuanLyKhachSan:
    def __init__(self):
        self.ds_human = {}


# ========== CLASS QUẢN LÝ HUMAN ==========

class QuanLyHuman:
    def __init__(self):
        self.ds_human = {}

    def them(self):

        # ========== CHỌN LOẠI ĐỐI TƯỢNG ==========

        loai = input(
            "Chon doi tuong muon them \n1 - Lễ tân, 2 - Khách hàng: "
        ).strip()

        while loai != "1" and loai != "2":
            print("Loại không hợp lệ!")

            loai = input(
                "Vui lòng nhập 1 - Lễ tân, 2 - Khách hàng: "
            ).strip()


        # ========== HỌ TÊN ==========

        ho_ten = input("Họ tên: ").strip()

        while ho_ten == "" or any(
            ky_tu.isdigit() for ky_tu in ho_ten
        ):
            if ho_ten == "":
                ho_ten = input(
                    "Họ tên không được để trống, nhập lại: "
                ).strip()
            else:
                ho_ten = input(
                    "Họ tên không được chứa số, nhập lại: "
                ).strip()


        # ========== NGÀY SINH ==========

        ngay_sinh = input("Ngày sinh: ").strip()

        while ngay_sinh == "":
            ngay_sinh = input(
                "Ngày sinh không được để trống, nhập lại: " #ktr chu
            ).strip()


        # ========== GIỚI TÍNH ==========

        gioi_tinh = input(
            "Giới tính (Nam/Nữ): "
        ).strip()

        while gioi_tinh == "" or any(
            ky_tu.isdigit() for ky_tu in gioi_tinh
        ):
            if gioi_tinh == "":
                gioi_tinh = input(
                    "Giới tính không được để trống, nhập lại: "
                ).strip()
            else:
                gioi_tinh = input(
                    "Giới tính không được chứa số, nhập lại: "
                ).strip()


        # ========== SỐ ĐIỆN THOẠI ==========

        so_dien_thoai = input(
            "Số điện thoại: "
        ).strip()

        while so_dien_thoai == "" or not so_dien_thoai.isdigit():
            if so_dien_thoai == "":
                so_dien_thoai = input(
                    "Số điện thoại không được để trống, nhập lại: "
                ).strip()
            else:
                so_dien_thoai = input(
                    "Số điện thoại chỉ được nhập số, nhập lại: "
                ).strip()


        # ==================================================
        #                    LỄ TÂN
        # ==================================================

        if loai == "1":

            # Mã lễ tân
            ma_le_tan = input(
                "Mã lễ tân: "
            ).strip()

            while ma_le_tan == "":
                ma_le_tan = input(
                    "Mã lễ tân không được để trống, nhập lại: "
                ).strip()


            # Ca làm
            ca_lam = input(
                "Ca làm: "
            ).strip()

            while ca_lam == "":
                ca_lam = input(
                    "Ca làm không được để trống, nhập lại: "
                ).strip()


            # Lương
            luong = input(
                "Lương(k/h): "
            ).strip()

            while luong == "" or not luong.replace(".", "", 1).isdigit():
                if luong == "":
                    luong = input(
                        "Lương không được để trống, nhập lại: "
                    ).strip()
                else:
                    luong = input(
                        "Lương phải là số, nhập lại: "
                    ).strip()

            luong = float(luong)


            # Chức vụ
            chuc_vu = input(
                "Chức vụ: "
            ).strip()

            while chuc_vu == "" or any(
                ky_tu.isdigit() for ky_tu in chuc_vu
            ):
                if chuc_vu == "":
                    chuc_vu = input(
                        "Chức vụ không được để trống, nhập lại: "
                    ).strip()
                else:
                    chuc_vu = input(
                        "Chức vụ không được chứa số, nhập lại: "
                    ).strip()


            # Tên đăng nhập
            ten_dang_nhap = input(
                "Tên đăng nhập: "
            ).strip()

            while ten_dang_nhap == "":
                ten_dang_nhap = input(
                    "Tên đăng nhập không được để trống, nhập lại: "
                ).strip()


            # Tạo đối tượng lễ tân
            le_tan = LeTan(
                ho_ten,
                ngay_sinh,
                gioi_tinh,
                so_dien_thoai,
                ma_le_tan,
                ca_lam,
                luong,
                chuc_vu,
                ten_dang_nhap
            )

            # Lưu vào dictionary
            self.ds_human[ma_le_tan] = le_tan


        # ==================================================
        #                  KHÁCH HÀNG
        # ==================================================

        elif loai == "2":

            # Mã khách hàng
            ma_khach_hang = input(
                "Mã khách hàng: "
            ).strip()

            while ma_khach_hang == "":
                ma_khach_hang = input(
                    "Mã khách hàng không được để trống, nhập lại: "
                ).strip()


            # Địa chỉ
            dia_chi = input(
                "Địa chỉ: "
            ).strip()

            while dia_chi == "":
                dia_chi = input(
                    "Địa chỉ không được để trống, nhập lại: "
                ).strip()


            # Email
            email = input(
                "Email: "
            ).strip()

            while email == "":
                email = input(
                    "Email không được để trống, nhập lại: "
                ).strip()


            # CCCD
            so_cccd = input(
                "Số CCCD: "
            ).strip()

            while so_cccd == "" or not so_cccd.isdigit():
                if so_cccd == "":
                    so_cccd = input(
                        "CCCD không được để trống, nhập lại: "
                    ).strip()
                else:
                    so_cccd = input(
                        "CCCD chỉ được nhập số, nhập lại: "
                    ).strip()


            # Quốc tịch
            quoc_tich = input(
                "Quốc tịch: "
            ).strip()

            while quoc_tich == "" or any(
                ky_tu.isdigit() for ky_tu in quoc_tich
            ):
                if quoc_tich == "":
                    quoc_tich = input(
                        "Quốc tịch không được để trống, nhập lại: "
                    ).strip()
                else:
                    quoc_tich = input(
                        "Quốc tịch không được chứa số, nhập lại: "
                    ).strip()


            # Tạo đối tượng khách hàng
            khach_hang = KhachHang(
                ho_ten,
                ngay_sinh,
                gioi_tinh,
                so_dien_thoai,
                ma_khach_hang,
                dia_chi,
                email,
                so_cccd,
                quoc_tich
            )

            # Lưu vào dictionary
            self.ds_human[ma_khach_hang] = khach_hang


        print("Thêm thành công!")
# ============XOA DOI TUONG THEO MA==============
    def xoa(self):
        if not self.ds_human:
            print("Danh sach rong!")
            return
        while True:
            key = input("Nhap ma doi tuong can xoa: ").strip()
            while key == "":
                key = input("Khong the bo trong! vui long nhap lai: ").strip()
            if key in self.ds_human:
                self.ds_human.pop(key)
                print(f"Da xoa thanh cong doi tuong co ma la {key}!")
            else:
                print("Khong tim thay doi tuong hop le!")
            chose = input("1 - nhap lai, 0 - thoat: ").strip()
            if chose != "1":
                break

# =================IN FULL DS================
    def inDanhSach(self):
        if not self.ds_human:
            print("Danh sach rong!")
            return
        for key, value in self.ds_human.items():
            print(f"Ma Doi Tuong: {key} : {value} \n")

#===========IN THEO MA===========
    def inTHeoMa(self,maDT):
        if not self.ds_human:
            print("Danh sach rong!")
            return
        for key, value in self.ds_human.items():
            if maDT == key:
                print(f"Ma Doi Tuong: {key} : {value} \n")

    def timTheoDieuKien_MaDoiTuong(self):
        if not self.ds_human:
            print("Danh sach rong!")
            return
        while True:
            key = input("Nhap ma doi tuong can tim: ").strip()
            if key in self.ds_human:
                self.inTHeoMa(key)
            else:
                print("Khong tim thay doi tuong hop le!")
            key = input("1 - nhap lai, 0 - thoat: ").strip()
            if key != "1":
                break


# ========== CHẠY CHƯƠNG TRÌNH ==========

if __name__ == "__main__":
    a,b = register()
    login(a,b)
    ql = QuanLyHuman()
    ql.them()
    ql.inDanhSach()
    ql.timTheoDieuKien_MaDoiTuong()
    ql.xoa()
    ql.inDanhSach()