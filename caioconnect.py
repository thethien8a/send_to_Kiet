import time
import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def scrape_caioconnect_news(total_pages):
    """
    Navigates through all pages of the CAIO Connect news section,
    scraping article titles and links.
    """
    base_url = 'https://caioconnect.org/news/'
    all_articles = []
    page_number = 1

    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--log-level=3')
  
        options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
        
        # This redirects the ChromeDriver service's logs to a "black hole"
        service = ChromeService(ChromeDriverManager().install(), log_output=os.devnull)
        
        driver = webdriver.Chrome(service=service, options=options)

        while True:
            # Construct URL for the current page
            if page_number == 1:
                current_url = base_url
            else:
                current_url = f"{base_url}page/{page_number}/"
            
            print(f"Scraping page: {current_url}")
            driver.get(current_url)
            
            # Give the page time to load
            time.sleep(2)

            # --- BeautifulSoup parsing starts here ---
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            
            # Find all article containers on the page
            articles_on_page = soup.find_all('div', class_='restly-blog-post-item restly-blog-one')
            
            # If no articles are found, we've reached the end
            if not articles_on_page:
                print("No more articles found. Reached the end.")
                break

            # Extract title and link from each article on the current page
            for article_element in articles_on_page:
                title_element = article_element.find('div', class_='restly-blog-post-title')
                if title_element and title_element.a:
                    title = title_element.a.text.strip()
                    link = title_element.a['href']
                    all_articles.append({
                        'title': title,
                        'url': link
                    })
            
            
            print(f"\nScraping news listing complete. Found {len(all_articles)} articles in total.")
        
            # Now, iterate through collected articles to visit each link and extract full content
            print("\nStarting to scrape full content for each article...")
            for article_data in all_articles:
                print(f"Visiting article: {article_data['url']}")
                driver.get(article_data['url'])
                time.sleep(2) # Give it time to load the article page
                
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                
                content_element = soup.find('div', class_='all-posts-wrapper')
                article_full_content_parts = []

                if content_element:
                    # Extract author from the article page
                    author_element = content_element.find('span', class_='author vcard')
                    article_author = author_element.a.text.strip() if author_element and author_element.a else "N/A"
                    
                    # Extract date from the article page (if different from listing page, or for consistency)
                    date_element = content_element.find('time', class_='entry-date')
                    article_date_text_from_page = date_element.text.strip() if date_element else "N/A"

                    for tag in content_element.find_all(['h2', 'h3', 'p']):
                        if tag.name in ['h2', 'h3']:
                            # For headings, check for a strong tag inside (as seen in your HTML example)
                            strong_tag = tag.find('strong')
                            if strong_tag:
                                article_full_content_parts.append(strong_tag.text.strip())
                            else:
                                article_full_content_parts.append(tag.text.strip())
                        elif tag.name == 'p':
                            article_full_content_parts.append(tag.text.strip())
                    
                    # Join all parts with a newline for the full content
                    article_full_text = "\n".join(article_full_content_parts)
                    
                    # Update the dictionary for the current article with new extracted data
                    article_data['author'] = article_author
                    article_data['date'] = article_date_text_from_page
                    article_data['content'] = article_full_text

                else:
                    # If content_element is not found, set values to N/A
                    article_data['author'] = "N/A"
                    article_data['date'] = "N/A"
                    article_data['content'] = "Content not found."

            # --- Save to JSON ---
            if all_articles:
                # Adjust keys to match the desired JSON output
                for article in all_articles:
                    article['error'] = False if article.get('content') != "Content not found." else True

                output_file = 'caioconnect_articles.json'
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(all_articles, f, ensure_ascii=False, indent=4)

            if(page_number == total_pages):
                break
            
            page_number += 1
            
        print(f"Scraping complete.Saved {len(all_articles)} articles to {output_file}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Ensure the browser is closed to free up resources
        if 'driver' in locals() and driver:
            print("Closing browser.")
            driver.quit()

if __name__ == '__main__':
    total_pages = 3
    scrape_caioconnect_news(total_pages)