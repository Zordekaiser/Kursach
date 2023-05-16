import pymongo


db_client = pymongo.MongoClient("mongodb://localhost:27017/")

current_db = db_client["kursach"]
workCollection = current_db["workCollection"]
systemCollection = current_db["systemCollection"]
dataCollection = current_db["dataCollection"]
smartcol = systemCollection.count_documents(({'key': 'smart_phone'}))
smarts = systemCollection.find(({'key': 'smart_phone'}))
buffer = smarts.next()
rot = buffer["name"]
rot += ".scs"
file = open(rot, "w+")

MYstring = ""
MYstring += buffer["name"]
MYstring += "<-concept_smartphone;"
file.write(MYstring)
MYstring = ""
file.write("=>nrel_main_idtf:")
MYstring += "["
MYstring += buffer["name"]
MYstring += "]"
file.write(MYstring)
MYstring = ""
file.write("(* <- lang_en;; <- name_en;;*);")
file.write("=>nrel_OS:")
MYstring += "["
MYstring += buffer["OS"]
MYstring += "]"
file.write(MYstring)
MYstring = ""
file.write("(* <- concept_OS;;*);")
file.write("=>nrel_processor:")
MYstring += "["
MYstring += buffer['processor']
MYstring += "]"
file.write(MYstring)
MYstring = ""
file.write("(* <- concept_processor;;*);")
file.write("=>nrel_matrix:")
MYstring += "["
MYstring += buffer['display']
MYstring += "]"
file.write(MYstring)
MYstring = ""
file.write("(* <- concept_matrix;;*);")
MYstring += "=>nrel_RAM:"
MYstring += "["
MYstring += buffer["RAM"]
MYstring += "]"
file.write(MYstring)
MYstring = ""
file.write("(* <- concept_RAM;;<-exact_value;;*);")
file.write("=>nrel_HDD:")
MYstring += "["
MYstring += buffer["HDD"]
MYstring += "]"
file.write(MYstring)
MYstring = ""
file.write("(* <- concept_HDD;;<-exact_value;;*);")
file.write("=>nrel_main_camera:")
MYstring += "["
MYstring += buffer["main_camera"]
MYstring += "]"
file.write(MYstring)
MYstring = ""
file.write("(* <- concept_camera;;<-exact_value;;*);")
file.write("=>nrel_front_camera:")
MYstring += "["
MYstring += buffer["front_camera"]
MYstring += "]"
file.write(MYstring)
MYstring = ""
file.write("(* <- concept_camera;;<-exact_value;;*);")
file.write("=>nrel_display_size:")
MYstring += "["
MYstring += buffer["display_size"]
MYstring += "]"
file.write(MYstring)
MYstring = ""
file.write("(* <- concept_matrix;;<-exact_value;;*);")
file.write("=>nrel_display_resolution:")
MYstring += "["
MYstring += buffer["display_resolution"]
MYstring += "]"
file.write(MYstring)
MYstring = ""
file.write("(* <- concept_matrix;;<-exact_value;;*);")
file.write("=>nrel_battery:")
MYstring += "["
MYstring += buffer["battery"]
MYstring += "]"
file.write(MYstring)
MYstring = ""
file.write("(* <- concept_battery;;<-exact_value;;*);;")




file.close()
#for i in range(0, systemCollection.count_documents({"key": "smart_phone"})):

