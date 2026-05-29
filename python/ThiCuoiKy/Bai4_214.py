"""
Bài 4: Xây dựng hàm ẩn danh (Lambda) kiểm tra Số chính phương và Số hoàn thiện.
Yêu cầu: 
- Hàm trả về kiểu boolean (True/False).
- Không gọi lại các User Defined Functions ở các câu trước.
- Lần lượt sử dụng các hàm này để in các số thỏa mãn trong khoảng từ 1 đến 10000.
Mã đề: 214
"""

def main():
    print("=" * 65)
    print("  CHƯƠNG TRÌNH LỌC SỐ BẰNG HÀM LAMBDA (KHOẢNG TỪ 1 ĐẾN 10000)")
    print("=" * 65)

    # 1. Định nghĩa hàm lambda kiểm tra số chính phương
    # Ý nghĩa: Lấy căn bậc hai của x, nếu phần thập phân bằng 0 (.is_integer()) thì là số chính phương
    is_chinh_phuong = lambda x: x >= 0 and (x ** 0.5).is_integer()

    # 2. Định nghĩa hàm lambda kiểm tra số hoàn thiện
    # Ý nghĩa: Chạy vòng lặp i từ 1 đến x-1 để tìm ước số, nếu tổng các ước số bằng chính x thì trả về True
    is_hoan_thien = lambda x: x > 1 and sum(i for i in range(1, x) if x % i == 0) == x


    # -------------------------------------------------------------------------
    # TIẾN HÀNH LỌC VÀ IN KẾT QUẢ THEO YÊU CẦU ĐỀ BÀI
    # -------------------------------------------------------------------------

    # Yêu cầu 1: Lọc và in danh sách các số chính phương từ 1 đến 10000
    danh_sach_cp = [str(num) for num in range(1, 10001) if is_chinh_phuong(num)]
    
    print(f"\n[+] Danh sách các số CHÍNH PHƯƠNG từ 1 đến 10000 (Tổng cộng: {len(danh_sach_cp)} số):")
    # Sử dụng dấu phẩy để phân tách các phần tử khi in ra cho gọn gàng
    print(", ".join(danh_sach_cp))
    
    print("\n" + "-" * 65)

    # Yêu cầu 2: Lọc và in danh sách các số hoàn thiện từ 1 đến 10000
    danh_sach_ht = [str(num) for num in range(1, 10001) if is_hoan_thien(num)]
    
    print(f"\n[+] Danh sách các số HOÀN THIỆN từ 1 đến 10000 (Tổng cộng: {len(danh_sach_ht)} số):")
    if danh_sach_ht:
        print(", ".join(danh_sach_ht))
    else:
        print("Không tìm thấy số hoàn thiện nào trong khoảng này.")
    print("\n" + "=" * 65)

if __name__ == "__main__":
    main()
