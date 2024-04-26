if ps -ef | grep -v grep | grep allocator.py > /dev/null; then
    echo "allocator.py is already running. Exiting."
else
    cd /home/wy/server_comfyui/paralle
    /root/anaconda3/envs/sd/bin/python allocator.py
fi