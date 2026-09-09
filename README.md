# Báo cáo Thực hành: Kiểm thử Hộp đen

## 1. Mô tả phương pháp áp dụng
Trong bài thực hành này, em đã áp dụng các kỹ thuật kiểm thử hộp đen bao gồm:
*   **Phân lớp tương đương (Equivalence Partitioning):** Chia tập dữ liệu đầu vào thành các lớp hợp lệ và không hợp lệ. Ví dụ: Với bài toán tính số ngày của tháng, em chia tháng thành lớp hợp lệ (1-12) và lớp không hợp lệ (<1 hoặc >12).
*   **Phân tích giá trị biên (Boundary Value Analysis):** Tập trung kiểm tra tại các điểm ranh giới của các lớp tương đương, vì đây là nơi dễ xảy ra lỗi nhất. Ví dụ: Kiểm tra tại n = 0, n = 1 cho các bài toán yêu cầu số nguyên dương n >= 1.
*   **Kiểm thử ngoại lệ:** Xử lý các trường hợp người dùng nhập sai kiểu dữ liệu (nhập chữ thay vì số, nhập số thập phân thay vì số nguyên).

## 2. Kết quả chạy kiểm thử
Toàn bộ 8 bài toán đã được viết kịch bản kiểm thử tự động (Unit Test) bằng thư viện `unittest` của Python.
*   **Tổng số test case:** > 50 test cases bao phủ dữ liệu hợp lệ, không hợp lệ, biên và ngoại lệ.
*   **Kết quả:** 100% PASS (OK). Mã nguồn xử lý tốt mọi tình huống đầu vào.

## 3. Danh sách Test Case (Tóm tắt)
Dưới đây là cấu trúc test case chung được áp dụng cho các bài:
*   **Issue #1 (Dữ liệu hợp lệ):**
    *   Các giá trị nằm trong khoảng tính toán đúng.
    *   Các trường hợp đặc biệt nhưng hợp lệ (VD: Năm nhuận, số nguyên tố chẵn nhỏ nhất...).
*   **Issue #2 (Dữ liệu không hợp lệ, biên và ngoại lệ):**
    *   Nhập số âm, số 0 (khi yêu cầu > 0).
    *   Nhập sai kiểu dữ liệu (String, Float thay vì Integer, Boolean...).
    *   Các trường hợp vô lý (VD: Tháng 13, chia cho 0).

