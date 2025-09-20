from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan


class ExistingUserGetDocumentsSeedsScenario(SeedsScenario):
    """
    Seeding scenario for existing user looking through their accounts and operations.
    Creates 100 users, opens debit and savings accounts.
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        Seeding plan describing how many users to create and what accounts to add.
        This plan creates 100 users with debit and credit accounts.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=100,
                savings_accounts=SeedAccountsPlan(count=1),
                debit_card_accounts=SeedAccountsPlan(count=1)
            )
        )

    @property
    def scenario(self) -> str:
        """
        Seeding scenario name used to save data.
        """
        return 'existing_user_get_documents'


if __name__ == '__main__':
    seeds_scenario = ExistingUserGetDocumentsSeedsScenario()
    seeds_scenario.build()
