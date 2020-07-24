from sqlalchemy import Column,Integer,String,TIMESTAMP,ForeignKey,Boolean,text,Enum
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

Base = declarative_base()


#Creting ENUM class
class UserType(enum.Enum):
    ADMIN="ADMIN"
    PROCTOR="PROCTOR"
    CUSTOMER="CUSTOMER"
    CANDIDATE="CANDIDATE"


class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,autoincrement=True)
    login=Column(String(),nullable=False)
    password=Column(String(),nullable=False)
    uid=Column(String(),unique=True,nullable=False)
    type=Column(Enum(UserType),nullable=False)

class LoginStatus(Base):
    __tablename__='login_status'
    id=Column(Integer,primary_key=True,autoincrement=True)
    email=Column(String(),nullable=False)
    status=Column(String(),nullable=False)

class OtpTable(Base):
    __tablename__='otp_table'
    id=Column(Integer,primary_key=True,autoincrement=True)
    email=Column(String(),nullable=False)
    otp=Column(Integer,nullable=False)

class AdminDetails(Base):
    __tablename__='admin_details'
    id=Column(Integer,primary_key=True,autoincrement=True)
    user_id=Column(Integer,ForeignKey('users.id'),nullable=False)
    name=Column(String(),nullable=False)
    email=Column(String(),nullable=False)

class CustomerDetails(Base):
    __tablename__ = 'customer_details'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(50), nullable = False)
    email = Column(String(50), nullable = False)
    organization = Column(String(50), nullable = False)

class ProctorDetails(Base):
    __tablename__ = 'proctor_details'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(50), nullable = False)
    email = Column(String(50), nullable = False)


class CandidateDetails(Base):
    __tablename__ = 'candidate_details'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(50), nullable = False)
    email = Column(String(50), nullable = False)

class BatchDetails(Base):
    __tablename__ = 'batch_details'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('project.id'), nullable=False)
    start = Column(TIMESTAMP, nullable = False)
    end = Column(TIMESTAMP, nullable = False)

class ExamEngineDetails(Base):
    __tablename__ = 'examengine_details'
    id = Column(Integer, primary_key=True)
    engine_code = Column(String(50), nullable = False)
    url = Column(String(255), nullable = False)

class Project(Base):
    __tablename__='project'
    id=Column(Integer,primary_key=True,autoincrement=True)
    customer_id=Column(Integer,ForeignKey('customer_details.id'))
    project_name=Column(String(155),nullable=False)
    created_dt=Column(TIMESTAMP,server_default=text('now()'))
    

class BatchProctorMap(Base):
    __tablename__='batch_proctor_map'
    id=Column(Integer,primary_key=True,autoincrement=True)
    batch_id=Column(Integer,ForeignKey('batch_details.id'))
    proctor_id=Column(Integer,ForeignKey('proctor_details.id'))
    project_id=Column(Integer,ForeignKey('project.id'))

class ProctorCandidateMap(Base):
    __tablename__='proctor_candidate_map'
    id=Column(Integer,primary_key=True,autoincrement=True)
    proctor_id=Column(Integer,ForeignKey('proctor_details.id'))
    candidate_id=Column(Integer,ForeignKey('customer_details.id'))
    batch_id=Column(Integer,ForeignKey('batch_details.id'))
    project_id=Column(Integer,ForeignKey('project.id'))

class Iframe(Base):
    __tablename__='tb_iframe'
    id=Column(Integer,primary_key=True,autoincrement=True)
    iframeid=Column(Integer,nullable=False,unique=True)
    iframeurl=Column(String(25))
    created_dt=Column(TIMESTAMP,server_default= text('now()'))
    deleteflag=Column(Boolean,server_default="False",nullable=False)



class Notification(Base):
    __tablename__='tb_notification'
    id=Column(Integer,primary_key=True,autoincrement=True)
    message= Column(String(225))
    fromid=Column(String(25))
    toid=Column(String(25))
    project_id=Column(Integer,ForeignKey('project.id'))
    created_dt=Column(TIMESTAMP,server_default= text('now()'))
    deleteflag=Column(Boolean,server_default="False",nullable=False)

class CandidateLog(Base):
    __tablename__='candidateLogsTbl'
    id=Column(Integer,primary_key=True,autoincrement=True)
    candidate_id=Column(Integer,ForeignKey('candidate_details.id'))
    candidateUsername=Column(String(20),nullable=False)
    candidateLogs=Column(String(),nullable=False)
    logtime=Column(String(),nullable=False)
