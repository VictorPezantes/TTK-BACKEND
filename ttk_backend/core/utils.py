import re


def camel_to_snake_str(camel_str):
    upper_snake_str = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', upper_snake_str).lower()


def camel_to_snake_object_keys(obj):
    return dict([(camel_to_snake_str(key), obj.get(key, None)) for key in obj.keys()])


def form_data_to_json(data):
    raw_json_data = {}
    for index, el in enumerate(list(data.items())):
        raw_key = el[0]
        value = el[1][0]
        result = re.search(r"\[([0-9]+)\]", raw_key)
        if result is not None:
            position = result.group(1)
            key = raw_key.split(f"""[{position}]""")[0]
            json_item = raw_json_data.get(position)
            if json_item is None:
                raw_json_data.update({position: {key: value}})
            else:
                json_item.update({key: value})
    return list(raw_json_data.values())
