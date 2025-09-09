from pydantic import BaseModel


class TariffSchema(BaseModel):
    """
    Tariff data structure.
    """
    url: str
    document: str


class GetTariffDocResponseSchema(BaseModel):
    """
    Get tariff document response data structure.
    """
    tariff: TariffSchema


class ContractSchema(BaseModel):
    """
    Contract data structure.
    """
    url: str
    document: str


class GetContractDocResponseSchema(BaseModel):
    """
    Get contract document response data structure.
    """
    contract: ContractSchema
