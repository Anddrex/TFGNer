#CON ESTE CODIGO ES POSIBLE LEER UN FICHERO PASARLO A DICTIONARIO Y RETRANSFORMALO A JSON PARA LUEGO METERLO EN UN NUEVO FICHERO
# 
# resultado = open("pylops_AN.json","r")
# ficheroLeer = resultado.read()
# dictionario = json.loads(ficheroLeer)
# resultado.close()
# diccionario2 = dictionario["citation"][0]
#print(diccionario2["originalHeader"])
# print(dictionario["citation"])
# nuevofichero = open("miFich.json","w")
# json1 = json.dumps(dictionario["citation"])
# nuevofichero.write(json1)
# leer = open("miFich.json","r")
# print(leer.read())


# dict = {"ner":{
#           "technique": "NER4Soft",
#           "version": "1.4.5",
#           "entities":[
#              {
               
#                "name": "python",
#                "type": "ProgrammmingLanguage",
#                "start": 55,
#                "end": 60
#              },
#              {
#                "id": 2,
#                "name": "2.7",
#                "type": "Version",
#                "start": 89,
#                "end": 100
#              },
#              {
#                "id": 3,
#                "name": "NVIDIA GTX1060",
#                "type": "Hardware",
#                "start": 222,
#                "end": 240
#              }
#           ]}
#           }
# entities = dict["ner"]["entities"]
# for entity in entities:
# 	if "id" in entity: print(entity)
 
# resultado = open("pylops_AN.json","r")
# ficheroLeer = resultado.read()
# dictionario = json.loads(ficheroLeer)
# resultado.close()
# keys = dictionario.keys() 
# print(keys)
# for key in keys:
#     print(key)

# import json
# 
# added_info = {"technique":"relation_extraction", "version":"1.0.0"}
# 
# def newInfo(entities,relationships):
    # global added_info
    # relations = relationships["relationships"]
    # for relation in relations:
        # print(relation["predicate"])
        # if  not("softwareRequirements" in added_info) and relation["predicate"] == "softwareRequirements":
                # added_info["softwareRequirements"] = []
        # elif  not("hardwareRequirements" in added_info) and relation["predicate"] == "hardwareRequirements": 
                # added_info["hardwareRequirements"] = []
        # elif  not("supportedLanguages" in added_info) and relation["predicate"] == "supportedLanguages":
                # added_info["supportedLanguages"] = []
        # elif  not("supportedOS" in added_info) and relation["predicate"] == "supportedOS":
                # added_info["supportedOS"] = []        
    # 
    # 
    # for entity in entities:
        # for relation in relations:
            # if relation["predicate"] == "softwareRequirements" and entity["id"] == relation["object"] and not {"name":entity["name"]} in added_info["softwareRequirements"]:
                # added_info["softwareRequirements"].append({"name":entity["name"]})
            # elif relation["predicate"] == "hardwareRequirements" and entity["id"] == relation["object"] and not {"name":entity["name"]} in added_info["hardwareRequirements"]:
                # added_info["hardwareRequirements"].append({"name":entity["name"]})
            # elif relation["predicate"] == "supportedLanguages" and entity["id"] == relation["object"] and not {"name":entity["name"]} in added_info["supportedLanguages"]:
                # added_info["supportedLanguages"].append({"name":entity["name"]})
            # elif relation["predicate"] == "supportedOS" and entity["id"] == relation["object"] and not {"name":entity["name"]} in added_info["supportedLanguages"]:
                # added_info["supportedOS"].append({"name":entity["name"]})    
    # 
    # 
# 
# 
# 
# def makeRelations(name,nerEntities):
    # relationship_dict = {"relationships":[]}
    # idRel = 1
    # 
    # for entity in nerEntities:
        # if entity["type"] == "ProgrammingLanguage":
            # relationship_dict["relationships"].append({ 
                # "id": idRel,
                # "subject": name,
                # "predicate": "supportedLanguages",
                # "object": entity["id"] 
            # })
            # idRel+=1
        # elif entity["type"] == "Hardware":
            # relationship_dict["relationships"].append({ 
                # "id": idRel,
                # "subject": name,
                # "predicate": "hardwareRequirements",
                # "object": entity["id"] 
            # })
            # idRel+=1
        # elif entity["type"] == "SoftwareDependency":
                # relationship_dict["relationships"].append({
                # "id": idRel,
                # "subject": name,
                # "predicate": "softwareRequirements",
                # "object": entity["id"] 
            # })
                # idRel+=1
    # newInfo(nerEntities,relationship_dict)               
    # return relationship_dict


# name = "DaSiamRPN"
# entities = [{'end': 153,
#    'id': 1,
#    'name': 'shelxs97',
#    'start': 145,
#    'type': 'Application'},
#   {'end': 220,
#    'id': 2,
#    'name': 'shelxl97',
#    'start': 212,
#    'type': 'Application'},
#   {'end': 269,
#    'id': 3,
#    'name': 'ortep-3',
#    'start': 262,
#    'type': 'SoftwareDependency'},
#   {'end': 220,
#    'id': 4,
#    'name': 'shelxl97',
#    'start': 379,
#    'type': 'Application'}]


# dict_relations = makeRelations(name, entities)
# print(dict_relations)
# print(added_info)


# # version = {"pin": 3}
# name1 = {"name": 0, "version":[1,3]}
# name1.update(version)
# version1 = {"name": 0,"version": 3}
# array = [name1,version1]
# # print(array)
# name2 = [{"name": 0, "version":[1,3]},{"name": 1, "version":[1,3]}]
# #print(name2[0]["version"])
# names = []
# for name in name2:
#     names.append(name["name"])
# print(names.__len__)
# if 1 in name2[0]["version"]:
#     name2[0]["version"].append(5)
#     print(name2)

import json
## version 1.2.0

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
    

def makeRelations(name,nerEntities):
    if type(name) != str or type(nerEntities) != list:
        print("Error: pasar una sección de ner válida")
        return None
    
    #First we initialize the relationship
    relationship_dict = {"relationships":[]}
    # nerEntities = section[0]["ner"]["entities"]
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
    # relationship_dict["relationships"].append({ 
                # "id": "r" + str(idRel),
                # "subject": 3,
                # "predicate": "versionOf",
                # "object": 7 
            # })
    # relationship_dict["relationships"].append({ 
                # "id": "r" + str((idRel+1)),
                # "subject": 6,
                # "predicate": "versionOf",
                # "object": 7 
            # })
    ##########################################################        
    newInfo(nerEntities,relationship_dict) # here we call newInfo since it needs the newly created dictionaru to update itself                      
    return relationship_dict    

name = "DaSiamRPN"
entities = [{'end': 153,
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


dict_relations = makeRelations(name, entities)
print(dict_relations)
print(added_info)