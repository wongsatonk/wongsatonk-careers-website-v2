from sqlalchemy import create_engine

db_connection_string = "mysql+pymysql://rn0ize609wscoeuidkau:pscale_pw_AvUxO9k7bFoZyXCnF5IuJJTX09iIlFVxHycFAmApcaR@aws.connect.psdb.cloud/wongsatonk_careers?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
          "ssl_ca": "/etc/ssl/cert.pem"
        }
    })