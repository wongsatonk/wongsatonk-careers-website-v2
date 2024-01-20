import os 
from sqlalchemy import create_engine, text

db_host = os.environ["DATABASE_HOST"]
db_username = os.environ["DATABASE_USERNAME"]
db_password = os.environ["DATABASE_PASSWORD"]
db_name = os.environ["DATABASE"]

# print(os.environ("DATABASE_HOST"))

db_connection_string = f'mysql+pymysql://{db_username}:{db_password}@{db_host}/{db_name}?charset=utf8mb4'

print(db_connection_string)

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
  
    results = result.all()
    jobs = [] 
    # print(results[0]._mapping)
    for row in results:
      jobs.append(row._mapping)
      # print(row._mapping)
  
    # print(result_dicts)
  return jobs


print(load_jobs_from_db())