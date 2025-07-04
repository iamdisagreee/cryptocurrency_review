from fastapi import APIRouter

from src.init import cmc_client

router = APIRouter(
    prefix="/currencies",
    tags=["currencies"]
)

@router.get("/", description="Топ-100 монет")
async def get_cryptocurrencies():
    return await cmc_client.get_listings()

@router.get("/{currency_id}", description="Конкретная монета по id")
async def get_cryptocurrency(currency_id: int):
    return await cmc_client.get_currency(currency_id)
