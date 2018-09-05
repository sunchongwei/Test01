from course import my_course
import os 
import re 
from datetime import datetime
#读取课程
def addCourse(name) :
    mycourse=[ ]
    with open(name,'r') as f :
        str=re.split(r'[\s\n]+',f.read())
        count=len(str)-1 #获得个数
        tream=int(count/5)
        for i in range(tream) :
            t=i*5
            index=int(t) 
            newcourse=my_course(str[index],str[index+1],str[index+2],str[index+3],str[index+4])
            mycourse.append(newcourse) 
    return mycourse  

#获取当前时间
def getNowTime():
    now=datetime.now()
    xingqi=now.weekday()+1
    return str(xingqi) 

#得到当天课程表
def getCourse(mycourse) :
    print("今天课程")
    for i in range(len(mycourse)) :
        if mycourse[i].returnXingqi()==getNowTime() :
            print("课程名称：%s      教师%s    单双周%s   开始节数%s,%s"%(mycourse[i].returnName(),mycourse[i].returnTeacher(),mycourse[i].returnDanshuang(),mycourse[i].returnTime(),int(mycourse[i].returnTime())+1) )
        else :
             pass 


#创建列表
name='D:\\course.txt'
mycourse=addCourse(name) #生成课程列表 
getCourse(mycourse)
