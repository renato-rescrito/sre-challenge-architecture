from locust import HttpUser, task, between
import csv

users = []
with open('user.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        users.append(row)

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def task_post(self):
        for userList in users:
            header={'Content-Type': 'application/xml',
            'User-Agent': 'locust',
            'nome' : userList[0],
            'sobrenome' : userList[1],
            'cpf' : userList[2],
            'bday' : userList[3] }

            self.client.post( "/post", headers=header )