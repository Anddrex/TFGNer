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

import json

# added_info = {"technique":"relation_extraction", "version":"1.0.0"}

# def newInfo(entities,relationships):
#     global added_info
#     relations = relationships["relationships"]
#     for relation in relations:
#         print(relation["predicate"])
#         if  not("softwareRequirements" in added_info) and relation["predicate"] == "softwareRequirements":
#                 added_info["softwareRequirements"] = []
#         elif  not("hardwareRequirements" in added_info) and relation["predicate"] == "hardwareRequirements": 
#                 added_info["hardwareRequirements"] = []
#         elif  not("supportedLanguages" in added_info) and relation["predicate"] == "supportedLanguages":
#                 added_info["supportedLanguages"] = []
#         elif  not("supportedOS" in added_info) and relation["predicate"] == "supportedOS":
#                 added_info["supportedOS"] = []        
    
    
#     for entity in entities:
#         for relation in relations:
#             if relation["predicate"] == "softwareRequirements" and entity["id"] == relation["object"] and not {"name":entity["name"]} in added_info["softwareRequirements"]:
#                 added_info["softwareRequirements"].append({"name":entity["name"]})
#             elif relation["predicate"] == "hardwareRequirements" and entity["id"] == relation["object"] and not {"name":entity["name"]} in added_info["hardwareRequirements"]:
#                 added_info["hardwareRequirements"].append({"name":entity["name"]})
#             elif relation["predicate"] == "supportedLanguages" and entity["id"] == relation["object"] and not {"name":entity["name"]} in added_info["supportedLanguages"]:
#                 added_info["supportedLanguages"].append({"name":entity["name"]})
#             elif relation["predicate"] == "supportedOS" and entity["id"] == relation["object"] and not {"name":entity["name"]} in added_info["supportedLanguages"]:
#                 added_info["supportedOS"].append({"name":entity["name"]})    
    
    



# def makeRelations(name,nerEntities):
#     relationship_dict = {"relationships":[]}
#     # Hacer bucle que acceda a las secciones
#     idRel = 1
    
#     for entity in nerEntities:
#         if entity["type"] == "ProgrammingLanguage":
#             relationship_dict["relationships"].append({ 
#                 "id": idRel,
#                 "subject": name,
#                 "predicate": "supportedLanguages",
#                 "object": entity["id"] 
#             })
#             idRel+=1
#         elif entity["type"] == "Hardware":
#             relationship_dict["relationships"].append({ 
#                 "id": idRel,
#                 "subject": name,
#                 "predicate": "hardwareRequirements",
#                 "object": entity["id"] 
#             })
#             idRel+=1
#         elif entity["type"] == "SoftwareDependency":
#                 relationship_dict["relationships"].append({
#                 "id": idRel,
#                 "subject": name,
#                 "predicate": "softwareRequirements",
#                 "object": entity["id"] 
#             })
#                 idRel+=1
#     newInfo(nerEntities,relationship_dict)               
#     return relationship_dict


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



version = {"pin": 3}
name1 = {"name": 0, "version":[1,3]}
name1.update(version)
version1 = {"name": 0,"version": 3}
array = [name1,version1]
# print(array)
name2 = [{"name": 0, "version":[1,3]}]
#print(name2[0]["version"])
if 1 in name2[0]["version"]:
    name2[0]["version"].append(5)
    print(name2)