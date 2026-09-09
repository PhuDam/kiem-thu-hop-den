def tinh_so_ngay(thang, nam):
    # Kiểm tra kiểu dữ liệu (phải là số nguyên)
    if not isinstance(thang, int) or not isinstance(nam, int):
        return "Lỗi: Tháng và năm phải là số nguyên"
    
    # Kiểm tra giá trị biên và tính hợp lệ
    if thang < 1 or thang > 12:
        return "Lỗi: Tháng không hợp lệ"
    if nam <= 0:
        return "Lỗi: Năm phải lớn hơn 0"
    
    # Tính số ngày cho các tháng 31 và 30 ngày
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    else:
        # Xử lý riêng cho tháng 2 (Kiểm tra năm nhuận)
        # Năm nhuận là năm chia hết cho 400 HOẶC (chia hết cho 4 nhưng không chia hết cho 100)
        if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
            return 29
        else:
            return 28