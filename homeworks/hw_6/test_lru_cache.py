import pytest
from lru_cache import LRUCache



def test_1():
    cache = LRUCache(1)
    assert cache.get("k1") is None
    cache.add_value("k1", "val1")
    assert cache.get('k1') == "val1"
    cache.add_value("k2", "val2")
    assert cache.get("k1") is None
    assert cache.get('k2') == "val2"
    

def test_2():
    cache = LRUCache(2)
    assert cache.get("k1") is None
    cache.add_value("k1", "val1")
    cache.add_value("k2", "val2")
    assert cache.get("k3") is None
    assert cache.get('k1') == "val1"
    assert cache.get('k2') == "val2"
    
    cache.add_value("k3", "val3")
    assert cache.get("k3") == "val3"  
    assert cache.get("k2") == "val2"  
    assert cache.get("k1") is None
    
    