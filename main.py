import streamlit as st
import pandas as pd
import numpy as np

# Cấu hình trang
st.set_page_config(
    page_title="Hướng dẫn Cài đặt Python 3.13 & UV (Chi tiết)",
    page_icon="🚀",
    layout="centered"
)

# Tiêu đề
st.title("🚀 Hướng dẫn Cài đặt Môi trường Python 3.13 trên Windows")
st.markdown("Tớ sẽ giải thích ý nghĩa của từng câu lệnh cậu cần nhập.")

st.divider()

# --- BƯỚC 1: CÀI PYTHON BẰNG WINGET ---
st.header("1️⃣ Bước 1: Cài đặt Python 3.13 bằng Winget")
st.write("Sử dụng **Windows Package Manager (Winget)** để cài đặt Python.")

st.warning("⚠️ LƯU Ý QUAN TRỌNG: Python 3.13 hiện đang ở giai đoạn **phát triển (alpha/beta)**. Gói này có thể chưa có sẵn trên Winget. Cậu nên kiểm tra gói `Python.Python.3.13` trước.")

st.info("💡 Mở **Windows Terminal** hoặc **PowerShell** với quyền Admin và chạy lệnh sau:")

st.write("**Mục đích:** Tìm và cài đặt Python 3.13 vào máy tính của cậu. **`--scope machine`** giúp cài đặt cho toàn bộ máy.")
st.code('winget install Python.Python.3.13 --scope machine', language='powershell')
st.caption("(*Nếu lệnh trên thất bại, cậu hãy thử cài đặt phiên bản ổn định hơn như `Python.Python.3.12`.*)")

st.write("**Mục đích:** Khởi động lại Terminal để hệ thống nhận diện Python vừa cài và kiểm tra phiên bản.")
st.code("python --version", language='bash')

# --- BƯỚC 2: CÀI UV ---
st.header("2️⃣ Bước 2: Cài đặt UV (Công cụ quản lý gói)")
st.write("Cài đặt UV bằng script PowerShell chính thức, đây là cách nhanh nhất để có bản mới nhất.")

st.write("**Mục đích:** Tải và thực thi script cài đặt UV trực tiếp từ nhà phát triển. `irm` (Invoke-RestMethod) tải script, `| iex` (Invoke-Expression) thực thi nó. Phương pháp này đảm bảo cậu luôn có phiên bản UV mới nhất.")
st.code('powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"', language='powershell')
st.success("Sau khi chạy xong, hãy khởi động lại Terminal để cập nhật biến môi trường PATH.")

# --- BƯỚC 3: KHỞI TẠO DỰ ÁN ---
st.header("3️⃣ Bước 3: Khởi tạo Dự án")
st.write("Sử dụng UV để thiết lập môi trường ảo và cấu trúc dự án.")

st.subheader("A. Tạo và Chuẩn bị Dự án")
st.write("**Mục đích:** Tạo thư mục dự án (`mkdir my_app`) và di chuyển vào bên trong thư mục đó (`cd my_app`).")
st.code("""
mkdir my_app
cd my_app
""", language='bash')

st.write("**Mục đích:** Lệnh `uv init` khởi tạo dự án. Nó tự động tạo môi trường ảo (`.venv`) và file cấu hình gói (`requirements.in`) cho dự án của cậu.")
st.code("uv init", language='bash')


st.subheader("B. Thêm thư viện Streamlit")
st.write("**Mục đích:** Lệnh `uv add streamlit` thêm gói Streamlit vào dự án. UV sẽ cài đặt Streamlit vào môi trường ảo vừa tạo (`.venv`) và tự động ghi tên gói vào file cấu hình dự án.")
st.code("uv add streamlit", language='bash')

# ------------------------------------------------------------------
# --- BƯỚC 4: KIỂM TRA CÀI ĐẶT (TEST) ---
# ------------------------------------------------------------------
st.header("4️⃣ Bước 4: Kiểm tra Cài đặt (Test)")
st.write("Đây là đoạn code **Streamlit** mẫu tạo ra một ứng dụng nhỏ để kiểm tra tính tương tác của cài đặt thành công:")

# Định nghĩa đoạn code test mới
test_code = """
import streamlit as st
import pandas as pd
import numpy as np

st.balloons()
st.subheader("✅ KIỂM TRA THÀNH CÔNG: Môi trường đã sẵn sàng!")
st.success("🎉 Chúc mừng bạn cài đặt thành công Streamlit, UV, Pandas và Numpy! 🎉")

# Hiển thị Widget
value = st.slider("1. Chọn một giá trị:", 0, 100, 50)
st.info(f"Giá trị bạn chọn là: {value}")

# Hiển thị Data
df = pd.DataFrame(
    np.random.randn(5, 4),
    columns=['Cột A', 'Cột B', 'Cột C', 'Cột D']
)
st.dataframe(df)

if st.button('2. Nhấn vào tớ!'):
    st.balloons()
    st.write("Đã nhấn nút. Ứng dụng hoạt động tương tác!")
"""
st.code(test_code, language='python')

# Hiển thị kết quả của đoạn code đó (đã được tích hợp vào file main.py này)
# Tái tạo output của code test
st.divider()
st.subheader("✅ KIỂM TRA THÀNH CÔNG: Môi trường đã sẵn sàng!")
st.success("🎉 Chúc mừng bạn cài đặt thành công Streamlit, UV, Pandas và Numpy! 🎉")

value = st.slider("1. Chọn một giá trị:", 0, 100, 50)
st.info(f"Giá trị bạn chọn là: {value}")

df = pd.DataFrame(
    np.random.randn(5, 4),
    columns=['Cột A', 'Cột B', 'Cột C', 'Cột D']
)
st.dataframe(df)

if st.button('2. Nhấn vào tớ!'):
    st.balloons()
    st.write("Đã nhấn nút. Ứng dụng hoạt động tương tác!")

st.markdown("Nếu cậu thấy **thanh trượt** và **bảng dữ liệu** này, nghĩa là các công cụ đã sẵn sàng.")
st.divider()

# ------------------------------------------------------------------
# --- BƯỚC 5: CHẠY FILE (RUN FILE) ---
# ------------------------------------------------------------------
st.header("5️⃣ Bước 5: Chạy Ứng dụng (Run File)")
st.write("Sử dụng lệnh `uv run` để chạy Streamlit và xem ứng dụng web của cậu.")

st.write("**Mục đích:** Lệnh **`uv run`** đảm bảo rằng lệnh tiếp theo (`streamlit run main.py`) được gọi từ môi trường ảo của dự án. Đây là lệnh tiêu chuẩn để **chạy** các ứng dụng Streamlit của cậu.")
st.code("uv run streamlit run main.py", language='bash')
st.info("Ứng dụng sẽ tự động mở trên trình duyệt của cậu tại địa chỉ `http://localhost:8501`.")


st.caption("Code by Gemini • Hỗ trợ học tập Python & Streamlit")