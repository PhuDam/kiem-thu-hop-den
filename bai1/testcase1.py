import unittest
from main import tinh_chu_vi_hcn

class TestChuViHCN(unittest.TestCase):
    # --- ISSUE 1: DỮ LIỆU HỢP LỆ ---
    def test_tc1_1_du_lieu_dung_so_nguyen(self):
        self.assertEqual(tinh_chu_vi_hcn(5, 3), 16)

    def test_tc1_2_du_lieu_dung_so_thap_phan(self):
        self.assertEqual(tinh_chu_vi_hcn(2.5, 4.5), 14.0)

    # --- ISSUE 2: DỮ LIỆU KHÔNG HỢP LỆ, BIÊN ---
    def test_tc1_3_gia_tri_bien_bang_0(self):
        self.assertEqual(tinh_chu_vi_hcn(0, 5), "Lỗi: Kích thước phải lớn hơn 0")

    def test_tc1_4_gia_tri_am(self):
        self.assertEqual(tinh_chu_vi_hcn(-2, 3), "Lỗi: Kích thước phải lớn hơn 0")

    def test_tc1_5_sai_kieu_du_lieu(self):
        self.assertEqual(tinh_chu_vi_hcn("năm", 3), "Lỗi: Đầu vào phải là số")

if __name__ == '__main__':
    unittest.main()