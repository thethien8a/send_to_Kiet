# Techmeme News Scraper - Project Overview

## Project Purpose
Dự án này là một công cụ web scraping được xây dựng bằng Python để cào dữ liệu tin tức từ Techmeme.com - một trang tổng hợp tin tức công nghệ hàng đầu. Mục tiêu là tự động thu thập và lưu trữ thông tin các bài viết tin tức công nghệ.

## Tech Stack
- **Python 3.x**: Ngôn ngữ lập trình chính
- **BeautifulSoup4**: Thư viện parse HTML
- **Requests**: Thư viện HTTP client để gửi request
- **lxml**: Parser nhanh cho BeautifulSoup
- **JSON/CSV**: Định dạng lưu trữ dữ liệu đầu ra

## Core Features
- Cào dữ liệu từ trang chủ Techmeme
- Trích xuất tiêu đề, URL, mô tả, thời gian và nguồn tin
- Lưu dữ liệu ra định dạng JSON và CSV
- Retry logic và xử lý lỗi
- Logging chi tiết
- Support cho nhiều định dạng đầu ra

## File Structure
- `techmeme.py`: Script chính chứa class TechmemeScraper
- `requirements.txt`: Dependencies Python
- `README.md`: Documentation chính
- `examples.md`: Ví dụ sử dụng
- `.gitignore`: Git ignore rules