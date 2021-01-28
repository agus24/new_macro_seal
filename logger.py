from datetime import datetime


class Logger:
    def __init__(self, user_id, file_name):
        self.user_id = user_id
        self.file_name = f"logs/{file_name}"

    def log(self, text="-"):
        with open(f"{self.file_name}{self.user_id}.txt", "a") as file:
            time = datetime.strftime(datetime.now(), '%Y-%m-%d_%H:%M')
            output = f"[{time}][{self.user_id}] {text}\n"
            print(output)
            file.write(output)
