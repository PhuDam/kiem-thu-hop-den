def tim_ucln(a, b):
    # Kiểm tra kiểu dữ liệu (phải là số nguyên)
    if not isinstance(a, int) or not isinstance(b, int) or isinstance(a, bool) or isinstance(b, bool):
        return "Lỗi: a và b phải là số nguyên"
    
    # Kiểm tra ngoại lệ: cả hai số cùng bằng 0
    if a == 0 and b == 0:
        return "Lỗi: a và b không thể cùng bằng 0"
    
    # Lấy giá trị tuyệt đối để xử lý cả số âm
    a = abs(a)
    b = abs(b)
    
    # Thuật toán Euclid
    while b > 0:
        a, b = b, a % b
        
    return a