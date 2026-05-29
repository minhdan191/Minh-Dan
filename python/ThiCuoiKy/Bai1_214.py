"""
Bài 1: Tính diện tích đáy và thể tích hình khối chữ nhật.
Mã đề: 214
"""

def main():
    # Nhập dữ liệu đầu vào từ bàn phím
    dai = float(input("Nhập chiều dài đáy hình khối chữ nhật (cm): "))
    rong = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm): "))
    cao = float(input("Nhập chiều cao hình khối chữ nhật (cm): "))
    so_le = int(input("Số lượng số lẻ cần hiển thị: "))

    # Tính toán diện tích đáy và thể tích
    dien_tich_day = dai * rong
    the_tich = dien_tich_day * cao

    # Cấu hình định dạng chuỗi hiển thị số thập phân theo yêu cầu (so_le)
    format_str = f"{{:.{so_le}f}}"

    # Định dạng kết quả ra chuỗi
    dt_formatted = format_str.format(dien_tich_day)
    vt_formatted = format_str.format(the_tich)

    # Xuất kết quả kèm ký tự Unicode \u00b2 (²) và \u00b3 (³)
    print(f"Diện tích đáy hình chữ nhật = {dt_formatted} cm\u00b2")
    print(f"Thể tích hình khối = {vt_formatted} cm\u00b3")

if __name__ == "__main__":
    main()
