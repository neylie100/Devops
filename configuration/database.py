from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root@localhost:3306/devop_vn_db")
meta = MetaData()
con = engine.connect()
