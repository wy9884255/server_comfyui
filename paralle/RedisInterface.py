import redis
import time
import datetime
import json

class RedisInterface():
    COMFYUI_DB = None
    
    @classmethod
    def init_redis(self):
        order_pool = redis.ConnectionPool(
            host='192.168.2.200',
            port='6379',
            password='Jyzn@#$1204', 
            db=6)
        RedisInterface.COMFYUI_DB = redis.Redis(connection_pool=order_pool)

    @classmethod
    def acquire_read_lock(self, lock_key):
        current_db = RedisInterface.COMFYUI_DB
        expiration = datetime.timedelta(seconds=2.0)
        acquire_result = current_db.setnx(lock_key, "locked")
        if acquire_result:
            current_db.expire(lock_key, expiration)
            return True
        return False
    
    @classmethod
    def release_read_lock(self, lock_key):
        current_db = RedisInterface.COMFYUI_DB
        current_db.delete(lock_key)
        
    @classmethod
    def write_queued_prompt(self, data):
        prompt_str = json.dumps(data, ensure_ascii=False).encode('utf-8').decode()
        time_str = datetime.datetime.now().strftime("%H%M%S%f")
        float_time = float(time_str[:-3] + '.' + time_str[-3:])
        RedisInterface.COMFYUI_DB.zadd(f"comfyui:queued_prompt", {prompt_str:float_time})
        