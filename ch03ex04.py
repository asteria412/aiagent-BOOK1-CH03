# API 데이터 자동 수집 파이프라인 실습
# API 요청 및 응답 확인(1단계)

import requests
import pandas as pd
from datetime import datetime

url = "https://hn.algolia.com/api/v1/search"
params = {
    "query": "AI",
    "tags": "story"
}

response = requests.get(url, params=params)

#print(response.status_code)
#print(response.json().keys())

# JSON 데이터에서 필요한 항목 추출(2단계)
data = response.json()
articles = data["hits"]

for article in articles:
    title = article.get("title")
    created_at = article.get("created_at")
    #print(title, created_at)

# 구조화된 데이터 리스트 생성(3단계)
structured_data =[]

for article in articles:
    structured_data.append({
        "title": article.get("title"),
        "author": article.get("author"),
        "date": article.get("created_at"),
        "url":article.get("url")
    })
    
# pandas 데이터프레임으로 변환(4단계)  
df = pd.DataFrame(structured_data)
#print(df.head())

# 수집 시점 정보 추가하기(5단계)
df["collected_at"] = datetime.now()
#print(df.head())

#  CSV 파일로 저장하기(6단계)
today = datetime.now().strftime("%Y-%m-%d")
df.to_csv(f"news_{today}.csv", index=False, encoding="utf-8-sig")
print("데이터 수집 및 저장 완료")


  