def generate_query_from_result_list(json_data):
    query_data = ""
    parameter_type = json_data.get("parameter_type", [])
    tab_names = [item.get("tab_name") for item in parameter_type if item.get("tab_name")]
    content_type = json_data.get("content_type", [])
    content_tab_names = [item.get("tab_name") for item in content_type if item.get("tab_name")]
    all_tab_names = sorted(set(tab_names + content_tab_names))
    all_tab_names_str = ",".join(all_tab_names)
    
    if len(all_tab_names) <= 1:
        list_str = "false" if "list" in tab_names else "true"
        query = f'?parameter_type={all_tab_names_str}&list={list_str}'
        return query
    else:
        return query_data
    
import urllib.parse

def generate_endpoint_query_from_result_list(query_string, json_data):
    # parameters = urllib.parse.parse_qs(query_string)
    # print(parameters)
    # parameter_type = parameters.get('parameter_type', [])
    # print(parameter_type)
    parameters = urllib.parse.parse_qs(query_string.lstrip('?'))
    print(parameters)
    parameter_type = parameters.get('parameter_type', [])
    print(parameter_type)
    print(parameter_type)
    if parameter_type:
        parameter_type_value = parameter_type[0]
        if parameter_type_value == "Genre":
            query_data = '/genres'
        elif parameter_type_value == "Language":
            query_data = '/content-language'
        elif parameter_type_value == "Gender":
            query_data = '/gender'
            
    else:
        query_data = ""

    return query_data

# Example query string and JSON data
query_string = "?parameter_type=Genre&list=true"
result = {
    "parameter_type": [
        {
            "request_type": "array",
            "tab_code": "Genre",
            "tab_name": "Genre"
        },
        {
            "request_type": "array",
            "tab_code": "OtherType",
            "tab_name": "OtherType"
        }
    ]
}

query = generate_endpoint_query_from_result_list(query_string, result)
print(query)



result = {
    "parameter_type": [
        {
            "request_type": "array",
            "tab_code": "genres",
            "tab_name": "Genre"
            
        }
    ],
    "display_rules": {
    "tab_code": "all",
    "tab_name": "All"
    }
}
