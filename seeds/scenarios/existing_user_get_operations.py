from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan, SeedOperationsPlan


class ExistingUserGetOperationsSeedsScenario(SeedsScenario):
    """
    Seeding scenario for existing user looking through operations.
    Creates 300 users, opens a credit account and makes operations.
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        Seeding plan describing how many users to create and what data to generate for them.
        This plan creates 300 users with a credit account and operations.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,
                credit_card_accounts=SeedAccountsPlan(
                    count=1,
                    purchase_operations=SeedOperationsPlan(count=5),
                    top_up_operations=SeedOperationsPlan(count=1),
                    cash_withdrawal_operations=SeedOperationsPlan(count=1)
                )
            )
        )

    @property
    def scenario(self) -> str:
        """
        Seeding scenario name used to save data.
        """
        return 'existing_user_get_operations'


if __name__ == '__main__':
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()
