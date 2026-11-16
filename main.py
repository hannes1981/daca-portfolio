import os
from dotenv import load_dotenv
import pandas as pd
from supabase import create_client

# 1. Laeme .env failist turvaliselt võtmed
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

# 2. Loome Supabase kliendi ühenduse
supabase = create_client(url, key)

# 3. Pärime andmebaasist suurema hulga müügiridu (kuni 1000 rida)
response = supabase.table("sales").select("*").limit(1000).execute()

# 4. Teisendame JSON vastuse pandas DataFrame'iks
df = pd.DataFrame(response.data)

print(f"📊 Laaditi kokku {len(df)} müügitehingut.\n")

# 5. Grupeerime andmed kaupluste kaupa ja arvutame summad ning keskmised
if "total_price" in df.columns:
    summary = df.groupby("store_location").agg(
        tehingute_arv=("id", "count"),
        kogukäive=("total_price", "sum"),
        keskmine_ostukorv=("total_price", "mean")
    ).reset_index()

    # Vormindame numbrid kahe komakoha täpsusega
    summary["kogukäive"] = summary["kogukäive"].round(2)
    summary["keskmine_ostukorv"] = summary["keskmine_ostukorv"].round(2)
else:
    summary = df.groupby("store_location").size().reset_index(name="tehingute_arv")

print("--- 🛒 MÜÜGITULEMUSED POODIDE KAUPA ---")
print(summary.to_string(index=False))