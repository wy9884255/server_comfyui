#This is an example that uses the websockets api to know when a prompt execution is done
#Once the prompt execution is done it downloads the images using the /history endpoint

import websocket #NOTE: websocket-client (https://github.com/websocket-client/websocket-client)
import uuid
import json
import urllib.request
import urllib.parse

def queue_prompt(prompt, client_id, img_url, server_address):
    p = {"prompt": prompt, "client_id": client_id, "img_url":img_url}
    data = json.dumps(p).encode('utf-8')
    req =  urllib.request.Request("http://{}/prompt".format(server_address), data=data)
    return json.loads(urllib.request.urlopen(req).read())

def get_image(filename, subfolder, folder_type, server_address):
    data = {"filename": filename, "subfolder": subfolder, "type": folder_type}
    url_values = urllib.parse.urlencode(data)
    with urllib.request.urlopen("http://{}/view?{}".format(server_address, url_values)) as response:
        return response.read()

def get_history(prompt_id, server_address):
    with urllib.request.urlopen("http://{}/history/{}".format(server_address, prompt_id)) as response:
        return json.loads(response.read())
      
def get_queue(server_address):
    with urllib.request.urlopen("http://{}/queue".format(server_address)) as response:
        return json.loads(response.read())
      
def post_interrupt(server_address):
    with urllib.request.urlopen("http://{}/interrupt".format(server_address)) as response:
        return json.loads(response.read())

def get_result(prompt_id, result_id, server_address):
    output_images = {}
    history = get_history(prompt_id, server_address)
    if prompt_id not in history.keys():
       return "" 
    history = history[prompt_id]
    for o in history['outputs']:
        for node_id in history['outputs']:
            node_output = history['outputs'][node_id]
            if 'images' in node_output:
                images_output = []
                for image in node_output['images']:
                    image_data = get_image(image['filename'], image['subfolder'], image['type'], server_address)
                    images_output.append(image_data)
                output_images[node_id] = images_output
    key = str(result_id)
    if key in output_images and output_images[key] != "":
        return output_images[str(result_id)]
    else:
        return ""

def get_images(ws, prompt, client_id, result_id, img_url, server_address):
    prompt_id = queue_prompt(prompt, client_id, img_url, server_address)['prompt_id']
    output_images = {}
    while True:
        out = ws.recv()
        if isinstance(out, str):
            message = json.loads(out)
            if message['type'] == 'executing':
                data = message['data']
                if data['node'] is None and data['prompt_id'] == prompt_id:
                    break #Execution is done
        else:
            continue #previews are binary data

    history = get_history(prompt_id, server_address)[prompt_id]
    for o in history['outputs']:
        for node_id in history['outputs']:
            node_output = history['outputs'][node_id]
            if 'images' in node_output:
                images_output = []
                for image in node_output['images']:
                    image_data = get_image(image['filename'], image['subfolder'], image['type'], server_address)
                    images_output.append(image_data)
                output_images[node_id] = images_output
    #获取preview image的节点
    return output_images[str(result_id)]
