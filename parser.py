import requests
from bs4 import BeautifulSoup

# HTTP GET Request
req = requests.get('https://juunone.github.io/tags/')

# HTML 소스 가져오기
html = req.text

# BeautifulSoup으로 html소스를 python객체로 변환하기
# 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
# 이 글에서는 Python 내장 html.parser를 이용했다.
soup = BeautifulSoup(html, 'html.parser')

post = soup.find(id="post")
titles = post.find_all(class_="tag-title")

for title in titles:
    title = title.get_text()
    print(title, end='')
    name = ' name::' + title
    print(name)

# HTTP Header 가져오기
# header = req.headers

# HTTP Status 가져오기 (200: 정상)
# status = req.status_code

# HTTP 가 정상적으로 되었는지 (True/False)
# is_ok = req.ok