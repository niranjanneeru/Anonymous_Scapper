from etlab import Etlab


def for_(data, per):
    for i in data:
        print(i[0], int(i[1] * (100 / per) - i[2]))


def process(data):
    data_sub = {
        'MAT203': 'DISCRETE MATHEMATICAL STRUCTURES',

        'CST201': 'DATA STRUCTURES',

        'CST203': 'LOGIC SYSTEM DESIGN',

        'CST205': 'OBJECT ORIENTED PROGRAMMING USING JAVA',

        'CSL201': 'DATA STRUCTURES LAB',

        'CSL203': 'OBJECT ORIENTED PROGRAMMING LAB(IN JAVA)',

        'HUT200': 'PROFESSIONAL ETHICS',

        'MNC201': 'SUSTAINABLE ENGINEERING',

        'VAC': 'REMEDIAL / MINOR COURSE',
    }
    for i in data_sub:
        data[data_sub[i]] = data[i]
        data.pop(i)
    for i in data:
        try:
            data[i] = data[i].split()[0].split("/")[0], data[i].split()[0].split("/")[1]
        except:
            continue
    cred = {'UNi Reg No': data['UNi Reg No'], 'Roll No': data['Roll No'], 'Name': data['Name'],
            'Percentage': data['Percentage']}
    data.pop('UNi Reg No')
    data.pop('Roll No')
    data.pop('Name')
    data.pop('Percentage')
    final = []
    # print(data)
    for i in data:
        att = int(data[i][0])
        tot = int(data[i][1])
        if tot == 0:
            continue
        else:
            per = att / tot * 100
        l = [i, att, tot, per]
        final.append(l)
    for_(final, 90)
    print()
    for_(final, 80)
    # print(cred)
    # print(final)


def main(username, password):
    data = Etlab(username, password)
    result = data.login()
    if result:
        d = data.fetch_data()
        process(d)  # Percent
        assignment = data.fetch_assignment()  # Assignments
        for l in assignment:
            for a in l:
                print(a, end="-")
            print()
        links = data.fetch_answers(assignment)  # Links to Assignment
        for link in links:
            print(link)


if __name__ == "__main__":
    usernam = input("Enter your username: ").strip()
    passwor = input("Enter your password: ").strip()
    if usernam == "" or passwor == "":
        print("Credentials can't be empty")
    else:
        main(usernam, passwor)
