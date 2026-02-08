

class Notification:
    def __init__(self, sender) -> None:
        self.sender = sender

    def send(self, message):
        self.sender.send(message)

    def get_ack(self):
        pass


class EmailSender:
    def send(self, message):
        print(f"Сообщение отправлено - {message}")


notif = Notification(EmailSender())
notif.send("'Это сообщение'")
