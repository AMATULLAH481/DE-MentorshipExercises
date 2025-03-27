import requests
import json
import pandas as pd

#Exploring the data first
# API_key = "45232e57-5335-4065-b4fd-1b11a1ca8ff8"
# url = f"https://content.guardianapis.com/search?q=Nigeria&from-date=2025-01-01&to-date=2025-12-31&api-key={API_key}"
# response = requests.get(url)
# response.status_code
# data = response.json()
# data["response"]["results"] #printing out our focus data

def fetch_Nigerian_articles(API_key):
    all_articles = []
    all_articles_list = []

    for page in range(1, 11):  # There are 10 pages in the response
        url = f"https://content.guardianapis.com/search?q=Nigeria&from-date=2025-01-01&to-date=2025-12-31&api-key={API_key}&page={page}&page-size=10"
        response = requests.get(url)
        data = response.json()
        articles = data["response"]["results"]
        
        if not articles:
            break  # Stop if no more results

        all_articles.extend(articles) #not using append because that is not allowing me to loop through each article

    #Getting our focus data for each article
    for article in all_articles:
        all_articles_list.append({
            'Title': article['webTitle'],
            'URL': article['webUrl']
        })

    # Convert to DataFrame and export to CSV
    df = pd.DataFrame(all_articles_list)
    df.to_csv('articles.csv', index=False)
    print("Data successfully exported to 'articles.csv'")

API_key = "45232e57-5335-4065-b4fd-1b11a1ca8ff8"
fetch_Nigerian_articles(API_key)
