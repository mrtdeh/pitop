import re
import json
import time
import actions as ac
pipekey = ""

def main():
    filepath = "./pipelines.yml"
    f = open(filepath,'r')
    # data = f.read()
    Lines = f.readlines()

    # Strips the newline character
    pipes = []
    keys = []
    pipe = {}
    for line in Lines:
        data = line.strip()
        enabled = True
        keys = pipe.keys()
        
        # print(keys)
            
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

    # print(json.dumps(pipes,indent=4))

    filepath = "./pipelines.yml"


    file = open(filepath, "r+")
  
        
    ac.commentPipe(file,"siem_cisco-ise")
    # file.close()
    # time.sleep(1)
    # file.flush()
    # file = open(filepath, "r+")
    ac.uncommentPipe(file,"siem_cisco-ise")

        
        
    #close the file
    file.close()
    # #Open file in write mode
    # write_file = open(filepath, "w")
    # #overwriting the old file contents with the new/replaced content
    # write_file.write(replaced_content)
    # #close the file
    # write_file.close()



# print(pipes)










main()