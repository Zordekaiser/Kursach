from sc_client.client import connect, disconnect, create_elements
from sc_client.constants import sc_types, exceptions
from sc_kpm.utils import get_system_idtf, get_element_by_norole_relation, get_link_content_data, get_edge
from sc_kpm.utils import  get_element_by_role_relation, delete_edges
from sc_kpm import ScKeynodes

# get_system_idtf(адрес) Для узлов
# get_link_content_data(адрес) Для ссылок



def get_smartphones_idtf():
    url = "ws://localhost:8090/ws_json"
    connect(url)

    addr = ScKeynodes["concept_smartphone"]
    trg = ScKeynodes["nrel_inclusion"]
    results = []

    while True:
        result = get_element_by_role_relation(addr, trg)
        if result.is_valid():
            results.append(get_system_idtf(result))
            ScKeynodes.delete(get_system_idtf(result))
        else:
            break

    disconnect()
    return results


a = get_smartphones_idtf()
print(a)
