# Techmeme News Scraper 🕷️📰

Một công cụ Python để cào dữ liệu tin tức từ [Techmeme.com](https://www.techmeme.com/) - trang tổng hợp tin tức công nghệ hàng đầu.

## ✨ Tính năng

- 🎯 Cào dữ liệu từ trang chủ Techmeme
- 📄 Trích xuất tiêu đề, liên kết, mô tả và thời gian
- 💾 Lưu dữ liệu ra file JSON và CSV
- 🔄 Tự động retry khi có lỗi mạng
- 📊 Logging chi tiết cho việc debug
- ⚡ Sử dụng BeautifulSoup và requests

## 🛠️ Cài đặt

### 1. Clone repository
```bash
git clone <repository-url>
cd Crawl-News
```

### 2. Cài đặt dependencies

#### Tự động (Windows):
```bash
setup.bat
```

#### Tự động (Linux/Mac):
```bash
chmod +x setup.sh
./setup.sh
```

#### Thủ công:
```bash
# Sử dụng pip
pip install -r requirements.txt

# Hoặc sử dụng uv (nếu có)
uv pip install -r requirements.txt

# Hoặc cài đặt từng package
pip install beautifulsoup4 requests lxml
```

### 3. Kiểm tra cài đặt
```bash
python -c "import requests, bs4, lxml; print('✅ Setup completed!')"
```

## 🚀 Sử dụng

### Cách cơ bản
```bash
python techmeme.py
```

### Import vào code khác
```python
from techmeme import TechmemeScraper

# Khởi tạo scraper
scraper = TechmemeScraper()

# Cào dữ liệu
articles = scraper.scrape_homepage()

# Lưu dữ liệu
scraper.save_to_json(articles, "my_articles.json")
scraper.save_to_csv(articles, "my_articles.csv")
```

## 📊 Dữ liệu Output

Mỗi bài viết được trích xuất bao gồm:

```json
{
  "title": "Tiêu đề bài viết",
  "url": "https://example.com/article",
  "description": "Mô tả ngắn gọn về bài viết",
  "timestamp": "Thời gian đăng",
  "source": "Nguồn tin",
  "scraped_at": "2025-07-06T10:30:00"
}
```

## 🔧 Cấu hình

### Thay đổi User-Agent
```python
scraper = TechmemeScraper()
scraper.session.headers.update({
    'User-Agent': 'Your Custom User Agent'
})
```

### Điều chỉnh retry logic
```python
soup = scraper.get_page_content(url, retries=5)
```

## 📁 Cấu trúc thư mục

```
Crawl-News/
├── techmeme.py           # Script chính
├── requirements.txt      # Dependencies
├── README.md            # Documentation
├── .gitignore          # Git ignore rules
└── logs/               # Log files (tự động tạo)
```

## 🐛 Troubleshooting

### Lỗi thường gặp

1. **Không cào được dữ liệu**
   - Kiểm tra kết nối internet
   - Website có thể đã thay đổi cấu trúc HTML
   - Xem log file để debug

2. **403 Forbidden Error**
   - Thay đổi User-Agent
   - Thêm delay giữa các request

3. **Timeout Error**
   - Tăng timeout trong requests
   - Kiểm tra tốc độ mạng

### Debug
```bash
# Xem log chi tiết
tail -f techmeme_scraper.log

# Chạy với debug level
python -c "import logging; logging.basicConfig(level=logging.DEBUG); exec(open('techmeme.py').read())"
```

## ⚖️ Lưu ý pháp lý

- Tuân thủ robots.txt của website
- Không spam request quá nhiều
- Chỉ sử dụng cho mục đích học tập/nghiên cứu
- Tôn trọng bản quyền nội dung

## 🤝 Đóng góp

1. Fork repository
2. Tạo feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push branch (`git push origin feature/amazing-feature`)
5. Tạo Pull Request

## 📝 License

Dự án này được phát hành dưới MIT License. Xem file [LICENSE](LICENSE) để biết thêm chi tiết.

## 📞 Liên hệ

Nếu có câu hỏi hoặc góp ý, vui lòng tạo [Issue](../../issues) trên GitHub.

---

**Lưu ý**: Đây là công cụ học tập. Vui lòng sử dụng một cách có trách nhiệm và tuân thủ các quy định về web scraping.