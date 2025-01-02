import multiprocessing
import requests
from multiprocessing.dummy import Pool
import time
import logging
import sys

logging.basicConfig(filename="results.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
logger = logging.getLogger()

logger.setLevel(logging.INFO)

def io(id):
        start_time=time.time()
        requests.get("host:port/testio")
        end_time=time.time()
        return end_time-start_time

def cpu(id):
        start_time=time.time()
        requests.get("host:port/")
        end_time=time.time()
        return end_time-start_time  

def main():

    pool = Pool(5)
    futures = []
    for x in range(5):
        futures.append(pool.apply_async(cpu,[x]))
        # futures.append(pool.apply_async(io, [x]))
    total_time=0
    for future in futures:
        total_time+=future.get()
    # logger.info(f"Time Taken when worker class is {sys.argv[1]} and no of threads is {sys.argv[2]} is {total_time/10}")

if __name__=='__main__':

    main()
