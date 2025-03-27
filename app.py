from flask import Flask, jsonify, render_template, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db
app = Flask(__name__)

COMPANY_NAME = "Job"

@app.route('/')
def hello_job():
  jobs = load_jobs_from_db()
  return render_template('home.html', 
                         jobs=jobs,
                         company_name=COMPANY_NAME)

@app.route('/api/jobs')
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route('/job/<id>')
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  else:
    job = job[0]
    return render_template('jobpage.html', job=job,
                         company_name=COMPANY_NAME)

@app.route("/job/<id>/apply", methods = ["post"])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)[0]
  response = add_application_to_db(id, data)
  if response.status_code == 201:
    return render_template('application_submitted.html', application=data, job=job)
  else:
    return f"Error code: {response.status_code}; If error code is 400 you did not complete the application."

if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug =True)