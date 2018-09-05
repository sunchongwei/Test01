class my_course(object) :

    #初始函数
    def __init__(self,name,teacher,danshuang,xingqi,time):
       self.name=name 
       self.teacher=teacher
       self.danshuang=danshuang
       self.xingqi=xingqi
       self.time=time 
    #添加课程名称
    def addName(self,name) :
        self.name=name 

    #添加老师名称
    def addTeacher(self,teacher) :
        self.teacher(teacher)
    
    #添加课程单双周
    def addDanshuang(self,danshuang) :
        self.danshuang=danshuang 

    #添加课程开始星期
    def addXingqi(self,xingqi) :
        self.xingqi=xingqi 

    #添加课程开始节数 
    def addTime(time) :
        self.time=time 

    #返回
    def returnDanshuang(self) :
        return self.danshuang 

    def returnTime(self) :
        return self.time 

    def returnXingqi(self) :
        return self.xingqi 

    def returnName(self) :
        return self.teacher 

    def returnTeacher(self):
        return self.teacher 
