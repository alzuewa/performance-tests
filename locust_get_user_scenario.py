from locust import HttpUser, between, task

from tools.fakers import fake


class GetUserScenarioUser(HttpUser):
    # Pause between requests for each virtual user (sec.)
    wait_time = between(1, 3)

    # A variable to store created user data
    user_data: dict

    def on_start(self) -> None:
        """
        on_start method is called 1 time when each virtual user session starts.
        Here we create a new user sending a POST-request to /api/v1/users.
        """
        request = {
            'email': fake.email(),
            'lastName': fake.last_name(),
            'firstName': fake.first_name(),
            'middleName': fake.middle_name(),
            'phoneNumber': fake.phone_number()
        }
        response = self.client.post('/api/v1/users', json=request)  # we don't pass host (use Web UI Locust for it)

        # Saving received data including user ID
        self.user_data = response.json()

    @task
    def get_user(self):
        """
        The main load task: getting data about user.
        Sending a GET-request to /api/v1/users/{user_id}.
        """
        self.client.get(
            f'/api/v1/users/{self.user_data['user']['id']}',
            name='/api/v1/users/{user_id}'  # Explicitly declaring request group name
        )
