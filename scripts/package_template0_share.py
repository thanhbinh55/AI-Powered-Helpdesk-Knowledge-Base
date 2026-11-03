#!/usr/bin/env python3
"""
scripts/package_template0_share.py
Đóng gói bộ công cụ Render Báo cáo Template 0 thành file zip kèm hướng dẫn chi tiết
để người dùng có thể chia sẻ trực tiếp cho các nhóm/bạn cùng lớp trong học phần NMCNPM - HCMUS.
"""

import os
import sys
import shutil
import zipfile

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PACKAGE_DIR = os.path.join(REPO_ROOT, "template0-toolkit")
ZIP_OUTPUT = os.path.join(REPO_ROOT, "template0-toolkit.zip")

README_CONTENT = """# BỘ CÔNG CỤ RENDER BÁO CÁO TEMPLATE 0 (HTML & PDF)
**Học phần:** Nhập môn Công nghệ Phần mềm (NMCNPM) — Khoa CNTT, ĐH Khoa học Tự nhiên TP.HCM (HCMUS)

---

## 📌 GIỚI THIỆU
Bộ công cụ này giúp các nhóm sinh viên viết báo cáo bằng **Markdown (.md)** trên GitHub nhưng xuất ra định dạng **HTML / PDF chuẩn mực 100% theo mẫu Template 0 của Thầy**:
- **Trang bìa chuẩn:** Logo HCMUS, tên trường, khoa, bộ môn, ô Project Proposal nền xanh dịu `#548dd4`.
- **100% Font Times New Roman:** Áp dụng trên toàn bộ tiêu đề, nội dung, bảng biểu, trích dẫn, mã nguồn và header/footer.
- **Header & Footer bar trên từng trang:** Tự động hiển thị tên môn, tên đồ án và số trang.
- **Tự động sinh Mục lục:** Trích xuất các đề mục lớn/nhỏ và căn chỉnh chấm lửng (`. . .`) thẳng hàng.
- **Hoàn toàn độc lập (Self-contained):** Logo HCMUS được nhúng trực tiếp dưới dạng Base64, không lo bị chết link ảnh hay lỗi định dạng khi Thầy Cô mở offline.

---

## 📂 NỘI DUNG GÓI TOOLKIT

```text
template0-toolkit/
├── README.md                           # Hướng dẫn chi tiết cách dùng
├── template0_styles.py                 # Bộ CSS Design System chuẩn A4 & Times New Roman
├── hcmus_logo.png                      # Logo chính thức của HCMUS
├── render_proposal_template0.py        # Script render Đề xuất đồ án (Project Proposal)
├── render_ai_usage_template0.py        # Script render Báo cáo sử dụng AI (AI Usage)
└── render_git_contributions_template0.py # Script render Báo cáo Git Commit History
```

---

## 🚀 HƯỚNG DẪN SỬ DỤNG NHANH (3 BƯỚC)

### Yêu cầu môi trường:
- Chỉ cần máy tính có cài sẵn **Python 3** (mặc định macOS, Linux, Windows đều có sẵn).
- Không cần cài bất kỳ thư viện ngoài phức tạp nào (`pip install` không bắt buộc).

---

### BƯỚC 1: Sao chép tệp vào repo của nhóm bạn
Giải nén và copy thư mục `template0-toolkit` hoặc toàn bộ các file `.py` cùng file `hcmus_logo.png` vào thư mục dự án của bạn (ví dụ đặt trong thư mục `scripts/`).

---

### BƯỚC 2: Tùy biến thông tin nhóm

Mở file script cần chạy (ví dụ `render_proposal_template0.py`) bằng bất kỳ trình soạn thảo nào (VS Code, Notepad, v.v.):

1. **Cấu hình đường dẫn tệp (dòng 20-22):**
   ```python
   MD_FILE = "path/to/your/project-proposal.md"    # File markdown báo cáo của bạn
   OUT_HTML = "path/to/your/project-proposal.html" # File HTML kết quả
   ```
   *(Mẹo: Bạn cũng có thể truyền trực tiếp qua dòng lệnh ở Bước 3 mà không cần sửa file!)*

2. **Cấu hình thông tin nhóm trên trang bìa (trong hàm `render_cover_page`):**
   - Đổi dòng: `NMCNPM - <Tên Dự Án Của Bạn> - Group <Mã Nhóm>`
   - Đổi tên đồ án trong khung banner: `Project Proposal`

---

### BƯỚC 3: Chạy lệnh Render

Mở Terminal / Command Prompt và chạy:

#### Cách 1: Chạy theo đường dẫn mặc định đã cấu hình:
```bash
python3 render_proposal_template0.py
```

#### Cách 2: Truyền trực tiếp đường dẫn file Markdown của bạn (Cực kỳ tiện lợi):
```bash
python3 render_proposal_template0.py duong_dan/file_bao_cao.md duong_dan/file_xuat.html
```

Tương tự cho báo cáo AI Usage và Git Contributions:
```bash
python3 render_ai_usage_template0.py
python3 render_git_contributions_template0.py
```

---

## 🖨️ CÁCH XUẤT RA FILE PDF CHUẨN NỘP BÀI

1. Mở file `.html` vừa sinh ra bằng trình duyệt web bất kỳ (**Google Chrome**, **Microsoft Edge**, hoặc **Apple Safari**).
2. Nhấn tổ hợp phím **`Ctrl + P`** (Windows/Linux) hoặc **`Cmd + P`** (macOS) để mở hộp thoại In (Print).
3. Tại mục **Máy in (Destination)**: Chọn **Lưu dưới dạng PDF (Save as PDF)**.
4. Tại mục **Khổ giấy (Paper size)**: Chọn **A4**.
5. Tại mục **Tùy chọn khác (More settings)**:
   - **Tỷ lệ (Scale):** Mặc định (`Default` hoặc `100%`).
   - **Tùy chọn đồ họa nền (Background graphics):** ✅ **Tích chọn (BẮT BUỘC)** để hiển thị màu nền bảng và banner.
   - **Đầu trang và chân trang của trình duyệt (Headers and footers):** ❌ **Bỏ tích** (để dùng header/footer bar chuẩn Template 0 được nhúng sẵn trong HTML).
6. Nhấn **Save (Lưu)**. Bạn đã có bản PDF tuyệt đẹp sẵn sàng nộp cho Thầy Cô!

---

## 💡 MẸO TRÌNH BÀY MARKDOWN ĐỂ ĐẠT ĐIỂM TỐI ĐA

- **Để ngắt trang chủ động:** Chèn dòng sau vào Markdown tại vị trí muốn sang trang mới:
  ```html
  <div style="page-break-after: always; break-after: page;"></div>
  ```
- **Tiêu đề bảng:** Dùng thẻ caption căn giữa:
  ```html
  <p class="table-caption" style="text-align: center; font-weight: 700; margin-bottom: 8px;">Bảng 1. Danh sách thành viên và đóng góp</p>
  ```
- **Tiêu đề hình ảnh / sơ đồ:**
  ```html
  <p class="figure-caption" style="text-align: center; font-style: italic; margin-top: 8px;">Hình 1. Kiến trúc tổng thể phần mềm</p>
  ```

---
*Chúc các bạn hoàn thành xuất sắc đồ án môn Nhập môn Công nghệ Phần mềm!*
"""


