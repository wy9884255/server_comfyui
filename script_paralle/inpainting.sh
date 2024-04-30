#!/bin/bash

# 定义 Python 文件路径
python_file="/home/wy/ComfyUI/main.py"

# 定义要调用的 Python 环境路径
python_env="/root/anaconda3/envs/instant/bin/python"

port=8101

# 检查端口是否被占用
ss -tln | grep ":$port " > /dev/null

# 检查netstat命令的退出状态
if [ $? -eq 0 ]; then
  echo "端口 $port 被占用"
else
  "$python_env" "$python_file"
fi
