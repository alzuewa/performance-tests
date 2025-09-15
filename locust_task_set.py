from locust import HttpUser, TaskSet, between, task


class MyUser(HttpUser):
    host = 'https://api.example.com'
    wait_time = between(1, 3)

    @task(4)
    def get_home(self):
        self.client.get('/home')

    @task(1)
    def get_dashboard(self):
        self.client.get('/dashboard')


# =========================================
class BrowseCatalog(TaskSet):
    host = 'https://api.example.com'

    @task(7)
    def get_product(self):
        self.client.get('/product/12345')

    @task(3)
    def get_category(self):
        self.client.get('/category/45678')


class BrowseBucket(TaskSet):
    host = 'https://api.example.com'

    @task
    def get_bucket(self):
        self.client.get('/bucket')


class ShopUser(HttpUser):
    host = 'https://api.example.com'

    tasks = [BrowseCatalog, BrowseBucket]
    wait_time = between(1, 3)


# ===================================
class ShopUserCustomWeights(HttpUser):
    host = 'https://api.example.com'

    tasks = {
        BrowseCatalog: 3,
        BrowseBucket: 2
    }
    wait_time = between(1, 3)
