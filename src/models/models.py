import sqlalchemy as _sql
import src.config.config as _database

class User(_database.Base):
    __tablename__ = "users"

    id  = _sql.Column(_sql.Integer,primary_key=True, index=True)
    name  = _sql.Column(_sql.String)
    email  = _sql.Column(_sql.String, unique=True)
    password  = _sql.Column(_sql.String)

