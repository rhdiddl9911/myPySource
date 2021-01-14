from bs4 import BeautifulSoup
from urllib.request import urlopen
import codecs, csv

def moviewReviewScrap(code, pageNum):
    url = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=" + code + "&page=" + str(pageNum)
    html = urlopen(url)
    bsObj = BeautifulSoup(html, "html.parser")

    reviews = bsObj.find("div", class_='score_result').find_all("li")

    for review in reviews:
        with codecs.open("movie_review_" + code + ".csv", "a", "euc_kr") as fp:
            writer = csv.writer(fp, delimiter=",", quotechar='"')
            writer.writerow([
                review.find('em').text,
                review.find("div", {"class": "score_reple"}).find("p").text.strip().replace("\t", "").replace("\n", ""),
                int(review.find_all("strong")[0].text),
                int(review.find_all("strong")[1].text)
            ])

code = '163834'
with codecs.open("movie_review_" + code + ".csv", "w", "euc_kr") as fp:
    writer = csv.writer(fp, delimiter=",", quotechar='"')
    writer.writerow(["평점", "리뷰", "공감수", "비공감수"])

for i in range(1, 11):
    moviewReviewScrap(code, i)