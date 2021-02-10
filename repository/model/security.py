from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import relationship 
from .base import Base

class Security(Base):
    __tablename__ = "Security"

    id = Column("ID",Integer,primary_key=True,comment="主键")
    security_code = Column("Security_Code",String(50),nullable=False,comment="证券代码")
    security_abbr = Column("Security_Abbr",String(50),nullable=False,comment="证券简称")
    company_code = Column("Company_Code",String(50),nullable=False,comment="公司代码")
    company_abbr = Column("Company_Abbr",String(50),nullable=False,comment="公司简称")
    exchange = Column("Exchange",String(10),nullable=False,comment="交易所")
    tasks = relationship("SecurityTask",back_populates="security")

    def __repr__(self):
        return "<Security(id='%s',security_code='%s',security_abbr='%s',company_code='%s',company_abbr='%s')>" %(
            self.id,self.security_code,self.security_abbr,self.company_code,self.company_abbr)

