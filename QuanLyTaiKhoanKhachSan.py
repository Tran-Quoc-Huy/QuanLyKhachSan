from QuanLyDoiTuongKhachSan import *

# ==========KHOI TAO TU DIEN LUU THONG TIN TAI KHOAN========
DSTaiKhoan = {}

# Luu tai khoan dang dang nhap hien tai
PHIEN_DANG_NHAP = {"ten_tai_khoan": None}

# Lien ket tai khoan voi ma khach hang
DSKhachHangTheoTaiKhoan = {}

# ========== REGISTER ==========
def register_QuanLy():
    ten_tk_ql = input("DANG KY TAI KHOANG QUAN LY! \nEnter your nick name: ").strip()
    while ten_tk_ql == "":
        ten_tk_ql = input("Khong the bo trong ten tai khoan: ").strip()

    mat_khau_tk_ql = input("Enter your password: ").strip()
    while mat_khau_tk_ql == "":
        mat_khau_tk_ql = input("Khong the bo trong mat khau: ").strip()

    DSTaiKhoan[ten_tk_ql] = mat_khau_tk_ql

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
            "Ngày sinh không được để trống, nhập lại: "
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


    # Mã lễ tân
    ma_le_tan = input(
        "Mã lễ tân: "
    ).strip()

    while ma_le_tan == "" or ma_le_tan in DSHuman:
        if ma_le_tan == "":
            ma_le_tan = input(
                "Mã lễ tân không được để trống, nhập lại: "
            ).strip()
        else:
            ma_le_tan = input("Ma da ton tai! vui long nhap lai: ").strip()

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

    while luong == "" or not luong.isdigit():
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


    # Tạo đối tượng lễ tân
    Quanly = QuanLyKhachSan(
        ho_ten,
        ngay_sinh,
        gioi_tinh,
        so_dien_thoai,
        ma_le_tan,
        ca_lam,
        luong,
        chuc_vu
    )

    # Lưu vào dictionary
    DSHuman[ma_le_tan] = Quanly


def register_KhachHang():
    ten_tk_kh = input("DANG KY TAI KHOAN KHACH HANG!\nEnter your nickname: ").strip()

    while ten_tk_kh == "" or ten_tk_kh in DSTaiKhoan:
        if ten_tk_kh == "":
            ten_tk_kh = input("Khong the bo trong ten tai khoan: ").strip()
        else:
            ten_tk_kh = input("Tai khoan da ton tai, nhap lai: ").strip()

    mat_khau_tk_kh = input("Enter your password: ").strip()
    while mat_khau_tk_kh == "":
        mat_khau_tk_kh = input("Khong the bo trong mat khau: ").strip()



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
            "Ngày sinh không được để trống, nhập lại: "
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

    while so_cccd == "" or not so_cccd.isdigit() or kiemTraCCCDTonTai(so_cccd):
        if so_cccd == "":
            so_cccd = input(
                "CCCD không được để trống, nhập lại: "
            ).strip()
        elif so_cccd.isdigit():
            so_cccd = input(
                "CCCD chỉ được nhập số, nhập lại: "
            ).strip()
        else:
            so_cccd = input("So cccd da ton tai! vui long nhap lai: ").strip()

    # Địa chỉ
    dia_chi = input(
        "Địa chỉ: "
    ).strip()

    while dia_chi == "":
        dia_chi = input(
            "Địa chỉ không được để trống, nhập lại: "
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



            # Mã khách hàng
    ma_khach_hang = input(
        "Mã khách hàng: "
    ).strip()
    while ma_khach_hang == "" or ma_khach_hang in DSHuman:
        if (ma_khach_hang == ""):
            ma_khach_hang = input(
                "Mã khách hàng không được để trống, nhập lại: "
            ).strip()
        else:
            ma_khach_hang = input("Ma da ton tai! nhap lai: ").strip()



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

    # 1. Lưu thông tin khách hàng
    DSHuman[ma_khach_hang] = khach_hang

    # 2. Lưu tài khoản và mật khẩu
    DSTaiKhoan[ten_tk_kh] = mat_khau_tk_kh

    # 3. Liên kết tài khoản với mã khách hàng
    DSKhachHangTheoTaiKhoan[ten_tk_kh] = ma_khach_hang

    # 4. Thiết lập phiên đăng nhập
    PHIEN_DANG_NHAP["ten_tai_khoan"] = ten_tk_kh

    print("Dang ky tai khoan thanh cong!")
    print("Them thong tin khach hang thanh cong!")
# ========== LOGIN ==========

def login_KhachHang():
    if not DSTaiKhoan:
        print("Chua co tai khoang! dang ky va quay lai")
        return

    so_lan_thu = 0

    print("DANG NHAP TAI KHOAN KHACH HANG!")

    while so_lan_thu < 3:
        nick_name = input("Enter your nick name: ").strip()
        mat_khau = input("Enter your password: ").strip()

        if nick_name in DSTaiKhoan and DSTaiKhoan[nick_name] == mat_khau:

            if nick_name not in DSKhachHangTheoTaiKhoan:
                print("Tai khoan chua duoc lien ket voi khach hang!")
                return None

            PHIEN_DANG_NHAP["ten_tai_khoan"] = nick_name

            print(f"Dang nhap thanh cong! Xin chao: {nick_name}!")

            return nick_name

        else:
            so_lan_thu += 1

            if so_lan_thu != 3:
                print(f"Sai thong tin! Con {3 - so_lan_thu} lan thu.")

    print("Dang nhap that bai!")
    return None
def login_QuanLy():
    so_lan_thu = 0

    print("DANG NHAP TAI KHOANG QUAN LY!")

    while so_lan_thu < 3:
        nick_name = input("Enter your nick name: ")
        mat_khau = input("Enter your password: ")

        if nick_name in DSTaiKhoan and DSTaiKhoan[nick_name] == mat_khau:
            print(f"Dang nhap thanh cong!\nXin chao quan ly: {nick_name}!")
            return True

        else:
            so_lan_thu += 1
            if so_lan_thu != 3:
                print(f"Sai thong tin dang nhap! so lan thu con: {3 - so_lan_thu}")

    print("Dang nhap that bai!")
    return False


if __name__ == '__main__':
    QL = QuanLyHuman()
    register_QuanLy()
    login_QuanLy()
    QL.inDanhSach()
