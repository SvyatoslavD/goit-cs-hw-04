import time
from multiprocessing import Process, Manager

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


def task2():
    with Manager() as manager:
        lock = manager.Lock()
        result = manager.dict()
        processes = []

        file_paths = ['file_1.txt', 'file_2.txt', 'file_3.txt', 'file_4.txt']
        keywords = ['ipsum', 'tempor']

        for k in keywords:
            result[k] = manager.list()

        for i in range(4):
            file = file_paths[i]
            process = Process(target=search_keywords,
                            args=(file, keywords, result, lock))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        for k, v in result.items():
            print(f"{k} : {v}")


start_time = time.time()
task2()
end_time = time.time()
print(f"Час виконання: {end_time - start_time}")