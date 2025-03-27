# 영화 목록 정의
movie_list = [
    ("오징어게임2", 50.45),
    ("범죄도시4", 35.46),
    ("미키17", 9.80),
    ("파묘", 52.50),
    ("스파이더맨", 15.47)
]

# 리스트를 딕셔너리로 변환
movie_dict = {title: rate for title, rate in movie_list}

# 예매율에 따라 내림차순 정렬
sorted_movies = sorted(movie_dict.items(), key=lambda x: x[1], reverse=True)

# 출력 헤더
print("영화제목\t예매율\t\t순위")
print("========\t=====\t\t===")

# 영화 제목, 예매율, 순위 출력
for rank, (title, rate) in enumerate(sorted_movies, start=1):
    print("{:<10}\t{:>5}\t\t{:>2}".format(title, rate, rank))
