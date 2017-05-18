from sqlalchemy import DateTime, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Collector(Base):
    __table__ = 'Collector'
    id = Column(Integer, primary_key=True)
    collector_name = Column(String(256), nullable=False)

class CollectorRunHistory(Base):
    __tablename__ = 'CollectorRunHistory'
    id = Column(Integer, primary_key=True)
    collector_id = Column(Integer, ForeignKey('Collector.id'))
    scheduled_run_date = Column(DateTime, nullable=False)
    run_date = Column(DateTime, nullable=False)
    is_cancelled = Column(Boolean, nullable=False)
    error = Column(Boolean, nullable=True)
    collector = relationship(Collector)

class Parser(Base):
    __table__ = 'Parser'
    id = Column(Integer, primary_key=True)
    parser_name = Column(String(256), nullable=False)

class ParserRunHistory(Base):
    __tablename__ = 'ParserRunHistory'
    id = Column(Integer, primary_key=True)
    collector_id = Column(Integer, ForeignKey('Collector.id'))
    parser_id = Column(Integer, ForeignKey('Parser.id'))
    run_date = Column(DateTime, nullable=True)
    next_run_date = Column(DateTime, nullable=True)
    error = Column(Boolean)
