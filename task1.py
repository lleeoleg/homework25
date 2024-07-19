"""
Задание №1
а) Напишите функцию, которая будет создавать файл, с задержкой 1 секунду.
б) Запустите циклом 100 таких функций, а также замерьте время.
в) Добавьте функционал многопоточного запуска, с замером времени.
"""
import time
import threading

def create_file(filename):
    """_summary_

    Args:
        filename (_type_): _description_
    """
    time.sleep(1)
    with open(filename, 'w', encoding="UTF-8"):
        pass
FILENAME = "createdfile.txt"
COUNT = 10
start = time.time()
for _ in range(COUNT):
    create_file(FILENAME)
end = time.time()
result = end - start
print(f"Без многопоточности {result}")
start_time = time.time()
threads = []
for _ in range(COUNT):
    my_thread = threading.Thread(target=create_file, args=(FILENAME,))
    my_thread.start()
    threads.append(my_thread)
for thread in threads:
    thread.join()
end_time = time.time()
new_result = end_time - start_time
print(f"C многопоточностью {new_result}")
