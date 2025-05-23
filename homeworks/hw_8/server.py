import socket
import threading
import queue
import sys
import json
import requests
import re
from bs4 import BeautifulSoup
from collections import Counter
import argparse

class Server:
    def __init__(self, host, port, num_workers, top_k):
        self.host = host
        self.port = port
        self.top_k = top_k
        self.counter = 0
        self.num_workers = num_workers
        self.task_queue = queue.Queue()
        self.lock = threading.Lock()

    def start(self):
        # Запуск воркеров
        for _ in range(self.num_workers):
            worker = threading.Thread(target=self.process_task)
            worker.daemon = True
            worker.start()

        # Настройка сокета
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen()

        print(f"Server started on {self.host}:{self.port}")

        # Мастер принимает подключения
        while True:
            client, addr = sock.accept() # Принятие нового подключения
            url = client.recv(1024).decode().strip() # Чтение URL от клиента
            if url:
                self.task_queue.put((client, url))

    def process_task(self):
        while True:
            client, url = self.task_queue.get()
            try:
                result = self.fetch_and_analyze(url)
                # Отправка результата клиенту в JSON-формате
                client.send(json.dumps(result).encode())
                with self.lock:
                    self.counter += 1
                    print(f"Total URLs processed: {self.counter}")
            except Exception as e:
                print(f"Error: {e}")
            finally:
                client.close()
            self.task_queue.task_done()

    def fetch_and_analyze(self, url):
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()
            words = re.findall(r'\b\w+\b', text.lower())
            return dict(Counter(words).most_common(self.top_k))
        except Exception as e:
            return {"error": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', type=int, required=True, help='Workers count')
    parser.add_argument('-k', type=int, required=True, help='Top K words')
    args = parser.parse_args()
    server = Server(host='localhost', port=8010, num_workers=args.w, top_k=args.k)
    server.start()