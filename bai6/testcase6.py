import unittest
from main import tinh_tong_dan_dau

class TestTinhTongDanDau(unittest.TestCase):
    # --- DỮ LIỆU HỢP LỆ ---
    def test_tc6_1_n_la_so_le(self):
        # S = 1 - 2 + 3 = 2
        self.assertEqual(tinh_tong_dan_dau(3), 2)

    def test_tc6_2_n_la_so_chan(self):
        # S = 1 - 2 + 3 - 4 = -2
        self.assertEqual(tinh_tong_dan_dau(4), -2)

    def test_tc6_3_gia_tri_bien_n_bang_1(self):
        # S = 1
        self.assertEqual(tinh_tong_dan_dau(1), 1)

    # --- DỮ LIỆU BIÊN VÀ NGOẠI LỆ ---
    def test_tc6_4_gia_tri_bien_n_bang_0(self):
        self.assertEqual(tinh_tong_dan_dau(0), "Lỗi: n phải lớn hơn hoặc bằng 1")

    def test_tc6_5_gia_tri_am(self):
        self.assertEqual(tinh_tong_dan_dau(-5), "Lỗi: n phải lớn hơn hoặc bằng 1")

    def test_tc6_6_sai_kieu_du_lieu_chu(self):
        self.assertEqual(tinh_tong_dan_dau("bốn"), "Lỗi: n phải là số nguyên")
        
    def test_tc6_7_sai_kieu_du_lieu_thap_phan(self):
        self.assertEqual(tinh_tong_dan_dau(3.5), "Lỗi: n phải là số nguyên")

if __name__ == '__main__':
    unittest.main()