from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedCardsPlan, SeedAccountsPlan


class ExistingUserMakePurchaseOperationSeedsScenario(SeedsScenario):
    """
    Seeding scenario for existing user making purchase operation.
    Creates 300 users, opens a credit account and issues cards.
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        Seeding plan describing how many users need to create and what data to generate for them.
        This plan creates 300 users with a credit account and a card.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,  # Users amount
                credit_card_accounts=SeedAccountsPlan(
                    count=1,  # Accounts amount per user
                    physical_cards=SeedCardsPlan(count=1)  # Physical cards amount
                )
            )
        )

    @property
    def scenario(self) -> str:
        """
        Seeding scenario name used to save data.
        """
        return 'existing_user_make_purchase_operation'


if __name__ == '__main__':
    seeds_scenario = ExistingUserMakePurchaseOperationSeedsScenario()
    seeds_scenario.build()
