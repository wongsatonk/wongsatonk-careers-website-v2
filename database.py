from sqlalchemy import create_engine

db_connection_string = "mysql+pymysql://znmk0o9e9yaqdjqwpave:pscale_pw_sdlC31AealJ6Xok04uE1eyTYJMl7FbfxhQYfttDBg0o@aws.connect.psdb.cloud/wongsatonk_careers?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
          "ssl_ca": "/etc/ssl/cert.pem"
        }
    })