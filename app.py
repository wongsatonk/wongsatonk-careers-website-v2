from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

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


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    results = result.all()
    jobs = []
    # print(results[0]._mapping)
    for row in results:
      jobs.append(row._mapping)
      # print(row._mapping)

    # print(result_dicts)
  return jobs


@app.route('/')
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs, my_name=my_name)


@app.route('/api/jobs')
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5001, debug=True)
