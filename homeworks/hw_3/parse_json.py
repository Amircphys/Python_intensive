import json

def parse_json(json_str: str, required_fields: list[str], keywords: list[str], keyword_callback: callable):
    json_dict = json.loads(json_str)
    result = []
    for key, value in json_dict.items():
        if key in required_fields:
            for word in keywords:
                if word in value:
                    result.append(keyword_callback(word))
    return result

def test_parse_json():
    def keyword_callback(text: str):
        return text.capitalize()
    input_data = [
        {
            "json_str": '{"key1": "Word1 word2", "key2": "word2 word3"}',
            "required_fields": ['key1'],
            "keywords": ['word2'],
            "output": ['Word2']
        },
        {
            "json_str": '{"key1": "Word1 word2", "key2": "word2 word3"}',
            "required_fields": ['key2'],
            "keywords": ['word3'],
            "output": ['Word3']
        },
        {
            "json_str": '{"key1": "Word1 word2", "key2": "word2 word3"}',
            "required_fields": ['key2'],
            "keywords": ['word4'],
            "output": []
        },
        {
            "json_str": '{"key1": "Word1 word2", "key2": "word2 word3"}',
            "required_fields": ['key1', 'key2'],
            "keywords": ['word2'],
            "output": ['Word2', 'Word2']
        },
        {
            "json_str": '{"key1": "Word1 word2", "key2": "word2 word3"}',
            "required_fields": ['key11', 'key22'],
            "keywords": ['word2'],
            "output": []
        },
        
    ]

    for item in input_data:
        assert parse_json(item['json_str'], item['required_fields'], item['keywords'], keyword_callback) == item['output']
        
        
if __name__ == "__main__":
    test_parse_json()