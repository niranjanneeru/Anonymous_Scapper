from bs4 import BeautifulSoup

from requests_html import HTMLSession

u = "190983"
p = "Niranjan_202"

login_cred = {
    "LoginForm[username]": u,
    "LoginForm[password]": p,
}
session = HTMLSession()

url = "https://tkmce.etlab.in/user/login"
r = session.post(url, data=login_cred).text

# print(r)


# soup = BeautifulSoup('<td><a href="/student/viewassignment/127">LAB 1</a></td>', "html.parser")
# print(soup.find_all('td')[0].attr)
