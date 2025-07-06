#!/bin/bash

echo "🚀 Setting up Techmeme Scraper..."
echo

echo "📦 Installing dependencies..."

# Check if uv is available
if command -v uv &> /dev/null; then
    echo "Using uv package manager..."
    uv pip install -r requirements.txt
    if [ $? -eq 0 ]; then
        echo "✅ Dependencies installed successfully with uv"
    else
        echo "❌ uv installation failed, falling back to pip"
        pip install -r requirements.txt
    fi
else
    echo "Using pip package manager..."
    pip install -r requirements.txt
fi

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    echo "Try manually: pip install beautifulsoup4 requests lxml"
    exit 1
fi

echo
echo "🧪 Testing installation..."
python -c "import requests, bs4, lxml; print('✅ All dependencies imported successfully')"

if [ $? -eq 0 ]; then
    echo
    echo "🎉 Setup completed successfully!"
    echo
    echo "📚 Quick start:"
    echo "  python techmeme.py"
    echo
    echo "📖 For more information, see README.md"
else
    echo "❌ Import test failed"
    echo "Check your Python environment and try again"
fi