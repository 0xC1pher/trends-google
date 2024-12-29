import pytrends
from pytrends.request import TrendReq
import pandas as pd

def get_trending_searches(region):
    pytrends = TrendReq()
    trending = pytrends.trending_searches(pn=region)
    return trending

def save_to_csv(trending_searches, filename):
    trending_searches.to_csv(filename, index=False)

def main():
    region = input("Ingresa la región (por ejemplo, germany): ").strip().lower()
    if not region:
        print("La región no puede estar vacía. Por favor, intenta de nuevo.")
        return
    try:
        trending_searches = get_trending_searches(region)
        print(trending_searches)
        save_to_csv(trending_searches, f"trending_searches_{region}.csv")
        print(f"Resultado guardado en trending_searches_{region}.csv")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()
