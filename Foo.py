from sc_client.client import connect, disconnect, template_search
from sc_client.constants import sc_types
from sc_client.models import ScTemplate, ScTemplateResult, ScAddr
from sc_kpm.utils import get_system_idtf, get_link_content_data, get_element_by_norole_relation
from sc_kpm import ScKeynodes
from operator import itemgetter

url = "ws://localhost:8090/ws_json"
connect(url)


def get_definition(name):
    sys_idtf = 'definition_of_' + name
    addr1 = ScKeynodes[sys_idtf]
    nrel_addr1 = ScKeynodes['nrel_sc_text_translation']
    my_template = ScTemplate()
    my_template.triple_with_relation(
        sc_types.NODE_VAR >> 'q_node',
        sc_types.EDGE_D_COMMON_VAR,
        addr1,
        sc_types.EDGE_ACCESS_VAR_POS_PERM,
        nrel_addr1
    )
    search_result = template_search(my_template)
    temp_node_addr = search_result[0].get('q_node')
    my_template1 = ScTemplate()
    my_template1.triple(temp_node_addr, sc_types.EDGE_ACCESS_VAR_POS_PERM, sc_types.LINK_VAR >> 'res')
    search_result = template_search(my_template1)
    link_addr = search_result[1].get('res')
    return get_link_content_data(link_addr)


def get_smartphones_addrs(): # Раздача названий телефонов

    concept_smartphone_addrs = ScKeynodes['concept_smartphone']

    my_template = ScTemplate()
    my_template.triple(concept_smartphone_addrs, sc_types.EDGE_ACCESS_VAR_POS_PERM, sc_types.NODE_VAR >> 'q_node')
    search_result = template_search(my_template)
    result = []
    for item in search_result:
        result.append(item.get('q_node'))

    return result


def get_processors_addrs(): # Раздача названий телефонов

    concept_smartphone_addrs = ScKeynodes['concept_processor']

    my_template = ScTemplate()
    my_template.triple(concept_smartphone_addrs, sc_types.EDGE_ACCESS_VAR_POS_PERM, sc_types.NODE_VAR >> 'q_node')
    search_result = template_search(my_template)
    result = []
    for item in search_result:
        result.append(item.get('q_node'))

    return result


def get_params_smartphone(_smartphone_addr: ScAddr):  # Лутает все параметры и собирает в словарь + name
    list_params = ['OS', 'processor', 'RAM', 'HDD', 'main_camera', 'front_camera', 'display_size', 'battery']
    result_dict = {}

    for param in list_params:
        result_dict[param] = get_param(_smartphone_addr, 'nrel_' + param)

    result_dict.setdefault('name', get_system_idtf(_smartphone_addr))
    return result_dict

def get_params_processor(_processor_addr: ScAddr):  # Лутает все параметры и собирает в словарь + name
    list_params = ['count_of_cores', 'frenquency', 'processor_manufacturer']
    result_dict = {}

    for param in list_params:
        result_dict[param] = get_param(_processor_addr, 'nrel_' + param)

    result_dict.setdefault('name', get_system_idtf(_processor_addr))
    return result_dict

def get_params_app(_smartphone_name: str):  # Лутает все параметры и собирает в словарь + name
    list_params = ['definition']
    result_dict = {}

    for param in list_params:
        result_dict[param] = get_param(_smartphone_name, 'nrel_' + param)

    result_dict.setdefault('name', _smartphone_name)
    return result_dict

def get_param(target: ScAddr, param: str): # Возвращает значение одной характеристики/комплектующей

    nrel_addr = ScKeynodes[param]

    my_template = ScTemplate()
    my_template.triple_with_relation(
        sc_types.NODE_VAR >> 'q_node',
        sc_types.EDGE_D_COMMON_VAR,
        target,
        sc_types.EDGE_ACCESS_VAR_POS_PERM,
        nrel_addr
    )
    search = template_search(my_template)
    if search:
        result = search[0].get('q_node')
        result = get_system_idtf(result)
        return result
    else:
        return None


def get_main_indtf(target: ScAddr):
    addr = ScKeynodes['nrel_main_idtf']
    if target.is_valid():
        my_template = ScTemplate()
        my_template.triple_with_relation(target, sc_types.EDGE_D_COMMON_VAR, sc_types.LINK_VAR >> 'link', sc_types.EDGE_ACCESS_VAR_POS_PERM, addr)
        search_results = template_search(my_template)

        return get_link_content_data(search_results[0].get('link'))




disconnect()
