from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db,load_job_from_db, add_application_to_db

app = Flask(__name__)

# JOBS = [
#     {
#         'id': 1,
#         'title': 'Data Analyst',
#         'location': 'Bengaluru, India',
#         'salary': 'Rs. 10,00,000'
#     },
#     {
#         'id': 2,
#         'title': 'Data Scientist',
#         'location': 'Delhi, India',
#         'salary': 'Rs. 15,00,000'
#     },
#     {
#         'id': 3,
#         'title': 'Frontend Engineer',
#         'location': 'Remote',
#     },
#     {
#         'id': 4,
#         'title': 'Backend Engineer',
#         'location': 'San Francisco,USA',
#         'salary': '$150,000'
#     }
# ]

@app.route("/")
def home():
    jobs=load_jobs_from_db()
    return render_template('home.html', jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
    jobs=load_jobs_from_db()
    return jsonify(jobs) 
# api: APPLICATION PROGRAMMING INTERFACE where, api will return the data in structured format rather then returning in html format

# <id> --> this is used to create dynamic route in flask
@app.route("/jobs/<id>")
def show_job(id):
    if not job:
        return "Not Found", 404
    else:
        job=load_job_from_db(id)
    return render_template('jobpage.html',job=job)

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
    # store this in db
    data=request.form
    job=load_job_from_db(id)
    add_application_to_db(id,data)
    
    # display an acknowledgement
    return render_template('application_submitted.html',application=data,job=job) 

if __name__ == '__main__':
    app.run(port='8000', debug=True)
