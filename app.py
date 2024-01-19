from flask import Flask, render_template, jsonify

app = Flask(__name__)

my_name = 'Wongsaton Kampusan'
jobs = [
    {
        'id': 1,
        'title': 'Programmer',
        'company': 'Delsnet Enterprise Co.,Ltd.',
        'location': 'Nonthaburi, Thailand',
        'salary': '0 Bath'
    },
    {
        'id': 2,
        'title': 'System Engineer',
        'company': 'Unity Focus Co.,Ltd.',
        'location': 'Bangkok, Thailand',
        'salary': '0 Bath'
    },
    {
        'id': 3,
        'title': 'Reliability Engineer (Automation & Server)',
        'company': 'Mars Petcare (Thailand)',
        'location': 'Chonburi, Thailand',
        'salary': '0 Bath'
    },
    {
        'id': 4,
        'title': 'Automation Engineer (Remote)',
        'company': 'Mars Petcare (Thailand)',
        'location': 'Chonburi, Thailand',
        'salary': '0 Bath'
    },
]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=jobs, my_name=my_name)


@app.route('/api/jobs')
def list_jobs():
  return jsonify(jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
