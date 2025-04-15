import re


def generator(file_obj, key_words: list[str]):
    pattern = r'|'.join([rf'\b{word}\b' for word in key_words])
    pattern = r'(' + pattern + r')'
    for line in file_obj:
        if re.findall(pattern, line):
            yield line.strip()

