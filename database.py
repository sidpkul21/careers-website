import os
import requests

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}"
}

def load_jobs_from_db():
    results = requests.get(f"{SUPABASE_URL}/rest/v1/jobs", headers=headers)
    jobs = []
    for row in results.json():
        jobs.append(row)
    return jobs

def load_job_from_db(id):
    url = f"{SUPABASE_URL}/rest/v1/jobs?id=eq.{id}"
    results = requests.get(url, headers=headers)
    job = results.json()
    return job
    
