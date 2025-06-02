# Crypto Summary API (Free CoinGecko Tier)

A small FastAPI service that takes a cryptocurrency name or symbol and returns its latest price, market cap, 24h volume, 24h change, and last-updated timestamp—using CoinGecko’s **free** API (no API key required).

## Tech Stack
- **FastAPI** – for routing & validation  
- **requests** – for HTTP calls to CoinGecko  
- **Pydantic** – for request/response models  

## File Overview
- `main.py`  
  - Defines FastAPI app  
  - `/summary` endpoint (query param: `coin`)  
  - Uses Pydantic model `SummaryResponse` to enforce output schema  
- `fetch.py`  
  - Contains `getCoinSummary(coin: str) -> dict | None`  
  - Hits CoinGecko Free API (`/simple/price` endpoint)  
  - Returns a dict matching `SummaryResponse` or `None` if not found  
- `requirements.txt`  
  - Lists Python dependencies  

## How to Run Locally

1. **Clone the repo**  
   ```bash
   git clone <your-fork-url>
   cd <your-repo-folder>
   ```

2. **Create & activate a virtual environment**  
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # on macOS/Linux
   .venv\Scripts\activate         # on Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the FastAPI server**  
   ```bash
   uvicorn main:app --reload
   ```

5. **Visit Interactive Docs**  
   Open [http://localhost:8000/docs](http://localhost:8000/docs) in your browser to see automatically generated Swagger UI.

## Usage Examples

### 1. Fetch Bitcoin Summary
```bash
curl "http://localhost:8000/summary?coin=bitcoin"
```
**Response** (example JSON):
```json
{
  "name": "Bitcoin",
  "symbol": "BTC",
  "usd": 54738.12,
  "usd_market_cap": 1034921934756,
  "usd_24h_vol": 28591452392,
  "usd_24h_change": -0.42,
  "last_updated_at": 1700000000
}
```