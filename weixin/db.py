from pickle import dumps, loads

from redis import StrictRedis

from weixin.config import REDIS_HOST, REDIS_PORT, REDIS_KEY
from weixin.request import WeixinRequest


class RedisQueue(object):
    def __init__(self):
        self.db = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

    def add(self, request):
        """
        向队列添加序列化的request
        :rtype: object
        """
        if isinstance(request, WeixinRequest):
            return self.db.lpush(REDIS_KEY, dumps(request))

    def pop(self):
        if self.db.llen(REDIS_KEY):
            return loads(self.db.rpop(REDIS_KEY))
        return None

    def clear(self):
        self.db.delete(REDIS_KEY)

    def empty(self):
        return self.db.llen(REDIS_KEY) == 0
