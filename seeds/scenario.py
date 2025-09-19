from abc import ABC, abstractmethod

from seeds.builder import build_grpc_seeds_builder
from seeds.dumps import save_seeds_result, load_seeds_result
from seeds.schema.plan import SeedsPlan
from seeds.schema.result import SeedsResult


class SeedsScenario(ABC):
    """
    Seeding scenarios abstract class.
    Encapsulates general logic of test data generation, saving and loading.
    """

    def __init__(self):
        self.builder = build_grpc_seeds_builder()

    @property
    @abstractmethod
    def plan(self) -> SeedsPlan:
        """
        Abstract property to get seeding plan.
        """
        ...

    @property
    @abstractmethod
    def scenario(self) -> str:
        """
        Abstract property to get seeding scenario name.
        """
        ...

    def save(self, result: SeedsResult) -> None:
        """
        Saves seeding result in the file.
        :param result: SeedsResult object containing generated data.
        """
        save_seeds_result(result=result, scenario=self.scenario)

    def load(self) -> SeedsResult:
        """
        Loads seeding results from the file.
        :return: SeedsResult object containing data loaded from the file.
        """
        return load_seeds_result(scenario=self.scenario)

    def build(self) -> None:
        """
        Generates data based on Seeding plan using the builder and saves result.
        """
        result = self.builder.build(self.plan)
        self.save(result)
