# Coding Style and Conventions

## Python Style Guidelines
- **PEP 8**: Tuân thủ Python PEP 8 style guide
- **Type Hints**: Sử dụng type hints cho tất cả functions và methods
- **Docstrings**: Google-style docstrings cho classes và functions
- **Line Length**: 100 characters max per line
- **Encoding**: UTF-8 cho tất cả file Python

## Naming Conventions
- **Classes**: PascalCase (VD: `TechmemeScraper`)
- **Functions/Methods**: snake_case (VD: `get_page_content`)
- **Variables**: snake_case (VD: `article_data`)
- **Constants**: UPPER_SNAKE_CASE (VD: `DEFAULT_TIMEOUT`)
- **Private methods**: Prefix với underscore (VD: `_parse_article_container`)

## Code Organization
- **Imports**: Standard library → Third party → Local imports
- **Class Structure**: 
  1. Class docstring
  2. `__init__` method
  3. Public methods
  4. Private methods
- **Error Handling**: Comprehensive try-except blocks với logging
- **Logging**: Sử dụng Python logging module với các level phù hợp

## Documentation Standards
- **README.md**: Tiếng Việt với emoji để dễ đọc
- **Code Comments**: Tiếng Anh cho technical details
- **Docstrings**: Tiếng Anh theo Google format
- **Examples**: Cung cấp examples thực tế trong `examples.md`