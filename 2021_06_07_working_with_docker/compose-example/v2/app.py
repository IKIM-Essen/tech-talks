import redis
from flask import Flask

redis_host = "store"
redis_port = 6379
redis_password = ""

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        r.set("msg:hello", "Hello Redis!")
        return r.get("msg:hello")
    except Exception:
        raise
