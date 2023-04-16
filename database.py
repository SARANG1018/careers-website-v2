from sqlalchemy import create_engine, text

db_connection_string="mysql+pymysql://bhowcyn9imxsixm7k6vn:pscale_pw_jcfbfH93xwY2YjeZ3JJRuAnMmSUJ82ekJ1X2WtmB2Uy@aws.connect.psdb.cloud/brightcareers?charset=utf8mb4"

engine = create_engine(db_connection_string,
                        connect_args={
                            "ssl":{
    "ssl_ca":"/etc/ssl/cert.pem"
    
                    }
                        })

def load_jobs_from_db():
    with engine.connect() as conn:
       result=conn.execute(text("select * from jobs"))
    jobs=[]
    for row in result.all(): 
            jobs.append(dict(row))
            return jobs

    
    # print("type(result):",type(result))
    # result_all=result.all()
    # print("type(result.all():",type(result_all))
    # first_result=result_all[0]
    # print("type(first_result):",type(first_result))
    # first_result_dict=dict(result_all[0])
    # print("type(first_result_dict):",type(first_result_dict))
    # print(first_result_dict)