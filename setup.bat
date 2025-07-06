@echo off
echo 🚀 Setting up Techmeme Scraper...

echo.
echo 📦 Installing dependencies...

REM Try uv first (if available)
where uv >nul 2>nul
if %ERRORLEVEL% == 0 (
    echo Using uv package manager...
    uv pip install -r requirements.txt
    if %ERRORLEVEL% == 0 (
        echo ✅ Dependencies installed successfully with uv
        goto test
    )
)

REM Fall back to pip
echo Using pip package manager...
pip install -r requirements.txt
if %ERRORLEVEL% == 0 (
    echo ✅ Dependencies installed successfully with pip
) else (
    echo ❌ Failed to install dependencies
    echo Try manually: pip install beautifulsoup4 requests lxml
    pause
    exit /b 1
)

:test
echo.
echo 🧪 Testing installation...
python -c "import requests, bs4, lxml; print('✅ All dependencies imported successfully')"
if %ERRORLEVEL% == 0 (
    echo.
    echo 🎉 Setup completed successfully!
    echo.
    echo 📚 Quick start:
    echo   python techmeme.py
    echo.
    echo 📖 For more information, see README.md
) else (
    echo ❌ Import test failed
    echo Check your Python environment and try again
)

echo.
pause