from sqlalchemy import Column,Integer,String,TIMESTAMP,ForeignKey,Boolean,text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()

#prashant start##############################################
#login part of bith aSPA and pSPA
class LoginStatus(Base):
    __tablename__='login_status'
    email=Column(String(),primary_key=True)
    status=Column(String(),nullable=False)
class OtpTable(Base):
    __tablename__='otp_table'
    email=Column(String(),primary_key=True)
    otp=Column(Integer,nullable=False)
    
class TokenMaster(Base):
    __tablename__='tokenmaster'
    email=Column(String(),primary_key=True)
    token=Column(String(),nullable=False)

class UserMaster(Base):
    __tablename__='usermaster'
    email=Column(String(),primary_key=True)
    password=Column(String(),nullable=False)

#upload customer user detail table (in aSPA)
class UserDetailList(Base):
    __tablename__='user_detail_list'
    id=Column(Integer,primary_key=True)
    username=Column(String(),nullable=False)
    phoneno=Column(String(),nullable=False)
    address=Column(String(),nullable=False)


#proctor batch details(in pSPA)
class ProctorBatchDetails(Base):
    __tablename__='proctor_batch_detail'
    batch=Column(String(),primary_key=True)
    batchname=Column(String(),nullable=False)
    projectid=Column(String(),nullable=False)
    proctorid=Column(String(),nullable=False)

#prashant finish##############################################

#Kamlesh start##############################################
#project batch details (in aSPA)
class AdminBatchDetails(Base):
    __tablename__='batchdetails'
    batchid=Column(String(),primary_key=True)
    startbatch=Column(String(),nullable=False)
    endbatch=Column(String(),nullable=False)
    cource=Column(String(),nullable=False)

#proctor details  (in pSPA )
class ProctorDetails(Base):
    __tablename__='proctordetails'
    proctorusername=Column(String(),primary_key=True)
    password=Column(String(),nullable=False)
    proctorcontact=Column(Integer,nullable=False)
    batchid=Column(String(),ForeignKey('batchdetails.batchid'))

# Candidate Details (in aSPA)
class CandidateDetails(Base):
    __tablename__='candidatedetails'
    useid=Column(String(),primary_key=True)
    password=Column(String(),nullable=False)
    usercontact=Column(Integer,nullable=False)
    batchid=Column(String(),ForeignKey('batchdetails.batchid'))

#admin customer upload (in aSPA)
class CustomerUserTable(Base):
    __tablename__='customerusertbl'
    id=Column(Integer,primary_key=True)# prev:Column(Integer,nullable=False)  
    customeruserid=Column(String(),nullable=False)
    customerusername=Column(String(),nullable=False)
    customerusertype=Column(String(),nullable=False)
    batchid=Column(String(),nullable=False)


# Exam Engine
class ExamEngine(Base):
    __tablename__='enginetable'
    id=Column(Integer,primary_key=True)# prev:Column(Integer,nullable=False)
    engineid=Column(String(),nullable=False)
    enginename=Column(String(),nullable=False)
    enginetype=Column(String(),nullable=False)
    batchid=Column(String(),nullable=False)


#kamlesh finish##############################################
#Shreeram start #############################################

class TbProject(Base):
    __tablename__='tb_project'
    code=Column(String(25),primary_key=True)
    name=Column(String(155),nullable=False)
    created_dt=Column(TIMESTAMP,server_default=text('now()'))#check
    deleteflag=Column(Boolean,server_default="False",nullable=False)
    customer_id_fk=Column(String(25))

class CustomerTable(Base):
    __tablename__='tb_customer'
    id=Column(String(25),primary_key=True)
    name=Column(String(155))
    created_dt=Column(TIMESTAMP,server_default= text('now()'))#check
    deleteflag=Column(Boolean,server_default="False",nullable=False)

#sequence tb_iframe_id_seq is replace with autoincrement 

class Iframe(Base):
    __tablename__='tb_iframe'
    id=Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    iframeid=Column(Integer,nullable=False,unique=True)
    iframeurl=Column(String(25))
    created_dt=Column(TIMESTAMP,server_default= text('now()'))#check
    deleteflag=Column(Boolean,server_default="False",nullable=False)

#sequence  tb_notification_id_seq is replaced with autoincrement 

class Notification(Base):
    __tablename__='tb_notification'
    id=Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    message= Column(String(225))
    fromid=Column(String(25))
    toid=Column(String(25))
    project_code_fk=Column(String(25))
    created_dt=Column(TIMESTAMP,server_default= text('now()'))#check
    deleteflag=Column(Boolean,server_default="False",nullable=False)


#shreeram finish########################################################
#ayaz start ########################################################
class CandidateLog(Base):
    __tablename__='candidateLogsTbl'
    candidateId=Column(Integer,primary_key=True)
    candidateUsername=Column(String(20),nullable=False)
    candidateLogs=Column(String(),nullable=False)
    logtime=Column(String(),nullable=False)
#ayaz finish ########################################################