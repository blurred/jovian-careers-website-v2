from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://24mip8r39hvrasar1ee8:pscale_pw_IbNUZK6xTYujDJiwg0DZbK8FE1BIesvE4U501UjKzGA@ap-southeast.connect.psdb.cloud/joviancareers?charset=utf8mb4"

engine = create_engine(
  db_connection_string, 
  connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
 })


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_dicts = result.mappings().all()
    jobs = []
    for row in result_dicts:
      jobs.append(row)
    return jobs


# with engine.connect() as conn:
#   result = conn.execute(text("select * from jobs"))

#   result_dicts = result.mappings().all()
#   jobs = []
#   for row in result_dicts:
#     jobs.append(row)
#   print(jobs)

