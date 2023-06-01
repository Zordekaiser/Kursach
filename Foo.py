from sc_client.client import connect, disconnect, template_search
from sc_client.constants import sc_types
from sc_client.models import ScTemplate, ScTemplateResult
from sc_kpm.utils import get_system_idtf, get_link_content_data, get_element_by_norole_relation
from sc_kpm import ScKeynodes


def get_smartphones_idtf():
    url = "ws://localhost:8090/ws_json"
    connect(url)

    concept_addr = ScKeynodes['concept_smartphone']

    my_template = ScTemplate()
    my_template.triple(concept_addr, sc_types.EDGE_ACCESS_VAR_POS_PERM, sc_types.NODE_VAR >> 'quest_node')

    search_results = template_search(my_template)
    result_addrs = []
    for result in search_results:
        result_addr = result.get('quest_node')
        result_addrs.append(result_addr)

    disconnect()
    return result_addrs


def get_params_smartphone(_smartphone_name: str):
    url = "ws://localhost:8090/ws_json"
    connect(url)
    result_dict = {}

    try:
        smartphone_addr = ScKeynodes[_smartphone_name]
    except:
        return False
    processor_relation_addr = ScKeynodes['nrel_processor']
    proc = get_system_idtf(get_element_by_norole_relation(smartphone_addr, processor_relation_addr))
    result_dict['processor'] = proc

    disconnect()
    return result_dict


name = input()
print(get_params_smartphone(name))