import unittest
from main import tinh_tong_giai_thua

class TestTongGiaiThua(unittest.TestCase):
    # --- DỮ LIỆU HỢP LỆ ---
    def test_tc8_1_gia_tri_bien_n_bang_1(self):
        # S = 1! = 1
        self.assertEqual(tinh_tong_giai_thua(1), 1)

    def test_tc8_2_n_la_so_nguyen_duong(self):
        # S = 1! + 2! + 3! = 1 + 2 + 6 = 9
        self.assertEqual(tinh_tong_giai_thua(3), 9)
        
    def test_tc8_3_n_lon_hon(self):
        # S = 1! + 2! + 3! + 4! = 9 + 24 = 33
        self.assertEqual(tinh_tong_giai_thua(4), 33)

    # --- DỮ LIỆU BIÊN VÀ NGOẠI LỆ ---
    def test_tc8_4_gia_tri_bien_n_bang_0(self):
        self.assertEqual(tinh_tong_giai_thua(0), "Lỗi: n phải lớn hơn hoặc bằng 1")

    def test_tc8_5_gia_tri_am(self):
        self.assertEqual(tinh_tong_giai_thua(-3), "Lỗi: n phải lớn hơn hoặc bằng 1")

    def test_tc8_6_sai_kieu_du_lieu_chu(self):
        self.assertEqual(tinh_tong_giai_thua("năm"), "Lỗi: n phải là số nguyên")
        
    def test_tc8_7_sai_kieu_du_lieu_thap_phan(self):
        self.assertEqual(tinh_tong_giai_thua(4.5), "Lỗi: n phải là số nguyên")

if __name__ == '__main__':
    unittest.main()