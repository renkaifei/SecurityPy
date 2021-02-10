from sqlalchemy import Column,String,Integer,DateTime,Float
from .base import Base
class SecurityDayQuotation(Base):
    __tablename__ = "SecurityDayQuotaiton"

    id = Column("ID",Integer,primary_key=True,comment="主键")
    security_code = Column("SecurityCode",String(50),nullable=False,comment="证券代码")
    exchange = Column("Exchange",String(10),nullable=False,comment="证券交易所")
    date = Column("Date",DateTime,nullable=False,comment="交易日期")
    tclose = Column("TCLOSE",Float,nullable=False,comment="收盘价")
    thigh = Column("THIGH",Float,nullable=False,comment="最高价")
    tlow = Column("TLOW",Float,nullable=False,comment="最低价")
    topen = Column("TOPEN",Float,nullable=False,comment="开盘价")
    lclose = Column("LCLOSE",Float,nullable=False,comment="昨日收盘价")
    change = Column("CHG",Float,nullable=False,comment="涨跌幅")
    pchange = Column("PCHG",Float,nullable=False,comment="涨跌额")
    turnover = Column("TURNOVER",Float,nullable=False,comment="换手率")
    voturnover = Column("VOTURNOVER",Float,nullable=False,comment="成交量")
    vaturnover = Column("VATURNOVER",Float,nullable=False,comment="成交金额")
    tcap = Column("TCAP",Float,nullable=False,comment="总市值")
    mcap = Column("MCAP",Float,nullable=False,comment="流通市值")

    def __repr__(self):
        return '''
        <SecurityDayQuotation(id='%s',security_code='%s',exchange='%s',date='%s',tclose='%f',thigh='%f',tlow='%f',topen='%f',lclose='%f',change='%f',pchange='%f',turnover='%f',voturnover='%f',vaturnover='%f',tcap='%f',mcap='%f')>
        ''' % (self.id,self.security_code,self.exchange,self.date,self.tclose,self.thigh,self.tlow,self.topen,self.lclose,self.change,self.pchange,self.turnover,self.voturnover,self.vaturnover,self.tcap,self.mcap)