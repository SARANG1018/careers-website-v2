from sqlalchemy import create_engine, text

db_connection_string="mysql+pymysql://x6ls692idward8w3u2h8:pscale_pw_aDgqIr95mm59CDu2NIgM1qCtTGNxhqBFOYaqjqdjRBa@aws.connect.psdb.cloud/ brightcareers?charset=utf8mb4"

engine = create_engine(db_connection_string,
                        connect_args={
                            "ssl":{
    "ssl_ca":"/etc/ssl/cert.pem"
    
                    }
                        })

with engine.connect() as conn:
    result=conn.execute(text("select * from jobs"))
    print("type(result):",type(result))
    result_all=result.all()
    print("type(result.all():",type(result_all))
    print("result.all():",result_all)