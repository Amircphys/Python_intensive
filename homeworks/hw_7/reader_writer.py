
import json
import csv


class BaseReader:
    def read(self, file_obj: str, type="txt"):
        if type == "txt":
            return self.read_text(file_obj)
        elif type == "json":
            return self.read_json(file_obj)
        elif type == "csv":
            return self.read_csv(file_obj)
        else:
            raise ValueError(f"The format of file is wrong, use (txt, csv, json) format files!!!")
    
    @staticmethod
    def read_text(file_obj: str):
        text = file_obj.read()
        return text
    
    @staticmethod
    def read_json(file_obj: str):
        result = {}
        result = json.load(file_obj)
        return result
    
    @staticmethod
    def read_csv(file_obj: str):
        result = []
        rows = csv.reader(file_obj, delimiter=' ', quotechar='|')
        for row in rows:
            result.append(row)
        return result


class BaseWriter:
    def write(self, data, file_obj: str, mode, type='txt')-> None:
        if type == "txt":
            return self.write_text(data, file_obj, mode)
        elif type == "json":
            return self.write_json(data, file_obj, mode)
        elif type == "csv":
            return self.write_csv(data, file_obj, mode)
        else:
            raise ValueError(f"The format of file is wrong, use (txt, csv, json) format files!!!")
        
    @staticmethod
    def write_text(data, file_obj: str, mode: str)-> None:
            file_obj.write(data)
    
    @staticmethod
    def write_json(data: dict, file_obj, mode: str)-> None:
            json.dump(data, file_obj, ensure_ascii=False)
    
    @staticmethod
    def write_csv(data: list[list[str]], file_obj, mode: str)-> None:
        writer = csv.writer(file_obj, delimiter=' ',  quoting=csv.QUOTE_MINIMAL)
        for row in data:
            writer.writerow(row)

        
basereader = BaseReader()
basewriter = BaseWriter()

# использование
def read_data(fileobj, reader_type: str):
    # возвращает распаршенные данные
    return basereader.read(fileobj, type=reader_type)

def write_data(data, fileobj, mode, reader_type):
    return basewriter.write(data, fileobj, mode=mode, type=reader_type)