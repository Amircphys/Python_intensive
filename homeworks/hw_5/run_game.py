import subprocess
import random
from tictac import (
    CORRECT_COORDINATES_MESSAGE,
    WRONG_COORDINATES_MESSAGE,
    WRONG_CELL_MESSAGE,
    WRONG_NUMBER_COORDINATES_MESSAGE,
    DRAW_MESSAGE,
    NEXT_STEP_MESSAGE,
)


def generate_random_coordinates():
    return f"{random.randint(0, 2)} {random.randint(0, 2)}\n"


wrong_messages = [
    WRONG_COORDINATES_MESSAGE,
    WRONG_CELL_MESSAGE,
    WRONG_NUMBER_COORDINATES_MESSAGE,
]


# Запуск целевого скрипта
process = subprocess.Popen(
    ["python", "-u", "tictac.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True,
)


def one_input_process(process):
    temp_inp = generate_random_coordinates()
    print(f"temp input: {temp_inp}")
    process.stdin.write(temp_inp)
    process.stdin.flush()
    output = process.stdout.readline()
    print(f"Вывод: {output}")
    return output


output_message = ""
while ("win!!!" not in output_message) and (DRAW_MESSAGE not in output_message):
    output_message = one_input_process(process)
    while any(message == output_message for message in wrong_messages):
        output_message = one_input_process(process)

# Завершаем процесс
process.stdin.close()
process.wait()
