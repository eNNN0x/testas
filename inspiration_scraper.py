#!/usr/bin/env python3
"""
🌟 Daily Inspiration Scraper 🌟
A fun web scraper that collects quotes, jokes, facts, and more!
"""

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from typing import Dict, List, Optional
import random
import time


class InspirationScraper:
    """A fun web scraper for collecting inspirational and entertaining content."""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.data = {
            'timestamp': datetime.now().isoformat(),
            'quotes': [],
            'jokes': [],
            'facts': [],
            'stats': {}
        }

        # Fallback data in case APIs are unavailable
        self.fallback_quotes = [
            {
                'text': '"The only way to do great work is to love what you do."',
                'author': 'Steve Jobs',
                'tags': ['inspiration', 'work', 'passion']
            },
            {
                'text': '"Innovation distinguishes between a leader and a follower."',
                'author': 'Steve Jobs',
                'tags': ['innovation', 'leadership']
            },
            {
                'text': '"Life is what happens when you\'re busy making other plans."',
                'author': 'John Lennon',
                'tags': ['life', 'planning']
            },
            {
                'text': '"The future belongs to those who believe in the beauty of their dreams."',
                'author': 'Eleanor Roosevelt',
                'tags': ['future', 'dreams', 'inspiration']
            },
            {
                'text': '"It is during our darkest moments that we must focus to see the light."',
                'author': 'Aristotle',
                'tags': ['inspirational', 'hope']
            }
        ]

        self.fallback_jokes = [
            {
                'setup': 'Why do programmers prefer dark mode?',
                'punchline': 'Because light attracts bugs!',
                'type': 'programming'
            },
            {
                'setup': 'Why did the scarecrow win an award?',
                'punchline': 'Because he was outstanding in his field!',
                'type': 'general'
            },
            {
                'setup': 'What do you call a bear with no teeth?',
                'punchline': 'A gummy bear!',
                'type': 'general'
            }
        ]

        self.fallback_facts = [
            {
                'title': 'Python Programming Language',
                'extract': 'Python was created by Guido van Rossum and first released in 1991. It emphasizes code readability and simplicity, making it one of the most popular programming languages today.',
                'url': 'https://en.wikipedia.org/wiki/Python_(programming_language)'
            },
            {
                'title': 'Web Scraping',
                'extract': 'Web scraping is the process of extracting data from websites. It involves fetching a web page and extracting useful information from it, often for analysis or data collection purposes.',
                'url': 'https://en.wikipedia.org/wiki/Web_scraping'
            },
            {
                'title': 'Beautiful Soup',
                'extract': 'Beautiful Soup is a Python library designed for web scraping purposes to pull data out of HTML and XML files. It creates parse trees that are helpful to extract data easily.',
                'url': 'https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)'
            }
        ]

    def scrape_quotes(self, num_quotes: int = 5) -> List[Dict]:
        """Scrape inspirational quotes from quotes.toscrape.com"""
        print("📝 Scraping quotes...")
        quotes = []

        try:
            url = "http://quotes.toscrape.com/"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            quote_divs = soup.find_all('div', class_='quote')

            for quote_div in quote_divs[:num_quotes]:
                text = quote_div.find('span', class_='text').get_text()
                author = quote_div.find('small', class_='author').get_text()
                tags = [tag.get_text() for tag in quote_div.find_all('a', class_='tag')]

                quotes.append({
                    'text': text,
                    'author': author,
                    'tags': tags
                })

            print(f"✅ Collected {len(quotes)} quotes from web!")

        except Exception as e:
            print(f"⚠️  Could not fetch quotes from web ({e})")
            print("📚 Using fallback quotes instead...")
            quotes = random.sample(self.fallback_quotes, min(num_quotes, len(self.fallback_quotes)))
            print(f"✅ Loaded {len(quotes)} quotes from fallback data!")

        return quotes

    def scrape_jokes(self, num_jokes: int = 3) -> List[Dict]:
        """Scrape jokes from various joke APIs"""
        print("😂 Fetching jokes...")
        jokes = []

        try:
            # Using Official Joke API (free, no auth required)
            url = f"https://official-joke-api.appspot.com/random_joke"

            for _ in range(num_jokes):
                response = self.session.get(url, timeout=10)
                response.raise_for_status()
                joke_data = response.json()

                jokes.append({
                    'setup': joke_data.get('setup', ''),
                    'punchline': joke_data.get('punchline', ''),
                    'type': joke_data.get('type', 'general')
                })
                time.sleep(0.5)  # Be nice to the API

            print(f"✅ Collected {len(jokes)} jokes from API!")

        except Exception as e:
            print(f"⚠️  Could not fetch jokes from API ({e})")
            print("🎭 Using fallback jokes instead...")
            jokes = random.sample(self.fallback_jokes, min(num_jokes, len(self.fallback_jokes)))
            print(f"✅ Loaded {len(jokes)} jokes from fallback data!")

        return jokes

    def scrape_facts(self, num_facts: int = 5) -> List[Dict]:
        """Scrape random facts"""
        print("🧠 Gathering interesting facts...")
        facts = []

        try:
            # Using Wikipedia's Random Article feature for interesting topics
            for _ in range(num_facts):
                url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
                response = self.session.get(url, timeout=10)
                response.raise_for_status()
                data = response.json()

                facts.append({
                    'title': data.get('title', ''),
                    'extract': data.get('extract', ''),
                    'url': data.get('content_urls', {}).get('desktop', {}).get('page', '')
                })
                time.sleep(0.5)  # Be nice to the API

            print(f"✅ Collected {len(facts)} interesting facts from Wikipedia!")

        except Exception as e:
            print(f"⚠️  Could not fetch facts from Wikipedia ({e})")
            print("📖 Using fallback facts instead...")
            facts = random.sample(self.fallback_facts, min(num_facts, len(self.fallback_facts)))
            print(f"✅ Loaded {len(facts)} facts from fallback data!")

        return facts

    def scrape_reddit_posts(self, subreddit: str = 'todayilearned', limit: int = 5) -> List[Dict]:
        """Scrape top posts from a subreddit (using JSON API)"""
        print(f"🌐 Scraping r/{subreddit}...")
        posts = []

        try:
            url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            for post in data['data']['children']:
                post_data = post['data']
                posts.append({
                    'title': post_data.get('title', ''),
                    'author': post_data.get('author', ''),
                    'score': post_data.get('score', 0),
                    'url': f"https://reddit.com{post_data.get('permalink', '')}",
                    'subreddit': subreddit
                })

            print(f"✅ Collected {len(posts)} posts from r/{subreddit}!")

        except Exception as e:
            print(f"❌ Error scraping Reddit: {e}")

        return posts

    def scrape_all(self):
        """Scrape all sources"""
        print("\n" + "="*60)
        print("🚀 Starting Daily Inspiration Scraper!")
        print("="*60 + "\n")

        self.data['quotes'] = self.scrape_quotes(num_quotes=5)
        time.sleep(1)

        self.data['jokes'] = self.scrape_jokes(num_jokes=3)
        time.sleep(1)

        self.data['facts'] = self.scrape_facts(num_facts=5)
        time.sleep(1)

        self.data['reddit_posts'] = self.scrape_reddit_posts(subreddit='todayilearned', limit=5)

        # Calculate stats
        self.data['stats'] = {
            'total_quotes': len(self.data['quotes']),
            'total_jokes': len(self.data['jokes']),
            'total_facts': len(self.data['facts']),
            'total_reddit_posts': len(self.data.get('reddit_posts', [])),
            'scrape_time': datetime.now().isoformat()
        }

        print("\n" + "="*60)
        print("✨ Scraping complete!")
        print("="*60)

        return self.data

    def display_summary(self):
        """Display a beautiful summary of scraped content"""
        print("\n" + "🎨 " + "="*58)
        print("                    CONTENT SUMMARY")
        print("="*60 + "\n")

        # Display random quote
        if self.data['quotes']:
            quote = random.choice(self.data['quotes'])
            print("💬 RANDOM QUOTE:")
            print(f"   {quote['text']}")
            print(f"   — {quote['author']}")
            print(f"   Tags: {', '.join(quote['tags'])}\n")

        # Display random joke
        if self.data['jokes']:
            joke = random.choice(self.data['jokes'])
            print("😄 RANDOM JOKE:")
            print(f"   {joke['setup']}")
            print(f"   → {joke['punchline']}\n")

        # Display random fact
        if self.data['facts']:
            fact = random.choice(self.data['facts'])
            print("🧠 RANDOM FACT:")
            print(f"   📚 {fact['title']}")
            print(f"   {fact['extract'][:200]}...")
            print(f"   🔗 {fact['url']}\n")

        # Display Reddit post
        if self.data.get('reddit_posts'):
            post = random.choice(self.data['reddit_posts'])
            print("🌐 TRENDING ON REDDIT:")
            print(f"   {post['title']}")
            print(f"   👤 by u/{post['author']} | ⬆️ {post['score']} points")
            print(f"   🔗 {post['url']}\n")

        # Display stats
        print("📊 STATISTICS:")
        for key, value in self.data['stats'].items():
            if key != 'scrape_time':
                print(f"   {key.replace('_', ' ').title()}: {value}")

        print("\n" + "="*60 + "\n")

    def save_to_json(self, filename: str = 'scraped_data.json'):
        """Save scraped data to JSON file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
            print(f"💾 Data saved to {filename}")
        except Exception as e:
            print(f"❌ Error saving data: {e}")

    def search_quotes_by_author(self, author: str) -> List[Dict]:
        """Search for quotes by a specific author"""
        return [q for q in self.data['quotes'] if author.lower() in q['author'].lower()]

    def get_quotes_by_tag(self, tag: str) -> List[Dict]:
        """Get quotes with a specific tag"""
        return [q for q in self.data['quotes'] if tag.lower() in [t.lower() for t in q['tags']]]


def interactive_menu():
    """Interactive menu for the scraper"""
    scraper = InspirationScraper()

    while True:
        print("\n" + "🌟 "*20)
        print("   DAILY INSPIRATION SCRAPER - MAIN MENU")
        print("🌟 "*20)
        print("\n1. 🚀 Scrape All Content")
        print("2. 📝 Scrape Only Quotes")
        print("3. 😂 Scrape Only Jokes")
        print("4. 🧠 Scrape Only Facts")
        print("5. 🌐 Scrape Reddit (r/todayilearned)")
        print("6. 📊 Display Summary")
        print("7. 💾 Save to JSON")
        print("8. 🔍 Search Quotes by Author")
        print("9. 🏷️  Get Quotes by Tag")
        print("0. 👋 Exit")

        choice = input("\n👉 Enter your choice: ").strip()

        if choice == '1':
            scraper.scrape_all()
            scraper.display_summary()
        elif choice == '2':
            quotes = scraper.scrape_quotes()
            scraper.data['quotes'] = quotes
            for q in quotes:
                print(f"\n{q['text']}\n— {q['author']}")
        elif choice == '3':
            jokes = scraper.scrape_jokes()
            scraper.data['jokes'] = jokes
            for j in jokes:
                print(f"\n{j['setup']}\n→ {j['punchline']}")
        elif choice == '4':
            facts = scraper.scrape_facts()
            scraper.data['facts'] = facts
            for f in facts:
                print(f"\n📚 {f['title']}\n{f['extract'][:200]}...\n🔗 {f['url']}")
        elif choice == '5':
            posts = scraper.scrape_reddit_posts()
            scraper.data['reddit_posts'] = posts
            for p in posts:
                print(f"\n{p['title']}\n👤 u/{p['author']} | ⬆️ {p['score']}")
        elif choice == '6':
            if scraper.data['quotes'] or scraper.data['jokes'] or scraper.data['facts']:
                scraper.display_summary()
            else:
                print("\n⚠️  No data to display! Please scrape some content first.")
        elif choice == '7':
            filename = input("Enter filename (default: scraped_data.json): ").strip()
            scraper.save_to_json(filename if filename else 'scraped_data.json')
        elif choice == '8':
            author = input("Enter author name: ").strip()
            results = scraper.search_quotes_by_author(author)
            if results:
                print(f"\n✅ Found {len(results)} quotes by {author}:")
                for q in results:
                    print(f"\n{q['text']}\n— {q['author']}")
            else:
                print(f"\n❌ No quotes found for '{author}'")
        elif choice == '9':
            tag = input("Enter tag: ").strip()
            results = scraper.get_quotes_by_tag(tag)
            if results:
                print(f"\n✅ Found {len(results)} quotes with tag '{tag}':")
                for q in results:
                    print(f"\n{q['text']}\n— {q['author']}")
            else:
                print(f"\n❌ No quotes found with tag '{tag}'")
        elif choice == '0':
            print("\n👋 Thanks for using Daily Inspiration Scraper! Have a great day!")
            break
        else:
            print("\n❌ Invalid choice! Please try again.")


if __name__ == "__main__":
    # Run interactive menu
    interactive_menu()
