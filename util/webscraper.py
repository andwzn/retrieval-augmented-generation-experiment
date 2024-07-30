import pandas as pd
import requests
from bs4 import BeautifulSoup
import re 
import tldextract
import numpy as np
from typing import List, Optional

class WebScraper:
    def __init__(self, tags: List[str], exclude: List[str]):
        """
        Initializes the WebScraper with tags to extract and domains to exclude.
        
        Args:
            tags (List[str]): A list of HTML tags to extract text from.
            exclude (List[str]): A list of domains to exclude.
        """
        self.tags = tags
        self.exclude = exclude
        self.pattern = r'\s+'
        
    def scrape(self, webpages: str) -> Optional[str]:
        """
        Scrapes the content of webpages and returns a concatenated string of cleaned texts.
        
        Args:
            webpages (str): A comma-separated string of URLs representing the webpages to scrape.
            
        Returns:
            Optional[str]: A concatenated string of cleaned texts extracted from the webpages, or None if no valid URLs.
        """
        
        if pd.isna(webpages) or not webpages:
            return np.nan
        
        webpages_content = []
        urls = webpages.split(",")
        
        for url in urls:
            if tldextract.extract(url).domain in self.exclude:
                continue
            
            try:
                print(f"Scraping {url} with parameters tags = {self.tags}")
                response = requests.get(url)
                response.raise_for_status()
            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred for {url}: {http_err}")
                continue
            except requests.exceptions.Timeout:
                print(f"Timeout occurred for {url}.")
                continue
            except requests.exceptions.RequestException as req_err:
                print(f"Request exception occurred for {url}: {req_err}")
                continue
            
            parser = BeautifulSoup(response.content, "html.parser")        

            texts = []

            for tag in self.tags:
                for element in parser.find_all(tag):
                    text = re.sub(self.pattern, ' ', element.get_text(strip=True))
                    texts.append(text)
            
            webpages_content.append(' '.join(texts))
        return ', '.join(webpages_content)
