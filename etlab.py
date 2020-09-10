from bs4 import BeautifulSoup
from requests_html import HTMLSession


class Etlab:
    def __init__(self, user, pas):
        self.username = user
        self.password = pas
        self.login_cred = {
            "LoginForm[username]": user,
            "LoginForm[password]": pas
        }

    def login_and_fetch(self):
        self.session = HTMLSession()
        url = "https://tkmce.etlab.in/user/login"
        return self.session.post(url, data=self.login_cred).text
        p = self.session.get('https://tkmce.etlab.in/ktuacademics/student/viewattendancesubject/6')
        soup = BeautifulSoup(p.text, "html.parser")
        result = ""
        for tables in soup.find_all('table'):
            for table in tables:
                for rows in table:
                    for row in rows:
                        for c in row:
                            if c.strip() != "":
                                result += (c.strip())
                                result += "\n"
        if "Percentage" not in result:
            return "Invalid Credentials"
        return result

    def fetch_data(self, result):
        sub = [i for i in result[:result.find("Percentage") + 10].split("\n") if i.strip() != ""]
        value = [i for i in result[result.find("Percentage") + 10:].split("\n") if i.strip() != ""]
        data = dict()
        for i in range(len(sub)):
            data[sub[i]] = value[i]
        return data
