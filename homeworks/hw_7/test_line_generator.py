from line_generator import generator
from io import StringIO


def test_generator():
    text = "word1 word2\nword3 word4 word5\nword6"
    file_obj = StringIO()
    file_obj.write(text)
    file_obj.seek(0)
    
    finded_lines = list(generator(file_obj, ['word4']))
    assert finded_lines == ['word3 word4 word5']
    
    file_obj.seek(0)
    finded_lines = list(generator(file_obj, ['word2', 'word4']))
    assert finded_lines == ['word1 word2', 'word3 word4 word5']
    
    file_obj.seek(0)
    finded_lines = list(generator(file_obj, ['word22', 'word42']))
    assert finded_lines == []
    
    file_obj.seek(0)
    finded_lines = list(generator(file_obj, ['word22', 'word6']))
    assert finded_lines == ['word6']