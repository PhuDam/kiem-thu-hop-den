import math

def kiem_tra_nguyen_to(n):
    # Kiểm tra kiểu dữ liệu (phải là số nguyên và không phải boolean)
    if not isinstance(n, int) or isinstance(n, bool):
        return "Lỗi: Đầu vào phải là số nguyên"
    
    # Các số nhỏ hơn hoặc bằng 1 không phải là số nguyên tố
    if n <= 1:
        return False
    
    # Kiểm tra từ 2 đến căn bậc 2 của n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False # Phát hiện có ước khác 1 và chính nó
            
    return True