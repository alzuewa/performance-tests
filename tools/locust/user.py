from locust import User, between


class LocustBaseUser(User):
    """
    Base virtual Locust User inherited by all the load tests scenarios.
    Holds common settings which can be overrided if necessary.
    """
    host: str = 'localhost'  # Fiction host to conform to Locust API
    abstract = True  # Flags that the class shouldn't be used directly
    wait_time = between(1, 3)
