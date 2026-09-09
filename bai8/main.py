# Hàm con tính giai thừa
def tinh_giai_thua(k):
    if k == 0 or k == 1:
        return 1
    giai_thua = 1
    for i in range(2, k + 1):
        giai_thua *= i
    return giai_thua

# Hàm chính tính tổng các giai thừa
def tinh_tong_giai_thua(n):
    # Kiểm tra kiểu dữ liệu (phải là số nguyên)
    if not isinstance(n, int) or isinstance(n, bool):
        return "Lỗi: n phải là số nguyên"
    
    # Kiểm tra giá trị hợp lệ (chuỗi bắt đầu từ 1!)
    if n < 1:
        return "Lỗi: n phải lớn hơn hoặc bằng 1"
    
    tong = 0
    for i in range(1, n + 1):
        tong += tinh_giai_thua(i)
        
    return tong