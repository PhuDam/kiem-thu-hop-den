import unittest
from main import giai_pt_bac_2

class TestGiaiPTBac2(unittest.TestCase):
    # --- DỮ LIỆU HỢP LỆ ---
    def test_tc3_1_delta_lon_hon_0(self):
        # pt: x^2 - 3x + 2 = 0 -> Nghiệm là 2 và 1
        self.assertEqual(giai_pt_bac_2(1, -3, 2), (2.0, 1.0))

    def test_tc3_2_delta_bang_0_nghiem_kep(self):
        # pt: x^2 - 2x + 1 = 0 -> Nghiệm kép là 1.0
        self.assertEqual(giai_pt_bac_2(1, -2, 1), 1.0)
        
    def test_tc3_3_delta_nho_hon_0_vo_nghiem(self):
        # pt: x^2 + x + 1 = 0 -> Vô nghiệm
        self.assertEqual(giai_pt_bac_2(1, 1, 1), "Vô nghiệm")

    # --- DỮ LIỆU BIÊN VÀ NGOẠI LỆ ---
    def test_tc3_4_he_so_a_bang_0_co_nghiem(self):
        # a=0, pt: 2x - 4 = 0 -> Nghiệm là 2.0
        self.assertEqual(giai_pt_bac_2(0, 2, -4), 2.0)

    def test_tc3_5_he_so_a_va_b_bang_0(self):
        # 0x = 5 -> Vô nghiệm
        self.assertEqual(giai_pt_bac_2(0, 0, 5), "Vô nghiệm")
        
    def test_tc3_6_tat_ca_he_so_bang_0(self):
        # 0 = 0 -> Vô số nghiệm
        self.assertEqual(giai_pt_bac_2(0, 0, 0), "Vô số nghiệm")

    def test_tc3_7_sai_kieu_du_lieu(self):
        self.assertEqual(giai_pt_bac_2(1, "hai", 3), "Lỗi: Đầu vào phải là số")

if __name__ == '__main__':
    unittest.main()