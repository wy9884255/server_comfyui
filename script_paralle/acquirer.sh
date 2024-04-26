if ps -ef | grep -v grep | grep acquirer.py > /dev/null; then
    echo "acquirer.py is already running. Exiting."
else
    cd /home/wy/server_comfyui/paralle
    /root/anaconda3/envs/sd/bin/python acquirer.py
fi