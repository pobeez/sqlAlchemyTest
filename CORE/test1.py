from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey

#엔진 초기화
engine = create_engine('sqlite:///E:\\source\\python\\Essential_SqlAlchemy\\CORE\\cookies.db')

#메타데이터
metadata = MetaData()

#테이블 생성
cookes = Table('cookies', metadata, 
    Column('cookie_id', Integer(), primary_key=True)
    , Column('cookie_name', String(50), index=True )
    , Column('cookie_recipe_url', String(255)
    , Column('cookie_sky', String(55))
    , Column('quantity', Integer())
    , Column('unit_cost', Numeric(12, 2))
)




