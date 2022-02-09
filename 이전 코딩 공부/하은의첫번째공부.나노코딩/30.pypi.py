from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())


#pip show beautifulsoup4 입력하면 beautifulsoup4 패키지에 대한 정보 확인.