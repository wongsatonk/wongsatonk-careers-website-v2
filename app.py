from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, insert_application_to_db

app = Flask(__name__)

my_name = 'Wongsaton Kampusan'
# jobs = [
#     {
#         'id': 1,
#         'title': 'Programmer',
#         'company': 'Delsnet Enterprise Co.,Ltd.',
#         'location': 'Nonthaburi, Thailand',
#         'salary': '0 Bath'
#     },
#     {
#         'id': 2,
#         'title': 'System Engineer',
#         'company': 'Unity Focus Co.,Ltd.',
#         'location': 'Bangkok, Thailand',
#         'salary': '0 Bath'
#     },
#     {
#         'id': 3,
#         'title': 'Reliability Engineer (Automation & Server)',
#         'company': 'Mars Petcare (Thailand)',
#         'location': 'Chonburi, Thailand',
#         'salary': '0 Bath'
#     },
#     {
#         'id': 4,
#         'title': 'Automation Engineer (Remote)',
#         'company': 'Mars Petcare (Thailand)',
#         'location': 'Chonburi, Thailand',
#         'salary': '0 Bath'
#     },
# ]

@app.route('/')
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs, my_name=my_name)


@app.route('/api/jobs')
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route('/job/<id>')
def show_job(id):
  job = load_job_from_db(id)
  # return jsonify(job)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html', job=job)

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)

  insert_application_to_db(id, data)
  # return jsonify(data)
  return render_template('application_submitted.html', application=data, job=job)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5001, debug=True)
