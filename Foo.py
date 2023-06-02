from sc_client.client import connect, disconnect, template_search
from sc_client.constants import sc_types
from sc_client.models import ScTemplate, ScTemplateResult, ScAddr
from sc_kpm.utils import get_system_idtf, get_link_content_data, get_element_by_norole_relation
from sc_kpm import ScKeynodes
from operator import itemgetter

url = "ws://localhost:8090/ws_json"
connect(url)

def get_smartphones_idtf(): # Раздача названий телефонов

    concept_addr = ScKeynodes['concept_smartphone']

    my_template = ScTemplate()
    my_template.triple(concept_addr, sc_types.EDGE_ACCESS_VAR_POS_PERM, sc_types.NODE_VAR >> 'quest_node')

    search_results = template_search(my_template)
    result_idtfs = []
    for result in search_results:
        result_addr = result.get('quest_node')
        result_idtf = get_system_idtf(result_addr)
        result_idtfs.append(result_idtf)

    return result_idtfs


def get_params_smartphone(_smartphone_name: str):  # Лутает все параметры и собирает в словарь + name
    list_params = ['OS', 'processor', 'matrix', 'RAM', 'HDD', 'main_camera', 'front_camera', 'display_size', 'display_resolution', 'battery']
    result_dict = {}

    for param in list_params:
        result_dict[param] = get_param(_smartphone_name, 'nrel_' + param)

    result_dict.setdefault('name', _smartphone_name)
    return result_dict

def get_params_processor(_smartphone_name: str):  # Лутает все параметры и собирает в словарь + name
    list_params = ['number_of_cores', 'frequency', 'graphics', 'manufacturer']
    result_dict = {}

    for param in list_params:
        result_dict[param] = get_param(_smartphone_name, 'nrel_' + param)

    result_dict.setdefault('name', _smartphone_name)
    return result_dict

def get_params_app(_smartphone_name: str):  # Лутает все параметры и собирает в словарь + name
    list_params = ['name', 'definition']
    result_dict = {}

    for param in list_params:
        result_dict[param] = get_param(_smartphone_name, 'nrel_' + param)

    result_dict.setdefault('name', _smartphone_name)
    return result_dict

def get_param(target: str, param: str): # Возвращает значение одной характеристики/комплектующей

    smartphone = ScKeynodes[target]
    nrel_addr = ScKeynodes[param]

    result = get_element_by_norole_relation(smartphone, nrel_addr)
    result = get_main_indtf(result)
    return result


def get_main_indtf(target: ScAddr):
    addr = ScKeynodes['nrel_main_idtf']
    if target.is_valid():
        my_template = ScTemplate()
        my_template.triple_with_relation(target, sc_types.EDGE_D_COMMON_VAR, sc_types.LINK_VAR >> 'link', sc_types.EDGE_ACCESS_VAR_POS_PERM, addr)
        search_results = template_search(my_template)

        return get_link_content_data(search_results[0].get('link'))


print(get_params_smartphone('Motorola_Edge_30_Ultra'))
disconnect()
