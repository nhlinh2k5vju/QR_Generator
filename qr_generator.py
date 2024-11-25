import qrcode
from PIL import Image

def generate_qr(data, fill_color="black", back_color="white", logo_path=None, box_size=10, output_file="qr_code.png"):
    """
    Tạo mã QR với tùy chọn màu sắc, logo, kích cỡ.
    
    :param data: Dữ liệu (URL hoặc văn bản) cần mã hóa.
    :param fill_color: Màu mã QR.
    :param back_color: Màu nền mã QR.
    :param logo_path: Đường dẫn đến file logo (nếu có).
    :param box_size: Kích cỡ ô vuông trong mã QR.
    :param output_file: Tên file đầu ra.
    """
    # Tạo đối tượng mã QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Mức độ sửa lỗi cao
        box_size=box_size,
        border=4,  # Độ dày viền
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Tạo hình ảnh mã QR với màu sắc tùy chỉnh
    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGB')

    # Thêm logo (nếu có)
    if logo_path:
        try:
            logo = Image.open(logo_path)
            # Điều chỉnh kích cỡ logo để vừa với mã QR
            base_width = img.size[0] // 4
            logo.thumbnail((base_width, base_width))
            
            # Vị trí dán logo (giữa mã QR)
            logo_pos = (
                (img.size[0] - logo.size[0]) // 2,
                (img.size[1] - logo.size[1]) // 2,
            )
            img.paste(logo, logo_pos, mask=logo if logo.mode == 'RGBA' else None)
        except Exception as e:
            print(f"⚠️ Không thể thêm logo: {e}")

    # Lưu file
    img.save(output_file)
    print(f"✅ Mã QR đã được lưu tại: {output_file}")

if __name__ == "__main__":
    # Nhập dữ liệu từ người dùng
    data = input("🔗 Nhập dữ liệu (URL hoặc văn bản) để tạo mã QR: ")
    fill_color = input("🎨 Nhập màu mã QR (ví dụ: black, blue, red): ") or "black"
    back_color = input("🎨 Nhập màu nền mã QR (ví dụ: white, yellow): ") or "white"
    logo_path = input("🖼️ Nhập đường dẫn tới file logo (hoặc để trống nếu không dùng): ")
    box_size = input("📏 Nhập kích cỡ ô vuông (ví dụ: 10, 15): ") or "10"
    
    try:
        box_size = int(box_size)
        output_file = input("💾 Nhập tên file đầu ra (mặc định: qr_code.png): ") or "qr_code.png"
        
        # Tạo mã QR
        generate_qr(data, fill_color, back_color, logo_path, box_size, output_file)
    except ValueError:
        print("⚠️ Kích cỡ ô vuông phải là một số nguyên!")
