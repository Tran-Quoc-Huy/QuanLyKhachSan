# ==========================================================
#              CLASS THIẾT BỊ
# ==========================================================

class ThietBi:
    def __init__(self, ma_thiet_bi, ten_thiet_bi, loai_thiet_bi,
                 phong_quan_ly, tinh_trang, ngay_mua, gia_mua, ghi_chu):

        self.ma_thiet_bi = ma_thiet_bi
        self.ten_thiet_bi = ten_thiet_bi
        self.loai_thiet_bi = loai_thiet_bi
        self.phong_quan_ly = phong_quan_ly
        self.tinh_trang = tinh_trang
        self.ngay_mua = ngay_mua
        self.gia_mua = gia_mua
        self.ghi_chu = ghi_chu

    def __str__(self):
        return (
            f"Mã thiết bị: {self.ma_thiet_bi}\n"
            f"Tên thiết bị: {self.ten_thiet_bi}\n"
            f"Loại thiết bị: {self.loai_thiet_bi}\n"
            f"Phòng quản lý: {self.phong_quan_ly}\n"
            f"Tình trạng: {self.tinh_trang}\n"
            f"Ngày mua: {self.ngay_mua}\n"
            f"Giá mua: {self.gia_mua:,.0f} VNĐ\n"
            f"Ghi chú: {self.ghi_chu}"
        )


# ==========================================================
#              CLASS QUẢN LÝ THIẾT BỊ
# ==========================================================

