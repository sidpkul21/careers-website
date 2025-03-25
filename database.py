import os
import requests

def load_jobs_from_db():
    SUPABASE_URL = os.getenv('SUPABASE_URL')
    SUPABASE_KEY = os.getenv('SUPABASE_KEY')
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}"
    }
    results = requests.get(f"{SUPABASE_URL}/rest/v1/jobs", headers=headers)
    jobs = []
    for row in results.json():
        jobs.append(row)
    return jobs
