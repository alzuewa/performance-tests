from abc import ABC, abstractmethod

from seeds.builder import build_grpc_seeds_builder
from seeds.dumps import save_seeds_result, load_seeds_result
from seeds.schema.plan import SeedsPlan
from seeds.schema.result import SeedsResult
from tools.logger import get_logger

logger = get_logger('SEEDS_SCENARIO')


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
        logger.info(f'[{self.scenario}] Saving seeding result to file.')
        save_seeds_result(result=result, scenario=self.scenario)
        logger.info(f'[{self.scenario}] Seeding result saved successfully.')

    def load(self) -> SeedsResult:
        """
        Loads seeding results from the file.
        :return: SeedsResult object containing data loaded from the file.
        """
        logger.info(f'[{self.scenario}] Loading seeding result from file.')
        result = load_seeds_result(scenario=self.scenario)
        logger.info(f'[{self.scenario}] Seeding result loaded successfully.')
        return result

    def build(self) -> None:
        """
        Generates data based on Seeding plan using the builder and saves result.
        """
        # Convert Seeding plan into JSON for logging (without default values)
        plan_json = self.plan.model_dump_json(indent=2, exclude_defaults=True)
        logger.info(f'[{self.scenario}] Starting seeding data generation for plan: {plan_json}')
        result = self.builder.build(self.plan)
        logger.info(f'[{self.scenario}] Seeding data generation completed.')
        self.save(result)
