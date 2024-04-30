import os
from PIL import Image
import json
import websocket
import random
from datetime import datetime, timedelta
import json
import time

from log import Log
import comfy_api as ComfyAPI
import workflows
from utils import INPAINTING_DEV, INSTANT_ID_DEV
from RedisInterface import RedisInterface
RedisInterface.init_redis()
log = Log()
class TaskAllocator():
    @classmethod
    def prompt_comfyUI_instantid(self, param, server_address):
        prompt = param['prompt']
        neg_prompt = param['negative_prompt']
        width = param['width']
        height = param['height']
        img_url = param['init_images'][0]
        client_id = param['id']
        img_name = f"{client_id}.jpg"
        workflow = workflows.workflow3
        workflow = json.loads(workflow)
        
        lower_bound = 10 ** 14 
        upper_bound = (10 ** 15) - 1 
        random_int = random.randint(lower_bound, upper_bound)
        workflow['3']['inputs']['seed'] = random_int
        workflow['5']['inputs']['width'] = width
        workflow['5']['inputs']['height'] = height
        workflow['13']['inputs']['image'] = img_name
        workflow['39']['inputs']['text'] = prompt
        workflow['40']['inputs']['text'] = neg_prompt
        workflow['60']['inputs']['weight'] = param['instantid_weight']
        workflow['91']['inputs']['strength'] = param['control_weight']
        if (param['daka'] != '' and (param['face_ratio'] > param['high_ratio'] or param['face_ratio'] < param['low_ratio'])) \
            or (param['daka'] != '' and (param['high_ratio'] == -1 and param['low_ratio'] == -1)):#(big head or full body or daka_only)
            daka_path = os.path.join('/home/wy/diffusion_station/daka', param['daka'])
            files = os.listdir(daka_path)
            random_file = random.choice(files)
            random_file_path = os.path.join(daka_path, random_file)
            image = Image.open(random_file_path)
            width, height = image.size
            workflow['125']['inputs']['image'] = random_file_path
            workflow['5']['inputs']['width'] = width
            workflow['5']['inputs']['height'] = height#------------------wqq----end--------------------
        else:   
            workflow['125']['inputs']['image'] = img_name
        if param['lora_name1'] != "":
            workflow['106']['inputs']['lora_name_1'] = param['lora_name1'] 
            workflow['106']['inputs']['model_weight_1'] = param['lora_weight1'] 
            workflow['106']['inputs']['switch_1'] = "On" 
        if param['lora_name2'] != "":
            workflow['106']['inputs']['lora_name_2'] = param['lora_name2']
            workflow['106']['inputs']['model_weight_2'] = param['lora_weight2'] 
            workflow['106']['inputs']['switch_2'] = "On" 
        if param['lora_name3'] != "":
            workflow['106']['inputs']['lora_name_3'] = param['lora_name3'] 
            workflow['106']['inputs']['model_weight_3'] = param['lora_weight3'] 
            workflow['106']['inputs']['switch_3'] = "On"
            
        #Image filter
        if param['image_filter'] != None:
            workflow['111']['inputs']['brightness'] = param['image_filter']['brightness']
            workflow['111']['inputs']['contrast'] = param['image_filter']['contrast']
            workflow['111']['inputs']['saturation'] = param['image_filter']['saturation']
            workflow['111']['inputs']['sharpness'] = param['image_filter']['sharpness']
            workflow['111']['inputs']['blur'] = param['image_filter']['blur']
            workflow['111']['inputs']['gaussian_blur'] = param['image_filter']['gaussian_blur']
            workflow['111']['inputs']['edge_enhance'] = param['image_filter']['edge_enhance']
            workflow['111']['inputs']['detail_enhance'] = "true" if param['image_filter']['detail_enhance'] == 1 else "false"
            workflow['119']['inputs']['temperature'] = param['image_filter']['temperature']
            workflow['119']['inputs']['hue'] = param['image_filter']['hue']
            workflow['119']['inputs']['gamma'] = param['image_filter']['gamma']
        ws = websocket.WebSocket()
        ws.connect("ws://{}/ws?clientId={}".format(server_address, client_id))
        ret = ComfyAPI.queue_prompt(workflow, client_id, img_url, server_address)
        prompt_id = ""
        if ret == "":
            return prompt_id
        if "prompt_id" in ret.keys():
            prompt_id = ret['prompt_id']
        log.output_logs(f"ComfyUI instand_id queued on prompt_id = {prompt_id}, server = {server_address}")
        return prompt_id
    
    @classmethod
    def prompt_comfyUI_inpainting(self, param, server_address):
        prompt = param['prompt']
        neg_prompt = param['negative_prompt']
        img_url = param['init_images'][0]
        client_id = param['id']
        img_name = f"{client_id}.jpg"
        workflow = workflows.workflow2
        workflow = json.loads(workflow)
        
        lower_bound = 10 ** 14 
        upper_bound = (10 ** 15) - 1 
        random_int = random.randint(lower_bound, upper_bound)
        workflow['993']['inputs']['seed'] = random_int
        workflow['144']['inputs']['image'] = img_name
        workflow['931']['inputs']['text'] = prompt
        workflow['22']['inputs']['text'] = neg_prompt
        if param['lora_name1'] != "":
            workflow['992']['inputs']['lora_name_1'] = param['lora_name1'] 
            workflow['992']['inputs']['model_weight_1'] = param['lora_weight1'] 
            workflow['992']['inputs']['switch_1'] = "On" 
        if param['lora_name2'] != "":
            workflow['992']['inputs']['lora_name_2'] = param['lora_name2']
            workflow['992']['inputs']['model_weight_2'] = param['lora_weight2']
            workflow['992']['inputs']['switch_2'] = "On"  
        if param['lora_name3'] != "":
            workflow['992']['inputs']['lora_name_3'] = param['lora_name3'] 
            workflow['992']['inputs']['model_weight_3'] = param['lora_weight3']
            workflow['992']['inputs']['switch_3'] = "On"  
            
        ws = websocket.WebSocket()
        ws.connect("ws://{}/ws?clientId={}".format(server_address, client_id))
        ret = ComfyAPI.queue_prompt(workflow, client_id, img_url, server_address)
        if "prompt_id" in ret.keys():
            prompt_id = ret['prompt_id']
        log.output_logs(f"ComfyUI inpainting queued on prompt_id = {prompt_id}, server = {server_address}")
        return prompt_id

    @classmethod
    def check_server_available(self, param):
        device_list = []
        if param['model'] == "instantid":
            device_list = INSTANT_ID_DEV
        elif param['model'] == "inpainting": 
            device_list = INPAINTING_DEV
        for device in device_list:
            queue_info = ComfyAPI.get_queue(device)
            if queue_info == "":
                continue
            if len(queue_info['queue_running']) == 0 and len(queue_info['queue_pending']) == 0:
                return device
        return "full"
    
    @classmethod
    def process_request(self):
        data_dict = {}
        request_key = "comfyui:requests"
        #delete data 3 min ago
        five_minutes_ago = (datetime.now() - timedelta(minutes=3)).strftime("%H%M%S%f")
        float_time = float(five_minutes_ago[:-3] + '.' + five_minutes_ago[-3:])
        RedisInterface.COMFYUI_DB.zremrangebyscore(request_key, 0, float_time)

        #get the lastest 10 data
        data_points = RedisInterface.COMFYUI_DB.zrevrange(request_key, 0, 9)
        if len(data_points) < 10:
            data_points = RedisInterface.COMFYUI_DB.zrange(request_key, 0, -1)
        for data in data_points:
            if data:
                key = data.decode()
                data_dict = json.loads(json.loads(key))
                if len(data_dict) == 0:
                    continue
                #check if the server available
                else:
                    address = TaskAllocator.check_server_available(data_dict)
                    if address != 'full':
                        if data_dict['model'] == "instantid":
                            prompt_id = TaskAllocator.prompt_comfyUI_instantid(data_dict,address)
                        elif data_dict['model'] == "inpainting": 
                            prompt_id = TaskAllocator.prompt_comfyUI_inpainting(data_dict,address)
                        if prompt_id == "":
                            log.output_logs(f"queue请求错误!!!")
                            RedisInterface.COMFYUI_DB.zrem(request_key, key)
                            continue
                        current_time = datetime.now()
                        time_str = current_time.strftime("%H%M%S")
                        data_dict = {
                            "prompt_id":prompt_id,
                            "ip_address":address,
                            "id":str(data_dict['id']),
                            "model":data_dict['model'],
                            "notifyUrl":data_dict['notifyUrl'],
                            "queue_time":time_str
                        }
                        print(f"allocator done prompt_id={data_dict['prompt_id']} ip={data_dict['ip_address']} model={data_dict['model']}")
                        RedisInterface.write_queued_prompt(data_dict)
                        RedisInterface.COMFYUI_DB.zrem(request_key, key)
        return data_dict
        

if __name__ == "__main__":
    while(True):
        time.sleep(1)
        TaskAllocator.process_request()