# instantid
workflow1 = """
{
  "3": {
    "inputs": {
      "seed": 52872813925831,
      "steps": 4,
      "cfg": 2,
      "sampler_name": "dpmpp_sde",
      "scheduler": "karras",
      "denoise": 1,
      "model": [
        "60",
        0
      ],
      "positive": [
        "91",
        0
      ],
      "negative": [
        "91",
        1
      ],
      "latent_image": [
        "5",
        0
      ]
    },
    "class_type": "KSampler",
    "_meta": {
      "title": "KSampler"
    }
  },
  "4": {
    "inputs": {
      "ckpt_name": "juggernautXL_v9Rdphoto2Lightning.safetensors"
    },
    "class_type": "CheckpointLoaderSimple",
    "_meta": {
      "title": "Load Checkpoint"
    }
  },
  "5": {
    "inputs": {
      "width": 856,
      "height": 1328,
      "batch_size": 1
    },
    "class_type": "EmptyLatentImage",
    "_meta": {
      "title": "Empty Latent Image"
    }
  },
  "8": {
    "inputs": {
      "samples": [
        "3",
        0
      ],
      "vae": [
        "96",
        0
      ]
    },
    "class_type": "VAEDecode",
    "_meta": {
      "title": "VAE Decode"
    }
  },
  "11": {
    "inputs": {
      "instantid_file": "ip-adapter.bin"
    },
    "class_type": "InstantIDModelLoader",
    "_meta": {
      "title": "Load InstantID Model"
    }
  },
  "13": {
    "inputs": {
      "image": "半身模特 (105).png",
      "upload": "image"
    },
    "class_type": "LoadImage",
    "_meta": {
      "title": "Load Image"
    }
  },
  "16": {
    "inputs": {
      "control_net_name": "diffusion_pytorch_model.safetensors"
    },
    "class_type": "ControlNetLoader",
    "_meta": {
      "title": "Load ControlNet Model"
    }
  },
  "38": {
    "inputs": {
      "provider": "CUDA"
    },
    "class_type": "InstantIDFaceAnalysis",
    "_meta": {
      "title": "InstantID Face Analysis"
    }
  },
  "39": {
    "inputs": {
      "text": "1 girl ,1 panda,Masterpiece,Best quality,bamboo in background,detailed background.",
      "clip": [
        "97",
        0
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Prompt)"
    }
  },
  "40": {
    "inputs": {
      "text": "(Extra arm:1.5),NSFW,lowres,(low quality:1.3),(worst quality:1.3),(monochrome:0.8),(deformed:1.3),(malformed hands:1.4),(poorly drawn hands:1.4),(mutated fingers:1.4),(bad anatomy:1.3),(extra limbs:1.35),(poorly drawn face:1.4),(signature:1.2),(artist name:1.2),(watermark:1.2),(beard:0.2)",
      "clip": [
        "97",
        0
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Prompt)"
    }
  },
  "60": {
    "inputs": {
      "weight": 0.6,
      "start_at": 0,
      "end_at": 1,
      "instantid": [
        "11",
        0
      ],
      "insightface": [
        "38",
        0
      ],
      "control_net": [
        "16",
        0
      ],
      "image": [
        "13",
        0
      ],
      "model": [
        "107",
        0
      ],
      "positive": [
        "39",
        0
      ],
      "negative": [
        "40",
        0
      ],
      "image_kps": [
        "108",
        0
      ]
    },
    "class_type": "ApplyInstantID",
    "_meta": {
      "title": "Apply InstantID"
    }
  },
  "84": {
    "inputs": {
      "low_threshold": 100,
      "high_threshold": 200,
      "resolution": 512,
      "image": [
        "108",
        0
      ]
    },
    "class_type": "CannyEdgePreprocessor",
    "_meta": {
      "title": "Canny Edge"
    }
  },
  "91": {
    "inputs": {
      "strength": 0.7000000000000001,
      "start_percent": 0,
      "end_percent": 0.5,
      "positive": [
        "60",
        1
      ],
      "negative": [
        "60",
        2
      ],
      "control_net": [
        "100",
        0
      ],
      "image": [
        "84",
        0
      ]
    },
    "class_type": "ControlNetApplyAdvanced",
    "_meta": {
      "title": "Apply ControlNet (Advanced)"
    }
  },
  "96": {
    "inputs": {
      "vae_name": "sdxl_vae.safetensors"
    },
    "class_type": "VAELoader",
    "_meta": {
      "title": "Load VAE"
    }
  },
  "97": {
    "inputs": {
      "stop_at_clip_layer": -2,
      "clip": [
        "107",
        1
      ]
    },
    "class_type": "CLIPSetLastLayer",
    "_meta": {
      "title": "CLIP Set Last Layer"
    }
  },
  "98": {
    "inputs": {
      "images": [
        "8",
        0
      ]
    },
    "class_type": "PreviewImage",
    "_meta": {
      "title": "Preview Image"
    }
  },
  "100": {
    "inputs": {
      "control_net_name": "control-lora-canny-rank256.safetensors"
    },
    "class_type": "ControlNetLoader",
    "_meta": {
      "title": "Load ControlNet Model"
    }
  },
  "106": {
    "inputs": {
      "switch_1": "Off",
      "lora_name_1": "None",
      "model_weight_1": 1,
      "clip_weight_1": 1,
      "switch_2": "Off",
      "lora_name_2": "None",
      "model_weight_2": 1,
      "clip_weight_2": 1,
      "switch_3": "Off",
      "lora_name_3": "None",
      "model_weight_3": 1,
      "clip_weight_3": 1
    },
    "class_type": "CR LoRA Stack",
    "_meta": {
      "title": "💊 CR LoRA Stack"
    }
  },
  "107": {
    "inputs": {
      "model": [
        "4",
        0
      ],
      "clip": [
        "4",
        1
      ],
      "lora_stack": [
        "106",
        0
      ]
    },
    "class_type": "CR Apply LoRA Stack",
    "_meta": {
      "title": "💊 CR Apply LoRA Stack"
    }
  },
  "108": {
    "inputs": {
      "image": "熊猫 (1).png",
      "upload": "image"
    },
    "class_type": "LoadImage",
    "_meta": {
      "title": "Load Image"
    }
  }
}
"""
# inpainting
workflow2 = """

{
  "16": {
    "inputs": {
      "ckpt_name": "makinaMix_v22.safetensors"
    },
    "class_type": "CheckpointLoaderSimple",
    "_meta": {
      "title": "Load Checkpoint"
    }
  },
  "21": {
    "inputs": {
      "text": [
        "288",
        0
      ],
      "token_normalization": "none",
      "weight_interpretation": "A1111",
      "clip": [
        "987",
        1
      ]
    },
    "class_type": "BNK_CLIPTextEncodeAdvanced",
    "_meta": {
      "title": "CLIP Text Encode (Advanced)"
    }
  },
  "22": {
    "inputs": {
      "text": "NSFW,lowres,shaded face,bad face,(facial decoration),bad anatomy,bad hand,paintings,sketches,(worst quality:2),(low quality:2),(normal quality:2),lowres,((monochrome)),((grayscale)),skin spots,acnes,skin blemishes,age spot,glans,extra fingers,fewer fingers,((watermark:2)),(white letters:1),(multi nipples),bad anatomy,bad hands,text,error,missing fingers,missing arms,missing legs,extra digit,fewer digits,cropped,worst quality,jpeg artifacts,signature,watermark,username,bad feet,Multiple people,blurry,poorly drawn hands,poorly drawn face,mutation,deformed,extra limbs,extra arms,extra legs,malformed limbs,fused fingers,too many fingers,long neck,cross-eyed,mutated hands,polar lowres,bad body,bad proportions,gross proportions,wrong feet bottom render,abdominal stretch,briefs,knickers,kecks,thong,fused fingers,bad body,bad proportion body to legs,wrong toes,extra toes,missing toes,weird toes,2 body,2 pussy,2 upper,2 lower,2 head,3 hand,3 feet,extra long leg,super long leg,mirrored image,mirrored noise",
      "token_normalization": "none",
      "weight_interpretation": "A1111",
      "clip": [
        "987",
        1
      ]
    },
    "class_type": "BNK_CLIPTextEncodeAdvanced",
    "_meta": {
      "title": "CLIP Text Encode (Advanced)"
    }
  },
  "40": {
    "inputs": {
      "pixels": [
        "917",
        0
      ],
      "vae": [
        "16",
        2
      ]
    },
    "class_type": "VAEEncode",
    "_meta": {
      "title": "VAE Encode"
    }
  },
  "41": {
    "inputs": {
      "samples": [
        "40",
        0
      ],
      "mask": [
        "349",
        0
      ]
    },
    "class_type": "SetLatentNoiseMask",
    "_meta": {
      "title": "Set Latent Noise Mask"
    }
  },
  "144": {
    "inputs": {
      "image": "1 (2).png",
      "upload": "image"
    },
    "class_type": "LoadImage",
    "_meta": {
      "title": "Load Image"
    }
  },
  "288": {
    "inputs": {
      "action": "append",
      "tidy_tags": "yes",
      "text_a": [
        "931",
        0
      ],
      "text_b": "(((masterpiece))),(((best quality))),((ultra-detailed))"
    },
    "class_type": "StringFunction|pysssss",
    "_meta": {
      "title": "String Function 🐍"
    }
  },
  "325": {
    "inputs": {
      "image": [
        "921",
        0
      ],
      "mask": [
        "349",
        0
      ]
    },
    "class_type": "InpaintPreprocessor",
    "_meta": {
      "title": "Inpaint Preprocessor"
    }
  },
  "326": {
    "inputs": {
      "control_net_name": "control_v11p_sd15_inpaint_fp16.safetensors"
    },
    "class_type": "ControlNetLoader",
    "_meta": {
      "title": "Load ControlNet Model"
    }
  },
  "327": {
    "inputs": {
      "strength": 0.85,
      "start_percent": 0,
      "end_percent": 0.5,
      "positive": [
        "21",
        0
      ],
      "negative": [
        "22",
        0
      ],
      "control_net": [
        "326",
        0
      ],
      "image": [
        "325",
        0
      ]
    },
    "class_type": "ControlNetApplyAdvanced",
    "_meta": {
      "title": "Apply ControlNet (Advanced)"
    }
  },
  "331": {
    "inputs": {
      "control_net_name": "control_v11p_sd15_openpose_fp16.safetensors"
    },
    "class_type": "ControlNetLoader",
    "_meta": {
      "title": "Load ControlNet Model"
    }
  },
  "332": {
    "inputs": {
      "strength": 1,
      "start_percent": 0,
      "end_percent": 1,
      "positive": [
        "327",
        0
      ],
      "negative": [
        "327",
        1
      ],
      "control_net": [
        "331",
        0
      ],
      "image": [
        "916",
        0
      ]
    },
    "class_type": "ControlNetApplyAdvanced",
    "_meta": {
      "title": "Apply ControlNet (Advanced)"
    }
  },
  "338": {
    "inputs": {
      "samples": [
        "993",
        0
      ],
      "vae": [
        "16",
        2
      ]
    },
    "class_type": "VAEDecode",
    "_meta": {
      "title": "VAE Decode"
    }
  },
  "349": {
    "inputs": {
      "start_offset": 3,
      "feathering_weight": 0.1,
      "mask": [
        "783",
        0
      ]
    },
    "class_type": "FeatheredMask",
    "_meta": {
      "title": "FeatheredMask"
    }
  },
  "360": {
    "inputs": {
      "max_width": 768,
      "max_height": 768,
      "min_width": 0,
      "min_height": 0,
      "crop_if_required": "no",
      "images": [
        "921",
        0
      ]
    },
    "class_type": "ConstrainImage|pysssss",
    "_meta": {
      "title": "Constrain Image 🐍"
    }
  },
  "783": {
    "inputs": {
      "mask": [
        "927",
        1
      ]
    },
    "class_type": "InvertMask",
    "_meta": {
      "title": "InvertMask"
    }
  },
  "916": {
    "inputs": {
      "detect_hand": "enable",
      "detect_body": "enable",
      "detect_face": "enable",
      "bbox_detector": "yolo_nas_s_fp16.onnx",
      "pose_estimator": "dw-ll_ucoco_384.onnx",
      "image": [
        "921",
        0
      ]
    },
    "class_type": "DWPreprocessor",
    "_meta": {
      "title": "DWPose Estimator"
    }
  },
  "917": {
    "inputs": {
      "batch_size": 1,
      "mode": "simple",
      "image": [
        "360",
        0
      ]
    },
    "class_type": "ChangeImageBatchSize //Inspire",
    "_meta": {
      "title": "Change Image Batch Size (Inspire)"
    }
  },
  "921": {
    "inputs": {
      "opacity": 25,
      "image": [
        "144",
        0
      ],
      "color_ref_image": [
        "144",
        0
      ]
    },
    "class_type": "LayerColor: ColorAdapter",
    "_meta": {
      "title": "LayerColor: ColorAdapter"
    }
  },
  "927": {
    "inputs": {
      "sam_model": "sam_hq_vit_h (2.57GB)",
      "grounding_dino_model": "GroundingDINO_SwinB (938MB)",
      "threshold": 0.3,
      "detail_range": 16,
      "black_point": 0.15,
      "white_point": 0.99,
      "process_detail": true,
      "prompt": "face",
      "image": [
        "921",
        0
      ]
    },
    "class_type": "LayerMask: SegmentAnythingUltra",
    "_meta": {
      "title": "LayerMask: SegmentAnythingUltra"
    }
  },
  "931": {
    "inputs": {
      "text": "Villain League, close-up shot of Joker wearing jacket, green hair, red lips, evil smile, neon red lighting, night time, highly detailed, ultra-high resolutions, 32K UHD, best quality, masterpiece"
    },
    "class_type": "TextInput_",
    "_meta": {
      "title": "TextInput_"
    }
  },
  "978": {
    "inputs": {
      "facedetection": "retinaface_mobile0.25",
      "codeformer_fidelity": 0.3,
      "facerestore_model": [
        "979",
        0
      ],
      "image": [
        "338",
        0
      ]
    },
    "class_type": "FaceRestoreCFWithModel",
    "_meta": {
      "title": "FaceRestoreCFWithModel"
    }
  },
  "979": {
    "inputs": {
      "model_name": "codeformer.pth"
    },
    "class_type": "FaceRestoreModelLoader",
    "_meta": {
      "title": "FaceRestoreModelLoader"
    }
  },
  "987": {
    "inputs": {
      "model": [
        "16",
        0
      ],
      "clip": [
        "16",
        1
      ],
      "lora_stack": [
        "992",
        0
      ]
    },
    "class_type": "CR Apply LoRA Stack",
    "_meta": {
      "title": "💊 CR Apply LoRA Stack"
    }
  },
  "992": {
    "inputs": {
      "switch_1": "Off",
      "lora_name_1": "None",
      "model_weight_1": 1,
      "clip_weight_1": 1,
      "switch_2": "Off",
      "lora_name_2": "None",
      "model_weight_2": 1,
      "clip_weight_2": 1,
      "switch_3": "Off",
      "lora_name_3": "None",
      "model_weight_3": 1,
      "clip_weight_3": 1
    },
    "class_type": "CR LoRA Stack",
    "_meta": {
      "title": "💊 CR LoRA Stack"
    }
  },
  "993": {
    "inputs": {
      "seed": 371373164601525,
      "steps": 30,
      "cfg": 7,
      "sampler_name": "ddim",
      "scheduler": "ddim_uniform",
      "denoise": 1,
      "model": [
        "987",
        0
      ],
      "positive": [
        "332",
        0
      ],
      "negative": [
        "332",
        1
      ],
      "latent_image": [
        "41",
        0
      ]
    },
    "class_type": "KSampler",
    "_meta": {
      "title": "KSampler"
    }
  },
  "994": {
    "inputs": {
      "images": [
        "978",
        0
      ]
    },
    "class_type": "PreviewImage",
    "_meta": {
      "title": "Preview Image"
    }
  }
}
"""