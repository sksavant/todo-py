# Written by Savant Krishna : savant.2020@gmail.com
# TODO list program :
# Functionalities needed :
# Function to add task : A task is a list that has a unique index,
# a task string, due date, importance and tag(s) attached to it.
# Function to modify a task, ,it's due date or importance or the string or tags
# Function to sort the task based on due date or importance or both
# Function to say that a task has been completed with the time of completion
#
import cmd
tasks_pending=[]
tasks_done=[]
tasks_got=[]

class todo(cmd.Cmd):
    prompt='todo :'
    tasks_index=0

    @classmethod
    def incrindex(self):
        todo.tasks_index=todo.tasks_index+1

    @classmethod
    def parselist(self,fline):
        task=[]
        listind=0
        gotcat=0
        now=''
        if fline[0]=='d':
            taskcat='d'
            gotcat=1
        elif fline[0]=='p':
            taskcat='p'
            gotcat=1
        else:
            taskcat='p'
        for char in fline[gotcat:]:
            if char==',':
                if listind==2:
                    task.append(int(now))
                elif listind==0 or listind==1:
                    task.append(now[0:len(now)])
                now=''
                listind=listind+1
            elif char=='\n':
                task.append(now[0:len(now)])
            elif not (char=='[' or char=='\'' or char==']'):
                now=now+char
        return task,taskcat

    def do_add(self,line):
        #if string is add Going to there @tomorrow 9 @travel :
        # give the command add(['1','Going to there','30/05/2012','9',['travel']])
        task_add=[]
        if not tasks_pending:
            todo.tasks_index=0
        task_add.append(todo.tasks_index)
        todo.incrindex()
        tasktime=''
        taskstr=''
        taskimp=''
        tasktag=''
        indexoft=0
        for e in line :
            if (not e=='@') and indexoft==0 :
                taskstr=taskstr+e
            elif(e=='@') and indexoft==0 :
                task_add.append(taskstr)
                taskstr=''
                indexoft=1
            elif(not e==' ') and indexoft==1 :
                #time.. more parsing
                tasktime=tasktime+e
            elif(e==' ') and indexoft==1 :
                task_add.append(tasktime)
                tasktime=''
                indexoft=2
            elif(not (e=='@' or e==' ')) and indexoft==2:
                taskimp=taskimp+e
            elif(e=='@' or e==' ') and indexoft==2:
                task_add.append(int(taskimp))
                taskimp=''
                indexoft=3
            elif indexoft==3:
                tasktag=tasktag+e
        task_add.append(tasktag)
        tasks_pending.append(task_add)

    def do_get(self,line):
        if line and not (line=='save' or line=='print'):
            task_file=''
            for e in line:
                task_file=task_file+e
        else:
            task_file="tasklist.txt"
        try:
            tf_read=open(task_file,'r')
        except IOError:
            print "Cannot open",task_file
        else:
            file_content=tf_read.readlines()
            tf_read.close()
            for fline in file_content:
                taskg,taskcat=todo.parselist(fline)
                tasks_got.append(str(taskcat)+str(taskg))
                if line=='save':
                    taskg=[todo.tasks_index]+taskg
                    if taskcat=='p':
                        tasks_pending.append(taskg)
                    elif taskcat=='d':
                        tasks_done.append(taskg)
                    todo.incrindex()
                elif line=='print':
                    print str(taskcat)+str(taskg)

    def do_finish(self,line):
        #"finish taskid" will say that the task has been completed and will remove it from the tasks_pending and add it to tasks_done
        idnow=''
        finid=[]
        for l in line:
            if l==',' or l==' ':
                try:
                    finid.append(int(idnow))
                except ValueError:
                    print "Invalid id number "+idnow
                idnow=''
            else:
                idnow=idnow+l
        try:
            finid.append(int(idnow))
        except ValueError:
            print "Invalid id number "+idnow
        for e in finid:
            foundind=-1
            for i in range(len(tasks_pending)):    
                    if e==tasks_pending[i][0]:
                        tasks_done.append(tasks_pending[i])
                        print "Congrats! You've completed the task \'"+tasks_pending[i][1]+"\'."
                        print
                        foundind=i
            if foundind==-1:
                indindone=0
                for x in tasks_done:
                    if x[1]==e:
                        indindone=1
                if not indindone:
                    print "No task with id "+str(e)+" found. \nSee the ids of all tasks with \'print\'"
                else:
                    print "The task with id "+str(e)+" is already completed! Yay!"
            else:
                tasks_pending.pop(foundind)

    def do_print(self,line):
        pt=0
        dt=0
        if not line:   
            pt=1
            dt=1
        elif line=='pending':
            pt=1
        elif line=='done':
            dt=1
        if pt:
            if tasks_pending:
                print "Pending tasks are :" 
            else:
                print "No pending tasks! \nAdd tasks with \'add task @due imp @tags\'"   
            for e in tasks_pending:
                print e
        if dt:    
            if tasks_done:
                print "Completed tasks are :"
            else:
                print "No completed tasks yet! \nTo mark a task as finished: \'finish task_index\'"
            for f in tasks_done:
                print f

    def do_exit(self,line):
        return True

    def do_save(self,line):
        if not line:
            fo=open('tasklist.txt','w')
            for e in tasks_pending:
                fo.write("p"+str(e[1:])+'\n')
            for f in tasks_done:
                fo.write("d"+str(f[1:])+'\n')
            fo.close()
        else:
            try:
                fo=open(line,'w')
            except IOError:
                print "The file "+line+" cannot be created"
            else:
                for e in tasks_pending:
                    fo.write("p"+str(e[1:])+'\n')
                for f in tasks_done:
                    fo.write("d"+str(f[1:])+'\n')
                fo.close()
#def modify(task,whattomod,modtask):
    # search for the task in the tasks_pending or tasks_done and
    # see whattomod (what to be modified) and modify it. Then write
    # the modified task into the tasks_* list



#def sort():


#def finish(taskid,):





'''def parser(input_string):
    stop=0
    while not stop:
'''
print "Hi, This is a simple command based TODO list program written in python.\nType 'help' to see all the possible commands and their functions"
todo().cmdloop()


