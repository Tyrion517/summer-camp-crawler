import json
from flask import Flask
from flask_cors import CORS, cross_origin

from get_info import get_title_addr
from file_manager import *

meta = read_mata()
length = len(meta)

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


@app.route('/peking', methods=['GET'])
@cross_origin()
def peking():
    print('data sent')
    return json.dumps(results.get('peking'), indent=4, ensure_ascii=False)


app.run()
