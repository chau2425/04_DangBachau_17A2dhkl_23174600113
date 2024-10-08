class HinhChuNhat:
    def __init__(self, dai=0, rong=0):
        self.dai = dai
        self.rong = rong

    def nhap_du_lieu(self):
        while True:
            try:
                self.dai = float(input("Nhập chiều dài: "))
                self.rong = float(input("Nhập chiều rộng: "))
                break
            except ValueError:
                print("Vui lòng nhập số!")

    def tinh_chu_vi(self):
        return 2 * (self.dai + self.rong)

    def tinh_dien_tich(self):
        return self.dai * self.rong

    def xuat_thong_tin(self):
        print("Chiều dài:", self.dai)
        print("Chiều rộng:", self.rong)
        print("Chu vi:", self.tinh_chu_vi())
        print("Diện tích:", self.tinh_dien_tich())

# Tạo đối tượng và sử dụng
hinh_chu_nhat = HinhChuNhat()
hinh_chu_nhat.nhap_du_lieu()
hinh_chu_nhat.xuat_thong_tin()