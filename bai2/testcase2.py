import unittest
from main import tinh_dien_tich_hcn

class TestDienTichHCN(unittest.TestCase):
    # --- DỮ LIỆU HỢP LỆ ---
    def test_tc2_1_du_lieu_dung_so_nguyen(self):
        self.assertEqual(tinh_dien_tich_hcn(5, 3), 15)

    def test_tc2_2_du_lieu_dung_so_thap_phan(self):
        self.assertEqual(tinh_dien_tich_hcn(2.5, 4.0), 10.0)

    # --- DỮ LIỆU KHÔNG HỢP LỆ, BIÊN ---
    def test_tc2_3_gia_tri_bien_bang_0(self):
        self.assertEqual(tinh_dien_tich_hcn(0, 5), "Lỗi: Kích thước phải lớn hơn 0")

    def test_tc2_4_gia_tri_am(self):
        self.assertEqual(tinh_dien_tich_hcn(-2, 3), "Lỗi: Kích thước phải lớn hơn 0")

    def test_tc2_5_sai_kieu_du_lieu(self):
        self.assertEqual(tinh_dien_tich_hcn("năm", 3), "Lỗi: Đầu vào phải là số")

if __name__ == '__main__':
    unittest.main()