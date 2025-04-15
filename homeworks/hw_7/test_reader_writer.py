from io import StringIO
import json
import csv
from reader_writer import read_data, write_data, BaseReader


def test_read_text():
    # empty file
    file_obj = StringIO()
    file_obj.seek(0)
    actual_data = read_data(fileobj=file_obj, reader_type="txt")
    assert actual_data == ''

    # one line
    file_obj = StringIO()
    text = "Line 1"
    file_obj.write(text)
    file_obj.seek(0)
    actual_data = read_data(fileobj=file_obj, reader_type="txt")
    assert actual_data == text

    # two lines
    file_obj = StringIO()
    file_obj.write("Line 1\n")
    file_obj.write("Line 2")
    file_obj.seek(0)
    actual_data = read_data(fileobj=file_obj, reader_type="txt")
    assert actual_data == "Line 1\nLine 2"


def test_read_json():
    # empty file
    expected_data = {}
    file_obj = StringIO()
    json.dump(expected_data, file_obj)
    file_obj.seek(0)
    actual_data = read_data(fileobj=file_obj, reader_type="json")
    assert actual_data == expected_data

    expected_data = {}
    file_obj = StringIO()
    json.dump(expected_data, file_obj)
    file_obj.seek(0)
    actual_data = read_data(fileobj=file_obj, reader_type="json")
    assert actual_data == expected_data

    # nonempty file
    expected_data = {
        "name": "Иван",
        "age": 30,
        "hobbies": ["чтение", "программирование"],
        "man": [1, 2, 3, 4, 5]
    }
    file_obj = StringIO()
    json.dump(expected_data, file_obj)
    file_obj.seek(0)
    actual_data = read_data(fileobj=file_obj, reader_type="json")
    assert actual_data == expected_data


def test_read_csv():
    # empty file
    expected_data = []
    file_obj = StringIO()
    writer = csv.writer(file_obj, delimiter=' ',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    file_obj.seek(0)
    actual_data = read_data(fileobj=file_obj, reader_type="csv")
    assert actual_data == expected_data

    # one row file
    expected_data = [['Spam', 'Lovely Spam', 'Wonderful Spam']]
    file_obj = StringIO()
    writer = csv.writer(file_obj, delimiter=' ',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in expected_data:
        writer.writerow(row)
    file_obj.seek(0)
    actual_data = read_data(fileobj=file_obj, reader_type="csv")
    assert actual_data == expected_data

    # two row file
    expected_data = [
        ['Spam1', 'Lovely Spam1', 'Wonderful Spam1'],
        ['Spam2', 'Lovely Spam2', 'Wonderful Spam2'],
    ]
    file_obj = StringIO()
    writer = csv.writer(file_obj, delimiter=' ',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in expected_data:
        writer.writerow(row)
    file_obj.seek(0)
    actual_data = read_data(fileobj=file_obj, reader_type="csv")
    assert actual_data == expected_data


def testw_write_text():
    # empty file
    file_obj = StringIO()
    file_obj.seek(0)
    write_data(data='', fileobj=file_obj, mode='w', reader_type="txt")
    actual_data = file_obj.read()
    assert actual_data == ''

    # # one line
    file_obj = StringIO()
    data = "Line 1"
    write_data(data=data, fileobj=file_obj, mode='w', reader_type="txt")
    file_obj.seek(0)
    actual_data = file_obj.read()
    assert actual_data == data

    # # two lines
    file_obj = StringIO()
    data = "Line 1\nLine 2"
    write_data(data=data, fileobj=file_obj, mode='w', reader_type="txt")
    file_obj.seek(0)
    actual_data = file_obj.read()
    assert actual_data == data


def testw_write_json():
    # empty file
    file_obj = StringIO()
    data = {}
    write_data(data=data, fileobj=file_obj, mode='w', reader_type="json")
    file_obj.seek(0)
    actual_data = json.load(file_obj)
    assert actual_data == data

    file_obj = StringIO()
    data = {"key_1": "value_1", "key_2": "value_2"}
    write_data(data=data, fileobj=file_obj, mode='w', reader_type="json")
    file_obj.seek(0)
    actual_data = json.load(file_obj)
    assert actual_data == data


def testw_write_csv():
    # one line
    file_obj = StringIO()
    data = [["one", "two"]]
    write_data(data=data, fileobj=file_obj, mode='w', reader_type="csv")
    file_obj.seek(0)
    reader = csv.reader(file_obj, delimiter=' ', quotechar='|')
    actual_data = []
    for row in reader:
        actual_data.append(row)
    assert actual_data == data

    # two lines
    file_obj = StringIO()
    data = [["one", "two"], ["three", "four"]]
    write_data(data=data, fileobj=file_obj, mode='w', reader_type="csv")
    file_obj.seek(0)
    reader = csv.reader(file_obj, delimiter=' ', quotechar='|')
    actual_data = []
    for row in reader:
        actual_data.append(row)
    assert actual_data == data
