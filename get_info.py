import requests
from bs4 import BeautifulSoup


def get_title_addr(URL: str, selector: str, encoding='utf-8') -> list:
    """

    :param URL: 要爬的网站
    :param selector: 要爬的元素，用于筛选
    :param encoding: 编码格式，默认为utf-8.要与目标网站header里的charset一致，否则出现乱码
    :return: 列表，每个元素均为{'title':..., 'addr':...}
    """
    resp = requests.get(URL)  # 获取网页数据
    resp.encoding = encoding
    soup = BeautifulSoup(resp.text, 'lxml')  # 解析resp
    data = soup.select(selector)  # 选择需要的信息
    result = []
    for i in range(len(data)):
        title = data[i].text.strip()
        addr = data[i].get("href")  # 夏令营网页地址,若href为相对地址，则前要加URL
        if not 'http' in addr:
            addr = URL + addr
        if title:
            result.append({'title': f'{title}', 'addr': f'{addr}'})  # 储存到字典中去
    return result
