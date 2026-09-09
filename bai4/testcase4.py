import unittest
from main import tinh_so_ngay

class TestTinhSoNgay(unittest.TestCase):
    # --- DỮ LIỆU HỢP LỆ ---
    def test_tc4_1_thang_31_ngay(self):
        self.assertEqual(tinh_so_ngay(1, 2023), 31)

    def test_tc4_2_thang_30_ngay(self):
        self.assertEqual(tinh_so_ngay(4, 2023), 30)
        
    def test_tc4_3_thang_2_nam_khong_nhuan(self):
        self.assertEqual(tinh_so_ngay(2, 2023), 28)
        
    def test_tc4_4_thang_2_nam_nhuan(self):
        self.assertEqual(tinh_so_ngay(2, 2024), 29)
        
    def test_tc4_5_thang_2_nam_nhuan_the_ky(self):
        # Năm 2000 là năm nhuận vì chia hết cho 400
        self.assertEqual(tinh_so_ngay(2, 2000), 29)

    # --- DỮ LIỆU BIÊN VÀ NGOẠI LỆ ---
    def test_tc4_6_thang_nho_hon_1_khong_hop_le(self):
        self.assertEqual(tinh_so_ngay(0, 2023), "Lỗi: Tháng không hợp lệ")

    def test_tc4_7_thang_lon_hon_12_khong_hop_le(self):
        self.assertEqual(tinh_so_ngay(13, 2023), "Lỗi: Tháng không hợp lệ")
        
    def test_tc4_8_nam_khong_hop_le(self):
        self.assertEqual(tinh_so_ngay(5, 0), "Lỗi: Năm phải lớn hơn 0")

    def test_tc4_9_sai_kieu_du_lieu(self):
        self.assertEqual(tinh_so_ngay("hai", 2023), "Lỗi: Tháng và năm phải là số nguyên")

if __name__ == '__main__':
    unittest.main()