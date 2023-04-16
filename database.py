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


    
    # print("type(result):",type(result))
    # result_all=result.all()
    # print("type(result.all():",type(result_all))
    # first_result=result_all[0]
    # print("type(first_result):",type(first_result))
    # first_result_dict=dict(result_all[0])
    # print("type(first_result_dict):",type(first_result_dict))
    # print(first_result_dict)