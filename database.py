from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://sa434cqvri60mvsem832:pscale_pw_Y7pEggBnjeLt9hxUZwkWQooVS8YvmNRsbriDncazhOz@aws.connect.psdb.cloud/brightcareers?charset=utf8mb4"

engine = create_engine(db_connection_string,
        connect_args={
        "ssl": {
                    "ssl_ca": "/etc/ssl/cert.pem"
                }
                                })

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
        return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id= :val "), val=id)
        # :val --> special way to provide value that u want to display and then passing the value as given above
    rows=result.all()
    if len(rows)==0:
        return None
    else:
        return dict(rows[0])

def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query =text("INSERT INTO applications (job_id,full_name,email,linkedin_url,education,work_experience,resume_url) VALUES (:job_id,:full_name,:email,:linkedin_url,:education,:work_experience,:resume_url)",)
        conn.execute(query,job_od=job_id,full_name=data['full_name'],email=data['email'],linkedin_url=data['linkedin_url'],education=data['education'],work_experience=data['work_experience'],resume_url=data['resume_url'],)
    # print("type(result):",type(result))
    # result_all=result.all()
    # print("type(result.all():",type(result_all))
    # first_result=result_all[0]
    # print("type(first_result):",type(first_result))
    # first_result_dict=dict(result_all[0])
    # print("type(first_result_dict):",type(first_result_dict))
    # print(first_result_dict)