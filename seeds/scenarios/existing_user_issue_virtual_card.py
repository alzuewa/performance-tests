from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan


class ExistingUserIssueVirtualCardSeedsScenario(SeedsScenario):
    """
    Seeding scenario for existing user issuing a virtual card.
    Creates 300 users and opens a debit account.
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        Seeding plan describing how many users to create and what data to generate for them.
        This plan creates 300 users with a debit account.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,
                debit_card_accounts=SeedAccountsPlan(count=1)
            )
        )

    @property
    def scenario(self) -> str:
        """
        Seeding scenario name used to save data.
        """
        return 'existing_user_issue_virtual_card'


if __name__ == '__main__':
    seeds_scenario = ExistingUserIssueVirtualCardSeedsScenario()
    seeds_scenario.build()
