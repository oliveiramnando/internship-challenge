from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class SummaryReponse(BaseModel):
    name: str = None
    symbol: str = None
    usd: float = None
    usd_market_cap: float = None
    usd_24h_vol: float = None
    usd_24h_change: float = None
    last_updated_at: int = None

@app.get("/summary", response_model = SummaryReponse)
async def getSummary(coin: str):

    return summary


