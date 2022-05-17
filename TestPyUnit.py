from audioop import add
import json

from numpy import empty
# import relation_extractionV1

added_info = {"technique":"relation_extraction", "version":"1.3."}

# This is the function newInfo which adds the knowledge gathered from our entities and relationships sections of ner as   
# parameters updating our global variable

def newInfo(entities,relationships):
    if (type(entities) != list or type(relationships) != dict) or (not bool(relationships) or not entities):
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
                            
            
    
    #print(added_info["softwareRequirements"])                        
    #print(added_info["supportedLanguages"])
    #print(added_info["supportedOS"])
    #print(added_info["usagePlatforms"])

def makeRelations(nerEntities):
    if type(nerEntities) != list or not nerEntities:
        print("Error: pasar una sección de ner válida")
        return None
    
    #First we initialize the relationship
    relationship_dict = {"relationships":[]}
    idRel = 1 #Needed for our creation of relationship ids (FORMAT r + idREl)
    
    #In this loop when we find entities corresponding to programing, languages hardware and software. The function
    #adds them accordingly into the relationship section of ner
    for entity in nerEntities:
        if entity["type"] == "ProgrammingLanguage":
            relationship_dict["relationships"].append({ 
                "id": "r" + str(idRel),
                "subject": 0,
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
    #newInfo(nerEntities,relationship_dict) # here we call newInfo since it needs the newly created dictionary to update itself                      
    return relationship_dict         

#HERE BEGINS THE BATTERY TESTS 

nuevoFichero = open("ResultadoTests.txt","w")

#Test 1: see if using null parameters works
nuevoFichero.write("###########Resultados del Test 1:###########\n")
if newInfo(None,None) == None:
    nuevoFichero.write("Test 1.1 with null for newInfo successful\n")
    
if makeRelations(None) == None:
    nuevoFichero.write("Test 1.2 with null for makeRelations successful\n")

#Test 2: check if function works if we give them 1 valid parameter (that is not empty) or 2 valid parameters that are empty
nuevoFichero.write("###########Resultados del Test 2:###########\n")
emptyList = []
emptyDict = {}
validList = [{'end': 153,
   'id': 1,
   'name': 'shelxs97',
   'start': 145,
   'type': 'Application'},
  {'end': 220,
   'id': 2,
   'name': 'shelxl97',
   'start': 212,
   'type': 'Application'},
  {'end': 269,
   'id': 3,
   'name': 'ortep-3',
   'start': 262,
   'type': 'SoftwareDependency'},
  {'end': 220,
   'id': 4,
   'name': 'shelxl97',
   'start': 379,
   'type': 'Application'}] 

validDict = makeRelations(validList)


if newInfo(validList,emptyDict) == None:
    nuevoFichero.write("Test 2.1 with one valid list for newInfo successful and displayed message\n")

if newInfo(emptyList,validDict) == None:
    nuevoFichero.write("Test 2.2 with one valid dictionary for newInfo successful and displayed message\n")
    
if makeRelations(emptyList) == None:
    nuevoFichero.write("Test 2.3 with empty list makeRelations successful and displayed message\n")


#Test 3 check if makeRelations and newInfo take our entities correctly

nuevoFichero.write("###########Resultados del Test 3:###########\n")
jsonTest31 = json.dumps(makeRelations(validList),indent=3)
nuevoFichero.write("+++++++++Relationships:+++++++++\n")
nuevoFichero.write(jsonTest31)
newInfo(validList,validDict)
nuevoFichero.write("+++++++++Relation_extraction:+++++++++\n")
jsonTest32 = json.dumps(added_info,indent=3)
nuevoFichero.write(jsonTest32)

#Test 4 check if passing more entities and relationships break newInfo
nuevoFichero.write("###########Resultados del Test 4:###########\n")
AnotherList = [
             {
               "id": 1,
               "name": "Intel(R) Core(TM) i7-7700 CPU @ 3.60GHz",
               "type": "Hardware",
               "start": "NUM",
               "end": "NUM"
             },
             {
               "id": 2,
               "name": "2.7",
               "type": "Version",
               "start": "NUM",
               "end": "NUM"
             },{
               "id": 3,
               "name": "python",
               "type": "ProgrammingLanguage",
               "start": "NUM",
               "end": "NUM"
             },
             {
               "id": 4,
               "name": "NVIDIA GTX1060",
               "type": "Hardware",
               "start": "NUM",
               "end": "NUM"
             },
			{
               "id": 5,
               "name": "pytorch",
               "type": "SoftwareDependency",
               "start": "NUM",
               "end": "NUM"
             },
        {
               "id": 6,
               "name": "0.3.1",
               "type": "Version",
               "start": "NUM",
               "end": "NUM"
             },
{
               "id": 7,
               "name": "opencv",
               "type": "SoftwareDependency",
               "start": "NUM",
               "end": "NUM"
             },
{
               "id": 8,
               "name": "numpy",
               "type": "SoftwareDependency",
               "start": "NUM",
               "end": "NUM"
             }
          ]
AnotherDict = makeRelations(AnotherList)
nuevoFichero.write("+++++++++Relationships:+++++++++\n")
jsonTest41 = json.dumps(AnotherDict,indent=3)
nuevoFichero.write(jsonTest41)
newInfo(AnotherList,AnotherDict)
nuevoFichero.write("+++++++++Relation_extraction:+++++++++\n")
jsonTest42 = json.dumps(added_info,indent=3)
nuevoFichero.write(jsonTest42)

#Test 5 here we will pass 2 relation versionOf to see how it magnages

added_info = {}
AnotherList = [
             {
               "id": 1,
               "name": "Intel(R) Core(TM) i7-7700 CPU @ 3.60GHz",
               "type": "Hardware",
               "start": "NUM",
               "end": "NUM"
             },
             {
               "id": 2,
               "name": "2.7",
               "type": "Version",
               "start": "NUM",
               "end": "NUM"
             },{
               "id": 3,
               "name": "python",
               "type": "ProgrammingLanguage",
               "start": "NUM",
               "end": "NUM"
             },
             {
               "id": 4,
               "name": "NVIDIA GTX1060",
               "type": "Hardware",
               "start": "NUM",
               "end": "NUM"
             },
			{
               "id": 5,
               "name": "pytorch",
               "type": "SoftwareDependency",
               "start": "NUM",
               "end": "NUM"
             },
        {
               "id": 6,
               "name": "0.3.1",
               "type": "Version",
               "start": "NUM",
               "end": "NUM"
             },
{
               "id": 7,
               "name": "opencv",
               "type": "SoftwareDependency",
               "start": "NUM",
               "end": "NUM"
             },
{
               "id": 8,
               "name": "numpy",
               "type": "SoftwareDependency",
               "start": "NUM",
               "end": "NUM"
             }
          ]
AnotherDict = makeRelations(AnotherList)
AnotherDict["relationships"].append({ 
            "id": "rE30" ,
            "subject": 2,
            "predicate": "versionOf",
            "object": 3
        })
AnotherDict["relationships"].append({ 
            "id": "rE31",
            "subject": 6,
            "predicate": "versionOf",
            "object": 5 
        })

jsonTest51 = json.dumps(AnotherDict,indent=3)
nuevoFichero.write("+++++++++Relationships:+++++++++\n")
nuevoFichero.write(jsonTest51)
newInfo(AnotherList,AnotherDict)
nuevoFichero.write("+++++++++Relation_extraction:+++++++++\n")
jsonTest52 = json.dumps(added_info,indent=3)
nuevoFichero.write(jsonTest52)


    