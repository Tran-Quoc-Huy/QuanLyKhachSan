# ========== CLASS THIẾT BỊ ==========

class ThietBi:
    def __init__(self, ma_thiet_bi, ten_thiet_bi, so_luong, tinh_trang):
        self.ma_thiet_bi = ma_thiet_bi
        self.ten_thiet_bi = ten_thiet_bi
        self.so_luong = so_luong
        self.tinh_trang = tinh_trang

    def __str__(self):
        return (f"Mã thiết bị: {self.ma_thiet_bi} - "
                f"Tên thiết bị: {self.ten_thiet_bi} - "
                f"Số lượng: {self.so_luong} - "
                f"Tình trạng: {self.tinh_trang}")
 # ========== CLASS QUẢN LÝ THIẾT BỊ ==========

class QuanLyThietBi:
    def __init__(self):
        self.ds_thiet_bi = {}

# ========== THÊM THIẾT BỊ ==========
    def them(self):
        ma = input("Nhập mã thiết bị: ").strip()

        while ma == "" or ma in self.ds_thiet_bi:
            if ma == "":
                ma = input("Mã không được để trống, nhập lại: ").strip()
            else:
                ma = input("Mã đã tồn tại, nhập lại: ").strip()

        ten = input("Nhập tên thiết bị: ").strip()

        while ten == "":
            ten = input("Tên thiết bị không được để trống: ").strip()

        so_luong = input("Nhập số lượng: ").strip()

        while not so_luong.isdigit() or int(so_luong) <= 0:
            if so_luong.isdigit():
                so_luong = input("Nhâp số! vui lòng nhập lại: ").strip()
            else:
                so_luong = input("Số lương phải lớn hơn 0! vui long nhap lại: ")

        tinh_trang = input("Nhập tình trạng thiết bị: ").strip()

        while tinh_trang == "":
            tinh_trang = input("Tình trạng không được để trống: ").strip()

        tb = ThietBi(ma, ten, int(so_luong), tinh_trang)
        self.ds_thiet_bi[ma] = tb

        print("Thêm thiết bị thành công!")

    # ========== IN DANH SÁCH ==========
    def inDanhSach(self):
        if not self.ds_thiet_bi:
            print("Danh sách thiết bị rỗng!")
            return

        for ma, tb in self.ds_thiet_bi.items():
            print(f"{tb}\n")

    # ========== TÌM THIẾT BỊ ==========
    def timTheoMa(self):
        if not self.ds_thiet_bi:
            print("Danh sách thiết bị rỗng!")
            return

        ma = input("Nhập mã thiết bị cần tìm: ").strip()

        if ma in self.ds_thiet_bi:
            print(self.ds_thiet_bi[ma])
        else:
            print("Không tìm thấy thiết bị!")

    # ========== XÓA THIẾT BỊ ==========
    def xoa(self):
        if not self.ds_thiet_bi:
            print("Danh sách thiết bị rỗng!")
            return

        ma = input("Nhập mã thiết bị cần xóa: ").strip()

        if ma in self.ds_thiet_bi:
            self.ds_thiet_bi.pop(ma)
            print("Xóa thiết bị thành công!")
        else:
            print("Không tìm thấy thiết bị!")


    # ========== SUA THIET BI ==========
    def sua(self):
        if not self.ds_thiet_bi:
            print("Danh sách thiết bị rỗng!")
            return

        ma = input("Nhập mã thiết bị cần sửa: ").strip()

        if ma not in self.ds_thiet_bi:
            print("Không tìm thấy thiết bị!")
            return

        tb = self.ds_thiet_bi[ma]

        print("Thông tin hiện tại:")
        print(tb)

        ten = input("Nhập tên thiết bị mới: ").strip()
        while ten == "":
            ten = input("Tên thiết bị không được để trống: ").strip()

        so_luong = input("Nhập số lượng mới: ").strip()
        while not so_luong.isdigit() or int(so_luong) <= 0:
            so_luong = input("Số lượng phải lớn hơn 0, nhập lại: ").strip()

        tinh_trang = input("Nhập tình trạng mới: ").strip()
        while tinh_trang == "":
            tinh_trang = input("Tình trạng không được để trống: ").strip()

        tb.ten_thiet_bi = ten
        tb.so_luong = int(so_luong)
        tb.tinh_trang = tinh_trang

        print("Cập nhật thiết bị thành công!")

    # ========== THONG KE ==========
    def thongKe(self):
        if not self.ds_thiet_bi:
            print("Danh sách thiết bị rỗng!")
            return

        tong_loai = len(self.ds_thiet_bi)
        tong_so_luong = 0

        for tb in self.ds_thiet_bi.values():
            tong_so_luong += tb.so_luong

        print("\n===== THỐNG KÊ THIẾT BỊ =====")
        print(f"Tổng số loại thiết bị: {tong_loai}")
        print(f"Tổng số lượng thiết bị: {tong_so_luong}")