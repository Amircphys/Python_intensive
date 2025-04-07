import subprocess
import random


def generate_random_coordinates():
    return f"{random.randint(0, 2)} {random.randint(0, 2)}\n"


wrong_messages = [
    "Число введенных координат должно равняться 2, пожалуйста введите две координаты"
    "Введены некорректные координаты - значение координат должно лежать в диапазоне [0, 2], пожалуйста введите корректные координаты",
    "Введены некорректные координаты - ячейка уже занята, пожалуйста введите корректные координаты",
]

end_messages = []
# Запуск целевого скрипта
process = subprocess.Popen(
    ["python", "-u", "tiktak.py"],
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
while ("win!!!" not in output_message) and ("Draw" not in output_message):
    output_message = one_input_process(process)
    while any(message == output_message for message in wrong_messages):
        output_message = one_input_process(process)

# Завершаем процесс
process.stdin.close()
process.wait()
