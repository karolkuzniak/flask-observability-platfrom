from locust import HttpUser, task, between

class FlaskUser(HttpUser):

    wait_time = between(1, 2)

    @task(3)
    def index (self):
        self.client.get("/")

    @task(1)
    def error(self):
        self.client.get("/error")

