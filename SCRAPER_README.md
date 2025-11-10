# 🌟 Daily Inspiration Scraper

A fun and interactive Python web scraper that collects inspirational quotes, jokes, interesting facts, and trending Reddit posts!

## ✨ Features

- **📝 Quote Scraping**: Collects inspirational quotes from quotes.toscrape.com
- **😂 Joke Collection**: Fetches random jokes from the Official Joke API
- **🧠 Interesting Facts**: Discovers fascinating topics from Wikipedia
- **🌐 Reddit Integration**: Scrapes trending posts from subreddits
- **💾 JSON Export**: Save all scraped data to JSON files
- **🔍 Search Features**: Search quotes by author or tags
- **📊 Statistics**: Track your scraping activity
- **🎨 Beautiful UI**: Colorful and interactive terminal interface

## 🚀 Quick Start

### Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

### Run the Scraper

```bash
# Interactive mode with menu
python inspiration_scraper.py

# Or import as a module
python
>>> from inspiration_scraper import InspirationScraper
>>> scraper = InspirationScraper()
>>> data = scraper.scrape_all()
>>> scraper.display_summary()
```

## 📋 Menu Options

1. **Scrape All Content** - Collect quotes, jokes, facts, and Reddit posts
2. **Scrape Only Quotes** - Get inspirational quotes
3. **Scrape Only Jokes** - Fetch funny jokes
4. **Scrape Only Facts** - Discover interesting facts
5. **Scrape Reddit** - Get trending posts from r/todayilearned
6. **Display Summary** - Show a beautiful summary of collected content
7. **Save to JSON** - Export data to a JSON file
8. **Search Quotes by Author** - Find quotes by specific authors
9. **Get Quotes by Tag** - Filter quotes by tags
0. **Exit** - Close the application

## 🎯 Usage Examples

### Example 1: Scrape Everything

```python
from inspiration_scraper import InspirationScraper

scraper = InspirationScraper()
data = scraper.scrape_all()
scraper.display_summary()
scraper.save_to_json('my_inspiration.json')
```

### Example 2: Get Specific Content

```python
from inspiration_scraper import InspirationScraper

scraper = InspirationScraper()

# Get 10 quotes
quotes = scraper.scrape_quotes(num_quotes=10)

# Get 5 jokes
jokes = scraper.scrape_jokes(num_jokes=5)

# Search for Einstein quotes
einstein_quotes = scraper.search_quotes_by_author('Einstein')
```

### Example 3: Scrape Different Subreddits

```python
from inspiration_scraper import InspirationScraper

scraper = InspirationScraper()

# Scrape different subreddits
til_posts = scraper.scrape_reddit_posts('todayilearned', limit=10)
shower_thoughts = scraper.scrape_reddit_posts('Showerthoughts', limit=5)
```

## 🛠️ Technical Details

### Data Sources

- **Quotes**: http://quotes.toscrape.com/
- **Jokes**: Official Joke API (https://official-joke-api.appspot.com)
- **Facts**: Wikipedia Random Article API
- **Reddit**: Reddit JSON API (no authentication required)

### Data Structure

```json
{
  "timestamp": "2025-11-10T...",
  "quotes": [
    {
      "text": "Quote text",
      "author": "Author name",
      "tags": ["tag1", "tag2"]
    }
  ],
  "jokes": [
    {
      "setup": "Setup line",
      "punchline": "Punchline",
      "type": "general"
    }
  ],
  "facts": [
    {
      "title": "Article title",
      "extract": "Summary text",
      "url": "Wikipedia URL"
    }
  ],
  "reddit_posts": [
    {
      "title": "Post title",
      "author": "Username",
      "score": 1234,
      "url": "Reddit URL",
      "subreddit": "todayilearned"
    }
  ],
  "stats": {
    "total_quotes": 5,
    "total_jokes": 3,
    "total_facts": 5,
    "total_reddit_posts": 5,
    "scrape_time": "2025-11-10T..."
  }
}
```

## 🤝 Features Explained

### Polite Scraping
- Implements delays between requests (0.5-1 second)
- Uses proper User-Agent headers
- Respects API rate limits
- Handles errors gracefully

### Error Handling
- Catches network errors
- Provides clear error messages
- Continues execution even if one source fails

### Extensibility
- Easy to add new data sources
- Modular design
- Well-documented code

## 📝 Notes

- The scraper is educational and for personal use
- All sources used are publicly available
- Be respectful of rate limits and terms of service
- Some content may require internet connection

## 🎉 Have Fun!

This scraper is designed to brighten your day with inspirational quotes, make you laugh with jokes, and teach you something new with interesting facts. Enjoy!
