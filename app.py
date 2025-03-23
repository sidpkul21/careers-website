from flask import Flask, jsonify, render_template
app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Grand Rapids, USA',
    'salary': '$100,000'
  },
  {
    'id': 2,
    'title': 'Frontend Eng',
    'location': 'Remote'
  },
  {
    'id': 3,
    'title': 'Backend Eng',
    'location': 'San Fransisco',
    'salary': '$150,000'
  }
]

@app.route('/')
def hello_job():
  return render_template('home.html', 
                         jobs=JOBS,
                         company_name='Job')

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug =True)