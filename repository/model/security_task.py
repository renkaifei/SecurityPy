from sqlalchemy import Column ,Integer,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class SecurityTask(Base):
    __tablename__= "SecurityTask"

    id = Column("ID",Integer,primary_key=True,comment="主键")
    begin_date = Column("BeginDate",DateTime,nullable=False,comment="开始时间")
    end_date = Column("EndDate",DateTime,nullable=False,comment="结束时间")
    is_finished = Column("IsFinished",Integer,nullable=False,comment="是否完成,0未完成 1 完成")
    security_id =Column("SecurityID",ForeignKey("Security.ID"),nullable=False,comment="证券ID外键")
    security = relationship("Security",back_populates="tasks")

    def __repr__(self):
        return "<SecurityTask(id='%d',begin_date='%s',end_date='%s',is_finished='%d',security_id='%d')>" % (
            self.id,self.begin_date.strftime("%Y%m%d"),self.end_date.strftime("%Y%m%d"),self.is_finished,self.security_id)

