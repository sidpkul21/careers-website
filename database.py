import os
import requests
from dotenv import load_dotenv

load_dotenv()
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

def add_application_to_db(job_id, application):
    application = dict(application)
    application["job_id"] = job_id
    del application["submit"]
    response = requests.post(f"{SUPABASE_URL}/rest/v1/applications", headers=headers, json=application)
    return response