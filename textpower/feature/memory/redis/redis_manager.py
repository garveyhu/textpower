from redis import Redis, Sentinel, ConnectionPool, SentinelConnectionPool

from textpower.complex.config.system_settings import system_settings


class RedisManager:
    _pool = None

    @classmethod
    def initialize_pool(cls):
        if system_settings.REDIS_SENTINEL_MASTER:
            sentinel = Sentinel(
                [(system_settings.REDIS_HOST, system_settings.REDIS_PORT)],
                socket_timeout=system_settings.SOCKET_TIMEOUT,
                sentinel_kwargs={"password": system_settings.REDIS_SENTINEL_PASSWORD},
            )
            cls._pool = SentinelConnectionPool(
                master_name=system_settings.REDIS_SENTINEL_MASTER,
                sentinel_manager=sentinel,
                socket_timeout=system_settings.SOCKET_TIMEOUT,
                password=system_settings.REDIS_PASSWORD,
                db=system_settings.REDIS_DB,
            )
        else:
            cls._pool = ConnectionPool(
                host=system_settings.REDIS_HOST,
                port=system_settings.REDIS_PORT,
                db=system_settings.REDIS_DB,
                password=system_settings.REDIS_PASSWORD,
            )

    def __init__(self):
        if self.__class__._pool is None:
            self.__class__.initialize_pool()
        self.client = Redis(connection_pool=self.__class__._pool)
