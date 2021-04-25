import json
import os
import threading
from Src.Http_parser import master_parser
from queue import Queue
from tqdm import tqdm


queue = Queue()


def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


def write_file(file_name, data):
    with open(file_name, 'w') as f:
        f.write(data)


def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


def write_json(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f)

def create_workers(NUMBER_OF_THREADS):
    print("Creating workers")
    for _ in tqdm(range(NUMBER_OF_THREADS)):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    global crawl_count
    crawl_count = 0
    OUTPUT_DIR = 'Json_data'
    while True:
        
        url = queue.get()
        crawl_count += 1
        filename = "{Website}-0{count}".format(Website = 'JSD', count = crawl_count)
        master_parser.Jsonbuild.parse(url, OUTPUT_DIR, filename)
        queue.task_done()


def create_jobs(INPUT_FILE):
    print("Creating Jobs")
    for url in tqdm(file_to_set(INPUT_FILE)):
        queue.put(url)
    queue.join()
