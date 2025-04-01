# 🚀 AI AGENT CODE GENERATOR
Dự án ứng dụng kỹ thuật Multi-LLM, RAG để phân tích ngữ cảnh, phân tích mã nguồn. Từ đó generate ra mã nguồn theo prompt như: unit test, request, mô tả mã nguồn.
Mã nguồn được tạo ra sau đó được generate vào một file mới.


## 📝 Giới Thiệu  
Dự án này xây dựng một hệ thống **AI Agent** có khả năng **phân tích, truy vấn và sinh mã nguồn** dựa trên tài liệu API và các tập tin mã nguồn. Hệ thống sử dụng **LlamaIndex**, **Ollama**, và **mô hình nhúng văn bản** để hỗ trợ lập trình viên tìm kiếm thông tin và tạo mã nguồn tự động.

---

## 🔧 Tính Năng  

✅ **Truy vấn tài liệu API**  
- Hệ thống có thể đọc và trích xuất thông tin từ các tài liệu API (PDF).  
- Sử dụng **VectorStoreIndex** để lưu trữ và tìm kiếm thông tin một cách hiệu quả.  

✅ **Đọc và hiểu mã nguồn**  
- Tích hợp một **code reader** giúp phân tích mã nguồn hiện có.  
- Sử dụng mô hình **CodeLlama** để hiểu và xử lý mã nguồn.  

✅ **Sinh mã nguồn tự động**  
- Nhận câu lệnh đầu vào từ người dùng và phản hồi bằng đoạn mã phù hợp.  
- Mô hình có thể cung cấp mô tả chi tiết và tên file đề xuất cho đoạn mã sinh ra.  

✅ **Pipeline xử lý truy vấn thông minh**  
- Kết hợp `ReActAgent` với `QueryPipeline` để tối ưu hóa quá trình xử lý truy vấn.  
- Tự động chuyển đổi truy vấn thành JSON để dễ dàng thao tác.  

✅ **Lưu mã nguồn tự động**  
- Mã được sinh ra sẽ được lưu vào thư mục `output` với tên file phù hợp.  

---

## 🚀 Công Nghệ Sử Dụng  
- **LlamaIndex**: Hỗ trợ xây dựng và truy vấn cơ sở tri thức từ tài liệu.  
- **Ollama**: Cung cấp các mô hình AI mạnh mẽ như `mistral` và `codellama`.  
- **FAISS**: Dùng để tìm kiếm vector hiệu quả trong quá trình truy vấn.  
- **Pydantic**: Định nghĩa mô hình dữ liệu đầu ra.  
- **AST (Abstract Syntax Tree)**: Dùng để xử lý và kiểm tra dữ liệu JSON sinh ra.  

---

## 🏃‍♂️ Cách Chạy  

### 1️⃣ Cài đặt thư viện cần thiết  
```sh
pip install -r requirements.txt
```

### 2️⃣ Cấu trúc thư mục  
```sh
📂 data        # Chứa các tài liệu API (PDF)  
📂 output      # Nơi lưu trữ mã nguồn được sinh ra  
📜 code_reader.py  # Trình đọc và phân tích mã nguồn  
📜 prompts.py      # Các mẫu prompt cho AI  
📜 main.py         # Chạy ứng dụng chính  
```

### 3️⃣ Chạy chương trình  
```sh
python main.py
```

Hệ thống sẽ yêu cầu bạn nhập truy vấn. Để thoát, nhập `q`.  

---

## 📌 Ví Dụ Sử Dụng  

### 🔍 Tìm hiểu API  
```sh
Enter a prompt (q to quit): Cách sử dụng API tạo người dùng?
```
👉 AI sẽ phân tích tài liệu API và trả lời cách sử dụng API tương ứng.  

### 🤖 Sinh mã nguồn tự động  
```sh
Enter a prompt (q to quit): read the content of test.py and write a python script that calls the post end point to make a new item
```
👉 AI sẽ sinh ra đoạn mã gọi API để thêm một item mới và lưu vào thư mục `output`.  

---

🚀 **Hãy thử ngay và khám phá sức mạnh của AI trong lập trình!**

