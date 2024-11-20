import plotly.express as px

results = ["결과1", "결과2", "결과3", "결과4", "결과5"]  # x축의 데이터 설정
answers = [100, 101, 150, 30, 70]  # y축의 데이터 설정
# x축에 대입되는 answers는 서로 같은 길이여야함!

fig = px.bar(x=results, y=answers)  # 차트 생성

fig.show()  # 차트 확인



a = ["나와 같은 결과"]
b = [105]

fig2 = px.bar(x = a, y = s)
fig2.show()

# 1 answers -> 같은 결과값 찾아서
# x = "1번 문제 선택"
# y = 쿼리 날리는 로직 -> 어떻게 할까?

# answer, question, choices join