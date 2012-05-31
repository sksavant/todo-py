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

    def do_add(self,line):
        #if string is add Going to there @tomorrow 9 @travel :
        # give the command add(['1','Going to there','30/05/2012','9',['travel']])
        task_add=[]
        tasktime=''
        taskstr=''
        taskimp=''
        tasktag=''
        # task_index+=1
        # task_add.append(task_index)
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
            elif(not e=='@') and indexoft==2:
                taskimp=taskimp+e
            elif(e=='@') and indexoft==2:
                task_add.append(int(taskimp))
                taskimp=''
                indexoft=3
            elif(not e=='.') and indexoft==3:
                tasktag=tasktag+e
            elif(e=='.') and indexoft==3 :
                task_add.append(tasktag)	            	
                tasktag=''
                indexoft=0
        tasks_pending.append(task_add)
    
    def do_printall(self,line):
        print tasks_pending
    
    def do_exit(self,line):
        return True


#def modify(task,whattomod,modtask):
	# search for the task in the tasks_pending or tasks_done and
	# see whattomod (what to be modified) and modify it. Then write
	# the modified task into the tasks_* list



#def sort():


#def finish(taskid,):


#def writetofile():


'''def parser(input_string):
	stop=0
	while not stop:
'''

todo().cmdloop()


