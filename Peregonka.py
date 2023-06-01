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
    file.write("    (* <- lang_ru;; <- name_en;;*);\n")
    file.write("=>nrel_OS:...(*\n   <- concept_OS;;\n")
    MYstring += "   =>nrel_main_idtf: ["
    MYstring += buffer["OS"]
    MYstring += "](*<-lang_ru;;*);;\n"
    MYstring += "   =>nrel_main_idtf: ["
    MYstring += buffer["OS"]
    MYstring += "](*<-lang_en;;*);;\n*);\n"
    file.write(MYstring)
    MYstring = ""
    file.write("=>nrel_processor:...(*\n   <- concept_processor;;\n")
    MYstring += "   =>nrel_main_idtf: ["
    MYstring += buffer['processor']
    MYstring += "](*<-lang_ru;;*);;\n"
    MYstring += "   =>nrel_main_idtf: ["
    MYstring += buffer['processor']
    MYstring += "](*<-lang_en;;*);;\n*);\n"
    file.write(MYstring)
    MYstring = ""
    file.write("=>nrel_matrix:...(*\n   <- concept_matrix;;\n")
    MYstring += "   =>nrel_main_idtf: ["
    MYstring += buffer['display']
    MYstring += "](*<-lang_ru;;*);;\n"
    MYstring += "   =>nrel_main_idtf: ["
    MYstring += buffer['display']
    MYstring += "](*<-lang_en;;*);;\n*);\n"
    file.write(MYstring)
    MYstring = ""
    MYstring += "=>nrel_RAM:...(*\n   <- concept_RAM;;\n"
    MYstring += "   =>nrel_main_idtf: ["
    MYstring += buffer["RAM"]
    MYstring += "](*<-lang_ru;;*);;\n"
    MYstring += "   =>nrel_main_idtf: ["
    MYstring += buffer["RAM"]
    MYstring += "](*<-lang_en;;*);;\n*);\n"
    file.write(MYstring)
    MYstring = ""
    file.write("=>nrel_HDD:...(*\n   <- concept_HDD;;\n")
    MYstring += "   =>nrel_main_idtf: ["
    MYstring += buffer["HDD"]
    MYstring += "](*<-lang_ru;;*);;\n"
    MYstring += "   =>nrel_main_idtf: ["
    MYstring += buffer["HDD"]
    MYstring += "](*<-lang_en;;*);;\n*);\n"
    file.write(MYstring)
    MYstring = ""
    file.write("=>nrel_main_camera:...(*\n   <- concept_main_camera;;\n")
    MYstring += "   =>nrel_main_idtf: ["
    MYstring += buffer["main_camera"]
    MYstring += "](*<-lang_ru;;*);;\n"
    MYstring += "   =>nrel_main_idtf: ["
    MYstring += buffer["main_camera"]
    MYstring += "](*<-lang_en;;*);;\n*);\n"
    file.write(MYstring)
    MYstring = ""
    file.write("=>nrel_front_camera:...(*\n   <- concept_front_camera;;\n")
    MYstring += "   =>nrel_main_idtf: ["
    MYstring += buffer["front_camera"]
    MYstring += "](*<-lang_ru;;*);;\n"
    MYstring += "   =>nrel_main_idtf: ["
    MYstring += buffer["front_camera"]
    MYstring += "](*<-lang_en;;*);;\n*);\n"
    file.write(MYstring)
    MYstring = ""
    file.write("=>nrel_display_size:...(*\n   <- concept_display_size;;\n")
    MYstring += "   =>nrel_main_idtf: ["
    MYstring += buffer["display_size"]
    MYstring += "](*<-lang_ru;;*);;\n"
    MYstring += "   =>nrel_main_idtf: ["
    MYstring += buffer["display_size"]
    MYstring += "](*<-lang_en;;*);;\n*);\n"
    file.write(MYstring)
    MYstring = ""
    file.write("=>nrel_display_resolution:...(*\n   <- concept_display_resolution;;\n")
    MYstring += "   =>nrel_main_idtf: ["
    MYstring += buffer["display_resolution"]
    MYstring += "](*<-lang_ru;;*);;\n"
    MYstring += "   =>nrel_main_idtf: ["
    MYstring += buffer["display_resolution"]
    MYstring += "](*<-lang_en;;*);;\n*);\n"
    file.write(MYstring)
    MYstring = ""
    file.write("=>nrel_battery:...(*\n   <- concept_battery;;\n")
    MYstring += "   =>nrel_main_idtf: ["
    MYstring += buffer["battery"]
    MYstring += "](*<-lang_ru;;*);;\n"
    MYstring += "   =>nrel_main_idtf: ["
    MYstring += buffer["battery"]
    MYstring += "](*<-lang_en;;*);;\n*);;\n"
    file.write(MYstring)
    MYstring = ""

    file.close()
