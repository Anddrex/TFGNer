import json
## version 1.2.0
## All code below is for TESTING PURPOSES ONLY and will be modified for our prototype


# This global variable added_info will have the extra information extracted from the relationships section of ner, as well
# as the technique and it's current version
added_info = {"technique":"relation_extraction", "version":"1.2.0"}

# This is the function newInfo which adds the knowledge gathered from our entities and relationships sections of ner as   
# parameters updating our global variable

def newInfo(entities,relationships):
    if type(entities) != list and type(relationships) != dict:
        print("Error: faltan entidades y/o relaciones")
        return None
    global added_info
    
    #Here we get the relationships array from the relationships section of our JSON
    #and depending on the entities we first initialize each section with the loop 
    #below depending on the relationships found
    relations = relationships["relationships"]
    
    for relation in relations:
        
        if  not("softwareRequirements" in added_info) and relation["predicate"] == "softwareRequirements":
                added_info["softwareRequirements"] = []
        
        
        elif  not("hardwareRequirements" in added_info) and relation["predicate"] == "hardwareRequirements": 
                added_info["hardwareRequirements"] = []
        
        
        elif  not("supportedLanguages" in added_info) and relation["predicate"] == "supportedLanguages":
                added_info["supportedLanguages"] = []
        
        
        elif  not("supportedOS" in added_info) and relation["predicate"] == "supportedOS":
                added_info["supportedOS"] = []        
    
   #Aftewards in the following loop we initialize an empty version dictionary and an object id, in
   #order to put the version with the corresponding software/language. That's why we loop both 
   #entities and relationships. In case we don't find any version we put put just the name of the
   #entity in the corresponding section
   
    version = {"version":[]}
    objectId = ""
   
    for entity in entities:
        for relation in relations:
            
            # Here since the the data is stored in a array of dictionary their search is a little complex
            # for that we first access and extract each name currently stored the corresponding section,
            # and check if the software is already there, afterwards we make the version list into a set 
            # to avoid repeating versions
            if relation["predicate"] == "softwareRequirements" and entity["id"] == relation["object"]:
                name = entity["name"]
                softwares = []
                for software in added_info["softwareRequirements"]:
                    softwares.append(software["name"])    
                if objectId == entity["id"] and len(version["version"]) != 0 and not name in softwares :
                    versionsSet = set(version["version"])
                    version.update({"version":list(versionsSet)})
                    ver = {"name":entity["name"]}
                    ver.update(version)
                    added_info["softwareRequirements"].append(ver)
                elif objectId == entity["id"] and len(version["version"]) != 0 and {"name":entity["name"]} in added_info["softwareRequirements"]:
                    versionsSet = set(version["version"])
                    version.update({"version":list(versionsSet)})
                    ver.update(version)
                    added_info["softwareRequirements"].append(ver)    
                else:
                    added_info["softwareRequirements"].append({"name":entity["name"]})
                
            
            #There are no versions for hardware so it's not required to check for versions
            elif relation["predicate"] == "hardwareRequirements" and entity["id"] == relation["object"] and not {"name":entity["name"]} in added_info["hardwareRequirements"]:
                added_info["hardwareRequirements"].append({"name":entity["name"]})
            
            
            elif relation["predicate"] == "supportedLanguages" and entity["id"] == relation["object"]:
                name = entity["name"]
                languages = []
                for language in added_info["supportedLanguages"]:
                    languages.append(language["name"])    
                if objectId == entity["id"] and len(version["version"]) != 0 and not name in languages :
                    versionsSet = set(version["version"])
                    version.update({"version":list(versionsSet)})
                    ver = {"name":entity["name"]}
                    ver.update(version)
                    added_info["supportedLanguages"].append(ver)
                elif objectId == entity["id"] and len(version["version"]) != 0 and {"name":entity["name"]} in added_info["supportedLanguages"]:
                    versionsSet = set(version["version"])
                    version.update({"version":list(versionsSet)})
                    ver.update(version)
                    added_info["supportedLanguages"].append(ver)    
                else:
                    added_info["supportedLanguages"].append({"name":entity["name"]})

            
            
            elif relation["predicate"] == "supportedOS" and entity["id"] == relation["object"]:
                name = entity["name"]
                OpSystems = []
                for OpSys in added_info["supportedOS"]:
                    OpSystems.append(OpSys["name"])    
                if objectId == entity["id"] and len(version["version"]) != 0 and not name in OpSystems :
                    versionsSet = set(version["version"])
                    version.update({"version":list(versionsSet)})
                    ver = {"name":entity["name"]}
                    ver.update(version)
                    added_info["supportedOS"].append(ver)
                elif objectId == entity["id"] and len(version["version"]) != 0 and {"name":entity["name"]} in added_info["supportedOS"]:
                    versionsSet = set(version["version"])
                    version.update({"version":list(versionsSet)})
                    ver.update(version)
                    added_info["supportedOS"].append(ver)    
                else:
                    added_info["supportedOS"].append({"name":entity["name"]})
            
            elif relation["predicate"] == "usagePlatforms" and entity["id"] == relation["object"]:
                name = entity["name"]
                platforms = []
                for platform in added_info["usagePlatforms"]:
                    platforms.append(platform["name"])    
                if objectId == entity["id"] and len(version["version"]) != 0 and not name in platforms :
                    versionsSet = set(version["version"])
                    version.update({"version":list(versionsSet)})
                    ver = {"name":entity["name"]}
                    ver.update(version)
                    added_info["usagePlatforms"].append(ver)
                elif objectId == entity["id"] and len(version["version"]) != 0 and {"name":entity["name"]} in added_info["usagePlatforms"]:
                    versionsSet = set(version["version"])
                    version.update({"version":list(versionsSet)})
                    ver.update(version)
                    added_info["usagePlatforms"].append(ver)         
                else:
                    added_info["usagePlatforms"].append({"name":entity["name"]})
 
            
            #this branch is for capturing the version if there exist a versionOf relationship
            elif relation["predicate"] == "versionOf" and entity["id"] == relation["subject"]:
                version["version"].append(entity["name"])
                objectId = relation["object"]
    
    # print(added_info)
    

