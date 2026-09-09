def tinh_tong_dan_dau(n):
    # Kiểm tra kiểu dữ liệu (bắt buộc là số nguyên)
    if not isinstance(n, int) or isinstance(n, bool):
        return "Lỗi: n phải là số nguyên"
    
    # Kiểm tra giá trị biên
    if n < 1:
        return "Lỗi: n phải lớn hơn hoặc bằng 1"
    
    # Tính tổng đan dấu
    tong = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            tong -= i
        else:
            tong += i
            
    return tong