import json
from flask import Flask
from flask_cors import CORS, cross_origin
from get_info import get_title_addr
from file_manager import *

# 读取元数据
meta = read_mata()
length = len(meta)

# result 格式{title:..., addr:...}
# results格式 {学校名(str): 夏令营(list<Result>)}
results = {}
for i in range(length):
    result = get_title_addr(meta[i].get('addr'), meta[i].get('selector'), meta[i].get('encoding'))
    results[meta[i].get('name')] = result

app = Flask(__name__)
CORS(app)

@app.route('/ustc', methods=['GET'])
@cross_origin()
def ustc():
    print('data sent')
    return json.dumps(results.get('ustc'), indent=4, ensure_ascii=False)
    # indent=4设置换行缩进，ensure_ascii保证中文正常显示


@app.route('/peking', methods=['GET'])
@cross_origin()
def peking():
    print('data sent')
    return json.dumps(results.get('peking'), indent=4, ensure_ascii=False)


app.run()
