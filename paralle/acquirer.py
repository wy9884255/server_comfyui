import json
from datetime import datetime, timedelta
import time

from log import Log
import comfy_api as ComfyAPI
from RedisInterface import RedisInterface
RedisInterface.init_redis()
log = Log()
class ResultAcquirer():
    @classmethod
    def get_result(self):
        request_key = "comfyui:queued_prompt"
        #delete data 3 min ago
        five_minutes_ago = (datetime.now() - timedelta(minutes=3)).strftime("%H%M%S%f")
        float_time = float(five_minutes_ago[:-3] + '.' + five_minutes_ago[-3:])
        RedisInterface.COMFYUI_DB.zremrangebyscore(request_key, 0, float_time)
        prompt_datas = RedisInterface.COMFYUI_DB.zrange(request_key, 0, -1)
        for data in prompt_datas:
            if data:
                key = data.decode()
                data_dict = json.loads(key)
                if len(data_dict) == 0:
                    continue
                prompt_id = data_dict['prompt_id']
                ip_address = data_dict['ip_address']
                id = data_dict['id']
                notifyUrl = data_dict['notifyUrl']
                model = data_dict['model']
                result_id = -1
                queue_time = int(data_dict['queue_time'])
                if model == 'comfy_instantid_anime':
                    result_id = 98
                elif model == 'comfy_inpainting':
                    result_id = 994
                    
                send_data = {}
                ret = ComfyAPI.get_result(prompt_id, result_id, ip_address)
                if ret == "":
                    continue
                current_time = int(datetime.now().strftime("%H%M%S"))
                elapsed_time = current_time - queue_time
                #>2min
                if elapsed_time > 120:
                    send_data = {
                        "id":id,
                        "images": [],
                        "success": False,
                        "message": "Generate error, time exceed!"
                    } 
                else:
                    send_data = {
                        "id":id,
                        "images": [ret],
                        "success": True,
                        "message": "Success"
                    }
                print(f"acquirer done on {prompt_id} model {model} duration={elapsed_time}s")
                log.output_logs(f"ComfyUI inpainting finished on prompt_id = {prompt_id}, server = {ip_address} duration={elapsed_time}s")
                #return_data = requests.post(notifyUrl, json=send_data)
                RedisInterface.COMFYUI_DB.zrem(request_key, key)
    
if __name__ == "__main__":
    while(True):
        time.sleep(1)
        ResultAcquirer.get_result()