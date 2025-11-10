#!/usr/bin/env python3
"""
Quick demo script for the Inspiration Scraper
Run this for a quick demo without the interactive menu
"""

from inspiration_scraper import InspirationScraper


def main():
    print("\n" + "🌟"*30)
    print("     DAILY INSPIRATION SCRAPER - QUICK DEMO")
    print("🌟"*30 + "\n")

    # Create scraper instance
    scraper = InspirationScraper()

    # Option 1: Scrape everything
    print("Option 1: Scraping all content...\n")
    data = scraper.scrape_all()

    # Display beautiful summary
    scraper.display_summary()

    # Option 2: Save to JSON
    print("\n💾 Saving data to JSON file...")
    scraper.save_to_json('inspiration_demo.json')

    # Option 3: Demonstrate search features
    print("\n🔍 Demonstrating search features...")

    if scraper.data['quotes']:
        # Show all authors
        authors = set(q['author'] for q in scraper.data['quotes'])
        print(f"\n📚 Authors found: {', '.join(authors)}")

        # Show all tags
        all_tags = set()
        for quote in scraper.data['quotes']:
            all_tags.update(quote['tags'])
        print(f"🏷️  Tags found: {', '.join(all_tags)}")

    # Display all content (optional)
    print("\n" + "="*60)
    print("                 ALL COLLECTED CONTENT")
    print("="*60)

    print("\n📝 ALL QUOTES:")
    for i, quote in enumerate(scraper.data['quotes'], 1):
        print(f"\n{i}. {quote['text']}")
        print(f"   — {quote['author']} ({', '.join(quote['tags'])})")

    print("\n\n😂 ALL JOKES:")
    for i, joke in enumerate(scraper.data['jokes'], 1):
        print(f"\n{i}. {joke['setup']}")
        print(f"   → {joke['punchline']} [{joke['type']}]")

    print("\n\n🧠 ALL FACTS:")
    for i, fact in enumerate(scraper.data['facts'], 1):
        print(f"\n{i}. 📚 {fact['title']}")
        print(f"   {fact['extract'][:150]}...")
        print(f"   🔗 {fact['url']}")

    if scraper.data.get('reddit_posts'):
        print("\n\n🌐 ALL REDDIT POSTS:")
        for i, post in enumerate(scraper.data['reddit_posts'], 1):
            print(f"\n{i}. {post['title']}")
            print(f"   👤 u/{post['author']} | ⬆️ {post['score']} points")
            print(f"   🔗 {post['url']}")

    print("\n\n" + "="*60)
    print("✨ Demo complete! Check 'inspiration_demo.json' for the data.")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
