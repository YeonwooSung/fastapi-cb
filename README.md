# fastapi-cb

`fastapi-cb` is a Python implementation of the Circuit Breaker pattern,
described in Michael T. Nygard's book `Release It!`_.

Circuit breakers exist to allow one subsystem to fail without destroying
the entire system. This is done by wrapping dangerous operations
(typically integration points) with a component that can circumvent
calls when the system is not healthy.

This project is a fork of aiobreaker by Alexander Lyon that
add support for integration with FastAPI.

- [Release It!](https://pragprog.com/titles/mnee2/release-it-second-edition/)
- [pybreaker](https://github.com/danielfm/pybreaker)
- [aiobreaker](https://github.com/arlyon/aiobreaker)

## Features

- Works well with FastAPI framework
- Configurable list of excluded exceptions (e.g. business exceptions)
- Configurable failure threshold and reset timeout
- Support for several event listeners per circuit breaker
- Can guard generator functions
- Functions and properties for easy monitoring and management
- `asyncio` support
- Optional redis backing
- Synchronous and asynchronous event listeners

## Requirements

All you need is `python 3.8` or higher.

## Installation

To install, simply download from pypi:

```bash
pip install fastapi_cb
```

## Usage

The first step is to create an instance of `CircuitBreaker` for each
integration point you want to protect against.

```python
from fastapi_cb import CircuitBreaker

# Used in database integration points
db_breaker = CircuitBreaker(fail_max=5, reset_timeout=timedelta(seconds=60))

@db_breaker
async def outside_integration():
    """Hits the api"""
    ...
```

At that point, go ahead and get familiar with the documentation.
