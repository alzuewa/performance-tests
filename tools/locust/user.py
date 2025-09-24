from config import settings
from locust import User, between


class LocustBaseUser(User):
    """
    Base virtual Locust User inherited by all the load tests scenarios.
    Holds common settings which can be overridden if necessary.
    """
    host: str = 'localhost'  # Fiction host to conform to Locust API
    abstract = True  # Flags that the class shouldn't be used directly
    wait_time = between(
        min_wait=settings.locust_user.wait_time_min,
        max_wait=settings.locust_user.wait_time_max
    )