def main():
    print("📦 Bắt đầu đóng gói bộ công cụ Template 0 Toolkit...")

    if os.path.exists(PACKAGE_DIR):
        shutil.rmtree(PACKAGE_DIR)
    os.makedirs(PACKAGE_DIR, exist_ok=True)

    # 1. Ghi file README.md
    readme_path = os.path.join(PACKAGE_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(README_CONTENT.strip() + "\n")
    print(f"  📝 Đã tạo: {readme_path}")

    # 2. Sao chép CSS tokens
    src_css = os.path.join(REPO_ROOT, "scripts", "template0_styles.py")
    dst_css = os.path.join(PACKAGE_DIR, "template0_styles.py")
    shutil.copy2(src_css, dst_css)
    print(f"  🎨 Đã sao chép: {dst_css}")

    # 3. Sao chép logo chính thức
    src_logo = os.path.join(REPO_ROOT, "reports", "assets", "hcmus_logo.png")
    dst_logo = os.path.join(PACKAGE_DIR, "hcmus_logo.png")
    shutil.copy2(src_logo, dst_logo)
    print(f"  🏛️ Đã sao chép: {dst_logo}")

    # 4. Sao chép các script render với hỗ trợ CLI arguments linh hoạt
    scripts_to_copy = [
        "render_proposal_template0.py",
        "render_ai_usage_template0.py",
        "render_git_contributions_template0.py",
    ]

    for script_name in scripts_to_copy:
        src_path = os.path.join(REPO_ROOT, "scripts", script_name)
        dst_path = os.path.join(PACKAGE_DIR, script_name)

        with open(src_path, "r", encoding="utf-8") as f:
            code = f.read()

        # Cải tiến script để hỗ trợ nhận file input/output qua command line argument
        cli_enhancement = """
    # Hỗ trợ nhận đường dẫn file từ dòng lệnh: python3 script.py [input.md] [output.html]
    global MD_FILE, OUT_HTML
    if len(sys.argv) > 1 and sys.argv[1].endswith('.md'):
        MD_FILE = os.path.abspath(sys.argv[1])
    if len(sys.argv) > 2 and sys.argv[2].endswith('.html'):
        OUT_HTML = os.path.abspath(sys.argv[2])
    elif len(sys.argv) > 1 and sys.argv[1].endswith('.md'):
        base, _ = os.path.splitext(MD_FILE)
        OUT_HTML = base + ".html"
"""
        # Inject sau khai báo def build_...
        if "def build_template0_document():" in code:
            code = code.replace("def build_template0_document():", "def build_template0_document():" + cli_enhancement)
        elif "def build_ai_usage_document():" in code:
            code = code.replace("def build_ai_usage_document():", "def build_ai_usage_document():" + cli_enhancement)
        elif "def build_git_contributions_document():" in code:
            code = code.replace("def build_git_contributions_document():", "def build_git_contributions_document():" + cli_enhancement)

        # Cập nhật đường dẫn logo dự phòng để ưu tiên file hcmus_logo.png nằm cùng thư mục script
        code = code.replace('candidates = [', 'candidates = [\n        os.path.join(os.path.dirname(__file__), "hcmus_logo.png"),')

        with open(dst_path, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"  ⚙️ Đã sao chép và tối ưu CLI: {dst_path}")

    # 5. Nén toàn bộ thư mục thành file zip
    print(f"\n🗜️ Đang nén thành file: {ZIP_OUTPUT}...")
    with zipfile.ZipFile(ZIP_OUTPUT, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(PACKAGE_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, REPO_ROOT)
                zipf.write(file_path, arcname)

    zip_size_kb = os.path.getsize(ZIP_OUTPUT) / 1024
    print(f"✅ HOÀN TẤT! File zip đã sẵn sàng: {ZIP_OUTPUT} ({zip_size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
