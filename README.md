---

## **Advanced QR Code Generator**

### **Mô tả dự án (Vietnamese)**
Dự án này là một công cụ Python nâng cao, cho phép bạn tạo mã QR với các tùy chỉnh như:
- Màu sắc mã QR và màu nền.
- Thêm logo vào giữa mã QR.
- Thay đổi kích thước mã QR.

Mã QR sẽ được lưu dưới dạng file hình ảnh (mặc định: `qr_code.png`).

---

### **Project Description (English)**
This is an advanced Python tool that allows you to generate QR codes with customizations such as:
- Custom QR code and background colors.
- Add a logo in the center of the QR code.
- Adjust the size of the QR code.

The QR code is saved as an image file (default: `qr_code.png`).

---

### **Cách sử dụng (Vietnamese)**
#### **1. Cài đặt môi trường**
1. Tải Python từ [python.org](https://www.python.org/) nếu chưa cài đặt.
2. Tạo và kích hoạt môi trường ảo:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/MacOS
   venv\Scripts\activate         # Windows
   ```

#### **2. Cài đặt thư viện**
- Sử dụng lệnh sau để cài đặt các thư viện cần thiết:
   ```bash
   pip install -r requirements.txt
   ```

#### **3. Chạy chương trình**
- Chạy file Python chính:
   ```bash
   python main.py
   ```
- Nhập các thông tin được yêu cầu:
  - **URL hoặc văn bản**: Dữ liệu cần mã hóa thành mã QR.
  - **Màu sắc mã QR**: Tùy chọn màu cho mã QR (ví dụ: `blue`, `red`).
  - **Màu nền**: Tùy chọn màu nền (ví dụ: `white`, `yellow`).
  - **Đường dẫn logo**: (Không bắt buộc) Đường dẫn tới file logo muốn thêm vào.
  - **Kích thước ô vuông**: Điều chỉnh độ lớn mã QR (ví dụ: `10`, `15`).

---

### **Usage Instructions (English)**
#### **1. Set up the environment**
1. Download Python from [python.org](https://www.python.org/) if not installed.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/MacOS
   venv\Scripts\activate         # Windows
   ```

#### **2. Install dependencies**
- Use the following command to install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

#### **3. Run the program**
- Run the main Python script:
   ```bash
   python main.py
   ```
- Enter the following details when prompted:
  - **URL or text**: The data you want to encode into the QR code.
  - **QR code color**: Choose a color for the QR code (e.g., `blue`, `red`).
  - **Background color**: Choose a background color (e.g., `white`, `yellow`).
  - **Logo path**: (Optional) Path to a logo file to embed in the QR code.
  - **Box size**: Adjust the size of the QR code blocks (e.g., `10`, `15`).

---

### **Ví dụ minh họa / Example**
#### **Input (Vietnamese/English):**
```plaintext
🔗 Nhập dữ liệu (URL hoặc văn bản) để tạo mã QR: https://www.facebook.com/NHL2K5
🎨 Nhập màu mã QR: black
🎨 Nhập màu nền mã QR: white
🖼️ Nhập đường dẫn tới file logo: logo.png
📏 Nhập kích cỡ ô vuông: 15
💾 Nhập tên file đầu ra: my_qr_code.png
```

#### **Kết quả / Result:**
File `my_qr_code.png` được tạo với mã QR như sau:

![alt text](qr_code.png)

---

### **Cấu trúc dự án / Project Structure**
```plaintext
qr-code-generator/
│
├── main.py                # File Python chính / Main Python script
├── requirements.txt       # Danh sách thư viện cần thiết / Required libraries
├── README.md              # File mô tả dự án / Project description
├── qr_code.png            # File kết quả mẫu / Sample QR code
└── logo.png               # File logo (nếu có / optional)
```

---

### **Thư viện sử dụng (Vietnamese)**
- **qrcode**: Tạo mã QR.
- **Pillow**: Hỗ trợ xử lý màu sắc, hình ảnh, và thêm logo.

### **Libraries Used (English)**
- **qrcode**: For QR code generation.
- **Pillow**: For image processing and logo embedding.

---

### **Đóng góp / Contributions**
- Nếu bạn muốn cải thiện hoặc thêm tính năng mới cho dự án, hãy mở **Pull Request** hoặc gửi ý kiến qua phần **Issues** trên GitHub.
- If you want to improve or add new features, feel free to open a **Pull Request** or report an issue.

---

### **License**
Dự án được cấp phép theo giấy phép **MIT License**.
This project is licensed under the **MIT License**.

---
