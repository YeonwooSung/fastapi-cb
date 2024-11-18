from datetime import timedelta

from _pytest.fixtures import fixture
from fakeredis import FakeStrictRedis

from fastapi_cb.state import CircuitBreakerState
from fastapi_cb.storage.memory import CircuitMemoryStorage
from fastapi_cb.storage.redis import CircuitRedisStorage

__all__ = ('redis_storage', 'storage', 'memory_storage', 'delta')


@fixture()
def redis_storage():
    redis = FakeStrictRedis()
    yield CircuitRedisStorage(CircuitBreakerState.CLOSED, redis)
    redis.flushall()


@fixture()
def memory_storage():
    return CircuitMemoryStorage(CircuitBreakerState.CLOSED)


@fixture(params=['memory_storage', 'redis_storage'])
def storage(request):
    return request.getfixturevalue(request.param)


@fixture()
def delta():
    return timedelta(seconds=1)
