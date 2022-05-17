import json
import os
## version 1.3.0
## All code below is for TESTING PURPOSES ONLY and will be modified for our prototype
## ADDED new function addVersions
## UPDATED makeRelations to detect supportedOS relations
## 


# This global variable added_info will have the extra information extracted from the relationships section of ner, as well
# as the technique and it's current version
added_info = {"technique":"relation_extraction", "version":"1.3.0"}

# This is the function newInfo which adds the knowledge gathered from our entities and relationships sections of ner as   
# parameters updating our global variable

def newInfo(entities,relationships):
    if (type(entities) != list or type(relationships) != dict) or (not relationships or not entities):
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
        
        elif  not("usagePlatforms" in added_info) and relation["predicate"] == "usagePlatforms":
            added_info["usagePlatforms"] = []                        
    
   #Aftewards in the following loop we initialize an empty version dictionary and an object id, in
   #order to put the version with the corresponding software/language. That's why we loop both 
   #entities and relationships. In case we don't find any version we put put just the name of the
   #entity in the corresponding section
   
    versions = []
   
    for entity in entities:
        for relation in relations:
            
            if relation["predicate"] == "softwareRequirements" and entity["id"] == relation["object"] and not {"name":entity["name"]} in added_info["softwareRequirements"]:
                added_info["softwareRequirements"].append({"name":entity["name"]})
                
            elif relation["predicate"] == "hardwareRequirements" and entity["id"] == relation["object"] and not {"name":entity["name"]} in added_info["hardwareRequirements"]:
                added_info["hardwareRequirements"].append({"name":entity["name"]})
            
            elif relation["predicate"] == "supportedLanguages" and entity["id"] == relation["object"] and not {"name":entity["name"]} in added_info["supportedLanguages"]:
                    added_info["supportedLanguages"].append({"name":entity["name"]})
            
            elif relation["predicate"] == "supportedOS" and entity["id"] == relation["object"] and not {"name":entity["name"]} in added_info["supportedOS"]:
                added_info["supportedOS"].append({"name":entity["name"]})
            
            elif relation["predicate"] == "usagePlatforms" and entity["id"] == relation["object"] and not {"name":entity["name"]} in added_info["usagePlatforms"]:
                added_info["usagePlatforms"].append({"name":entity["name"]})
 
            
            #this branch is for capturing the version if there exist a versionOf relationship
            elif relation["predicate"] == "versionOf" and entity["id"] == relation["subject"]:
                versions.append((relation["object"],entity["name"]))
                
    if versions:
        addVersions(entities,versions)              
    #print(versions)
    # print(added_info)

def addVersions (entities,versions):
    if (type(entities) != list or type(versions) != list) or not entities:
        print("Error: faltan entidades y/o relaciones")
        return None
    
    global added_info
    
    for entity in entities:  
        for version in versions:
            if version[0] == entity["id"]:
                
                if entity["type"] == "SoftwareDependency":
                    for software in added_info["softwareRequirements"]:
                        if entity["name"] == software["name"]:
                            if  not "version" in software: 
                                software.update({"version":[]})
                            newVersions = set(software["version"])
                            newVersions.add(version[1])
                            software["version"] = list(newVersions)
                
                if entity["type"] == "ProgrammingLanguage":
                    print("LLEGA AQUI")
                    for language in added_info["supportedLanguages"]:
                        if entity["name"] == language["name"]:
                            if  not "version" in language: 
                                language.update({"version":[]})
                            newVersions = set(language["version"])
                            newVersions.add(version[1])
                            language["version"] = list(newVersions)

                if entity["type"] == "DeploymentPlatforms":
                    for depployPlatform in added_info["usagePlatforms"]:
                        if entity["name"] == depployPlatform["name"]:
                            if  not "version" in depployPlatform: 
                                depployPlatform.update({"version":[]})
                            newVersions = set(depployPlatform["version"])
                            newVersions.add(version[1])
                            depployPlatform["version"] = list(newVersions)
                
                if entity["type"] == "OperativeSystem":
                    for oSystem in added_info["supportedOS"]:
                        if entity["name"] == oSystem["name"]:
                            if  not "version" in oSystem: 
                                oSystem.update({"version":[]})
                            newVersions = set(oSystem["version"])
                            newVersions.add(version[1])
                            oSystem["version"] = list(newVersions)
                            
            
    
    print(added_info["softwareRequirements"])                        
    print(added_info["supportedLanguages"])
    #print(added_info["supportedOS"])
    #print(added_info["usagePlatforms"])

def makeRelations(nerEntities):
    if type(nerEntities) != list or not nerEntities:
        print("Error: pasar una sección de ner válida")
        return None
    
    #First we initialize the relationship
    relationship_dict = {"relationships":[]}
    #nerEntities = section[0]["ner"]["entities"]  #This line is deleted in the joint version because we will receive it directly from our service
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
        elif entity["type"] == "DeploymentPlatform":
                relationship_dict["relationships"].append({ 
                "id": "r" + str(idRel),
                "subject": 0,
                "predicate": "usagePlatforms",
                "object": entity["id"] 
            })
                idRel+=1
        elif entity["type"] == "OperativeSystem":
                relationship_dict["relationships"].append({ 
                "id": "r" + str(idRel),
                "subject": 0,
                "predicate": "supportedOS",
                "object": entity["id"] 
            })
                idRel+=1
                
    
    # The following code is for testing our version extraction            
    ##########################################################            
    # relationship_dict["relationships"].append({ 
                # "id": "r" + str(idRel),
                # "subject": 2,
                # "predicate": "versionOf",
                # "object": 3
            # })
    # relationship_dict["relationships"].append({ 
                # "id": "r" + str((idRel+1)),
                # "subject": 6,
                # "predicate": "versionOf",
                # "object": 5 
            # })
    #########################################################        
    newInfo(nerEntities,relationship_dict) # here we call newInfo since it needs the newly created dictionary to update itself                      
    return relationship_dict         
