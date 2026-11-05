# ==========KHOI TAO TU DIEN LUU THONG TIN TAI KHOAN========
DSTaiKhoan = {}

# ========== REGISTER ==========

def register():
    ten_tk = input("DANG KY! \nEnter your nick name: ").strip()
    while ten_tk == "":
        ten_tk = input("Khong the bo trong ten tai khoan: ").strip()

    mat_khau_tk = input("Enter your password: ").strip()
    while mat_khau_tk == "":
        mat_khau_tk = input("Khong the bo trong mat khau: ").strip()

    DSTaiKhoan[ten_tk] = mat_khau_tk

# ========== LOGIN ==========

def login():
    so_lan_thu = 0

    print("DANG NHAP!")

    while so_lan_thu < 3:
        nick_name = input("Enter your nick name: ")
        mat_khau = input("Enter your password: ")

        if nick_name in DSTaiKhoan and DSTaiKhoan[nick_name] == mat_khau:
            print(f"Dang nhap thanh cong! ten tai khoan cua ban la: {nick_name} ")
            return True

        else:
            so_lan_thu += 1
            if so_lan_thu != 3:
                print(f"Sai thong tin dang nhap! so lan thu con: {3 - so_lan_thu}")

    print("Dang nhap that bai!")
    return False
