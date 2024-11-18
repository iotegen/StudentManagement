import logging
from django.core.cache import cache

logger = logging.getLogger('app_logger')

def log_cache(key):
    data = cache.get(key)
    if data:
        logger.info(f"Cache hit for key: {key}")
    else:
        logger.info(f"Cache miss for key: {key}")
    return data
