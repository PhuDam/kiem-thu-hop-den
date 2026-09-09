def tinh_dien_tich_hcn(a, b):
    # Kiểm tra kiểu dữ liệu
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Lỗi: Đầu vào phải là số"
    
    # Kiểm tra giá trị biên và không hợp lệ
    if a <= 0 or b <= 0:
        return "Lỗi: Kích thước phải lớn hơn 0"
    
    # Tính diện tích nếu dữ liệu hợp lệ
    return a * b