import random
import requests
from PIL import Image
from utils import ImageUtils

# 1. 获取 apiKey
api_key = "BGEECHIJFGHGEIJHCIB"

# 2. 获取风格列表
style_list_url = "https://magic.artfy.cc/rest-api/api/style"
headers = {"x-api-key": api_key}
response = requests.get(style_list_url, headers=headers)
style_list = response.json()["data"]

# 随机选择三种风格
selected_styles = random.sample(style_list, 3)

# 3. 生成图像
generate_url = "https://magic.artfy.cc/rest-api/api/generate"
init_image_url = "参考图url"  # 替换为参考图像的 URL
notify_url = "生成成功通知地址"  # 替换为生成成功通知的地址
image = Image.open('/home/wy/test.jpg')
bs64_img = ImageUtils.pil_base64(image)
for style in selected_styles:
    style_id = style["id"]
    style_name = style["name"]

    generate_data = {
        "initImageUrl": "",
        "initImageBase64":bs64_img,
        "styleId": style_id,
        "notifyUrl": notify_url
    }

    response = requests.post(generate_url, json=generate_data, headers=headers)
    task_id = response.json()["data"]
    print("生成任务 ID:", task_id)
    print("风格名称:", style_name)
    print()

# 4. 通知回调
# 在生成成功后，API 将会向指定的 notify_url 发送回调通知，包含生成结果信息