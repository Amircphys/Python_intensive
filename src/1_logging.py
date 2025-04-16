#######################################################################################

import logging

# Уровни логирования (по возрастанию важности): DEBUG < INFO < WARNING < ERROR < CRITICAL
logging.debug("Это сообщение уровня DEBUG")  # Не будет выведено (по умолчанию уровень = WARNING)
logging.info("Это сообщение уровня INFO")    # Не будет выведено
logging.warning("Это предупреждение!")
logging.error("Это ошибка!")
logging.critical("Критическая ошибка!")


#######################################################################################

import logging

# Настройка уровня логирования и формата
logging.basicConfig(
    level=logging.DEBUG,  # Теперь видны все сообщения от DEBUG и выше
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.info("Теперь это сообщение видно!")

#######################################################################################
import logging

logging.basicConfig(
    filename='app.log',        # Логи сохраняются в файл
    filemode='a',               # 'a' - дописывать, 'w' - перезаписать
    level=logging.INFO,
    format='%(levelname)s - %(message)s'
)

logging.info("Сообщение записано в файл")

#######################################################################################

import logging

# Создание кастомного логгера
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# Создание обработчиков
console_handler = logging.StreamHandler()  # Вывод в консоль
file_handler = logging.FileHandler("advanced.log")  # Запись в файл

# Настройка уровней для обработчиков
console_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.DEBUG)

# Создание форматеров
console_format = logging.Formatter('%(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Привязка форматеров к обработчикам
console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# Добавление обработчиков к логгеру
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Пример использования
logger.debug("Это DEBUG-сообщение (только в файл)")
logger.warning("Это WARNING-сообщение (в файл и консоль)")


try:
    1 / 0
except ZeroDivisionError:
    logger.exception("Произошло исключение:")  # Автоматически добавляет traceback
    
    
class CustomFilter(logging.Filter):
    def filter(self, record):
        return "SECRET" not in record.getMessage()  # Игнорировать сообщения с "SECRET"

logger.addFilter(CustomFilter())
logger.error("Это сообщение с SECRET")  # Не будет записано
logger.error("Это сообщение должно быть пропущено фильтром")  # Не будет записано

#######################################################################################


import logging
import logging.config


log_conf = {
    "version": 1,
    "formatters": {
        "simple": {
            "format": "%(asctime)s\t%(levelname)s\t%(message)s",
        },
        "processed": {
            "format": "%(asctime)s\t%(levelname)s\t%(name)s\t%(message)s",
        },
    },
    "handlers": {
        "file_handler": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "filename": "file_handler.log",
            "formatter": "simple",

        },
        "stream_handler": {
            "level": "DEBUG",
            "formatter": "processed",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "file_logger": {
            "level": "INFO",
            "handlers": ["file_handler"],
        },
        "stream_logger": {
            "level": "INFO",
            "handlers": ["stream_handler"],
        },
        "total": {
            "level": "DEBUG",
            "handlers": ["file_handler", "stream_handler"],
        },
    },
}


logging.config.dictConfig(log_conf)
total_logger = logging.getLogger("total")
total_logger.debug("debug_total")
total_logger.info("info_total")
total_logger.error("error_total")

root_logger = logging.getLogger()
root_logger.debug("debug_root")
root_logger.info("info_root")
root_logger.error("error_root")

#####################################################################################################################

