def tinh_chu_vi_hcn(a, b):
    # Kiểm tra kiểu dữ liệu
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Lỗi: Đầu vào phải là số"
    
    # Kiểm tra giá trị biên và không hợp lệ
    if a <= 0 or b <= 0:
        return "Lỗi: Kích thước phải lớn hơn 0"
    
    # Tính chu vi nếu dữ liệu hợp lệ
    return 2 * (a + b)

# Nếu bạn vẫn muốn có phần nhập từ bàn phím để test thủ công,
# hãy đặt nó vào khối __main__ này để nó không bị chạy khi unit test gọi tới:
if __name__ == '__main__':
    chieudai = float(input("Nhập chiều dài: "))
    chieurong = float(input("Nhập chiều rộng: "))
    print(f"Chu vi hình chữ nhật: {tinh_chu_vi_hcn(chieudai, chieurong)}")