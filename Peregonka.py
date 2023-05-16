import pymongo


db_client = pymongo.MongoClient("mongodb://localhost:27017/")

current_db = db_client["kursach"]
workCollection = current_db["workCollection"]
systemCollection = current_db["systemCollection"]
dataCollection = current_db["dataCollection"]
smartcol = systemCollection.count_documents(({'key': 'smart_phone'}))
smarts = systemCollection.find(({'key': 'smart_phone'}))

for i in range(0, systemCollection.count_documents({"key": "smart_phone"})):
    buffer = smarts.next()
    rot = "SCS/Smartphones/"
    rot += buffer["name"]
    rot += ".scs"
    file = open(rot, "w+")

    MYstring = ""
    MYstring += buffer["name"]
    MYstring += "<-concept_smartphone;\n"
    file.write(MYstring)
    MYstring = "    "
    file.write("=>nrel_main_idtf:\n")
    MYstring += "["
    MYstring += buffer["name"]
    MYstring += "]\n"
    file.write(MYstring)
    MYstring = "    "
    file.write("    (* <- lang_en;; <- name_en;;*);\n")
    file.write("=>nrel_OS:\n")
    MYstring += "["
    MYstring += buffer["OS"]
    MYstring += "]\n"
    file.write(MYstring)
    MYstring = "    "
    file.write("    (* <- concept_OS;;*);\n")
    file.write("=>nrel_processor:\n")
    MYstring += "["
    MYstring += buffer['processor']
    MYstring += "]\n"
    file.write(MYstring)
    MYstring = "    "
    file.write("    (* <- concept_processor;;*);\n")
    file.write("=>nrel_matrix:\n")
    MYstring += "["
    MYstring += buffer['display']
    MYstring += "]\n"
    file.write(MYstring)
    MYstring = ""
    file.write("    (* <- concept_matrix;;*);\n")
    MYstring += "=>nrel_RAM:\n"
    MYstring += "    ["
    MYstring += buffer["RAM"]
    MYstring += "]\n"
    file.write(MYstring)
    MYstring = "    "
    file.write("    (* <- concept_RAM;;<-exact_value;;*);\n")
    file.write("=>nrel_HDD:\n")
    MYstring += "["
    MYstring += buffer["HDD"]
    MYstring += "]\n"
    file.write(MYstring)
    MYstring = "    "
    file.write("    (* <- concept_HDD;;<-exact_value;;*);\n")
    file.write("=>nrel_main_camera:\n")
    MYstring += "["
    MYstring += buffer["main_camera"]
    MYstring += "]\n"
    file.write(MYstring)
    MYstring = "    "
    file.write("    (* <- concept_camera;;<-exact_value;;*);\n")
    file.write("=>nrel_front_camera:\n")
    MYstring += "["
    MYstring += buffer["front_camera"]
    MYstring += "]\n"
    file.write(MYstring)
    MYstring = "    "
    file.write("    (* <- concept_camera;;<-exact_value;;*);\n")
    file.write("=>nrel_display_size:\n")
    MYstring += "["
    MYstring += buffer["display_size"]
    MYstring += "]\n"
    file.write(MYstring)
    MYstring = "    "
    file.write("    (* <- concept_matrix;;<-exact_value;;*);\n")
    file.write("=>nrel_display_resolution:\n")
    MYstring += "["
    MYstring += buffer["display_resolution"]
    MYstring += "]\n"
    file.write(MYstring)
    MYstring = "    "
    file.write("    (* <- concept_matrix;;<-exact_value;;*);\n")
    file.write("=>nrel_battery:\n")
    MYstring += "["
    MYstring += buffer["battery"]
    MYstring += "]\n"
    file.write(MYstring)
    MYstring = "    "
    file.write("    (* <- concept_battery;;<-exact_value;;*);;\n")

    file.close()
