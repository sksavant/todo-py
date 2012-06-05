# Written by Savant Krishna : savant.2020@gmail.com
# 
# 
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
tasklists_done=[]

class todo(cmd.Cmd):
    prompt='todo :'
    tasks_index=0

    @classmethod
    def incrindex(self):
        todo.tasks_index=todo.tasks_index+1

    def do_add(self,line):
        #if string is add Going to there @tomorrow 9 @travel :
        # give the command add(['1','Going to there','30/05/2012','9',['travel']])
        task_add=[]
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

    def do_printall(self,line):
        for e in tasks_pending:
            print e

    def do_exit(self,line):
        return True

    def do_save(self,line):
        fo=open('tasklist.txt','w')
        for e in tasks_pending:
            fo.write(str(e)+'\n')
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

todo().cmdloop()


