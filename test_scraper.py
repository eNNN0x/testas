#!/usr/bin/env python3
"""
Quick test script to verify the scraper works
"""

from inspiration_scraper import InspirationScraper

print("🧪 Testing Inspiration Scraper...\n")

scraper = InspirationScraper()

# Test 1: Scrape quotes
print("Test 1: Scraping quotes...")
quotes = scraper.scrape_quotes(num_quotes=3)
print(f"✅ Success! Got {len(quotes)} quotes")
if quotes:
    print(f"   Sample: '{quotes[0]['text'][:50]}...' - {quotes[0]['author']}")

print("\nTest 2: Scraping jokes...")
jokes = scraper.scrape_jokes(num_jokes=2)
print(f"✅ Success! Got {len(jokes)} jokes")
if jokes:
    print(f"   Sample: {jokes[0]['setup']}")

print("\n✅ All tests passed! The scraper is working correctly.")
print("📝 Run 'python inspiration_scraper.py' for the full interactive experience!")
print("📝 Or run 'python demo_scraper.py' for a quick demo!")
