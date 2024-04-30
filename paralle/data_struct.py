from typing import Optional, List
from pydantic import BaseModel

class ImageFilter(BaseModel):
    brightness:Optional[float] = 0.0
    contrast:Optional[float] = 1.0
    saturation:Optional[float] = 1.0
    sharpness:Optional[float] = 1.0
    blur:Optional[float] = 0.0
    gaussian_blur:Optional[float] = 0.0
    edge_enhance:Optional[float] = 0.0
    detail_enhance:Optional[int] = 0
    temperature:Optional[int] = 0
    hue:Optional[int] = 0
    gamma:Optional[float] = 1.0
    
class Parameter(BaseModel):
    name:Optional[str] = ""
    id:int
    action:str
    model:str
    prompt:str
    width: Optional[int] = 512
    height: Optional[int] = 512
    uuid: Optional[str] = 'test'
    debug_mode: Optional[bool] = False
    init_images: Optional[List[str]] = []
    negative_prompt:Optional[str] = None
    seed:Optional[int] = -1
    steps:Optional[int] = 20    
    
    # Strategy
    face_ratio:Optional[float] = -1
    high_ratio:Optional[float] = -1
    low_ratio:Optional[float] = -1
    # ComfyUI
    notifyUrl:Optional[str] = ''
    lora_name1:Optional[str] = ''
    lora_name2:Optional[str] = ''
    lora_name3:Optional[str] = ''
    lora_weight1:Optional[float] = 0.0
    lora_weight2:Optional[float] = 0.0
    lora_weight3:Optional[float] = 0.0
    instantid_weight:Optional[float] = 0.5
    control_weight:Optional[float] = 0.5
    daka:Optional[str] = ''
    #ImageFilter
    image_filter:Optional[ImageFilter] = None


    
