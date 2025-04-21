##############################################################################################################################

import threading
import time

def task(name):
    print(f"Задача {name} началась")
    time.sleep(2)  # Имитация долгой операции (I/O-bound)
    print(f"Задача {name} завершилась")

# Создаем два потока
thread1 = threading.Thread(target=task, args=("A",))
thread2 = threading.Thread(target=task, args=("B",))

# Запускаем потоки
thread1.start()
thread2.start()

# Ждем завершения работы потоков
thread1.join()
thread2.join()

print("Все потоки завершены")

##############################################################################################################################

t = threading.Thread(target=worker, daemon=True)
t.start()

##############################################################################################################################

'''
Тут создается 100 потоков и в каждом потоке значение increment увеличивается на 1
Через lock только в одном потоке значение глобально переменной увеличивается на 1, остальные потоки ждут пока lock освободится
'''
lock = threading.Lock()
counter = 0

def increment():
    global counter
    with lock:  # Автоматически захватывает и освобождает блокировку
        counter += 1

threads = []
for _ in range(100):
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()

for t in threads:
    t.join()

print("Counter:", counter)  # Всегда 100

### Еще пример
counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(5)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)  # Ожидаем 500000, Без блокировки результат, скорее всего, будет меньше 500000 из-за условий гонки.

##############################################################################################################################

semaphore = threading.Semaphore(3)  # Одновременно могут работать 3 потока

def task():
    with semaphore:
        print("Поток начал работу")
        time.sleep(2)
        print("Поток завершил работу")

for _ in range(5):
    threading.Thread(target=task).start()
# >>> Поток начал работу 
# >>> Поток начал работу 
# >>> Поток начал работу
# >>> Поток завершил работу 
# >>> Поток начал работу 
# >>> Поток завершил работу 
# >>> Поток начал работу 
# >>> Поток завершил работу 
# >>> Поток завершил работу 
# >>> Поток завершил работу


##############################################################################################################################

event = threading.Event()

def waiter():
    print("Ожидаем событие...")
    event.wait()  # Блокируется, пока событие не будет установлено
    print("Событие произошло!")

def setter():
    time.sleep(3)
    print(f"Сигнализируем о наступлении события")
    event.set()  # Сигнализирует о наступлении события

threading.Thread(target=waiter).start()
threading.Thread(target=setter).start()
# >>> Ожидаем событие...
# >>> Сигнализируем о наступлении события 
# >>> Событие произошло!


##############################################################################################################################

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

timer = threading.Timer(3, greet, args=("Alice",), kwargs={"greeting": "Hi"})
timer.start() # Через 3 секунды выведет: `Hi, Alice!
 
 
##############################################################################################################################

local_data = threading.local()

def task():
    local_data.value = threading.get_ident()  # ID потока
    print(f"Локальное значение: {local_data.value}")

threads = []
for _ in range(3):
    t = threading.Thread(target=task)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
# >>> Локальное значение: 128705372358208 
# >>> Локальное значение: 128705372358208 
# >>> Локальное значение: 128705372358208
