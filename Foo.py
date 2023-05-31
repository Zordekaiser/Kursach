from sc_client.client import connect, disconnect, create_elements
from sc_kpm.utils import get_system_idtf, get_element_by_norole_relation, get_link_content_data
from sc_kpm import ScKeynodes


url = "ws://localhost:8090/ws_json"
connect(url)

addr = ScKeynodes["asdasd"] # Вводим название смартфона
print(get_system_idtf(addr))

addr1 = ScKeynodes["nrel_matrix"]
print(get_system_idtf(addr1))


addr2 = get_element_by_norole_relation(addr, addr1)
print(get_link_content_data(addr2))

disconnect()
