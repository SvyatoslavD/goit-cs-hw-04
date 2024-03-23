import time
from threading import Thread, Lock

def search_keywords(file_path, keywords, result_dict, lock):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            for keyword in keywords:
                if keyword in content:
                    with lock:
                        result_dict[keyword].append(file_path)
    except Exception as e:
        print(f"Error [{file_path}]: {e}")


def task1():
    lock = Lock()
    result = {}
    threads = []

    file_paths = ['file_1.txt', 'file_2.txt', 'file_3.txt', 'file_4.txt']
    keywords = ['ipsum', 'tempor']

    for k in keywords:
        result[k] = []

    for i in range(4):
        file = file_paths[i]
        thread = Thread(target=search_keywords,
                        args=(file, keywords, result, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for k, v in result.items():
        print(f"{k} : {v}")


start_time = time.time()
task1()
end_time = time.time()
print(f"Час виконання: {end_time - start_time}")