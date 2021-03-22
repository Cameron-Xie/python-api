import json
import os

import multiprocessing

host = os.getenv("HOST", "0.0.0.0")
port = os.getenv("PORT", "8080")
api_bind = f"{host}:{port}"
api_loglevel = os.getenv("LOG_LEVEL", "info")
graceful_timeout_str = os.getenv("GRACEFUL_TIMEOUT", "120")
timeout_str = os.getenv("TIMEOUT", "120")
keepalive_str = os.getenv("KEEP_ALIVE", "5")
workers_per_core_str = os.getenv("WORKERS_PER_CORE", "1")
api_workers = max(int(multiprocessing.cpu_count() * float(workers_per_core_str)), 2)

loglevel = api_loglevel
workers = api_workers
bind = api_bind
graceful_timeout = int(graceful_timeout_str)
timeout = int(timeout_str)
keepalive = int(keepalive_str)

print(json.dumps({
    "loglevel": loglevel,
    "workers": workers,
    "bind": bind,
    "graceful_timeout": graceful_timeout,
    "timeout": timeout,
    "keepalive": keepalive,
}))
