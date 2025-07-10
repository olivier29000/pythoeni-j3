from serpapi import GoogleSearch

params = {
    "engine": "google",
    "q": "site:marmiton.org inurl:/recettes/",  # ou adapter selon le site ciblé
    "num": "100",
    "api_key": "1b3cf884f408804a49aedc73fc62e50b3885b8d93164e7feb5c4836cb1e8f17b"
}

search = GoogleSearch(params)
results = search.get_dict()

# Vérifie d'abord que 'organic_results' existe
if 'organic_results' in results:
    urls = [
        res['link']
        for res in results['organic_results']
        if res.get('link', '').endswith('.aspx')
    ]
    print("URLs .aspx trouvées :")
    for url in urls:
        print(url)
    print(urls)
else:
    print("Aucun résultat organique trouvé.")
    if 'error' in results:
        print("Erreur retournée :", results['error'])