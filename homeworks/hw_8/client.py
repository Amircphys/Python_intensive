import socket
import threading
import queue
import argparse

class Client:
    def __init__(self, host, port, url_file, num_threads):
        self.host = host
        self.port = port
        self.num_threads = num_threads
        self.url_queue = queue.Queue()
        self.load_urls(url_file)

    def load_urls(self, path):
        with open(path) as f:
            for line in f:
                if url := line.strip():
                    self.url_queue.put(url)

    def worker(self):
        while True:
            url = self.url_queue.get()
            if url is None:
                break
            
            try:
                with socket.socket() as s:
                    s.connect((self.host, self.port))
                    s.send(url.encode())
                    data = s.recv(4096).decode()
                    print(f"{url}: {data}")
            except Exception as e:
                print(f"Failed {url}: {e}")
            finally:
                self.url_queue.task_done()

    def run(self):
        threads = []
        for _ in range(self.num_threads):
            t = threading.Thread(target=self.worker)
            t.start()
            threads.append(t)
        
        self.url_queue.join()
        
        # Завершение потоков
        for _ in range(self.num_threads):
            self.url_queue.put(None)
        for t in threads:
            t.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('threads', type=int, help='Threads count')
    parser.add_argument('url_file', help='Path to URLs file')
    args = parser.parse_args()
    
    client = Client('localhost', 8010, args.url_file, args.threads)
    client.run()