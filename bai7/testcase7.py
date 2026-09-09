import unittest
from main import tim_ucln

class TestTimUCLN(unittest.TestCase):
    # --- DỮ LIỆU HỢP LỆ ---
    def test_tc7_1_hai_so_nguyen_duong(self):
        # UCLN của 12 và 18 là 6
        self.assertEqual(tim_ucln(12, 18), 6)

    def test_tc7_2_hai_so_nguyen_to_cung_nhau(self):
        # UCLN của 7 và 13 là 1
        self.assertEqual(tim_ucln(7, 13), 1)

    def test_tc7_3_co_chua_so_am(self):
        # UCLN của -12 và 18 vẫn là 6
        self.assertEqual(tim_ucln(-12, 18), 6)
        
    def test_tc7_4_mot_so_bang_0(self):
        # UCLN của 0 và 5 là 5
        self.assertEqual(tim_ucln(0, 5), 5)

    # --- DỮ LIỆU BIÊN VÀ NGOẠI LỆ ---
    def test_tc7_5_ca_hai_so_bang_0(self):
        self.assertEqual(tim_ucln(0, 0), "Lỗi: a và b không thể cùng bằng 0")

    def test_tc7_6_sai_kieu_du_lieu_chu(self):
        self.assertEqual(tim_ucln("ba", 5), "Lỗi: a và b phải là số nguyên")
        
    def test_tc7_7_sai_kieu_du_lieu_thap_phan(self):
        self.assertEqual(tim_ucln(12.5, 18), "Lỗi: a và b phải là số nguyên")

if __name__ == '__main__':
    unittest.main()