# -*- coding: utf-8 -*-

from sqlalchemy import *
from datetime import datetime
import sqlalchemy.types
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm  import  sessionmaker

metadata = MetaData()
__engine = create_engine('mysql://root:2222@localhost/nba_stat', connect_args={'charset': 'UTF8'}, echo=True,
                         encoding='UTF-8')

Session_class = sessionmaker(bind=__engine) # 用于session创建

metadata.bind = __engine
Base = declarative_base()

t_city = Table(
    'city', metadata,
    Column('id', Integer, primary_key=True),
    Column('city_name', Unicode(200, collation='utf8_bin'), unique=True, nullable=True),
    Column('city_name_cn', Unicode(200, collation='utf8_bin'), unique=True, nullable=True),
    Column('create_time', DateTime, onupdate=datetime.now),
    Column('update_time', DateTime, onupdate=datetime.now)
)

t_team = Table(
    'team', metadata,
    Column('id', Integer, primary_key=True),
    Column('team_name', Unicode(200, collation='utf8_bin'), unique=True, nullable=True),
    Column('team_name_cn', Unicode(200, collation='utf8_bin'), unique=True, nullable=True),
    Column('city_id', Integer),
    Column('conference_id', Unicode(200, collation='utf8_bin'), onupdate=datetime.now),
    Column('division_id', Unicode(200, collation='utf8_bin'), nullable=True),
    Column('create_time', DateTime, onupdate=datetime.now),
    Column('update_time', DateTime, onupdate=datetime.now)
)

t_city_gdp = Table(
    'city_gdp', metadata,
    Column('id', Integer, primary_key=True),
    Column('city_id', Integer, primary_key=True),
    Column('year', Integer, nullable=True),
    Column('gdp', Unicode(200, collation='utf8_bin'), nullable=True),
    Column('create_time', DateTime, onupdate=datetime.now),
    Column('update_time', DateTime, onupdate=datetime.now)
)

t_team_stats = Table(
    'team_stats', metadata,
    Column('id', Integer, primary_key=True),
    Column('team_id', Integer, primary_key=True),
    Column('year', Integer, nullable=True),
    Column('win', Integer, nullable=True),
    Column('loss', Integer, nullable=True),
    Column('conference_id', Unicode(255, collation='utf8_bin'), nullable=True),
    Column('create_time', DateTime, onupdate=datetime.now),
    Column('update_time', DateTime, onupdate=datetime.now)
)

class TeamStats(Base):
    __tablename__ = 'team_stats'
    id = Column('id', Integer, primary_key=True)
    team_id = Column('team_id', Integer, primary_key=True)
    year = Column('year', Integer, nullable=True)
    win = Column('win', Integer, nullable=True)
    loss = Column('loss', Integer, nullable=True)
    conference_id = Column('conference_id', Unicode(255, collation='utf8_bin'), nullable=True)
    create_time = Column('create_time', DateTime, onupdate=datetime.now)
    update_time = Column('update_time', DateTime, onupdate=datetime.now)

metadata.create_all()