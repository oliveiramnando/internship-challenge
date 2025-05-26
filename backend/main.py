from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fetch import getCoinSummary

app = FastAPI()

class SummaryReponse(BaseModel):
    name: str 
    symbol: str
    usd: float 
    usd_market_cap: float 
    usd_24h_vol: float 
    usd_24h_change: float 
    last_updated_at: int 

@app.get("/summary", response_model = SummaryReponse)
async def getSummary(coin: str):
    summary = getCoinSummary(coin)
    if summary is None:
        raise HTTPException(status_code=404, detail=f"No summary data found for coin '{coin}'.")
    
    return summary


