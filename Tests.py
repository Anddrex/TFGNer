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
