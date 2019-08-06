import os
import psutil
import logging
import datetime

THRESHOLD = 2 * 1024 * 1024
logger = logging.getLogger(__name__)


class MemoryUsageMiddleware(object):
    def process_request(self, request):
        request._time_received = datetime.datetime.now()
        request._mem = psutil.Process(os.getpid()).memory_info()
        request._cpu_percent = psutil.Process(os.getpid()).cpu_times().system

    def process_response(self, request, response):
        # MEMORY LOGGING in bytes
        mem = psutil.Process(os.getpid()).memory_info()
        mem_diff = mem.rss - request._mem.rss
        # CPU LOGGING
        response_cpu_percent = psutil.Process(os.getpid()).cpu_times().system
        cpu_diff = response_cpu_percent - request._cpu_percent
        # 'cpu_percent', 'cpu_times'
        # SERVER REQUEST RESPONSE TIME
        response_time = (datetime.datetime.now() - request._time_received).total_seconds()
        # log the request/response data
        logger.error(u'{};{};{}'.format(mem_diff, cpu_diff, response_time))
        return response
