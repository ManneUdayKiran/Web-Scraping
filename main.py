import requests
from bs4 import BeautifulSoup
import csv

def scrape_github_trending():
    url = "https://github.com/trending"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    repo_list = soup.find_all('article', class_='Box-row')
    if not repo_list:
        print("Could not find repository list on the page. The structure may have changed.")
        return

    trending_repos = []

    for repo in repo_list[:5]:
        try:
            anchor = repo.h2.a
            repo_name = anchor.get_text(strip=True).replace('\n', '').replace(' ', '')
            repo_link = "https://github.com" + anchor['href']
            trending_repos.append((repo_name, repo_link))
        except AttributeError:
            print("Unexpected structure in repository card. Skipping.")
            continue

    if not trending_repos:
        print("No repositories found. Please check the page structure.")
        return

    # Save to CSV
    try:
        with open("trending_repos.csv", "w", newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Repository Name", "Link"])
            writer.writerows(trending_repos)
        print("✅ Successfully saved top 5 trending repositories to trending_repos.csv")
    except IOError as e:
        print(f"Error writing to CSV file: {e}")

if __name__ == "__main__":
    scrape_github_trending()
