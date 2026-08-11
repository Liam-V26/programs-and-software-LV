# This code is used to scrape any useful info in a website.
# Creator: Liam Viljoen

import requests
from bs4 import BeautifulSoup
import re
import sys
import csv
import pandas as pd
import json
import os

def main():
    url = "https://quotes.toscrape.com"

    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code == 200:
            print("Request successful!")

            # target folder
            target_folder = r"C:\Users\liamv\Desktop\Desktop\MyPython projects\Web Scraper"
            os.makedirs(target_folder, exist_ok=True)

            # Save raw HTML
            raw_path = os.path.join(target_folder, "raw.html")
            with open(raw_path, "w", encoding="utf-8") as file:
                file.write(response.text)

            # Parse HTML
            soup = BeautifulSoup(response.text, "html.parser")
            quotes = soup.find_all("div", class_="quote")
            print(f"Found {len(quotes)} quotes")

            extracted_data = []
            for quote in quotes:
                text = quote.find("span", class_="text").get_text(strip=True)
                author = quote.find("small", class_="author").get_text(strip=True)
                tags = [tag.get_text(strip=True) for tag in quote.find_all("a", class_="tag")]

                clean_text = re.sub(r"[^\w\s.,!?]", "", text)
                clean_author = re.sub(r"[^a-zA-Z\s]", "", author)

                extracted_data.append({
                    "quote": clean_text,
                    "author": clean_author,
                    "tags": ", ".join(tags)
                })

            # Save to CSV
            csv_path = os.path.join(target_folder, "output.csv")
            with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=["quote", "author", "tags"])
                writer.writeheader()
                writer.writerows(extracted_data)

            print(f"Data successfully saved to {csv_path}")

            # Save to JSON
            json_path = os.path.join(target_folder, "output.json")
            with open(json_path, "w", encoding="utf-8") as jsonfile:
                json.dump(extracted_data, jsonfile, ensure_ascii=False, indent=4)

            print(f"Data successfully saved to {json_path}")

            # Summary 
            df = pd.read_csv(csv_path)
            print("\n--- Quick Analysis ---")
            print("Total quotes scraped:", len(df))
            print("\nTop 5 Authors:")
            print(df['author'].value_counts().head())
            print("\nMost Common Tags:")
            all_tags = df['tags'].str.split(", ").explode()
            print(all_tags.value_counts().head())
            print("\nUnique Authors:", df['author'].nunique())
            print("Average number of tags per quote:", df['tags'].str.count(",").mean() + 1)

        else:
            print(f"Error: Received status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()


