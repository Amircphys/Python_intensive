import logging
import argparse


def add_file_handler(logger, file_path: str):
    file_handler = logging.FileHandler(file_path, mode="w")
    file_handler.setLevel(logging.INFO)
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    return logger


def add_stream_handler(logger):
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(stream_formatter)
    logger.addHandler(stream_handler)
    return logger


class Node():
    def __init__(self, name, val, prev=None, next=None):
        self.name = name
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"key: {self.name}; value: {self.val}"


class LRUCache:
    def __init__(self, logger, limit=42):
        self.dict = {}
        self.head = None
        self.tail = None
        self.limit = limit
        self.logger = logger

    def get(self, key):
        self.logger.info(f"Get value with name {key}")
        return self.dict.get(key, None)

    def add_value(self, key, value):
        self.logger.info(f"Add item with name={key} and value={value}")
        node = Node(key, value)
        if not self.head:
            self.head = node
        if not self.tail:
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.dict[key] = value
        if len(self.dict) > self.limit:
            self.logger.info(f"Cache is full: remove item from cache...")
            self.remove()

    def remove(self):
        rm_key = self.head.name
        rm_value = self.head.val
        self.head = self.head.next
        self.dict.pop(rm_key, None)
        self.logger.info(
            f"Remove item with name={rm_key} and value={rm_value}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-l',
        '--limit',
        required=False,
        default=2,
        dest="limit",
        help="The limit size of cache"
    )
    parser.add_argument(
        '-s',
        '--stream_logs',
        required=False,
        default='false',
        dest="stream_logs",
        help="Is use stream logs"
    )
    parser.add_argument(
        '-f',
        '--file_logs',
        required=False,
        default='cache_logs.log',
        dest="file_logs",
        help="File path for logs"
    )
    arguments = parser.parse_args()
    logger = logging.getLogger("lru_cache")
    logger.setLevel(logging.INFO)
    logger = add_file_handler(logger, arguments.file_logs)
    if arguments.stream_logs:
        logger = add_stream_handler(logger)
    lru_cache = LRUCache(logger=logger, limit=arguments.limit)
    lru_cache.add_value("k1", "val1")
    lru_cache.add_value("k2", "val2")
    lru_cache.get("k3")
    lru_cache.get("k2") 
    lru_cache.get("k1")

    lru_cache.add_value("k3", "val3")

    lru_cache.get("k3")
    lru_cache.get("k2")
    lru_cache.get("k1")


if __name__ == "__main__":
    main()
