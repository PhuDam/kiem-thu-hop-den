import unittest
from main import kiem_tra_nguyen_to

class TestKiemTraNguyenTo(unittest.TestCase):
    # --- DỮ LIỆU HỢP LỆ (Các số hợp lệ > 1) ---
    def test_tc5_1_la_so_nguyen_to(self):
        # 17 là số nguyên tố
        self.assertTrue(kiem_tra_nguyen_to(17))

    def test_tc5_2_so_nguyen_to_nho_nhat(self):
        # 2 là số nguyên tố chẵn duy nhất
        self.assertTrue(kiem_tra_nguyen_to(2))

    def test_tc5_3_khong_la_so_nguyen_to(self):
        # 15 chia hết cho 3 và 5
        self.assertFalse(kiem_tra_nguyen_to(15))

    # --- DỮ LIỆU BIÊN VÀ NGOẠI LỆ ---
    def test_tc5_4_gia_tri_bien_bang_1(self):
        self.assertFalse(kiem_tra_nguyen_to(1))

    def test_tc5_5_gia_tri_bien_bang_0(self):
        self.assertFalse(kiem_tra_nguyen_to(0))

    def test_tc5_6_gia_tri_am(self):
        self.assertFalse(kiem_tra_nguyen_to(-5))

    def test_tc5_7_sai_kieu_du_lieu_chu(self):
        self.assertEqual(kiem_tra_nguyen_to("năm"), "Lỗi: Đầu vào phải là số nguyên")
        
    def test_tc5_8_sai_kieu_du_lieu_so_thap_phan(self):
        self.assertEqual(kiem_tra_nguyen_to(5.5), "Lỗi: Đầu vào phải là số nguyên")

if __name__ == '__main__':
    unittest.main()