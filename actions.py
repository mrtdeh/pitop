import re

pipes = []

def loadPipelines(filepath = "./pipelines.yml"):
    f = open(filepath,'r')
    Lines = f.readlines()
    keys = []
    pipe = {}
    for line in Lines:
        data = line.strip()
        enabled = True
        keys = pipe.keys()
        if  re.search("pipeline.id:", data) :        
            if "id" in keys and "config_path" in keys:
                pipes.append(pipe)
                pipe = {}
            d = data.split(":")[1]
            pipe["id"] = d
            pipe["enabled"] = True
            if data.startswith("#"):
                pipe["enabled"] = False
        elif  re.search("path.config:", data) :
            d = data.split(":")[1]
            pipe["config_path"] = d
            if data.startswith("#") :
                pipe["enabled"] = False
            # print( pipe["id"], pipe["enabled"], pipe["config_path"])
        elif  re.search("pipeline.workers:", data) :
            d = data.split(":")[1]
            pipe["workers"] = d
        elif  re.search("pipeline.batch.size:", data) :
            d = data.split(":")[1]
            pipe["batch_size"] = d
        elif  re.search("pipeline.batch.delay:", data) :
            d = data.split(":")[1]
            pipe["batch_delay"] = d

    if "id" in keys and "config_path" in keys:
        pipes.append(pipe)

def uncommentPipe(file,pipeid):
    global pipekey
    pipekey = ""
    replaced_content = ""   
    #looping through the file
    file.seek(0)
    for line in file:
        new_line = line
        # print(line.strip())
        # myid = ""

        if  re.search("pipeline.id:", line) :
           
            myid = line.split(":")[1].strip()
            if re.search(pipeid,line):
                    pipekey = pipeid
            else:
                if myid != pipeid:
                    # print(myid)
                    pipekey = ""
                    # continue
                    # return line

        if  re.search("pipeline.id:", line) and pipekey == pipeid: 
            streped_line = line.replace("#","").lstrip()
            new_line = streped_line
        if  re.search("path.config:", line) and pipekey == pipeid:
            streped_line = line.replace("#","")
            new_line = "  "+streped_line.lstrip()
        if  re.search("pipeline.workers:", line) and pipekey == pipeid:
            streped_line = line.replace("#","")
            new_line = "  "+streped_line.lstrip()
        if  re.search("pipeline.batch.size:", line) and pipekey == pipeid:
            streped_line = line.replace("#","")
            new_line = "  "+streped_line.lstrip()
        if  re.search("pipeline.batch.delay:", line) and pipekey == pipeid:
            streped_line = line.replace("#","")
            new_line = "  "+streped_line.lstrip()

        replaced_content = replaced_content + new_line
    file.seek(0) 
    file.write(replaced_content)
    file.truncate()



def commentPipe(file,pipeid):
    global pipekey
    pipekey = ""
    replaced_content = ""   
    #looping through the file
    file.seek(0)
    for line in file:
        new_line = line
        if  re.search("pipeline.id:", line) :
            myid = line.split(":")[1].strip()
            if re.search(pipeid,line):
                    pipekey = pipeid
            else:
                if myid != pipeid:
                    # print(myid)
                    pipekey = ""
                    # return line
        if  re.search("pipeline.id:", line) and pipekey == pipeid: 
            new_line = "#"+line
        if  re.search("path.config:", line) and pipekey == pipeid:
            # print(pipekey)
            new_line = "#"+line
        if  re.search("pipeline.workers:", line) and pipekey == pipeid:
            new_line = "#"+line
        if  re.search("pipeline.batch.size:", line) and pipekey == pipeid:
            new_line = "#"+line
        if  re.search("pipeline.batch.delay:", line) and pipekey == pipeid:
            new_line = "#"+line 
        replaced_content = replaced_content + new_line
    file.seek(0) 
    file.write(replaced_content)
    file.truncate()
 



