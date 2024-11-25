import qrcode
from PIL import Image

def generate_qr(data, fill_color="black", back_color="white", logo_path=None, box_size=10, output_file="qr_code.png"):
    """
    Tạo mã QR với tùy chọn màu sắc, logo, kích cỡ.

    Generate a QR code with customizable colors, logo, and size.

    :param data: Dữ liệu (URL hoặc văn bản) cần mã hóa / Data (URL or text) to encode.
    :param fill_color: Màu mã QR / QR code color.
    :param back_color: Màu nền mã QR / Background color.
    :param logo_path: Đường dẫn đến file logo (nếu có) / Path to the logo file (if any).
    :param box_size: Kích cỡ ô vuông trong mã QR / Size of QR code blocks.
    :param output_file: Tên file đầu ra / Output file name.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Tạo hình ảnh mã QR với màu sắc tùy chỉnh / Create QR code image with custom colors
    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGB')

    # Thêm logo (nếu có) / Add logo (if any)
    if logo_path:
        try:
            logo = Image.open(logo_path)
            # Điều chỉnh kích cỡ logo để vừa với mã QR / Resize logo to fit in the QR code
            base_width = img.size[0] // 4
            logo.thumbnail((base_width, base_width))

            # Vị trí dán logo (giữa mã QR) / Position logo in the center of the QR code
            logo_pos = (
                (img.size[0] - logo.size[0]) // 2,
                (img.size[1] - logo.size[1]) // 2,
            )
            img.paste(logo, logo_pos, mask=logo if logo.mode == 'RGBA' else None)
        except Exception as e:
            print(f"⚠️ Không thể thêm logo / Unable to add logo: {e}")

    # Lưu file / Save the file
    img.save(output_file)
    print(f"✅ Mã QR đã được lưu tại: {output_file} / QR code saved to: {output_file}")

if __name__ == "__main__":
    # Nhập dữ liệu từ người dùng / Input data from the user
    data = input("🔗 Nhập dữ liệu (URL hoặc văn bản) để tạo mã QR:\nEnter data (URL or text) to generate QR: ")

    fill_color = input("🎨 Nhập màu mã QR (ví dụ: black, #000000, red):\nEnter QR code color (e.g., black, #000000, red): ") or "black"
    back_color = input("🎨 Nhập màu nền mã QR (ví dụ: white, #FFFFFF, yellow):\nEnter background color of QR (e.g., white, #FFFFFF, yellow): ") or "white"

    logo_path = input("🖼️ Nhập đường dẫn tới file logo (hoặc để trống nếu không dùng):\nEnter path to logo file (or leave blank if none): ")
    box_size = input("📏 Nhập kích cỡ ô vuông (ví dụ: 10, 15):\nEnter QR code block size (e.g., 10, 15): ") or "10"

    try:
        box_size = int(box_size)
        output_file = input("💾 Nhập tên file đầu ra (mặc định: qr_code.png):\nEnter output file name (default: qr_code.png): ") or "qr_code.png"

        # Tạo mã QR / Generate QR code
        generate_qr(data, fill_color, back_color, logo_path, box_size, output_file)
    except ValueError:
        print("⚠️ Kích cỡ ô vuông phải là một số nguyên / Block size must be an integer!")
