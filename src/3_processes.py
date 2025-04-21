##############################################################################################################################

from multiprocessing import Process
import os

def worker(number):
	print(f'Процесс {os.getpid()} получил число: {number}')

if __name__ == '__main__':
	p = Process(target=worker, args=(42,))
	p.start() # Запускаем процесс
	p.join() # Ждём, пока он завершится

##############################################################################################################################

from multiprocessing import Process
def worker(num):
	print(f'Process {num} started')

if __name__ == '__main__':
	processes = []
	for i in range(4):
		p = Process(target=worker, args=(i,))
		p.start()
		processes.append(p)
	for p in processes:
		p.join()
	
	print('Все процессы завершены')
# >>> Process 0 started 
# >>> Process 1 started 
# >>> Process 2 started 
# >>> Process 3 started 
# >>> Все процессы завершены


##############################################################################################################################

from multiprocessing import Process, Queue
def worker(q, n):
	q.put(n * n) # Кладём в очередь квадрат числа

if __name__ == '__main__':
	q = Queue()
	p = Process(target=worker, args=(q, 7))
	p.start()
	p.join()
	result = q.get()
	print(f'Квадрат: {result}') # Квадрат: 49

##############################################################################################################################


from multiprocessing import Pool
def square(n):
	return n * n

if __name__ == '__main__':
	with Pool(4) as pool:
	    results = pool.map(square, [1, 2, 3, 4, 5])
	print(results) # [1, 4, 9, 16, 25]
 
 
##############################################################################################################################

from multiprocessing import Process, Queue
def sender(q):
	for i in range(5):
	    print(f"Отправляем: {i}")
	    q.put(i) # помещаем данные в очередь

def receiver(q):
	while True:
		item = q.get() # забираем данные из очереди
		print(f"Получили: {item}")
		if item == 4:
			break

if __name__ == '__main__':
	q = Queue()

	p1 = Process(target=sender, args=(q,))
	p2 = Process(target=receiver, args=(q,))
	
	p1.start()
	p2.start()
	
	p1.join()
	p2.join()

##############################################################################################################################

from multiprocessing import Process, Value, Lock
import time

def increment(counter, lock):
	for _ in range(100):
	    time.sleep(0.01) # имитируем работу
	    with lock:
		    counter.value += 1 # изменяем общую переменную с блокировкой

if __name__ == '__main__':
	counter = Value('i', 0) # целочисленная общая переменная
	lock = Lock() # объект блокировки
	processes = []
	for _ in range(5):
		p = Process(target=increment, args=(counter, lock))
		p.start()
		processes.append(p)
		
	for p in processes:
	    p.join()

	print(f"Итоговое значение счетчика: {counter.value}")


##############################################################################################################################

from multiprocessing import Process, Manager
def worker(shared_list, idx):
	shared_list.append(f"данные из процесса {idx}")
  
if __name__ == '__main__':
	manager = Manager()
	shared_list = manager.list() # создаём разделяемый список
	processes = []
	for i in range(3):
		p = Process(target=worker, args=(shared_list, i))
		p.start()
		processes.append(p)

	for p in processes:
		p.join()
	print(f"Общий список: {shared_list}")
	# >>> Общий список: ['данные из процесса 0', 'данные из процесса 1', 'данные из процесса 2']
 
 
##############################################################################################################################

from multiprocessing import Process, Event
import time

def waiter(event):
	print("Жду сигнала от другого процесса...")
	event.wait() # ждём сигнала
	print("Получен сигнал! Работаем дальше.")
	
def setter(event):
	time.sleep(3)
	print("Отправляю сигнал.")
	event.set() # устанавливаем событие (сигнал)

if __name__ == '__main__':
	event = Event()
	p1 = Process(target=waiter, args=(event,))
	p2 = Process(target=setter, args=(event,))

	p1.start()
	p2.start()

	p1.join()
	p2.join()

##############################################################################################################################

from multiprocessing import Process, Value, Array

def task(n, arr):
    n.value = 42
    arr[0] = 100

if __name__ == "__main__":
    num = Value("i", 0)
    arr = Array("i", [1, 2, 3])
    
    p = Process(target=task, args=(num, arr))
    p.start()
    p.join()
    
    print(num.value)  # 42
    print(arr[:])     # [100, 2, 3]

##############################################################################################################################




##############################################################################################################################


##############################################################################################################################