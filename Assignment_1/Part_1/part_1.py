import urllib.request
from urllib.parse import quote
from bs4 import BeautifulSoup
import re
import time

import sys


def printProgress(iteration, total, prefix='', suffix='', decimals=1, barLength=100):
    formatStr = "{0:." + str(decimals) + "f}"
    percent = formatStr.format(100 * (iteration / float(total)))
    filledLength = int(barLength * iteration / float(total))
    bar = '#' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)),
    if iteration > total:
        sys.stdout.write("\n")
        sys.stdout.flush()


def cleaning_contents(contents):
    contents = re.sub('\/\/.*\n.*\{\}\n*', '', contents)
    return contents.strip()
    # 기사의 본문 이외의 내용을 모두 지움.
    # strip()을 통해 앞뒤의 공백을 지우는 함수이다.


# [Q1]  링크 수집 ---------------------------------------------------------------------------------------------------
print("[문제 1번]")
# [Q1 - 1]  URL 열기
key_words = urllib.parse.quote("금리")
url = "https://search.naver.com/search.naver?where=news&query=" + key_words + "&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=2019.10.13&de=2019.10.14"
req = urllib.request.urlopen(url)
print("\tOpened an URL Successfully!")

# [Q1 - 2]  read() 메소드 사용
data = req.read().decode('utf8')
# [Q1 - 3]  BeautifulSoup 객체 생성
soup = BeautifulSoup(data, 'html.parser')
# [Q1 - 4]  findAll() 메소드 사용 및 특정 태그 수집
anchor_set = soup.findAll('a')
# [Q1 - 5]  링크 주소 저장을 위한 리스트 생성
news_link = []
# [Q1 - 6]  리스트에 링크 주소 넣기
print("\tGetting articles' links...")
for x in range(len(anchor_set)):
    if re.search('^https://news.naver.com/main/read.nhn', anchor_set[x]['href']):
        news_link.append(anchor_set[x]['href'])
print("\tArticles' links were completely collected!")

# [Q2]  특정 검색어가 포함된 기사 찾기 ------------------------------------------------------------------------------
print("\n[문제 2번]")
# 뉴스 검색과 연관된 총 기사 수 구하기
count_tag = soup.find("div", {"class", "title_desc all_my"})
count_text = count_tag.find("span").get_text().split()
total_num = count_text[-1][0:-1].replace(",", "")
print("\t%d articles were found." % int(total_num))

print("\tCollecting URLs of articles...\n\tPLEASE WAIT UNTIL THE END>>>")
for val in range(int(total_num) // 10):
    start_val = 10 * val + 1
    if val == 1:
        url2 = "https://search.naver.com/search.naver?where=news&query=" + key_words + "&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=2019.10.13&de=2019.10.14&docid=&nso=so:r,p:from20191013to20191014,a:all&mynews=0&cluster_rank=26&start=0" + str(
            start_val) + "&refresh_start=0"
    else:
        url2 = "https://search.naver.com/search.naver?where=news&query=" + key_words + "&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=2019.10.13&de=2019.10.14&docid=&nso=so:r,p:from20191013to20191014,a:all&mynews=0&cluster_rank=26&start=" + str(
            start_val) + "&refresh_start=0"
    req2 = urllib.request.urlopen(url2)

    data2 = req2.read().decode('utf8')
    soup2 = BeautifulSoup(data2, 'html.parser')
    anchor_set2 = soup2.findAll('a')

    for x in range(len(anchor_set2)):
        if re.search('^https://news.naver.com/main/read.nhn', anchor_set2[x]['href']):
            news_link.append(anchor_set2[x]['href'])
    printProgress(val, int(total_num) // 10, prefix='START', suffix='END', decimals=1, barLength=100)
print("\n\tCompleted!")

# [Q3]  뉴스 제목과 본문 수집하기 -----------------------------------------------------------------------------------
print("\n[문제 3번]")
# 중복된 기사 제거
news_link = list(set(news_link))
title_list = []  # 뉴스 제목
text_list = []  # 뉴스 본문 내용

print("\tCollecting titles and texts of articles...\n\tPLEASE WAIT UNTIL THE END>>>")
for article in range(len(news_link)):
    news = urllib.request.urlopen(news_link[article])
    soup_news = BeautifulSoup(news, 'html.parser')
    title_list.append(soup_news.find("h3", {"id": "articleTitle"}).get_text())

    contents = soup_news.find("div", {"id": "articleBodyContents"}).get_text()
    contents = cleaning_contents(contents)
    text_list.append(contents)
    printProgress(article, len(news_link), prefix='START', suffix='END', decimals=1, barLength=100)

print("\n\tCompleted!")

# [Q4]  정규표현식을 통한 뉴스 제목 출력 ----------------------------------------------------------------------------
print("\n[문제 4번]")

print("\tTitles of articles which inclues \"금리\" and \"인하\"\n")
a=1
for title in range(len(title_list)):
    if re.search('.*금리.*인하.*', title_list[title]):
        print("\t%2d]   %s" % (a, title_list[title]))
        a+=1
