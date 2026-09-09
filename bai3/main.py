import math

def giai_pt_bac_2(a, b, c):
    # Kiểm tra kiểu dữ liệu
    if not all(isinstance(i, (int, float)) for i in [a, b, c]):
        return "Lỗi: Đầu vào phải là số"
    
    # Trường hợp a = 0 (Trở thành phương trình bậc 1: bx + c = 0)
    if a == 0:
        if b == 0:
            return "Vô số nghiệm" if c == 0 else "Vô nghiệm"
        return round(-c / b, 2)
    
    # Trường hợp a != 0, tính Delta
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Vô nghiệm"
    elif delta == 0:
        return round(-b / (2*a), 2)
    else:
        # Trả về tuple 2 nghiệm phân biệt
        x1 = round((-b + math.sqrt(delta)) / (2*a), 2)
        x2 = round((-b - math.sqrt(delta)) / (2*a), 2)
        return (x1, x2)