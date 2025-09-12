import time

from google.protobuf.internal.enum_type_wrapper import EnumTypeWrapper
from faker import Faker
from faker.providers.python import TEnum


class Fake:
    """
    Class to generate random test data with Faker lib.
    """

    def __init__(self, faker: Faker):
        """
        :param faker: Faker instance used to generate data.
        """
        self.faker = faker

    def enum(self, value: type[TEnum]) -> TEnum:
        """
        Chooses random value from enum-type.

        :param value: Enum-class to generate value.
        :return: Random value from enum.
        """
        return self.faker.enum(value)

    def proto_enum(self, value: EnumTypeWrapper) -> int:
        """
        Chooses random value from proto enum-type.

        :param value: Proto enum-class to generate values.
        :return: Random value from enum.
        """
        return self.faker.random_element(value.values())

    def email(self) -> str:
        """
        Generates random email.
        :return: Random email.
        """
        return f'{time.time()}.{self.faker.email()}'

    def category(self) -> str:
        """
        Chooses random purchase category from a pre-defined list.

        Used to imitate spending purpose in systems modelling user transactions or
        behaviour when purchasing goods.

        :return: Random category (i.e., 'gas', 'taxi', 'supermarkets' and ).
        """
        return self.faker.random_element([
            'gas',
            'taxi',
            'tolls',
            'water',
            'beauty',
            'mobile',
            'travel',
            'parking',
            'catalog',
            'internet',
            'satellite',
            'education',
            'government',
            'healthcare',
            'restaurants',
            'electricity',
            'supermarkets',
        ])

    def last_name(self) -> str:
        """
        Generates random last name.

        :return: Random last name.
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
        Generates random first name.

        :return: Random first name.
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Generates random middle name.

        :return: Random middle name.
        """
        return self.faker.first_name()

    def phone_number(self) -> str:
        """
        Generates random phone number.

        :return: Random phone number.
        """
        return self.faker.phone_number()

    def float(self, start: int = 1, end: int = 100) -> float:
        """
        Generates random float within a defined range.

        :param start: Range start (inclusive).
        :param end: Range end (inclusive).
        :return: Random float.
        """
        return self.faker.pyfloat(min_value=start, max_value=end, right_digits=2)

    def amount(self) -> float:
        """
        Chooses random total amount from 1-1000 range.

        :return: Any amount from 1 to 1000.
        """
        return self.float(1, 1000)


fake = Fake(faker=Faker())
