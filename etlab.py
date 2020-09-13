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

    def login(self):
        self.session = HTMLSession()
        url = "https://tkmce.etlab.in/user/login"
        r = self.session.post(url, data=self.login_cred).text
        try:
            soup = BeautifulSoup(r, "html.parser")
            c = soup.find(id="LoginForm_password_em_").get_text()
            print(c)
            return 0
        except:
            return 1

    def fetch_data(self):
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
        sub = [i for i in result[:result.find("Percentage") + 10].split("\n") if i.strip() != ""]
        value = [i for i in result[result.find("Percentage") + 10:].split("\n") if i.strip() != ""]
        data = dict()
        for i in range(len(sub)):
            data[sub[i]] = value[i]
        return data

    def fetch_assignment(self):
        url = "https://tkmce.etlab.in/student/assignments"
        p = self.session.get(url).text
        soup = BeautifulSoup(p, "html.parser")
        l = []
        for row in soup.find('table'):
            for cols in row:
                ll = []
                for col in cols:
                    try:
                        col = str(col)
                        if col.strip() != '':
                            if col.find('</a>') == -1:
                                souped = BeautifulSoup(col, "html.parser")
                                ll.append(souped.find_all('td')[0].text)
                            else:
                                souped = BeautifulSoup(col, "html.parser")
                                ll.append(souped.find_all('a', href=True)[0]['href'])
                    except:
                        pass
                if len(ll) > 1:
                    l.append(ll)
        return l

    def fetch_answers(self, assignments):
        links = []
        for assignment in assignments:
            url = assignment[2].split('/')
            url[-2] = 'submitassignment'
            url = "https://tkmce.etlab.in" + '/'.join(url)
            # print(url)
            ass = self.session.get(url).text
            soup = BeautifulSoup(ass, "html.parser")
            try:
                c = soup.find(id='AssignmentData_upload_file').get_text()
            except:
                table = soup.find('table')
                for row in table:
                    row = str(row)
                    if row.strip() != '':
                        souped = BeautifulSoup(row, 'html.parser')
                        for a in souped.find_all('a', href=True):
                            links.append("https://tkmce.etlab.in/"+a['href'])
        return links
