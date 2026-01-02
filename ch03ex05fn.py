def fetch_and_save_news(query:str ="AI") -> None:
    import requests
    import pandas as pd
    from datetime import datetime 
    
    url = "https://hn.algolia.com/api/v1/search"
    params =  {
        "query": query,
        "tags" : "story"
    }
    
    response = requests.get(url, params = params, timeout = 10)
    response.raise_for_status()
    
    data = response.json()
    articles = data["hits"]
    
    raws = []
    collected_at = datetime.now()
    
    for article in articles:
        raws.append({
            "title": article.get("title"),
            "author":article.get("author"),
            "date": article.get("created_at"),
            "url": article.get("url"),
            "collected_at": collected_at
        })
    df = pd.DataFrame(raws)
    
    today = collected_at.strftime("%Y-%m-%d")
    df.to_csv(f"news_{today}.csv", index=False, encoding="utf-8-sig")
    
fetch_and_save_news()    