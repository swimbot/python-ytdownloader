from pytube import YouTube

link = input("유튜브 영상 링크 : ")
print("기다려주세요")
try:
    yt = YouTube(link)
except Exception as e:
	print("영상을 찾을수 없습니다")
	exit()
path = input("저장 경로 : ")

print("제목 : ",yt.title)
print("길이 : ",yt.length)
print("조회수 : ",yt.views)
print("평점 : ",yt.rating)

yh = yt.streams.get_highest_resolution()

print("다운중~...")
yh.download(path)
print("다운완료!")
