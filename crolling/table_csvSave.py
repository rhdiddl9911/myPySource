import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 특정 사이트로부터 테이블을 읽어서 csv 로 저장하는 에쩨
html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html, "html.parser")

table = bsObj.findAll("table", {"class":"wikitable"})[0]
rows = table.findAll("tr")

csvFile = open("./csvFiles/editors.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()