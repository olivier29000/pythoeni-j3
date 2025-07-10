from serpapi import GoogleSearch

params = {
    "engine": "google",
    "q": "site:allrecipes.com inurl:/recipe/",
    "num": "100",
    "api_key": "API_KEY"
}

search = GoogleSearch(params)
results = search.get_dict()
urls = [res['link'] for res in results['organic_results']]

print(urls)