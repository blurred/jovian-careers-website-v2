from flask import Flask, render_template, jsonify
from database import engine

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,000,000'
  },
    {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,000,000'
  },
    {
    'id': 3,
    'title': 'Front Engineer',
    'location': 'Remote',
    'salary': 'Rs. 12,000,000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
  },
]

def load_jobs_from_db():
  with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  result_dicts = result.mappings().all()
  jobs = []
  for row in result_dicts:
    jobs.append(row)

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         jobs=JOBS,
                        company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ ==  "__main__":
  app.run(host='0.0.0.0', debug=True)