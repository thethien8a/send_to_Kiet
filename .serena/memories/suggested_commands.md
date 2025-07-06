# Suggested Commands for Development

## Environment Setup
```bash
# Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Install development dependencies (if needed)
pip install black flake8 pytest
```

## Running the Scraper
```bash
# Basic run
python techmeme.py

# Run with Python module syntax
python -m techmeme

# Run with logging output to file
python techmeme.py > output.log 2>&1
```

## Development Commands
```bash
# Format code with Black
black techmeme.py

# Lint code with flake8
flake8 techmeme.py --max-line-length=100

# Check for Python syntax errors
python -m py_compile techmeme.py

# Run in interactive mode for debugging
python -i techmeme.py
```

## Git Commands
```bash
# Initialize git repository
git init

# Add all files
git add .

# Initial commit
git commit -m "Initial commit: Techmeme scraper with BeautifulSoup"

# Check status
git status

# View changes
git diff

# Add remote repository
git remote add origin <repository-url>

# Push to remote
git push -u origin main
```

## Testing and Validation
```bash
# Test if dependencies are installed correctly
python -c "import requests, bs4; print('Dependencies OK')"

# Quick syntax check
python -c "exec(open('techmeme.py').read()); print('Syntax OK')"

# Test scraper functionality
python -c "from techmeme import TechmemeScraper; s=TechmemeScraper(); print('Import OK')"
```

## Windows-specific Commands
```bash
# List directory contents
dir

# Change directory
cd path\to\directory

# Find files
where python
where pip

# Check Python version
python --version

# View file contents
type filename.txt

# Search in files
findstr "search_term" *.py
```

## Data Management
```bash
# View scraped data
type *.json | head -20   # View first 20 lines of JSON files
# python -m json.tool filename.json  # Pretty print JSON

# Count articles in JSON
python -c "import json; data=json.load(open('filename.json')); print(f'Articles: {len(data)}')"

# Convert JSON to CSV (if needed)
python -c "import json,csv,sys; data=json.load(sys.stdin); csv.writer(sys.stdout).writerows([data[0].keys()]+[row.values() for row in data])" < input.json > output.csv
```