def makeRelations(name,section):
    if type(name) != str or type(section) != list:
        print("Error: pasar una sección de ner válida")
        return None
    
    #First we initialize the relationship
    relationship_dict = {"relationships":[]}
    nerEntities = section[0]["ner"]["entities"]  #This line is deleted in the joint version because we will receive it directly from our service
    idRel = 1 #Needed for our creation of relationship ids (FORMAT r + idREl)
    
    #In this loop when we find entities corresponding to programing, languages hardware and software. The function
    #adds them accordingly into the relationship section of ner
    for entity in nerEntities:
        if entity["type"] == "ProgrammingLanguage":
            relationship_dict["relationships"].append({ 
                "id": "r" + str(idRel),
                "subject": 0, #this will be changed with id=0 (which will be the id of the named repository) in order to maintain consistency
                "predicate": "supportedLanguages",
                "object": entity["id"] 
            })
            idRel+=1
        elif entity["type"] == "Hardware":
            relationship_dict["relationships"].append({
                "id": "r" + str(idRel),
                "subject": 0,
                "predicate": "hardwareRequirements",
                "object": entity["id"] 
            })
            idRel+=1
        elif entity["type"] == "SoftwareDependency":
                relationship_dict["relationships"].append({ 
                "id": "r" + str(idRel),
                "subject": 0,
                "predicate": "softwareRequirements",
                "object": entity["id"] 
            })
                idRel+=1
        elif entity["type"] == "Deployment":
                relationship_dict["relationships"].append({ 
                "id": "r" + str(idRel),
                "subject": 0,
                "predicate": "usagePlatforms",
                "object": entity["id"] 
            })
                idRel+=1
    
    # The following code is for testing our version extraction            
    ##########################################################            
    relationship_dict["relationships"].append({ 
                "id": "r" + str(idRel),
                "subject": 3,
                "predicate": "versionOf",
                "object": 7 
            })
    relationship_dict["relationships"].append({ 
                "id": "r" + str((idRel+1)),
                "subject": 6,
                "predicate": "versionOf",
                "object": 7 
            })
    ##########################################################        
    newInfo(nerEntities,relationship_dict) # here we call newInfo since it needs the newly created dictionaru to update itself                      
    return relationship_dict         
    


#In proccesFich() we will receive a filename and from that we will create a new dictionary that will be added
#to the corresponding section in our new JSON 

def proccessFich(fileName):
    global added_info
    fich_input = open(fileName,"r")
    dict_input = json.loads(fich_input.read())
    fich_input.close()
    section = dict_input.get("requirement")
    name = dict_input.get("name")
    relationships = makeRelations(name,section)
    # entities = section[0]["ner"]["entities"]
    # newInfo(entities,relationships)
    dict_input["requirement"][0]["ner"].update(relationships)
    dict_input["relation_extraction"] = [added_info] 
    return dict_input

#Here is where we will call proccesfich and create our new file with the aforemetioned dictionary

dict_proccessed = proccessFich("data.json")
nuevofichero = open("proData.json","w")
json1 = json.dumps(dict_proccessed,indent=4)
nuevofichero.write(json1)
nuevofichero.close()
#print(leer.read())