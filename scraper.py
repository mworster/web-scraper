import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def scrape_hackernews():
    url = 'https://news.ycombinator.com/'
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve page: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    title_spans = soup.find_all('span', class_='titleline')

    stories = []
    for span in title_spans:
        link = span.find('a')
        if link:
            stories.append({
                'title': link.get_text(),
                'url': link['href']
            })

    if not stories:
        print("No stories found.")
        return

    # Print results to console
    for i, story in enumerate(stories, 1):
        print(f"{i}. {story['title']}\n   {story['url']}\n")

    # Save to JSON file
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'results_{timestamp}.json'

    with open(filename, 'w') as f:
        json.dump(stories, f, indent=2)

    print(f"\n✅ Scraped {len(stories)} stories. Results saved to {filename}")

if __name__ == '__main__':
    scrape_hackernews()