class QuanLyThietBi:

    def __init__(self):
        self.ds_thiet_bi = {}

        # Danh sách kho/phòng hiện có
        self.ds_phong = [
            "Kho",
            "Phòng 101",
            "Phòng 102",
            "Phòng 103",
            "Phòng 104",
            "Phòng 105",
            "Phòng 106",
            "Phòng 107",
            "Phòng 108",
            "Phòng 109"
        ]

    # ======================================================
    # CHỌN PHÒNG QUẢN LÝ
    # ======================================================

    def chonPhongQuanLy(self, phong_hien_tai=None):
        print("\n===== CHỌN PHÒNG QUẢN LÝ =====")

        for i, phong in enumerate(self.ds_phong, 1):
            print(f"{i}. {phong}")

        if phong_hien_tai is not None:
            print("0. Giữ nguyên phòng hiện tại")

        while True:
            chon = input("Chọn kho/phòng: ").strip()

            if phong_hien_tai is not None and chon == "0":
                return phong_hien_tai

            if chon.isdigit() and 1 <= int(chon) <= len(self.ds_phong):
                return self.ds_phong[int(chon) - 1]

            print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")

    # ======================================================
    # KIỂM TRA MÃ THIẾT BỊ
    # ======================================================

    def kiemTraMa(self, ma):
        return ma in self.ds_thiet_bi

    # ======================================================
    # NHẬP TÌNH TRẠNG
    # ======================================================

    def nhapTinhTrang(self):
        print("\n===== CHỌN TÌNH TRẠNG =====")
        print("1. Tốt")
        print("2. Hỏng")
        print("3. Đang sửa")
        print("4. Thanh lý")

        chon = input("Chọn tình trạng: ").strip()

        if chon == "1":
            return "Tốt"
        elif chon == "2":
            return "Hỏng"
        elif chon == "3":
            return "Đang sửa"
        elif chon == "4":
            return "Thanh lý"
        else:
            print("Lựa chọn không hợp lệ!")
            return self.nhapTinhTrang()

    # ======================================================
    # NHẬP GIÁ
    # ======================================================

    def nhapGia(self):
        while True:
            try:
                gia = int(input("Nhập giá mua: "))
                if gia >= 0:
                    return gia
                else:
                    print("Giá phải lớn hơn hoặc bằng 0!")
            except ValueError:
                print("Vui lòng nhập giá tiền bằng số!")
    # ======================================================
    # THÊM THIẾT BỊ
    # ======================================================

    def them(self):

        print("\n========== THÊM THIẾT BỊ ==========")

        # Chọn phòng quản lý trước khi nhập thiết bị
        phong_quan_ly = self.chonPhongQuanLy()

        ma = input("Nhập mã thiết bị: ").strip()
        while not ma.isdigit():
            print("Mã thiết bị chỉ được nhập số!")
            ma = input("Nhập lại mã thiết bị: ").strip()

        while ma == "":
            print("Mã thiết bị không được để trống!")
            ma = input("Nhập lại mã thiết bị: ").strip()

        if ma in self.ds_thiet_bi:
            print("Mã thiết bị đã tồn tại!")
            return

        ten = input("Nhập tên thiết bị: ").strip()
        while not ten or any(char.isdigit() for char in ten):
            print("Tên thiết bị không được để trống hoặc chứa số!")
            ten = input("Nhập lại tên thiết bị: ").strip()

        while ten == "":
            print("Tên thiết bị không được để trống!")
            ten = input("Nhập lại tên thiết bị: ").strip()

        loai = input("Nhập loại thiết bị: ").strip()
        while not loai or any(char.isdigit() for char in loai):
            print("Loại thiết bị không được để trống hoặc chứa số!")
            loai = input("Nhập lại loại thiết bị: ").strip()

        while loai == "":
            print("Loại thiết bị không được để trống!")
            loai = input("Nhập lại loại thiết bị: ").strip()

        tinh_trang = self.nhapTinhTrang()

        ngay_mua = input("Nhập ngày mua (dd/mm/yyyy): ").strip()

        while ngay_mua == "":
            print("Ngày mua không được để trống!")
            ngay_mua = input("Nhập lại ngày mua: ").strip()

        gia_mua = self.nhapGia()

        ghi_chu = input("Nhập ghi chú: ").strip()

        tb = ThietBi(
            ma,
            ten,
            loai,
            phong_quan_ly,
            tinh_trang,
            ngay_mua,
            gia_mua,
            ghi_chu
        )

        self.ds_thiet_bi[ma] = tb

        print("\nThêm thiết bị thành công!")

    # ======================================================
    # IN MỘT THIẾT BỊ
    # ======================================================

    def inThietBi(self, tb):
        print("\n----------------------------------------")
        print(tb)
        print("----------------------------------------")

    # ======================================================
    # IN DANH SÁCH THIẾT BỊ
    # ======================================================

    def inDanhSach(self):

        if not self.ds_thiet_bi:
            print("\nDanh sách thiết bị đang rỗng!")
            return

        print("\n========== DANH SÁCH THIẾT BỊ ==========")

        for tb in self.ds_thiet_bi.values():
            self.inThietBi(tb)

        tong = sum(len(tb.ma_thiet_bi.split(",")) for tb in self.ds_thiet_bi.values())
        print(f"\nTổng số thiết bị: {tong}")
    # ======================================================
    # TÌM THEO MÃ
    # ======================================================

    def timTheoMa(self):

        if not self.ds_thiet_bi:
            print("\nDanh sách thiết bị đang rỗng!")
            return

        ma = input("Nhập mã thiết bị cần tìm: ").strip()

        if ma in self.ds_thiet_bi:
            print("\nTìm thấy thiết bị:")
            self.inThietBi(self.ds_thiet_bi[ma])
        else:
            print("Không tìm thấy thiết bị!")

    # ======================================================
    # TÌM THEO TÊN
    # ======================================================

    def timTheoTen(self):

        if not self.ds_thiet_bi:
            print("\nDanh sách thiết bị đang rỗng!")
            return

        ten = input("Nhập tên thiết bị cần tìm: ").strip().lower()

        tim_thay = False

        for tb in self.ds_thiet_bi.values():

            if ten in tb.ten_thiet_bi.lower():
                self.inThietBi(tb)
                tim_thay = True

        if not tim_thay:
            print("Không tìm thấy thiết bị!")

    # ======================================================
    # TÌM THEO PHÒNG
    # ======================================================

    def timTheoPhong(self):

        if not self.ds_thiet_bi:
            print("\nDanh sách thiết bị đang rỗng!")
            return

        phong = input("Nhập phòng cần tìm: ").strip().lower()

        danh_sach = []

        for tb in self.ds_thiet_bi.values():

            if tb.phong_quan_ly.lower() == phong:
                danh_sach.append(tb)

        if not danh_sach:
            print("Phòng này không có thiết bị!")
            return

        print(f"\n===== THIẾT BỊ TRONG PHÒNG {phong.upper()} =====")

        for tb in danh_sach:
            self.inThietBi(tb)

        print(f"\nPhòng quản lý {phong.upper()} có {len(danh_sach)} thiết bị.")

    # ======================================================
    # TÌM THEO LOẠI
    # ======================================================

    def timTheoLoai(self):

        if not self.ds_thiet_bi:
            print("\nDanh sách thiết bị đang rỗng!")
            return

        loai = input("Nhập loại thiết bị cần tìm: ").strip().lower()

        tim_thay = False

        for tb in self.ds_thiet_bi.values():

            if loai in tb.loai_thiet_bi.lower():
                self.inThietBi(tb)
                tim_thay = True

        if not tim_thay:
            print("Không tìm thấy thiết bị!")

    # ======================================================
    # TÌM THEO TÌNH TRẠNG
    # ======================================================

    def timTheoTinhTrang(self):

        if not self.ds_thiet_bi:
            print("\nDanh sách thiết bị đang rỗng!")
            return

        print("\n===== TÌM THEO TÌNH TRẠNG =====")
        print("1. Tốt")
        print("2. Hỏng")
        print("3. Đang sửa")
        print("4. Thanh lý")

        chon = input("Chọn: ").strip()

        if chon == "1":
            tinh_trang = "Tốt"
        elif chon == "2":
            tinh_trang = "Hỏng"
        elif chon == "3":
            tinh_trang = "Đang sửa"
        elif chon == "4":
            tinh_trang = "Thanh lý"
        else:
            print("Lựa chọn không hợp lệ!")
            return

        tim_thay = False

        for tb in self.ds_thiet_bi.values():

            if tb.tinh_trang == tinh_trang:
                self.inThietBi(tb)
                tim_thay = True

        if not tim_thay:
            print("Không có thiết bị thuộc tình trạng này!")

    # ======================================================
    # SỬA THIẾT BỊ
    # ======================================================

    def sua(self):

        if not self.ds_thiet_bi:
            print("\nDanh sách thiết bị đang rỗng!")
            return

        ma = input("Nhập mã thiết bị cần sửa: ").strip()

        if ma not in self.ds_thiet_bi:
            print("Không tìm thấy thiết bị!")
            return

        tb = self.ds_thiet_bi[ma]

        print("\n===== THÔNG TIN HIỆN TẠI =====")
        self.inThietBi(tb)

        print("\n===== NHẬP THÔNG TIN MỚI =====")

        ten = input(f"Tên mới [{tb.ten_thiet_bi}]: ").strip()

        if ten != "":
            tb.ten_thiet_bi = ten

        loai = input(f"Loại mới [{tb.loai_thiet_bi}]: ").strip()

        if loai != "":
            tb.loai_thiet_bi = loai

        # Chọn lại phòng quản lý nếu muốn thay đổi
        tb.phong_quan_ly = self.chonPhongQuanLy(tb.phong_quan_ly)

        print("\nTình trạng mới:")
        print("1. Giữ nguyên")
        print("2. Tốt")
        print("3. Hỏng")
        print("4. Đang sửa")
        print("5. Thanh lý")

        chon = input("Chọn: ").strip()

        if chon == "2":
            tb.tinh_trang = "Tốt"
        elif chon == "3":
            tb.tinh_trang = "Hỏng"
        elif chon == "4":
            tb.tinh_trang = "Đang sửa"
        elif chon == "5":
            tb.tinh_trang = "Thanh lý"

        ngay_mua = input(f"Ngày mua mới [{tb.ngay_mua}]: ").strip()

        if ngay_mua != "":
            tb.ngay_mua = ngay_mua

        gia = input("Giá mua mới (bỏ trống nếu giữ nguyên): ").strip()

        if gia != "":
            if gia.isdigit():
                tb.gia_mua = int(gia)
            else:
                print("Giá không hợp lệ, giữ nguyên giá cũ!")

        ghi_chu = input("Ghi chú mới (bỏ trống nếu giữ nguyên): ").strip()

        if ghi_chu != "":
            tb.ghi_chu = ghi_chu

        print("\nCập nhật thiết bị thành công!")

    # ======================================================
    # XÓA THIẾT BỊ
    # ======================================================

    def xoa(self):

        if not self.ds_thiet_bi:
            print("\nDanh sách thiết bị đang rỗng!")
            return

        ma = input("Nhập mã thiết bị cần xóa: ").strip()

        if ma not in self.ds_thiet_bi:
            print("Không tìm thấy thiết bị!")
            return

        tb = self.ds_thiet_bi[ma]

        print("\nThiết bị cần xóa:")
        self.inThietBi(tb)

        xac_nhan = input("Bạn có chắc muốn xóa? (Y/N): ").strip().upper()

        if xac_nhan == "Y":
            del self.ds_thiet_bi[ma]
            print("Xóa thiết bị thành công!")
        else:
            print("Đã hủy xóa.")

    # ======================================================
    # CHUYỂN THIẾT BỊ SANG PHÒNG KHÁC
    # ======================================================

    def chuyenPhong(self):

        if not self.ds_thiet_bi:
            print("\nDanh sách thiết bị đang rỗng!")
            return

        ma = input("Nhập mã thiết bị cần chuyển phòng: ").strip()

        if ma not in self.ds_thiet_bi:
            print("Không tìm thấy thiết bị!")
            return

        tb = self.ds_thiet_bi[ma]

        print(f"\nThiết bị hiện đang thuộc phòng quản lý: {tb.phong_quan_ly}")

        phong_moi = self.chonPhongQuanLy(tb.phong_quan_ly)
        tb.phong_quan_ly = phong_moi

        print("Chuyển thiết bị sang phòng mới thành công!")

    # ======================================================
    # CẬP NHẬT TÌNH TRẠNG
    # ======================================================

    def capNhatTinhTrang(self):

        if not self.ds_thiet_bi:
            print("\nDanh sách thiết bị đang rỗng!")
            return

        ma = input("Nhập mã thiết bị: ").strip()

        if ma not in self.ds_thiet_bi:
            print("Không tìm thấy thiết bị!")
            return

        tb = self.ds_thiet_bi[ma]

        print(f"\nThiết bị: {tb.ten_thiet_bi}")
        print(f"Tình trạng hiện tại: {tb.tinh_trang}")

        tb.tinh_trang = self.nhapTinhTrang()

        print("Cập nhật tình trạng thành công!")

    # ======================================================
    # ĐẾM THIẾT BỊ TRONG PHÒNG
    # ======================================================

    def demTheoPhong(self):

        if not self.ds_thiet_bi:
            print("\nDanh sách thiết bị đang rỗng!")
            return

        thong_ke = {}

        for tb in self.ds_thiet_bi.values():

            if tb.phong_quan_ly not in thong_ke:
                thong_ke[tb.phong_quan_ly] = 0

            thong_ke[tb.phong_quan_ly] += 1

        print("\n===== SỐ LƯỢNG THIẾT BỊ THEO PHÒNG =====")

        for phong, so_luong in thong_ke.items():
            print(f"{phong}: {so_luong} thiết bị")

    # ======================================================
    # THỐNG KÊ THEO LOẠI
    # ======================================================

    def thongKeTheoLoai(self):

        if not self.ds_thiet_bi:
            print("\nDanh sách thiết bị đang rỗng!")
            return

        thong_ke = {}

        for tb in self.ds_thiet_bi.values():

            if tb.loai_thiet_bi not in thong_ke:
                thong_ke[tb.loai_thiet_bi] = 0

            thong_ke[tb.loai_thiet_bi] += 1

        print("\n===== THỐNG KÊ THEO LOẠI =====")

        for loai, so_luong in thong_ke.items():
            print(f"{loai}: {so_luong} thiết bị")

    # ======================================================
    # THỐNG KÊ THEO TÌNH TRẠNG
    # ======================================================

    def thongKeTheoTinhTrang(self):

        if not self.ds_thiet_bi:
            print("\nDanh sách thiết bị đang rỗng!")
            return

        thong_ke = {
            "Tốt": 0,
            "Hỏng": 0,
            "Đang sửa": 0,
            "Thanh lý": 0
        }

        for tb in self.ds_thiet_bi.values():

            if tb.tinh_trang in thong_ke:
                thong_ke[tb.tinh_trang] += 1

        print("\n===== THỐNG KÊ THEO TÌNH TRẠNG =====")

        for tinh_trang, so_luong in thong_ke.items():
            print(f"{tinh_trang}: {so_luong} thiết bị")

    # ======================================================
    # THỐNG KÊ TỔNG QUÁT
    # ======================================================

    def thongKe(self):

        if not self.ds_thiet_bi:
            print("\nDanh sách thiết bị đang rỗng!")
            return

        tong = len(self.ds_thiet_bi)

        tot = 0
        hong = 0
        dang_sua = 0
        thanh_ly = 0

        for tb in self.ds_thiet_bi.values():

            if tb.tinh_trang == "Tốt":
                tot += 1
            elif tb.tinh_trang == "Hỏng":
                hong += 1
            elif tb.tinh_trang == "Đang sửa":
                dang_sua += 1
            elif tb.tinh_trang == "Thanh lý":
                thanh_ly += 1

        print("\n======================================")
        print("       THỐNG KÊ THIẾT BỊ")
        print("======================================")

        print(f"Tổng số thiết bị: {tong}")
        print(f"Thiết bị tốt: {tot}")
        print(f"Thiết bị hỏng: {hong}")
        print(f"Thiết bị đang sửa: {dang_sua}")
        print(f"Thiết bị thanh lý: {thanh_ly}")

    # ======================================================
    # MENU TÌM KIẾM
    # ======================================================

    def menuTimKiem(self):

        chon = ""

        while chon != "0":

            print("\n======================================")
            print("          TÌM KIẾM THIẾT BỊ")
            print("======================================")
            print("1. Tìm theo mã")
            print("2. Tìm theo tên")
            print("3. Tìm theo phòng")
            print("4. Tìm theo loại")
            print("5. Tìm theo tình trạng")
            print("0. Quay lại")

            chon = input("Chọn chức năng: ").strip()

            if chon == "1":
                self.timTheoMa()

            elif chon == "2":
                self.timTheoTen()

            elif chon == "3":
                self.timTheoPhong()

            elif chon == "4":
                self.timTheoLoai()

            elif chon == "5":
                self.timTheoTinhTrang()

            elif chon == "0":
                print("Quay lại menu chính.")

            else:
                print("Lựa chọn không hợp lệ!")

    # ======================================================
    # MENU THỐNG KÊ
    # ======================================================

    def menuThongKe(self):

        chon = ""

        while chon != "0":

            print("\n======================================")
            print("          THỐNG KÊ THIẾT BỊ")
            print("======================================")
            print("1. Thống kê tổng quát")
            print("2. Thống kê theo phòng")
            print("3. Thống kê theo loại")
            print("4. Thống kê theo tình trạng")
            print("0. Quay lại")

            chon = input("Chọn chức năng: ").strip()

            if chon == "1":
                self.thongKe()

            elif chon == "2":
                self.demTheoPhong()

            elif chon == "3":
                self.thongKeTheoLoai()

            elif chon == "4":
                self.thongKeTheoTinhTrang()

            elif chon == "0":
                print("Quay lại menu chính.")

            else:
                print("Lựa chọn không hợp lệ!")

    # ======================================================
    # MENU CHÍNH
    # ======================================================

    def menu(self):

        chon = ""

        while chon != "0":

            print("\n")
            print("==============================================")
            print("       PHẦN MỀM QUẢN LÝ THIẾT BỊ")
            print("              KHÁCH SẠN")
            print("==============================================")
            print("1. Thêm thiết bị")
            print("2. Hiển thị danh sách thiết bị")
            print("3. Tìm kiếm thiết bị")
            print("4. Sửa thông tin thiết bị")
            print("5. Xóa thiết bị")
            print("6. Chuyển thiết bị sang phòng")
            print("7. Cập nhật tình trạng thiết bị")
            print("8. Thống kê thiết bị")
            print("0. Thoát chương trình")
            print("==============================================")

            chon = input("Nhập lựa chọn: ").strip()

            if chon == "1":
                self.them()

            elif chon == "2":
                self.inDanhSach()

            elif chon == "3":
                self.menuTimKiem()

            elif chon == "4":
                self.sua()

            elif chon == "5":
                self.xoa()

            elif chon == "6":
                self.chuyenPhong()

            elif chon == "7":
                self.capNhatTinhTrang()

            elif chon == "8":
                self.menuThongKe()

            elif chon == "0":
                print("\nĐã thoát chương trình.")

            else:
                print("\nLựa chọn không hợp lệ! Vui lòng chọn lại.")


# ==========================================================
#              CHẠY CHƯƠNG TRÌNH
# ==========================================================

ql = QuanLyThietBi()
ql.menu()