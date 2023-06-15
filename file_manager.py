import json
from get_info import get_title_addr


def save_json(filename:str, ob):
    """

    :param filename: 文件名，不带后缀
    :param ob:
    :return:
    """
    with open('./data/'+filename+'.json', 'w') as f:
        json.dump(ob, f, indent=4, ensure_ascii=False)


def print_json(file: str):
    """

    :param file: 文件名，不带后缀
    :return:
    """
    with open('./data/'+file+'.json', "r") as f:
        y = json.load(f)
        print(y)


def read_common(file: str):
    """
    读取一切形式的文件，并以object形式传出
    :param file: data目录下的文件名,带后缀
    :return: object形式的读取结果
    """
    with open(f'./data/{file}') as f:
        result = json.load(f)
        return result


def read_mata() -> list:
    return read_common('meta.json')


