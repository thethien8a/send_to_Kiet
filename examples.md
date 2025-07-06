# Techmeme Scraper - Example Usage

This file demonstrates various ways to use the Techmeme scraper.

## Basic Usage Example

```python
#!/usr/bin/env python3

from techmeme import TechmemeScraper
import json

# Initialize scraper
scraper = TechmemeScraper()

# Scrape articles
print("🕷️ Scraping Techmeme...")
articles = scraper.scrape_homepage()

if articles:
    print(f"✅ Found {len(articles)} articles")
    
    # Save to files
    json_file = scraper.save_to_json(articles)
    csv_file = scraper.save_to_csv(articles)
    
    # Display some statistics
    print(f"📊 Articles with descriptions: {sum(1 for a in articles if a['description'])}")
    print(f"📊 Articles with timestamps: {sum(1 for a in articles if a['timestamp'])}")
    
    # Show first article
    if articles:
        first_article = articles[0]
        print(f"\n📰 First article:")
        print(f"   Title: {first_article['title']}")
        print(f"   URL: {first_article['url']}")
        
else:
    print("❌ No articles found")
```

## Advanced Usage with Custom Settings

```python
from techmeme import TechmemeScraper
import time

# Custom scraper with different settings
scraper = TechmemeScraper()

# Update headers for better compatibility
scraper.session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Edge/91.0.864.59',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
})

# Scrape with retry logic
max_retries = 3
for attempt in range(max_retries):
    try:
        articles = scraper.scrape_homepage()
        if articles:
            print(f"✅ Successfully scraped {len(articles)} articles on attempt {attempt + 1}")
            break
    except Exception as e:
        print(f"❌ Attempt {attempt + 1} failed: {e}")
        if attempt < max_retries - 1:
            time.sleep(5)  # Wait before retry
```

## Filtering and Processing Articles

```python
from techmeme import TechmemeScraper
from datetime import datetime
import re

scraper = TechmemeScraper()
articles = scraper.scrape_homepage()

if articles:
    # Filter articles by keywords
    ai_articles = [
        article for article in articles 
        if any(keyword in article['title'].lower() 
               for keyword in ['ai', 'artificial intelligence', 'machine learning', 'llm'])
    ]
    
    # Filter articles with descriptions
    detailed_articles = [
        article for article in articles 
        if article['description'] and len(article['description']) > 50
    ]
    
    # Sort by title length (assuming longer titles might be more detailed)
    sorted_articles = sorted(articles, key=lambda x: len(x['title']), reverse=True)
    
    print(f"📊 Statistics:")
    print(f"   Total articles: {len(articles)}")
    print(f"   AI-related articles: {len(ai_articles)}")
    print(f"   Articles with detailed descriptions: {len(detailed_articles)}")
    
    # Save filtered results
    if ai_articles:
        scraper.save_to_json(ai_articles, "ai_articles.json")
        print(f"💾 Saved {len(ai_articles)} AI articles to ai_articles.json")
```

Run any of these examples by saving to a .py file and running:
```bash
python example_usage.py
```