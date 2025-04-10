from sqlalchemy import Column, Integer, String, Float, Date,DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Salaries(Base):
    __tablename__ = 'salaries'
    id = Column(Integer, primary_key=True, autoincrement=True)
    work_year = Column(Integer, nullable=False)
    experience_level = Column(String, nullable=False)
    employment_type = Column(String, nullable=False)
    job_title = Column(String, nullable=False)
    salary = Column(Float, nullable=False)
    salary_currency = Column(String, nullable=False)
    salary_in_usd = Column(Float, nullable=False)
    employee_residence = Column(String, nullable=False)
    remote_ratio = Column(Integer, nullable=False)
    company_location = Column(String, nullable=False)
    company_size = Column(String, nullable=False)
    time_stamp = Column(DateTime, default=func.current_timestamp())
    train = Column(Integer, default=0)

    def __repr__(self):
        return f"<Salaries(id={self.id}, employee_id={self.employee_id}, salary={self.salary}, start_date={self.start_date}, end_date={self.end_date})>"