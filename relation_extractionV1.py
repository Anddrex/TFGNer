from html import entities
import json

##AQUI empiezo a desarrollar el codigo para crear las funciones que harán el trabajo de modificar el json (poner más comentarios en cada funcion para explicar)

added_info = {"technique":"relation_extraction", "version":"1.0.0"}

def newInfo(entities,relationships):
    global added_info
    relations = relationships["relationships"]
    for relation in relations:
        # print(relation["predicate"])
        if  not("softwareRequirements" in added_info) and relation["predicate"] == "softwareRequirements":
                added_info["softwareRequirements"] = []
        elif  not("hardwareRequirements" in added_info) and relation["predicate"] == "hardwareRequirements": 
                added_info["hardwareRequirements"] = []
        elif  not("supportedLanguages" in added_info) and relation["predicate"] == "supportedLanguages":
                added_info["supportedLanguages"] = []
        elif  not("supportedOS" in added_info) and relation["predicate"] == "supportedOS":
                added_info["supportedOS"] = []        
    
    
    for entity in entities:
        for relation in relations:
            if relation["predicate"] == "softwareRequirements" and entity["id"] == relation["object"] and not {"name":entity["name"]} in added_info["softwareRequirements"]:
                added_info["softwareRequirements"].append({"name":entity["name"]})
            elif relation["predicate"] == "hardwareRequirements" and entity["id"] == relation["object"] and not {"name":entity["name"]} in added_info["hardwareRequirements"]:
                added_info["hardwareRequirements"].append({"name":entity["name"]})
            elif relation["predicate"] == "supportedLanguages" and entity["id"] == relation["object"] and not {"name":entity["name"]} in added_info["supportedLanguages"]:
                added_info["supportedLanguages"].append({"name":entity["name"]})
            elif relation["predicate"] == "supportedOS" and entity["id"] == relation["object"] and not {"name":entity["name"]} in added_info["supportedLanguages"]:
                added_info["supportedOS"].append({"name":entity["name"]})    
    
    
    print(added_info)
    pass
    

def makeRelations(name,section):
    relationship_dict = {"relationships":[]}
    nerEntities = section[0]["ner"]["entities"]
    idRel = 1
    
    for entity in nerEntities:
        if entity["type"] == "ProgrammingLanguage":
            relationship_dict["relationships"].append({ 
                "id": idRel,
                "subject": name,
                "predicate": "supportedLanguages",
                "object": entity["id"] 
            })
            idRel+=1
        elif entity["type"] == "Hardware":
            relationship_dict["relationships"].append({ 
                "id": idRel,
                "subject": name,
                "predicate": "hardwareRequirements",
                "object": entity["id"] 
            })
            idRel+=1
        elif entity["type"] == "SoftwareDependency":
                relationship_dict["relationships"].append({ 
                "id": idRel,
                "subject": name,
                "predicate": "softwareRequirements",
                "object": entity["id"] 
            })
                idRel+=1          
    return relationship_dict         
    


def proccessFich(fileName):
    global added_info
    fich_input = open(fileName,"r")
    dict_input = json.loads(fich_input.read())
    fich_input.close()
    section = dict_input.get("requirement")
    name = dict_input.get("name")
    relationships = makeRelations(name,section)
    entities = section[0]["ner"]["entities"]
    newInfo(entities,relationships)
    dict_input["requirement"][0]["ner"].update(relationships)
    dict_input["relation_extraction"] = [added_info] 
    return dict_input


dict_proccessed = proccessFich("data.json")
nuevofichero = open("proData.json","w")
json1 = json.dumps(dict_proccessed,indent=4)
nuevofichero.write(json1)
nuevofichero.close()
#print(leer.read())




# print("Antes:" + added_info)

# print("Despues:" + added_info)



# resultado = open("pylops_AN.json","r")
# ficheroLeer = resultado.read()
# dictionario = json.loads(ficheroLeer)
# resultado.close()
# keys = dictionario.keys() 
# print(keys)
# for key in keys:
#     print(key)

