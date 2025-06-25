##### to do list 
tasks = []
donetasks =[]

while True:
    task=input("enter today goals one by one or press q to exit ").lower()
    if task.lower()=="q" :
       break
    elif task in tasks:
        continue
    else:
        tasks.append(task)

print("ur today tasks are:")
i=1
for task in tasks:
    print(f"{i} {task}")
    i+=1
while True:

    donetask=input("which task have u completed and q to exit").lower()
    if donetask.lower()=="q" :
       break
    elif donetask  in donetasks:
        continue
    else:
        donetasks.append(donetask)
i=1
for task in tasks:
    if task in donetasks:
        print(f"{i}✅ {task}")
    else:
        print(f"{i}⬜ {task}")
    i+=1

    
    

   