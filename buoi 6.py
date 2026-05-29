import json


# 1. Hàm nén file
def compress_file(input_path, compressed_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Tách văn bản thành danh sách các từ và ký tự xuống dòng
    # Để đơn giản, ta tách theo khoảng trắng nhưng giữ lại cấu trúc
    words = content.split()

    # Tạo danh sách từ duy nhất (từ điển)
    vocabulary = []
    word_to_index = {}
    for word in words:
        if word not in word_to_index:
            word_to_index[word] = len(vocabulary)
            vocabulary.append(word)

    # Chuyển văn bản thành dãy các chỉ số
    encoded_content = [word_to_index[word] for word in words]

    # Lưu từ điển và nội dung đã mã hóa vào file mới (dạng JSON để tối ưu cấu trúc)
    data = {
        "vocab": vocabulary,
        "data": encoded_content
    }

    with open(compressed_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
    print(f"Đã nén xong: {compressed_path}")


# 2. Hàm giải nén file
def decompress_file(compressed_path, output_path):
    with open(compressed_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    vocabulary = data["vocab"]
    encoded_content = data["data"]

    # Khôi phục lại các từ từ chỉ số
    decoded_words = [vocabulary[index] for index in encoded_content]

    # Ghép lại thành văn bản (Lưu ý: Cách này sẽ làm mất format xuống dòng chính xác
    # nếu không xử lý ký tự \n đặc biệt, nhưng đáp ứng đúng logic gợi ý)
    full_text = " ".join(decoded_words)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_text)
    print(f"Đã giải nén xong: {output_path}")

# --- Thực thi ---
# Giả sử bạn đã có file fileName.txt với nội dung bài thơ
# compress_file('fileName.txt', 'compressed.json')
# decompress_file('compressed.json', 'restored.txt')
