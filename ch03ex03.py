import matplotlib.pyplot as plt
import matplotlib.font_manager as fm 
import pandas as pd

#============== 한글 깨질 때 ================
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
#===========================================

# 기사 반응 데이터 예시
df = pd.DataFrame({
    "views": [120, 340, 560, 430, 290],
    "comments": [5, 18, 42, 30, 12]
})

# plot 챠트 사용 시 정렬 필수
df_sorted = df.sort_values("views")

# 산점도 작성
# plt.scatter(df["views"], df["comments"])
# plot챠트와 marker 사용
plt.plot(df_sorted["views"], df_sorted["comments"], marker="o")

# 그래프 정보 설정
plt.title("조회 수와 댓글 수의 관계")
plt.xlabel("조회 수")
plt.ylabel("댓글 수")

# 그래프 출력
plt.show()
