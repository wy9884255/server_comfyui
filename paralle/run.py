from fastapi import FastAPI
import uvicorn
import requests
from log import Log
from datetime import datetime
from data_struct import Parameter
import os
import json
os.environ["NUMEXPR_MAX_THREADS"] = "16"

from RedisInterface import RedisInterface
RedisInterface.init_redis()
app = FastAPI()

@app.post('/request_in')
def call_diffusion(param: Parameter):
    data_json = json.dumps(param.dict())
    data_json_str = json.dumps(data_json,ensure_ascii=False).encode('utf-8').decode()
    time_str = datetime.now().strftime("%H%M%S%f")
    float_time = float(time_str[:-3] + '.' + time_str[-3:])
    RedisInterface.COMFYUI_DB.zadd(f"comfyui:requests", {data_json_str:float_time})
    return {"success":True}

@app.get('/status')
def call_status():
    return 200


if __name__ == '__main__':
    try:
        url = "http://127.0.0.1:6000"
        response = requests.get(url + '/status')
    except:
        uvicorn.run("run:app", host="0.0.0.0", port=6000)
        logger = Log()
        logger.output_logs("server port 6000 start!")
 